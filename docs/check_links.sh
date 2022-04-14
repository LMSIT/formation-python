#!/bin/bash

# Usage :
# ./check_links.sh
# Or to not check all external links
# DISABLE_EXTERNAL=1 ./check_links.sh

missing_file=/tmp/missing
todo_file=/tmp/todo
missing_type_file=/tmp/missing_type

echo -n 0 > $missing_file
echo -n 0 > $todo_file
echo -n 0 > $missing_type_file

function increment_counter {
	counter=$1
	count=$(eval "cat \$${counter}_file")
	#echo counter $counter count=$count
	count=$((count+1))
	eval "echo -n $count > \$${counter}_file"
}

function get_links {
	while read file; do
		for link_dest in $(grep -E '\[[^\]+\]\([^)]+\)' $file | sed -e 's/^.*\[[^\]\+](\([^)]\+\)).*$/\1/'); do
			echo  $file $link_dest
		done
	done
}

function check_link {
	local file=$1
	local link_dest=$2
        #echo "======================================"
	#echo "Checking $file $link_dest"

	# external ?
	echo $link_dest | grep -E '^http' &>/dev/null
	if [ $? -eq 0 ]; then
		check_external_link $file $link_dest
		return
	fi

	# mailto ?
	echo $link_dest | grep -E '^mailto' &>/dev/null
	if [ $? -eq 0 ]; then
		# OK
		return
	fi


	# bad anchor ?
	echo $link_dest | grep -E '?id=.*' &>/dev/null
	if [ $? -eq 0 ]; then
		echo "ERROR in $file : $link_dest: anchor should be # and not ?id="
		increment_counter missing
		return
	fi

	# anchor only ?
	echo $link_dest |grep -E '^#' &>/dev/null
	if [ $? -eq 0 ]; then
		# anchor only
		check_anchor $file $link_dest $file
		return
	fi

	# path ?
	echo $link_dest | grep -E '^/' &>/dev/null
	if [ $? -eq 0 ]; then
		#echo Absolute path
		dest_path=$(echo $link_dest | sed -e 's/^\//.\//' -e 's/#.*//')
		
		#echo $file link_dest=$link_dest path=$dest_path
		echo $dest_path | grep -E '/$' &>/dev/null
		if [ $? -eq 0 ]; then
			#echo "$dest_path is a folder"
			if [ -f "${dest_path}README.md" ]; then
				check_anchor $file $link_dest ${dest_path}README.md
				#true
			else
				echo "ERROR $file link_dest=$link_dest : ${dest_path}README.md does not exist"
				increment_counter missing
			fi
		else
			if [ -f "${dest_path}" -o -f "${dest_path}.md" ]; then
				if [ -f "${dest_path}" ]; then
					check_anchor $file $link_dest $dest_path
				fi
				if [ -f "${dest_path}.md" ]; then
					check_anchor $file $link_dest $dest_path.md
				fi
			else
				echo "ERROR $file link_dest=$link_dest : $dest_path does not exist"
				increment_counter missing
			fi
		fi
	else
		#echo Relative path
		basedir=$(echo $file | sed -e 's/[^/]\+$//' -e 's/#.*//')
                dest_path=$(echo $link_dest | sed -e 's/#.*//')
		#echo "$file link_dest=$link_dest : basedir=$basedir / dest_path=$dest_path"

		echo $dest_path | grep -E '/$' &>/dev/null
		if [ $? -eq 0 ]; then
	        	#echo "$dest_path is a folder"
			if [ -f "$basedir/${dest_path}README.md" ]; then
				check_anchor $file $link_dest "$basedir/${dest_path}README.md"
			else
				echo "ERROR $file link_dest=$link_dest: $dest_path does not exist"
				increment_counter missing
			fi
		else
			#echo "$dest_path is not a folder"
			if [ -f "$basedir/$dest_path" -o -f "$basedir/$dest_path.md" ]; then
				if [ -f "$basedir/$dest_path" ]; then
					check_anchor $file $link_dest "$basedir/$dest_path"
				fi
				if [ -f "$basedir/$dest_path.md" ]; then
					check_anchor $file $link_dest "$basedir/$dest_path.md"
				fi
			else
				echo "ERROR $file link_dest=$link_dest : dest with basedir $basedir is missing"
				increment_counter missing
			fi
		fi
	fi

}

function check_links {
	while read file link_dest; do
		check_link $file $link_dest
	done
}

function check_anchor {
	local file=$1
	local link_dest=$2
	local file_dest=$3
	#echo "check_anchor $file $link_dest $file_dest"
	echo $link_dest | grep '#' > /dev/null
	if [ $? -eq 0 ]; then
		anchor=$(echo $link_dest | sed -e 's/^.*#/#/' -e "s/'/39/g" | tr 'A-Z' 'a-z')
		#echo "Anchor is $anchor"
		#grep -E '^#' $file_dest | sed -e 's/#\+ /#/' | tr 'A-Z ' 'a-z-'
		grep -E '^#' $file_dest | sed -e 's/#\+ /#/' -e "s/'/39/g" | tr 'A-Z ' 'a-z-' |grep -E "^$anchor\$" >/dev/null
		if [ $? -eq 0 ]; then
			#echo "OK : $file link_dest=$link_dest : Anchor $anchor found in $file_dest"
			return
		else
			missing=$((missing+1))
			echo "ERROR : $file link_dest=$link_dest : Anchor $anchor not found in $file_dest"
			echo "Available anchors are :"
			grep -E '^#' $file_dest | sed -e 's/#\+ /#/' -e "s/'/39/g" | tr 'A-Z ' 'a-z-'
			return
		fi
	else
		# no anchor
		true
	fi
}

function check_external_link {
	local file=$1
	local link_dest=$2
	#echo "check_external_link $file $link_dest ..."

	if [ ! -z "$DISABLE_EXTERNAL" ]; then
		return
	fi

	echo $link_dest | grep -E '(git.lms.fr|wiki.linkbynet.com|lms-pid.slack.com|formatix.lms.fr|intranet.linkbynet.com|calculator.managed-containers.lms.fr|app.datadoghq.com|linkbynet365.sharepoint.com|github.com)' >/dev/null
	if [ $? -eq 0 ]; then
		#echo "excluded due to auth : $link_dest"
		#increment_counter todo
		return
	fi

	curl $link_dest --fail --silent --head --insecure >/dev/null
	if [ $? -eq 0 ]; then
		#echo "OK : $file $link_dest : external link is good"
		return
	else
		echo "ERROR : $file $link_dest : external link failed"
		curl $link_dest --fail --head --insecure
		increment_counter missing
		echo "If destination is in openshift documentation, put the url from the git release instead: ex: https://github.com/openshift/openshift-docs/blob/enterprise-3.11/install_config/cluster_metrics.adoc#metrics-ansible-role"
	fi
}

function check_code_type {
	local file=$1
	#echo "check_code_type $file"
	local code_begin=$(grep -E '^```[a-z]+$' $file | wc -l)
	local code_end=$(grep -E '^```$' $file | wc -l)
	if [ $code_begin -ne $code_end ]; then
		echo "ERROR : $file : missing code language (begin:$code_begin / end:$code_end)"
		increment_counter missing_type
	fi
}

function check_code_types {
	while read file; do
		check_code_type $file
	done
}

function get_files {
	find . -name "*.md"
}

function exclude_plantuml {
	while read file; do
	        grep plantuml $file &>/dev/null
		if [ $? -eq 0 ]; then
			#echo "Excluded plantuml" 1>&2
			continue
		else
			echo $file
		fi
	done
}

function filter_links {
	type=$1
	while read file link_dest; do
		grep http <<< $link_dest &>/dev/null
		grep_code=$?
		if [ $grep_code -eq 0 -a $type == external ]; then
			echo $file $link_dest
		fi
		if [ $grep_code -ne 0 -a $type == internal ]; then
			echo $file $link_dest
		fi
	done
}

echo Cheking code syntax
get_files | check_code_type
echo Extacting all links
get_files | exclude_plantuml | get_links > /tmp/links
echo Checking internal links
cat /tmp/links | filter_links internal | check_links
if [ $(cat $missing_file) -ne 0 ]; then
	echo "$missing files are missing"
	exit 1
fi
echo Checking external links
cat /tmp/links | filter_links external | check_links
if [ $(cat $missing_file) -ne 0 ]; then
	echo $(cat $missing_file)" files are missing"
	exit 1
fi

if [ $(cat $missing_type_file) -ne 0 ]; then
	echo $(cat $missing_type_file)" code type are missing"
	echo "type list : https://github.com/PrismJS/prism/blob/gh-pages/components.json"
	echo "use 'output' for commands output even if colororation does not exists"
	exit 1
fi


if [ $(cat $todo_file) -ne 0 ]; then
	echo "TODO : "$(cat $todo_file)" not suported dest"
	exit 1
fi

echo "All links are good"

echo "Remaning TODOs and FIXMEs in pages"
find . -name "*.md" -exec grep -H -E '(TODO|FIXME)' {} \;

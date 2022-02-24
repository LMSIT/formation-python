from setuptools import setup

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='htaccess-generator',
    version="0.1.0",
    description="htaccess file generator from csv file",
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=[
        "generate_htaccess.py"
    ],
    install_requires=[
        "jinja2"
    ],
    author='Stephane RAULT',
    author_email="s.rault@linkbynet.com",
    python_requires='>=3.7',
)


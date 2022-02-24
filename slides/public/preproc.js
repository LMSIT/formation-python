const exercice_url_default = process.env.LBN_EXERCICE_URL || 'http://127.0.0.1:8080'; 

module.exports = (markdown, options) => {
    return new Promise((resolve, reject) => {
      return resolve(
        markdown
          .split('\n')
          .map((line, index) => {
            if (/.*EXERCICE_URL.*/.test(line)) {
                return line.replace('EXERCICE_URL', exercice_url_default);
            }
            return line
          })
          .join('\n')
      );
    });
  };
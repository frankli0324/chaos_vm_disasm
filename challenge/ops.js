let fs = require('fs');
let g = JSON.parse(fs.readFileSync('./ops4.json'))

exports.g = g;

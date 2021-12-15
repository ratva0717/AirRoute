const fs = require('fs')
console.log("j")
fs.readFile('data.txt', (err, data) => {
    if (err) throw err;

    console.log(data.toString());
})
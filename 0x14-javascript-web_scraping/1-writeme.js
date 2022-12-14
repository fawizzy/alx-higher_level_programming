#!/usr/bin/node

let fs = require('fs')
file = process.argv[2]
text = process.argv[3]

fs.writeFile(file, text, 'utf-8', (err) => {
    if (err)
        console.log(err)
});
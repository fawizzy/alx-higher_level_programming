#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
let data

request(url, function (err, response, body) {
    fs.writeFile(filePath, body,'utf-8', (error) =>{})
});


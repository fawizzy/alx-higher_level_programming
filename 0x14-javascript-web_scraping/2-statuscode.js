#!/usr/bin/node

let request = require('request')

let url = process.argv[2]

request(url, (error, response, body) => {
    // console.log(error)
    console.log(`code: ${response.statusCode}`)
})
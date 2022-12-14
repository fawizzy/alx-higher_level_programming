#!/usr/bin/node

let request = require('request')

let id = process.argv[2]
url =`https://swapi-api.hbtn.io/api/films/${id}`

request(url, (error, response, body) => {
    console.log(JSON.parse(body))
})
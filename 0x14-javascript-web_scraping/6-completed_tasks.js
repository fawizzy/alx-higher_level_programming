#!/usr/bin/node

const request = require('request')
const URL = process.argv[2]
let completed = {}
request(URL, (error, response, body) => {
    todos = JSON.parse(body)
    todos.forEach(element => {
        completed[element["userId"]] = 0
    })
    todos.forEach(element => {
        // completed[element["userId"]] = 1
        if (element["completed"] === true){
            completed[element["userId"]] += 1
        }
    });
    console.log(completed)
})

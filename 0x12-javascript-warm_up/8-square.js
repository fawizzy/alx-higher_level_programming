#!/usr/bin/node
const value = process.argv[2];
if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    let myVar = '';
    for (let j = 0; j < value; j++) {
      myVar += 'X';
    }
    console.log(myVar);
  }
}

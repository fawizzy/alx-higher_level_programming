#!/usr/bin/node
const val = parseInt(process.argv[2]);

function factorial (val) {
  if (val === 0 || isNaN(val)) {
    return 1;
  }

  return val * factorial(val - 1);
}

console.log(factorial(val));

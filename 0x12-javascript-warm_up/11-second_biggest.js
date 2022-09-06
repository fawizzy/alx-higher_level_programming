#!/usr/bin/node

const val = process.argv.slice(2);
val.sort().reverse();

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(val[1]);
}

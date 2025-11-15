#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const firstArg = process.argv[2];
const secondArg = process.argv[3];

console.log(add(firstArg, secondArg));

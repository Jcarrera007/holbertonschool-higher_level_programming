#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const firstArg = process.argv[2];
const num = parseInt(firstArg);

console.log(factorial(num));

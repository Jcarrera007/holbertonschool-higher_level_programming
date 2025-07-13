#!/usr/bin/node
const firstArg = process.argv[2];
const size = parseInt(firstArg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}

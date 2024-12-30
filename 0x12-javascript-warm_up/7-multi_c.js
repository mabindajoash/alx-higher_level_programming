#!/usr/bin/node
let i = 0;
const args = process.argv.slice(2);
while (i < args[0]) {
  console.log('C is fun');
  i += 1;
}

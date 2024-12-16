#!/usr/bin/node
function add(a, b){
  const args = process.argv.slice(2);
  if (args[1] === undefined) {
    console.log('NaN');
  } else {
    const num1 = Number(args[0]);
    const num2 = Number(args[1]);
    if (isNaN(num1) || isNaN(num2)) {
      console.log('NaN');
    } else {
      console.log(num1 + num2);
    }
  }
}
add();

#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}
module.exports = Square;

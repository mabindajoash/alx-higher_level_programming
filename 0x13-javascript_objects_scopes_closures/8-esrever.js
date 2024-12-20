#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    list1[j] = list[i];
    j++;
  }
  return (list1);
};

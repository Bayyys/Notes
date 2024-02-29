var number = require("./a.js");

console.log(number.num); // 1
number.add();
console.log(number.num); // 1

var b = require("./b.js");
b.obj.color.push("yellow");
console.log(b.obj.color); // [ 'red', 'green', 'blue', 'yellow' ]

var c = require("./b.js");
console.log(c.obj.color); // [ 'red', 'green', 'blue', 'yellow' ]

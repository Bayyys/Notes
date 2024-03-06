let buf_1 = Buffer.alloc(10);
console.log(buf_1);

let buf_2 = Buffer.allocUnsafe(10);
console.log(buf_2);

let buf_3 = Buffer.from("Hello world!");
console.log(buf_3);

let buf_4 = Buffer.from([105, 108, 111, 118, 101, 121, 111, 117]);
console.log(buf_4.toString());

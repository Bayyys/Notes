let p1 = Promise.resolve(101); //
let p2 = Promise.resolve(
  new Promise((resolve, reject) => {
    // resolve("OK");
    reject("NO");
  })
);
console.log(p1);
console.log(p2);

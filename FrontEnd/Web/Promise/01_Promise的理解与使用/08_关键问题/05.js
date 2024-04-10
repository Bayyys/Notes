let p = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("OK");
  }, 1000);
});
p.then((value) => {
  return new Promise((resolve, reject) => {
    resolve("success");
  });
})
  .then((value) => {
    console.log(value);
  })
  .then((value) => {
    console.log(value);
  });

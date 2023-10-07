async function main() {
  const result1 = await Promise.resolve("OK");
  console.log("await1", result1); // await1 OK
  try {
    const result2 = await Promise.reject("Error");
  } catch (error) {
    console.log("await2", error); // await2 Error
  }
  const result3 = await 20;
  console.log("await3", result3); // await3 20
}

let result = main();
console.log("main()", result);  // main() Promise { <pending> }

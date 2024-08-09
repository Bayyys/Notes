function* walk(str) {
  let res = "";
  const split = [".", "-"];
  for (let i = 0; i < str.length; i++) {
    if (split.includes(str[i])) {
      yield res;
      res = "";
    } else {
      res += str[i];
    }
  }
  if (res) {
    yield res;
  }
}

const version = "v2.1.12.alpha.1";
for (let v of walk(version)) {
  console.log(v); // v2 1 12 alpha 1
}

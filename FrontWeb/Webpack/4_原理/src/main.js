import "./css/index.css";
console.log("hello world");
alert("hello world");

const sum = (...args) => {
  return args.reduce((p, c) => p + c, 0);
};

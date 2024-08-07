const str = "100000000000";

const result = str.replace(/\B(?=(\d{3})+\b)/g, ",");

console.log(result);

/(?=(\d{3})+\b)/g;

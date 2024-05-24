// 生成器
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}

const g = gen();
console.log(g.next()); // { value: 1, done: false }
console.log(g.next()); // { value: 2, done: false }
console.log(g.next()); // { value: 3, done: false }
console.log(g.next()); // { value: undefined, done: true }

// 迭代器
let set: Set<number> = new Set([1, 1, 2, 3]); // 1 2 3 [天然去重]
for (const iter of set) {
  console.log(iter);
}

let map: Map<string, number> = new Map([
  ["a", 1],
  ["b", 2],
  ["c", 3],
]);
for (const iter of map) {
  console.log(iter);
}

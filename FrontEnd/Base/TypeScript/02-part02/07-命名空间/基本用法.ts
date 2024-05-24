namespace Utils {
  let useTimes = 0;
  export const add = (a: number, b: number): number => {
    useTimes++;
    return a + b;
  };
  export const sub = (a: number, b: number): number => {
    useTimes++;
    return a - b;
  };
  export const getUseTimes = (): number => {
    return useTimes;
  };
}

Utils.add(1, 2);
console.log(Utils.getUseTimes());
Utils.sub(2, 1);
console.log(Utils.getUseTimes());

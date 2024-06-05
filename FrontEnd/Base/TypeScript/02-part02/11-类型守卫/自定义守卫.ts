const isNum = (val: any): val is number => typeof val === "number";
const isStr = (val: any): val is string => typeof val === "string";
const isBool = (val: any): val is boolean => typeof val === "boolean";
const isObj = (val: any): val is object => typeof val === "object";

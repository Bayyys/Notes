const getType = (val: Function | Date | number[]) => {
  if (typeof val === "function") {
    return "fuction";
  } else if (val instanceof Date) {
    return "Date";
  } else if (Array.isArray(val)) {
    return "Array";
  } else {
    throw new Error("unsupported type");
  }
};

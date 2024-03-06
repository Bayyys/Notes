import { ADD_PERSON } from "../constant";

const initState = [{ id: "001", name: "匿名", age: 0 }];

export default function countReducer(preState = initState, action) {
  const { type, data } = action;
  switch (type) {
    case ADD_PERSON:
      return [data, ...preState];
    default:
      return preState;
  }
}

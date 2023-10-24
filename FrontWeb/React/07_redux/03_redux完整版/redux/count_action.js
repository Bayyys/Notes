import { INCREMENT, DECREMENT } from "./constant";
export const incrementAction = (data) => ({ type: INCREMENT, data });

export const decrementAction = (data) => ({ type: DECREMENT, data });

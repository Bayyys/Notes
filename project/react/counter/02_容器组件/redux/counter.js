import { createSlice } from "@reduxjs/toolkit";

export const counterSlice = createSlice({
  name: "counter",
  initialState: {
    value: 0,
  },
  reducers: {
    /**
     * 增加
     */
    increment: (state, action) => {
      state.value += action.payload * 1;
    },
    /**
     * 减少
     */
    decrement: (state, action) => {
      state.value -= action.payload;
    },
    /**
     * 奇数增加
     */
    incrementIfOdd: (state) => {
      if (state.value % 2 !== 0) {
        state.value += 1;
      }
    },
  },
});

export const { increment, decrement, incrementIfOdd } = counterSlice.actions;

/**
 * 异步增加
 */
export const incrementAsync = (select, msTime) => (dispatch) => {
  setTimeout(() => {
    dispatch(increment(select));
  }, msTime);
};

export default counterSlice.reducer;

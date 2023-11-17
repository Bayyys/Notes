import { createSlice } from "@reduxjs/toolkit";
import menuList from "../config/menuConfig";

const keyLabel = menuList.reduce((pre, item) => {
  if (!item.children) {
    pre[item.key] = item.title;
  } else {
    item.children.forEach((cItem) => {
      pre[cItem.key] = cItem.title;
    });
  }
  return pre;
}, {});

const headTitleSlice = createSlice({
  name: "headTitle",
  initialState: {
    title: "首页",
    keyLabel: keyLabel,
  },
  reducers: {
    setHeadTitle: (state, action) => {
      state.title = state.keyLabel[action.payload];
    },
  },
});

export const { setHeadTitle } = headTitleSlice.actions;
export default headTitleSlice.reducer;

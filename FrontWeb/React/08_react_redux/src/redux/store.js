import { applyMiddleware, createStore } from "redux";

// 引入 reducer
import reducer from "./reducers";

// 引入 redux-thunk 用于支持异步 action
import thunk from "redux-thunk";

// 引入 开发者工具 redux-devtools-extension
import { composeWithDevTools } from "redux-devtools-extension";

export default createStore(
  reducer,
  composeWithDevTools(applyMiddleware(thunk))
);

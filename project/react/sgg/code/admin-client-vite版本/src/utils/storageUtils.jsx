/**
 * 1. 登陆后, 刷新后依然是已登陆状态 (维持登陆)
 * 2. 登陆后, 关闭浏览器后打开浏览器访问依然是已登陆状态 (自动登陆)
 * 3. 登陆后, 访问登陆路径自动跳转到管理界面
 */

import store from 'store';

const USER_KEY = 'user_key';

const storageUtils = {
    // 保存 user
    saveUser(user) {
        // localStorage.setItem(USER_KEY, JSON.stringify(user));
        // localStorage存在的问题: localStroage 只能保存 string, 如果传递是对象, 会自动调用对象的 toString()并保存
        store.set(USER_KEY, user);
    },

    // 读取 user
    getUser() {
        // return JSON.parse(localStorage.getItem(USER_KEY) || '{}');
        return store.get(USER_KEY) || {};
    },

    // 删除 user
    removeUser() {
        // localStorage.removeItem(USER_KEY);
        store.remove(USER_KEY);
    }
}
export default storageUtils;
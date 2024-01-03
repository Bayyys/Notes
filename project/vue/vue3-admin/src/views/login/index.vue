<template>
  <div class="login_container">
    <el-row>
      <el-col :span="12" :xs="0"></el-col>
      <el-col :span="12" :xs="24">
        <el-form
          class="login_form"
          :model="loginForm"
          :rules="loginRules"
          ref="loginFormRef"
        >
          <h1>Welcome!</h1>
          <h2>欢迎来到管理界面</h2>
          <el-form-item prop="username">
            <el-input
              v-model="loginForm.username"
              placeholder="请输入用户名"
              :prefix-icon="User"
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              v-model="loginForm.password"
              type="password"
              placeholder="请输入密码"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>
          <el-form-item>
            <el-button
              class="login_btn"
              type="primary"
              size="default"
              @click="login"
              :loading="loading"
            >
              登录
            </el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { User, Lock } from '@element-plus/icons-vue'
import { reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElNotification } from 'element-plus'
import useUserStore from '@/store/modules/user'
let $router = useRouter()
let $route = useRoute()
const userStore = useUserStore()
let loading = ref(false)
let loginFormRef = ref() // 表单ref

/**  登录表单(账号+密码)
 */
let loginForm = reactive({
  username: 'admin',
  password: 'admin',
})

/** 登录表单验证规则
 */
const loginRules = reactive({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    {
      min: 5,
      max: 20,
      message: '用户名长度在 5 到 20 个字符',
      trigger: 'blur',
    },
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    {
      min: 5,
      max: 20,
      message: '密码长度在 6 到 20 个字符',
      trigger: 'blur',
    },
  ],
})

/** 登录按钮点击回调
 * @async
 */
const login = async () => {
  loading.value = true
  await loginFormRef.value.validate() // 校验表单
  try {
    await userStore.userLogin(loginForm)
    if ($route.query.redirect)
      $router.push({ path: $route.query.redirect as string })
    else $router.push({ path: '/' })
    // ElNotification({
    //   type: 'success',
    //   message: '欢迎回来',
    //   title: `HI, ${getTimePeriod()}好`,
    // })
  } catch (error) {
    ElNotification({
      title: '登录失败',
      message: (error as Error).message,
      type: 'error',
    })
  } finally {
    loading.value = false
  }
}
</script>

<style scoped lang="scss">
.login_container {
  width: 100%;
  height: 100vh;
  background: url('@/assets/images/background.jpg') no-repeat;
  background-size: cover;
  .login_form {
    position: relative;
    width: 80%;
    top: 30vh;
    background: url('@/assets/images/login_form.png') no-repeat;
    background-size: cover;
    padding: 40px;
    h1 {
      color: white;
      font-size: 40px;
    }
    h2 {
      color: white;
      font-size: 20px;
      margin: 20px 0;
    }
    .login_btn {
      width: 100%;
    }
  }
}
</style>

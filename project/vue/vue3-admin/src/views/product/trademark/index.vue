<template>
  <div>
    <el-card>
      <!-- Card头部: 添加品牌按钮 -->
      <template #header>
        <div class="clearfix">
          <el-button type="primary" icon="Plus" @click="addTrademark">
            添加品牌
          </el-button>
        </div>
      </template>
      <!-- Card内容: 表格
      el-table: 表格主体
        border: 是否显示纵向边框
      el-table-column: 表格列
        label: 列标题
        width: 列宽度
        align: 对齐方式
    -->
      <el-table :data="trademarkArr" :style="{ width: '100%' }" border>
        <el-table-column
          type="index"
          label="序号"
          width="60px"
          align="center"
        />
        <el-table-column prop="tmName" label="品牌名称" />
        <el-table-column label="品牌logo">
          <template v-slot="{ row, $index }">
            <img
              :src="row.logoUrl"
              alt="图片加载错误"
              :index="$index"
              style="width: 100px; height: 100px"
            />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="150px">
          <template v-slot="{ row }">
            <el-button
              type="warning"
              size="small"
              icon="Edit"
              @click="updateTrademark(row)"
            ></el-button>
            <el-popconfirm
              :title="`确认删除${row.tmName}?`"
              icon="Delete"
              icon-color="red"
              @confirm="deleteTrademark(row.id)"
            >
              <template #reference>
                <el-button size="small" type="danger" icon="Delete"></el-button>
              </template>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页器 
      v-model:current-page="currentPage" 当前页码
      v-model:page-size="pageSize" 每页显示条数
      :page-sizes="[100, 200, 300, 400]" 每页显示条数选项
      :small="false" 是否使用小型分页样式[默认false]
      background 是否为分页按钮添加背景色[默认false]
      layout 分页布局，子组件名用逗号分隔[默认total, sizes, prev, pager, next, jumper](-> 表示后续右对齐)
      :total="total" 总条数
      :page-count="5" 总页数
      @size-change="handleSizeChange" 每页显示条数改变时触发
      @current-change="changePageNo" 当前页码改变时触发
    -->
      <el-pagination
        v-model:current-page="pageNum"
        v-model:page-size="pageSize"
        :page-sizes="[3, 5, 7, 9]"
        :small="true"
        :background="true"
        layout="prev, pager, next, jumper, ->, total, sizes"
        :total="total"
        @current-change="getHasTrademark"
        @size-change="getHasTrademark"
      />
    </el-card>
    <!-- Dialog: 对话框组件 -->
    <el-dialog v-model="dialogFormVisible" :title="dialog_title">
      <main>
        <el-form
          label-width="auto"
          :model="trademarkParams"
          :rules="rules"
          ref="formRef"
        >
          <el-form-item label="品牌名称" prop="tmName" label-width="100px">
            <el-input
              placeholder="请输入品牌名称"
              v-model="trademarkParams.tmName"
            ></el-input>
          </el-form-item>
          <el-form-item label="品牌logo" prop="logoUrl" label-width="100px">
            <!-- el-upload 
              action: 上传图片的请求地址
              :show-file-list: 是否显示已上传文件列表
              :before-upload: 上传文件之前的钩子, 参数为上传的文件, 若返回 false 或者 Promise 且被reject, 则停止上传
              :on-success: 文件上传成功时的钩子
            -->
            <el-upload
              class="avatar-uploader"
              action="/api/admin/product/fileUpload"
              :show-file-list="false"
              :before-upload="beforeAvatarUpload"
              :on-success="handleAvatarSuccess"
            >
              <img
                v-if="trademarkParams.logoUrl"
                :src="trademarkParams.logoUrl"
                class="avatar"
              />
              <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
            </el-upload>
          </el-form-item>
        </el-form>
      </main>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="warning" @click="reset_dialog">重置</el-button>
          <el-button type="danger" @click="cancel">取消</el-button>
          <el-button type="primary" @click="confirm">确认</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts" name="Trademark">
import { ref, onMounted, reactive } from 'vue'
import {
  reqHasTrademark,
  reqAddOrUpdateTrademark,
  reqDeleteTrademark,
} from '@/api/product_api/trademark'
import { ElMessage, FormRules } from 'element-plus'
import {
  Trademark,
  type Records,
  type TradeMarkResponseData,
} from '@/api/product_api/trademark/type'
import type { UploadProps } from 'element-plus'
// 分页器相关数据
let pageNum = ref<number>(1) // 当前页码
let pageSize = ref<number>(5) // 每页显示条数
let total = ref<number>(400) // 总条数
// 表格数据
let formRef = ref()
let trademarkArr = ref<Records>([])
// 对话框数据
let dialogFormVisible = ref<boolean>(false)
let dialog_title = ref<string>('添加品牌')
// 新增品牌数据
let trademarkParams = reactive<Trademark>({
  tmName: '',
  logoUrl: '',
})

// 封装获取品牌列表数据的方法
const getHasTrademark = async (page: number = 1) => {
  pageNum.value = page
  try {
    const res: TradeMarkResponseData = await reqHasTrademark(
      pageNum.value,
      pageSize.value,
    )
    if (res.code === 200) {
      total.value = res.data.total
      trademarkArr.value = res.data.records
    }
  } catch (error) {
    console.log(error)
  }
}

// 表单校验规则
const rules = reactive<FormRules<typeof trademarkParams>>({
  tmName: [
    { required: true, message: '请输入品牌名称', trigger: 'blur' },
    {
      validator: (_, value, callback) => {
        if (value.trim().length < 2 || value.trim().length > 8) {
          callback(new Error('品牌名称长度为2-8位'))
        } else {
          callback()
        }
      },
    },
  ],
  logoUrl: [
    {
      required: true,
      trigger: 'change',
      validator: (_, value, callback) => {
        if (value) {
          callback()
        } else {
          callback(new Error('请上传品牌logo'))
        }
      },
    },
  ],
})

// 新增品牌
const addTrademark = () => {
  dialog_title.value = '添加品牌'
  trademarkParams.id = undefined
  trademarkParams.tmName = ''
  trademarkParams.logoUrl = ''
  // 1. 使用ts的类型断言, 重置表单校验
  formRef.value?.clearValidate('tmName')
  formRef.value?.clearValidate('logoUrl')
  // nextTick(() => {
  //   // 2. 使用nextTick, 获取更新后的dom, 重置表单校验
  //   formRef.value.clearValidate('tmName')
  //   formRef.value.clearValidate('logoUrl')
  // })
  dialogFormVisible.value = true
}

// 更新
const updateTrademark = (row: Trademark) => {
  dialog_title.value = '修改品牌'
  trademarkParams.id = row.id
  trademarkParams.tmName = row.tmName
  trademarkParams.logoUrl = row.logoUrl
  formRef.value?.clearValidate('tmName')
  formRef.value?.clearValidate('logoUrl')
  dialogFormVisible.value = true
}

// 删除
const deleteTrademark = async (id: number) => {
  const res = await reqDeleteTrademark(id)
  if (res.code === 200) {
    ElMessage.success('删除成功')
    getHasTrademark(
      trademarkArr.value.length === 1 ? pageNum.value - 1 : pageNum.value,
    )
  } else {
    ElMessage.error('删除失败')
  }
}

// 对话框重置
const reset_dialog = () => {
  trademarkParams.tmName = ''
  trademarkParams.logoUrl = ''
}

// 对话框取消
const cancel = () => {
  dialogFormVisible.value = false
}

// 对话框确认
const confirm = async () => {
  // 进行全部表单校验
  await formRef.value.validate()
  const res = await reqAddOrUpdateTrademark(trademarkParams)
  if (res.code === 200) {
    ElMessage.success(`${dialog_title.value}成功`)
    dialogFormVisible.value = false
    getHasTrademark(trademarkParams.id ? pageNum.value : 1)
  } else {
    ElMessage.error(`${dialog_title.value}失败`)
  }
}

// 图片上传前的钩子
const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  if (
    rawFile.type !== 'image/jpeg' &&
    rawFile.type !== 'image/png' &&
    rawFile.type !== 'image/gif'
  ) {
    // 上传文件格式: JPG、PNG、GIF
    ElMessage.error('上传图片格式错误(仅支持JPG、PNG、GIF格式)')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    // 上传文件大小: 2MB
    ElMessage.error('上传图片大小不能超过2MB')
    return false
  }
  return true
}

// 图片上传成功的钩子
const handleAvatarSuccess: UploadProps['onSuccess'] = (response) => {
  trademarkParams.logoUrl = response.data
  formRef.value.clearValidate('logoUrl')
}

onMounted(() => {
  getHasTrademark()
})
</script>

<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>

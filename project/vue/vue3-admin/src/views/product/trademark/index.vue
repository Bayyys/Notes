<template>
  <el-card>
    <template #header>
      <!-- Card头部: 添加品牌按钮 -->
      <div class="clearfix">
        <el-button type="primary" icon="Plus">添加品牌</el-button>
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
      <el-table-column type="index" label="序号" width="60px" align="center" />
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
        <template v-slot="{ row, $index }">
          <el-button type="primary" size="small" icon="Edit"></el-button>
          <el-button type="danger" size="small" icon="Delete"></el-button>
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
      @size-change="handleSizeChange" 每页显示条数改变时触发
      @current-change="handleCurrentChange" 当前页码改变时触发
    -->
    <el-pagination
      v-model:current-page="pageNum"
      v-model:page-size="pageSize"
      :page-sizes="[3, 5, 7, 9]"
      :small="true"
      :background="true"
      layout="prev, pager, next, jumper, ->, total, sizes"
      :total="total"
    />
  </el-card>
</template>

<script setup lang="ts" name="Trademark">
import { ref, onMounted } from 'vue'
import { reqHasTrademark } from '@/api/product_api/trademark'
// 分页器相关数据
let pageNum = ref<number>(1) // 当前页码
let pageSize = ref<number>(5) // 每页显示条数
let total = ref<number>(400) // 总条数
// 表格数据
let trademarkArr = ref([])

// 封装获取品牌列表数据的方法
const getHasTrademark = async () => {
  try {
    const res = await reqHasTrademark(pageNum.value, pageSize.value)
    if (res.code === 200) {
      console.log(res.data)
      total.value = res.data.total
      trademarkArr.value = res.data.records
    }
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => {
  getHasTrademark()
})
</script>

<style scoped></style>

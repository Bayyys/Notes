<template>
  <div>
    <!-- 三级分类组件 -->
    <Category />
    <!-- 平台属性表格展示 -->
    <el-card style="margin: 10px 0px">
      <!-- Card头部: 添加品牌按钮 -->
      <template #header>
        <div class="clearfix">
          <el-button type="primary" icon="Plus">添加平台属性</el-button>
        </div>
      </template>
      <!-- 属性表格 -->
      <el-table>
        <el-table-column
          label="序号"
          type="index"
          align="center"
          width="60px"
        />
        <el-table-column label="属性名称" width="120px" />
        <el-table-column label="属性值名称" />
        <el-table-column label="操作" align="center" width="120px">
          <template v-slot="{ row }">
            <el-button type="warning" size="small" icon="Edit"></el-button>
            <el-popconfirm
              :title="`确认删除${row.tmName}?`"
              icon="Delete"
              icon-color="red"
            >
              <template #reference>
                <el-button size="small" type="danger" icon="Delete"></el-button>
              </template>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts" name="Attr"></script>

<style scoped></style>

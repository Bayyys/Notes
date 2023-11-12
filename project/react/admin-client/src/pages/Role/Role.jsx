import React, { useCallback, useEffect, useState } from "react";
import { Card, Table, Button, message } from "antd";
import { PAGE_SIZE } from "../../utils/constants";
import { reqAddRole, reqRoles } from "../../api/api";
import RoleAdd from "./RoleAdd";

export default function Role() {
  const [messageApi, contextHolder] = message.useMessage();
  const [loading, setLoading] = useState(false);
  const [roles, setRoles] = useState([]); // 所有角色的列表
  const [role, setRole] = useState({}); // 选中的角色
  const [mOpen, setMOpen] = useState(false); // 添加角色的对话框是否显示

  // 获取角色列表
  const getRoles = useCallback(async () => {
    setLoading(true);
    try {
      const result = await reqRoles();
      if (result.status === 0) {
        setRoles(result.data);
      } else {
        messageApi.error("获取角色列表失败");
      }
    } catch (error) {
      messageApi.error("获取角色列表失败");
    }
    setLoading(false);
  }, [messageApi]);

  // 表格行的点击事件
  const onRowClick = (role) => {
    return {
      onClick: () => {
        setRole(role);
      },
    };
  };

  const addRole = async (role) => {
    try {
      const result = await reqAddRole(role);
      if (result.status === 0) {
        messageApi.success("添加角色成功");
        setRoles([...roles, result.data]);
      } else {
        messageApi.error("添加角色失败");
      }
    } catch (error) {
      messageApi.error("添加角色失败");
    }
  };

  // 表格列的配置
  const columns = [
    { title: "角色名称", dataIndex: "name" },
    { title: "创建时间", dataIndex: "create_time" },
    { title: "授权时间", dataIndex: "auth_time" },
    { title: "授权人", dataIndex: "auth_name" },
  ];

  // 表格的选择框的配置
  const title = (
    <span>
      <Button
        type="primary"
        onClick={() => {
          setMOpen(true);
        }}
      >
        创建角色
      </Button>
      &nbsp;&nbsp;
      <Button type="primary" disabled={!role._id}>
        设置角色权限
      </Button>
    </span>
  );

  useEffect(() => {
    getRoles();
  }, [getRoles]);

  return (
    <Card title={title}>
      <Table
        bordered
        rowKey="_id"
        loading={loading}
        dataSource={roles}
        columns={columns}
        rowSelection={{
          type: "radio",
          selectedRowKeys: [role._id],
          onSelect: (role) => {
            setRole(role);
          },
        }}
        onRow={onRowClick}
        pagination={{ pageSize: PAGE_SIZE, showQuickJumper: true }}
      ></Table>
      <RoleAdd mOpen={mOpen} setMOpen={setMOpen} addRole={addRole} />
      {contextHolder}
    </Card>
  );
}

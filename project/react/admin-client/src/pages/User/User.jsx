import React, { useCallback, useEffect, useState } from "react";
import { Card, Table, Button, message, Popconfirm } from "antd";
import { PAGE_SIZE } from "../../utils/constants";
import { formateDate } from "../../utils/dateUtils";
import UserModal from "./UserAddUpdate";
import { reqUsers, reqDeleteUser, reqAddOrUpdateUser } from "../../api/api";

export default function User() {
  const [messageApi, messageContextHolder] = message.useMessage();
  const [loading] = useState(false); // 是否显示loading
  const [users, setUsers] = useState([]); // 所有用户的列表
  const [roles, setRoles] = useState([]); // 所有角色的列表
  const [roleNames, setRoleNames] = useState({}); // 保存角色名称的对象
  const [onUOpen, setOnUOpen] = useState(false); // 添加/修改用户的对话框是否显示
  const [user, setUser] = useState({}); // 需要修改的用户

  /**
   * 初始化角色名称
   */
  const initRoleNames = useCallback((roles) => {
    const roleNames = roles.reduce((pre, role) => {
      pre[role._id] = role.name;
      return pre;
    }, {});
    setRoleNames(roleNames);
  }, []);

  /**
   * 获取用户列表
   */
  const initUsers = useCallback(async () => {
    try {
      const result = await reqUsers();
      if (result.status === 0) {
        setUsers(result.data.users);
        initRoleNames(result.data.roles); // 初始化角色名称
        setRoles(result.data.roles);
      } else {
        messageApi.error("获取用户列表失败");
      }
    } catch (error) {
      messageApi.error("获取用户列表失败");
    }
  }, [messageApi, initRoleNames]);

  /**
   * 删除指定用户
   * @param {*} user 用户对象
   */
  const handleDelete = async (user) => {
    try {
      const result = await reqDeleteUser(user._id);
      if (result.status === 0) {
        messageApi.success(`删除用户${user.name}成功`);
        setUsers(users.filter((u) => u._id !== user._id));
      } else {
        messageApi.error("删除用户失败");
      }
    } catch (error) {
      messageApi.error("删除用户失败");
    }
  };

  const handleForm = async (user) => {
    try {
      const result = await reqAddOrUpdateUser(user);
      if (result.status === 0) {
        messageApi.success(`${user._id ? "修改" : "添加"}用户成功`);
        setOnUOpen(false);
        initUsers();
      } else {
        console.log(result);
        messageApi.error(`${user._id ? "修改" : "添加"}用户失败`);
      }
    } catch (error) {
      messageApi.error(`${user._id ? "修改" : "添加"}用户失败`);
    }
    setUser({}); // 清除user
    // setOnUOpen(false);
  };

  // 表格列的配置
  const columns = [
    { title: "用户名", dataIndex: "username" },
    { title: "邮箱", dataIndex: "email" },
    { title: "电话", dataIndex: "phone" },
    { title: "注册时间", dataIndex: "create_time", render: formateDate },
    {
      title: "所属角色",
      dataIndex: "role_id",
      render: (role_id) => {
        return roleNames[role_id];
      },
    },
    {
      title: "操作",
      render: (user) => {
        return (
          <span>
            <Button
              type="link"
              onClick={() => {
                setUser(user);
                setOnUOpen(true);
              }}
            >
              修改
            </Button>
            <Popconfirm
              title={`确认删除${user.username}吗？`}
              okText="确认"
              cancelText="取消"
              onConfirm={() => handleDelete(user)}
            >
              <Button type="link">删除</Button>
            </Popconfirm>
          </span>
        );
      },
    },
  ];

  // 表格的选择框的配置
  const title = (
    <span>
      <Button
        type="primary"
        onClick={() => {
          setUser({});
          setOnUOpen(true);
        }}
      >
        创建用户
      </Button>
    </span>
  );

  useEffect(() => {
    initUsers();
  }, [initUsers]);

  return (
    <Card title={title}>
      <Table
        bordered // 显示边框
        rowKey="_id" // 指定唯一key
        loading={loading} // 是否显示loading
        dataSource={users} // 数据源
        columns={columns} // 表格列的配置
        pagination={{ pageSize: PAGE_SIZE, showQuickJumper: true }} // 分页器
      ></Table>
      <UserModal
        open={onUOpen}
        setOpen={setOnUOpen}
        roles={roles}
        user={user}
        handleForm={handleForm}
      />
      {messageContextHolder}
    </Card>
  );
}

import React, {
  useCallback,
  useEffect,
  useLayoutEffect,
  useState,
} from "react";
import { Card, Table, Button, message } from "antd";
import { PAGE_SIZE } from "../../utils/constants";
import { reqAddRole, reqRoles, reqUpdateRole } from "../../api/api";
import RoleAdd from "./RoleAdd";
import RoleEdit from "./RoleEdit";
import { formateDate } from "../../utils/dateUtils";

export default function Role() {
  const [messageApi, contextHolder] = message.useMessage();
  const [loading, setLoading] = useState(false);
  const [roles, setRoles] = useState([]); // 所有角色的列表
  const [role, setRole] = useState({}); // 选中的角色
  const [aOpen, setAOpen] = useState(false); // 添加角色的对话框是否显示
  const [eOpen, setEOpen] = useState(false); // 设置角色权限的对话框是否显示

  useLayoutEffect(() => {
    setRole({});
  }, [roles]);

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

  const editRole = async (role) => {
    try {
      const result = await reqUpdateRole(role);
      if (result.status === 0) {
        messageApi.success("设置角色权限成功");
        setRoles(
          roles.map((item) => {
            if (item._id === role._id) {
              return result.data;
            } else {
              return item;
            }
          })
        );
      } else {
        messageApi.error("设置角色权限失败");
      }
    } catch (error) {
      messageApi.error("设置角色权限失败");
    }
  };

  // 表格列的配置
  const columns = [
    { title: "角色名称", dataIndex: "name" },
    {
      title: "创建时间",
      dataIndex: "create_time",
      render: formateDate,
    },
    { title: "授权时间", dataIndex: "auth_time", render: formateDate },
    { title: "授权人", dataIndex: "auth_name" },
  ];

  // 表格的选择框的配置
  const title = (
    <span>
      <Button
        type="primary"
        onClick={() => {
          setAOpen(true);
        }}
      >
        创建角色
      </Button>
      &nbsp;&nbsp;
      <Button
        type="primary"
        disabled={!role._id}
        onClick={() => {
          setEOpen(true);
        }}
      >
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
      <RoleAdd open={aOpen} setOpen={setAOpen} addRole={addRole} />
      <RoleEdit
        open={eOpen}
        setOpen={setEOpen}
        editRole={editRole}
        role={role}
      />
      {contextHolder}
    </Card>
  );
}

import React, { useEffect } from "react";
import { Modal, Form, Input, Spin, Tree } from "antd";
import menuList from "../../config/menuConfig";
import { useSelector } from "react-redux";
const { Item } = Form;

const initMenuList = () => {
  const treeList = [];
  treeList.push({
    title: "平台权限",
    key: "/all",
    children: menuList,
  });
  return treeList;
};

export default function RoleEdit({ open, setOpen, editRole, role }) {
  const [form] = Form.useForm();
  const [loading, setLoading] = React.useState(false);
  const [selectedKeys, setSelectedKeys] = React.useState([]); // 选中的菜单项的key数组
  const treeData = initMenuList(); // 生成树形结构的菜单列表
  const auth_name = useSelector((state) => state.user.user.username);

  const handleAddOk = async () => {
    setLoading(true);
    const { _id } = role;
    const menus = selectedKeys;
    editRole({ _id, menus, auth_name });
    setOpen(false);
    setLoading(false);
  };

  const handleOnCheck = (checkedKeys) => {
    setSelectedKeys(checkedKeys);
  };

  useEffect(() => {
    setSelectedKeys(role.menus);
  }, [role]);

  return (
    <Modal
      destroyOnClose={true}
      open={open}
      onCancel={() => {
        setOpen(false);
      }}
      onOk={handleAddOk}
      title="角色权限设置"
    >
      <Spin spinning={loading}>
        <Form form={form} preserve={false}>
          <Item label="角色名称" name="name" initialValue={role.name}>
            <Input disabled={true}></Input>
          </Item>
        </Form>
        <Tree
          treeData={treeData}
          checkable
          defaultExpandAll
          defaultCheckedKeys={role.menus}
          onCheck={handleOnCheck}
        />
      </Spin>
    </Modal>
  );
}

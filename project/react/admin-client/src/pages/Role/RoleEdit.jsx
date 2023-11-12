import React from "react";
import { Modal, Form, Input, Spin, Tree } from "antd";
import menuList from "../../config/menuConfig";
const { Item } = Form;

export default function RoleEdit({ open, setOpen, editRole, role }) {
  const [form] = Form.useForm();
  const [loading, setLoading] = React.useState(false);

  const handleAddOk = async (form) => {
    setLoading(true);
    try {
      const result = await form.validateFields();
      if (result) {
        console.log(role);
        editRole(role);
        setOpen(false);
      }
    } catch (error) {}
    setLoading(false);
  };

  const initMenuList = () => {
    const treeList = [];
    treeList.push({
      title: "平台权限",
      key: "all",
      children: menuList,
    });
    return treeList;
  };

  const treeData = initMenuList();

  return (
    <Modal
      destroyOnClose={true}
      open={open}
      onCancel={() => {
        setOpen(false);
      }}
      onOk={() => handleAddOk(form)}
      title="角色权限设置"
    >
      <Spin spinning={loading}>
        <Form form={form} preserve={false}>
          <Item label="角色名称" name="name" initialValue={role.name}>
            <Input disabled={true}></Input>
          </Item>
        </Form>
        <Tree treeData={treeData} checkable defaultExpandAll />
      </Spin>
    </Modal>
  );
}

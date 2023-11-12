// import React from "react";
// import { Form, Input, TreeSelect } from "antd";
// const { Item } = Form;

// export default function RoleAdd({ form, categorys, parentId }) {
//   const treeData = [
//     {
//       value: "一级分类",
//       title: "一级分类",
//       _id: "0",
//       items: [],
//     },
//   ];

//   treeData[0].items = categorys.map((item) => {
//     return {
//       value: item.name,
//       title: item.name,
//       _id: item._id,
//     };
//   });

// return (
//   <Form form={form} preserve={false}>
//     <Item
//       label="所属分类"
//       name="kind"
//       initialValue={
//         parentId === "0"
//           ? "一级分类"
//           : categorys.find((item) => item._id === parentId).name
//       }
//     >
//       <TreeSelect
//         treeData={treeData}
//         treeLine
//         showSearch
//         treeDefaultExpandAll
//       />
//     </Item>
//     <Item
//       label="品类名称"
//       name="name"
//       rules={[{ required: true, message: "分类名称不能为空" }]}
//     >
//       <Input placeholder="请输入分类名称"></Input>
//     </Item>
//   </Form>
// );
// }

import React from "react";
import { Modal, Form, Input, Spin } from "antd";
const { Item } = Form;

export default function RoleAdd({ mOpen, setMOpen, addRole }) {
  const [form] = Form.useForm();
  const [loading, setLoading] = React.useState(false);

  const handleAddOk = async (form) => {
    setLoading(true);
    try {
      const result = await form.validateFields();
      if (result) {
        addRole(result.name);
        setMOpen(false);
      }
    } catch (error) {}
    setLoading(false);
  };

  return (
    <Modal
      destroyOnClose={true}
      open={mOpen}
      onCancel={() => {
        setMOpen(false);
      }}
      onOk={() => handleAddOk(form)}
      title="添加角色"
    >
      <Spin spinning={loading}>
        <Form form={form} preserve={false}>
          <Item
            label="角色名称"
            name="name"
            rules={[{ required: true, message: "角色名称不能为空" }]}
          >
            <Input placeholder="请输入角色名称"></Input>
          </Item>
        </Form>
      </Spin>
    </Modal>
  );
}

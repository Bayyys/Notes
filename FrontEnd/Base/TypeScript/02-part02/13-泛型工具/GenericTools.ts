// 1. Partial<Type>: 将类型的所有属性设置为可选
interface PartialTool {
  name: string;
  age: number;
  sex: boolean;
}

type PartialToolType = Partial<PartialTool>;

// 2. Required<Type>: 将类型的所有属性设置为必选
interface RequiredTool {
  name?: string;
  age?: number;
}

type RequiredToolType = Required<RequiredTool>;

// type RequiredToolType = {
//     name: string;
//     age: number;
// }

// 3. Pick<Type, Keys>: 从类型中挑选指定的属性
interface PickTool {
  name: string;
  age: number;
  sex?: boolean;
}

type PickToolType = Pick<PickTool, "name" | "sex">;

// type PickToolType = {
//    name: string;
//    sex?: boolean | undefined;
// }

// 4. Exclude<UnionType, ExcludedUnion>: 从Type中排除ExcludedUnion
type T1 = Exclude<"a" | "b" | "c", "a">; // 'b'|'c'
type T2 = Exclude<"a" | "b" | "c", "a" | "b">; // 'c'
type T3 = Exclude<string | (() => void), Function>; // string
type T4 = Exclude<string | string[], any[]>; // string
type T5 = Exclude<(() => void) | null, Function>; // null
type T6 = Exclude<200 | 400, 200 | 201>; // 400
type T7 = Exclude<number, boolean>; // number

// 5. Omit<Type, Keys>: 从对象类型Type中排除指定的属性
interface OmitTool {
  name: string;
  age: number;
  sex?: string;
}

type OmitToolType = Omit<OmitTool, "age" | "name">;

// type OmitToolType = {
//    sex?: string | undefined;
// }

// 6. Record<Keys, Type>: 构造一个类型，其属性名的类型为Keys，属性值的类型为Type
type RecordType = Record<"name" | "age", string>;
// type RecordType = {
//    name: string;
//    age: string;
// }

// 7. ReturnType<Type>: 获取函数类型的返回值类型
// type Return1 = ReturnType<() => string>; // string

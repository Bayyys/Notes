type ParamType<T> = T extends (param: infer P) => any ? P : T;

interface User {
  name: string;
  age: number;
}
type Func = (user: User) => void;

type Param = ParamType<Func>; // Param = User
type Other = ParamType<string>; // Other = string

// 递归提取
type PromiseUser = Promise<Promise<User>>;
type RecursiveType<T> = T extends Promise<infer P> ? RecursiveType<P> : T;

type T = RecursiveType<PromiseUser>; // T = User

// 逆变 | 协变
type Bar<T> = T extends { name: infer U; age: infer U } ? U : never;
type BarType = Bar<{
  name: string;
  age: number;
  sex?: boolean;
}>; // BarType = string | number

type Foo<T> = T extends {
  a: (x: infer U) => void;
  b: (y: infer U) => void;
}
  ? U
  : never;

type FooType = Foo<{
  a: (x: string) => void;
  c: (z: number) => void;
}>; // FooType = string & number = never

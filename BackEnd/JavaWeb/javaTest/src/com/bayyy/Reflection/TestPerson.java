package com.bayyy.Reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Properties;

public class TestPerson {
    public static void main(String[] args) throws Exception {
//        Person person = new Person("Bay", 18, "China");
//        System.out.println(person);
//        mygetClass();
//        reflectOpe1();
//        reflectOpe2();
//        reflectOpe3();
//        invokeAnyTest();
        reflectOpe4();
    }

    /**
     * 获取Class对象的三种方式.
     */
    public static void mygetClass() {
        // 1. 通过类的对象获取
        Person person = new Person("Bay", 18, "China");
        Class personClass = person.getClass();
        System.out.println(personClass);
        // 2. 通过类名.class获取
        Class personClass2 = Person.class;
        System.out.println(personClass2);
        // 3. 通过Class.forName("全类名")获取
        try {
            Class personClass3 = Class.forName("com.bayyy.Reflection.Person");
            System.out.println(personClass3);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    /**
     * 使用反射获取类的名字、包名、父类、接口等.
     */
    public static void reflectOpe1() throws Exception {
        // 1. 获取类的名字
        String name = Person.class.getName();
        System.out.println(name);
        // 2. 获取包名
        Package personPackage = Person.class.getPackage();
        System.out.println(personPackage);
        // 3. 获取父类
        Class<?> superClass = Person.class.getSuperclass();
        System.out.println(superClass);
        // 4. 获取接口
        Class<?>[] interfaces = Person.class.getInterfaces();
        for (Class<?> anInterface : interfaces) {
            System.out.println(anInterface);
        }
    }

    /**
     * 使用反射获取类的构造方法、创建对象
     */
    public static void reflectOpe2() throws Exception {
        // 1. 获取类的名字
        Class<?> class1 = Class.forName("com.bayyy.Reflection.Person");
        // 2. 获取构造方法
        // 2.1 获取所有构造方法
        Constructor<?>[] cons = class1.getConstructors();
        for (Constructor<?> con : cons) {
            System.out.println(con.toString());
        }
        // 2.2 获取指定构造方法
        // 2.2.1 获取无参构造方法
        // 方法1
        Constructor<?> con1 = class1.getConstructor();
        // 使用无参构造方法创建对象
        Object obj1 = con1.newInstance();
        Person person1 = (Person) obj1;
        System.out.println(person1);
        // 方法2
        // Person lisi = (Person)class1.newInstance();   // 已弃用
        Person lisi = (Person) class1.getDeclaredConstructor().newInstance();
        System.out.println(lisi);

        // 2.2.2 获取带参构造方法
        Constructor<?> con3 = class1.getConstructor(String.class, int.class, String.class);
        Person wangwu = (Person) con3.newInstance("Bay", 18, "China");
    }

    /**
     * 使用反射获取类的方法，并调用方法.
     */
    public static void reflectOpe3() throws Exception {
        Class<?> class1 = Class.forName("com.bayyy.Reflection.Person");
        // 1. 获取所有方法
        // 1.1 getMethods()获取所有public方法，包括父类的
        Method[] methods1 = class1.getMethods(); // 只能获取public方法
//        for (Method method : methods1) {
//            System.out.println(method);
//        }
        // 1.2 getDeclaredMethods()获取所有方法，不包括父类的
        Method[] methods2 = class1.getDeclaredMethods();
//        for (Method method : methods2) {
//            System.out.println(method);
//        }
        // 2. 获取指定方法
        // 2.1 eat
        // 2.1.1 无参
        Method eatMethod = class1.getMethod("eat");
        // 调用方法
        Person zhangsan = (Person) class1.getDeclaredConstructor().newInstance();
        eatMethod.invoke(zhangsan);
        System.out.println("-------------");
        // 2.1.2 带参
        Method eatMethod2 = class1.getMethod("eat", String.class);
        // 调用方法
        Constructor con1 = class1.getConstructor(String.class, int.class, String.class);
        Person zhaoliu = (Person) con1.newInstance("赵六", 18, "China");
        eatMethod2.invoke(zhaoliu, "rice");
        System.out.println("-------------");
        // 2.2 toString
        Method toStringMethod = class1.getMethod("toString");
        // 调用方法
        Constructor<?> con = class1.getConstructor(String.class, int.class, String.class);
        Person lisi = (Person) con.newInstance("李四", 18, "China");
        String str = (String) toStringMethod.invoke(lisi);
        System.out.println(str);
        System.out.println("-------------");
        // 2.3 私有方法
        Method method = class1.getDeclaredMethod("privateMethod");
        // 调用方法
        method.setAccessible(true); // 设置访问权限
        method.invoke(lisi);
        System.out.println("-------------");
        // 2.4 静态方法
        Method staticMethod = class1.getMethod("staticMethod");
        // 调用方法
        staticMethod.invoke(null);
        // staticMethod.invoke(lisi); // 报错
        staticMethod.invoke(class1);
    }

    /**
     * 使用反射实现一个可以调用任何对象方法的通用方法.
     */
    public static Object invokeAny(Object obj, String methodName, Class<?>[] types, Object... args) throws Exception {
        // 1. 获取Class对象
        Class<?> class1 = obj.getClass();
        // 2. 获取方法
        Method method = class1.getMethod(methodName, types);
        return method.invoke(obj, args);
    }

    public static void invokeAnyTest() {
        Properties properties = new Properties();
//        properties.setProperty("name","Bay");
//        System.out.println(properties.toString());
        try {
            invokeAny(properties, "setProperty", new Class[]{String.class, String.class}, "name", "Bay");
            System.out.println(properties.toString());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    /**
     * 使用反射获取类的属性，并调用属性.
     */
    public static void reflectOpe4() throws ClassNotFoundException, NoSuchFieldException, InstantiationException, IllegalAccessException, NoSuchMethodException, InvocationTargetException {
        // 1. 获取Class对象
        Class<?> class1 = Class.forName("com.bayyy.Reflection.Person");
        // 2. 获取属性(字段) // 只能获取public属性
        Field[] fields = class1.getFields();
        System.out.println("getFields()获取public属性：");
        for (Field field : fields) {
            System.out.println(field);  // null
        }
        // 3. 获取属性(字段) // 可以获取所有属性
        Field[] fields2 = class1.getDeclaredFields();
        System.out.println("getDeclaredFields()获取所有属性：");
        for (Field field : fields2) {
            System.out.println(field);
        }
        // 4. 获取指定属性
        Field nameField = class1.getDeclaredField("name");
        // 5. 赋值
        Person zhangsan = (Person) class1.getDeclaredConstructor().newInstance();
        nameField.setAccessible(true); // 设置访问权限
        nameField.set(zhangsan, "张三");
        // 6. 获取值
        System.out.println(nameField.get(zhangsan));
    }
}

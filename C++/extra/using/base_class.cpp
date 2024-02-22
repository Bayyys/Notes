#include <iostream>
using namespace std;

class Base {
    public:
        void show() {
            cout << "Base class\n";
        }
    protected:
        int a;
};

class Derived : private Base {
    public:
    using Base::show;   // 基类成员函数
    using Base::a;  // 基类成员变量
};

int main() {
    Derived d;
    d.a = 20;
    cout << "d.a: " << d.a << endl;
    d.show();
    return 0;
}
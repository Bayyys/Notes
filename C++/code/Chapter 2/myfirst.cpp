// myfirst.cpp--显示一条消息

#include <iostream>                           // 一条预处理器编译指令 PREPROCESSOR DIRECTIVE
int main()                                    // 函数头
{                                             // 函数体开始
    using namespace std;                      // 使用名称空间
    cout << "Come up and C++ me some time.";  // 消息
    cout << endl;                             // 开始新行
    cout << "You won't regret it!" << endl;   // 更多消息
// 如果程序运行完毕后窗口自动关闭,
// 加上如下两条语句，使程序暂停，等待用户输入
    // cout << "Press any key to continue." <<endl;
	// cin.get();                                                   
    return 0;                                 // main()函数结束
}                                             // 函数体结束

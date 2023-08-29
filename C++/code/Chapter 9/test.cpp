... int global = 1000;    // 静态持续变量, 外部链接(static duration, external linkage)
static int one_file = 50; // 静态持续变量, 内部链接(static duration, internal linkage)

extern "C" void spiff(int);  // 使用C语言的函数名
extern void spiff(int);      // 使用C++语言的函数名
extern "C++" void spiff(int); // 使用C++语言的函数名

// file1.cpp 
float *p_press = new float[20];

// file2.cpp
extern *p_press;

int main()
{
    struct data
    {
        char name[30];
        mutable int accesses;
    } const data veep = {"Bayyy", 0};
    strcpy(veep.name, "Phipps"); // not allowed
    veep.accesses++;             // allowed
    ... return 0;
}
void funct1(int n)
{
    static int count = 0; // 静态持续变量, 无链接(static duration, no linkage)
    int llama = 0;        // 自动持续变量
}
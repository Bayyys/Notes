#include <iostream>
#include <sstream>
using namespace std;

/**
 * @brief 单行 m 个输入
 */
void main1() {
  int a, b;
  cin >> a >> b;
  cout << "cin: a: " << a << ", b: " << b << endl;
}

/**
 * @brief n行m个输入
 */
void main2() {
  int n, a, b;
  cin >> n;
  while (n--) {
    cin >> a >> b;
    cout << "cin: a: " << a << ", b: " << b << endl;
  }
}

/**
 * @brief  不定行m个输入(遇0截止)
 */
void main3() {
  int a, b;
  while (cin >> a >> b) {
    if (a == 0 && b == 0) break;
    cout << "cin: a: " << a << ", b: " << b << endl;
  }
}

/**
 * @brief 单行不定数量个输入
 */
void main4() {
  string str;
  int a;
  getline(cin, str);
  stringstream ss(str);  // 将字符串 str
  while (ss >> a) {
    cout << a << endl;
  }
}

/**
 * @brief 多行不定数量个输入
 */
void main5() {
  int a;
  string str;
  while (getline(cin, str)) {
    stringstream ss(str);
    while (ss >> a) {
      cout << a << endl;
    }
  }
}

/**
 * @brief n行不定数量个输入
 */
void main6() {
  int a, n;
  string str;
  cin >> n;
  while (n--) {
    getline(cin, str);
    stringstream ss(str);
    while (ss >> a) {
      cout << a << endl;
    }
  }
}

int main() {
  //   main1();
  //   main2();
  //   main3();
  //   main4();
  //   main5();
  main6();
  return 0;
}
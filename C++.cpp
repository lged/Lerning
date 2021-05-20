【GLFW配置】
1，下载GLFW：https://www.glfw.org/download.html。32-bit Windows Binaries
2，下载GLAD：https://glad.dav1d.de/。C/C++；OpenGL；Version 3.3；Core；Generate a loader >> GENERATE
3，把 GLFW、KHR、glad 三个文件夹拷贝到 vs2015/VC/include 中，glfw3.lib、glfw3dll.lib拷贝到 vs2015/VC/lib 中
4，把 glad.c 拷贝到项目并添加，(把 glfw3.dll 拷贝到 Debug/Release，好像不必要)
5，先 #include <glad/glad.h>，再 #include <GLFW/glfw3.h>。项目属性>链接器>输入>附加依赖项：glfw3.lib

【请按任意键继续】
由空项目创建的项目运行完控制台自动关闭的解决办法：项目属性>链接器>系统>子系统：控制台
如果是窗体程序不要控制台，则子系统选择窗口，并设置 高级>入口点：mainCRTStartup

【泛型】
template <class T>
class A
{
public:
    A(T v){
        cout << v << endl;
    }
};
A<char*> a("Hello");
A<int> b(10);
A<float> c(3.14);

【命名空间】
using namespace myNamaspace; 命名空间内所有可见
using myNamaspace::value; 只让某个可见
namespace mn = myNamaspace; 缩写：mn::value

【文件读写】
{
    ofstream fo;
    fo.open("d:\\ttt.txt", ios::out);
    fo << "You good!\n你好！";
    fo.close();

    vector<string> aa;
    string a;
    ifstream fi;
    fi.open("d:\\ttt.txt", ios::in);
    while(getline(fi, a, '\n'))
        aa.push_back(a);
    fi.close();
    for (int i = 0; i < aa.size(); i++)
        cout << aa[i] << endl;
}

【泛型指针】
int c = 12; 
void* p = &c; 
cout << *(static_cast<int*>(p)) <<endl;

【链表】
{
    list<int> x;
    x.push_back(135);
    x.push_back(246);
    for (list<int>::iterator i = x.begin(); i != x.end(); i++)
        cout << *i << endl;
}

【操作符重载】
C& operator > (int i); //链式编程
void operator()(int, int); //仿函数

【笔记】
父类的虚函数表示可被重写
子类必须重写父类的纯虚函数，否则也是抽象类无法实例化对象
虚析构防泄漏，干净释放堆区
void*可以存放任意对象地址，仅用于指针比较或函数IO
const只在文件内有效，多文件共享可加extern
自制代码检查器 if...=，指针是否初始化，
Linux: g++ first.cpp -o first (-lpthread 多线程) ./first
decltype(f()) a = ...; decltype(v) b = ...; decltype((v)) 双层括号永远是引用
头文件不应该包含 using
for (auto c : str) ...; 转大写 for (auto &c : str) c = toupper(c);
vector 能高效增长，定义时无需指定大小
迭代器的末尾条件判断习惯使用 != 而非 <。但凡使用了迭代器的循环体都不要向其容器添加元素
用 begin(a) end(a) 可以很方便的通过指针遍历数组，且 end(a) - begin(a) 可得出元素数量。可以 *(p + i) 或 p++ 或 p[i]
现代 C++ 应该尽量使用 vector 和迭代器，避免使用内置数组和指针；尽量使用 string，避免使用 C 风格字符串
优先使用前置递增递减 ++i --i for 中也是；*p++ 即 *(p++)
三目运算符如果在表达式中最好加上括号
逗号运算符通常用在 for (i=0; i<10; ++i, --x) 逗号优先级最低，但不低于分号?
命名的强制类型转换比旧式清晰明了 double v = static_cast<double>(3)/4; static_cast 还能转回 void* 指针，但必须确保是指针所指的类型
switch 中多个 case 共享可以写在一行，case 内定义变量应该加 {}
类定义末尾加分号，do while 末尾加分号
goto 不能绕过带初始化的变量定义
异常安全：处理异常并继续执行的话，要确保对象有效，资源无泄漏，程序处于合理状态……考虑对象无效或未完成，资源是否释放
C++ 中建议使用引用类型的形参替代指针。无需改变可声明为常量引用
因为不能拷贝数组，所以无法以值传递的方式使用数组参数，因为数组会被转换成指针。参数可以传 begin end 或 a[] size_t
int main(int argc, char *argv[]) argc数量 argv数组，也可以：int main(int argc, char **argv)；argv[0] 是程序名
函数在含有 return 的循环语句后面也要有 return，很多编译器无法发现此错误。不要返回局部对象的引用或指针
内联函数可以避免函数调用的开销，适用于规模小、流程直接、频繁调用的函数，在返回类型前加 inline。内联函数和 constexpr 函数通常定义在头文件中
assert 宏常用于检查“不能发生”的条件，仅当作调试辅助手段，如果定义了 NDEBUG 则 assert 什么也不做
函数指针 bool (*pf) (const string&, const string&); pf = &compare; &可有可无，调用时无需解引用。作为形参 void fun(const string &s1, const string &s2, bool (*pf)(const string&, const string&)); fun(s1, s2, compare);
保留默认构造函数：A() = default;
class 与 struct 定义类的唯一区别是默认的访问权限？
AA a() 会被识别为函数声明。静态成员在类外部定义时不能重复statiic
endl ends flush 都会刷新缓冲区。调试模式可以强制刷新缓冲区 cout << unitbuf ... cout << nounitbuf 以确保崩溃时输出的数据已经刷新
优先使用 vector。不需要写访问时，应该使用 cbegin cend 常量迭代器。vector deque 在首尾之外插入元素很耗时。
容器 front back at 和下标返回的都是引用，空容器使用 front() back() 属越界。不要缓存 end() 一直作为容器末尾
容器中放入值时是原对象的拷贝，与原对象无任何关联。
reserve 并不改变容器元素数量，仅影响 vector 预先分配多大内存空间。capacity 是最多可保存多少元素
成员函数返回 *this 可实现链式编程
可以这样赋值 int a(10); bool b(true);
谓词为 bool 类型的仿函数，也可用 lambda 作谓词 [](const int a, const int b) { return a > b; }
使用一个不在 map 中的关键字作为下标，会自动添加一个具有此关键字的元素。而使用 .at(k) 则会抛出 out_of_range 异常
如果关键字类型固有就是无序的，或者性能测试发现问题可以用哈希技术解决，就可以使用无序容器
new delete 非常容易出错，可使坚持只用智能指针 shared_ptr unique_ptr。如果内存耗尽时 new 会抛出 bad_alloc 异常，而 new (nothrow) 能返回一个空指针
智能指针实质就是重载了->和*操作符的类，由类来实现对内存的管理，确保即使有异常产生，也可以通过智能指针类的析构函数完成内存的释放
阻止拷贝 A(const A&) = delete; 阻止赋值 A &operator=(const A&) = delete; 使用合成的析构函数 ~A() = default;

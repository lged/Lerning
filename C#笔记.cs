#region 遍历属性
Type t = typeof(Colors);
PropertyInfo[] pInfo = t.GetProperties();
foreach (PropertyInfo pi in pInfo)
{
    Color c = (Color)ColorConverter.ConvertFromString(pi.Name);
    ……
}
#endregion


#region yield
public static IEnumerable<int> getOdds(int n)
{
    for (int i=0; i<=n; i++)
        if (i % 2 != 0)
            yield return i;
}
#endregion


#region virtual abstract
重写：virtual 在基类可实现方法，派生类可 override 重写
抽象：abstract 在基类不实现方法，派生类中必须用 override 实现，有 abstract 方法的类必须为 abstract class，且不能直接实例化
覆盖：new 定义父类的同名方法，即非 virtual 方法
#endregion


#region IDisposable
class A : IDisposable
{
    ~A()
    {
        Console.WriteLine("Deleted!");
    }
    public void Dispose()
    {
        Console.WriteLine("Disposed!");
    }
}

new A();
using (A a = new A()) 
{
}
Console.WriteLine("TEST");

输出：Disposed! TEST Deleted! Deleted!
即加了 using 的 Dispose 会最先调用，而析构函数会在最后释放类时调用
#endregion


#region 泛型
class A<T>
{
    public void Print(T v)
    {
        Console.WriteLine(v);
    }
}
A<string> a1 = new A<string>();
a1.Print("string");
A<int> a2 = new A<int>();
a2.Print(123);

public static void Print<T>(T v) //泛型方法
{
    Console.WriteLine(v);
}
Print(111);
Print("abc");

public static void Print<Ti, Tj>(Ti a, Tj b)
{
    Console.WriteLine("{0}, {1}", a, b);
}
Print(111, "abc");
#endregion


#region 让接口实现方法
interface IMy
{
}

static class MyFunc
{
    public static void Func<T>(this T obj) where T : IMy
    {
        Console.WriteLine(obj);
    }
    public static void Func<T>(this T obj, int i, int j) where T : IMy
    {
        Console.WriteLine("{0}  {1}", i, j);
    }
}

class MyClass : IMy //可同时继承某类以及多个接口的实体方法
{
    public MyClass()
    {
        this.Func();
        this.Func(12, 35);
    }
}
#endregion

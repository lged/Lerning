//遍历属性
Type t = typeof(Colors);
PropertyInfo[] pInfo = t.GetProperties();
foreach (PropertyInfo pi in pInfo)
{
    Color c = (Color)ColorConverter.ConvertFromString(pi.Name);
    ……
}


//yield
public static IEnumerable<int> getOdds(int n)
{
    for (int i=0; i<=n; i++)
        if (i % 2 != 0)
            yield return i;
}


//让接口实现方法
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

class MyClass : IMy
{
    public MyClass()
    {
        this.Func();
        this.Func(12, 35);
    }
}

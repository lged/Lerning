using System;
using System.Linq;
using System.Xml.Linq;

namespace LinqTest
{
    public class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 15, 2, 10, 11, 5, 3, 9, 7, 1 };
            var res = from i in arr where i > 3 orderby i select i;
            Console.WriteLine(string.Join(",", res.ToArray()));

            string xml = @"d:\test.xml";
            new XDocument(
                new XElement("Root",
                    new XElement("First",
                        new XElement("Item", "Text", new XAttribute("name", "tst")),
                        new XElement("Item", "Me too")
                        ),
                    new XElement("Second",
                        new XElement("Item"),
                        new XElement("Item")
                        )
                    )
                ).Save(xml);
                
            XDocument doc = XDocument.Load(xml);
            XElement root = doc.Root;
            XElement first = root.Element("First");
            foreach (XElement item in first.Elements())
            {
                Console.WriteLine(item.Value);
                if (item.Attribute("name") != null)
                    Console.WriteLine(item.Attribute("name").Value);
            }
        }
    }
}

# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
#     Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

Console.Write("Введите значения координаты X: ");
string userA = Console.ReadLine();
int a = Convert.ToInt32(userA);
Console.Write("Введите значения координаты Y: ");
string userB = Console.ReadLine();
int b = Convert.ToInt32(userB);
if (a==0 ^ b==0)
{
    System.Console.WriteLine("Введена нулевая координата");
}
else
{
    if (a>0 & b>0)
    {
        System.Console.WriteLine("Координаты первой четверти");
    }
    else
    {
        if (a<0 & b>0)
        {
            System.Console.WriteLine("Координаты второй четверти");
        }
        else
        {
            if (a<0 & b<0)
            {
                System.Console.WriteLine("Координаты третьей четверти");
            }
            else
            {
                System.Console.WriteLine("Координаты четвертой четверти");
            }
        }
    }
}

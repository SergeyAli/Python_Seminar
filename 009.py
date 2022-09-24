# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

Console.Write("Введите номер четверти: ");
string userA = Console.ReadLine();
int a = Convert.ToInt32(userA);
string[] coordinateRange = new string[] {"Введенные данные не соответствует условию" , "Диапазон первой четверти +X +Y", "Диапазон второй четверти -X +Y", "Диапазон третьей четверти -X -Y", "Диапазон четвертой четверти +X -Y"};

if ((a==1)^(a==2)^(a==3)^(a==4))
{
    System.Console.WriteLine(coordinateRange[a]);
}
else
{
    System.Console.WriteLine(coordinateRange[0]);
}

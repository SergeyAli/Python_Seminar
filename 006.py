# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

lint =
Console.Write("Введите номер дня недели: ");
string userD= Console.ReadLine();
int d = Convert.ToInt32(userD);
string[] weekDays = new string[] {"Понедельник" , "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"};
if (d==6 ^ d==7)
{
    System.Console.WriteLine($"Это Выходной день {weekDays[d-1]}");
}
else
{
    System.Console.WriteLine($"Это Рабочий день {weekDays[d-1]}");
}


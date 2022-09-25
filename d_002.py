# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import datetime
sec = 5600
minute = sec % 60
sec1 = minute % 60
hour = int(sec/3600)  # 1 hour
timeobj = datetime.time(hour, minute, sec1)
print(timeobj)

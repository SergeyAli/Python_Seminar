# 20.	Определить, присутствует ли в заданном списке строк, некоторое число

list_text = ["ffd55", "45125", "dd"]
control = '4'
for i in list_text:
    if control in i:
        print("присутствует")

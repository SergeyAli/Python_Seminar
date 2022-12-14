# 41.	Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# a.	Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

# import re
#
# actions = {
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
# }
#
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
#
#
# def my_eval(expresion: str) -> str:
#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
#
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
#
#     return expresion
#
# exp = input()
# # exp = "(1 + 4) * (5 * (10 - 2)) / 5"
# print(my_eval(exp), eval(exp))  # 40.0 40.0


# Вариант семинара

st = input()
for el in ['+', '-', '*', '/']:
    st = st.replace(el, f' {el} ')
st_list = st.split()

for i in range(len(st_list)-1):
    if st_list[i] == '*':
        result = int(st_list[i-1]) * int(st_list[i+1])
        st_list[i] = result
        st_list[i-1] = None
        st_list[i+1] = None
st_list = [el for el in st_list if el != None]

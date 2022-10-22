# import in_out
# import logger
# import ui
# import search

# def button_click():
#     ui.print_data("Вы можете: \n1. Вывести всю информацию\n2. Добавить информацию \n3. Поиск по ID")
#     user_answer = ui.input_data("Введите цифру: ")
#     print()
#     if user_answer == "1":
#         ui.print_all()
#     elif user_answer == "2":
#         id_pes = ui.input_data("Введите id: ")
#
#         data_personal = ui.add_data_pi(id_pes)
#         in_out.append_data("general_work_personnel\PI.csv.txt", data_personal)
#         logger.info_logger(f'Новая запись в таблицу "PI" {data_personal}')
#
#         data_personal = ui.add_data_Salary(id_pes)
#         in_out.append_data("general_work_personnel\Salary.csv.txt", data_personal)
#         logger.info_logger(f'Новая запись в таблицу "Salary" {data_personal}')
#
#         data_personal = ui.add_data_Department(id_pes)
#         in_out.append_data("general_work_personnel\Department.csv.txt", data_personal)
#         logger.info_logger(f'Новая запись в таблицу "Department" {data_personal}')
#
#         ui.print_data("\nДанные успешно добавлены.")
#
#     elif user_answer == "3":
#         id_pes = input("Введите id: ")
#         search.search_data(id_pes)
#         logger.info_logger(f'Запрос на поиск по ID {id_pes}')


import pandas as pd


# Load the xlsx file
excel_data_1 = pd.read_excel(r'E:\GeekBrains\08\python\Seminar\Sem\Sem_001.xlsx')
excel_data_2 = pd.read_excel(r'E:\GeekBrains\08\python\Seminar\Sem\Sem_002.xlsx')
# Read the values of the file in the dataframe
data_1 = pd.DataFrame(excel_data_1, columns=['UID', 'phone:', 'surname:', 'name:', 'patronymic:'])
data_2 = pd.DataFrame(excel_data_2, columns=['UID', 'job_title:', 'phone_vts:', 'bldg:', 'department:', 'salary:'])
# Print the content
# print("The content of the file is:\n", data)
# data_1 = pd.DataFrame(excel_data_1, columns=['surname:', 'name:', 'patronymic:'])
# data_2 = pd.DataFrame(excel_data_2, columns=['job_title:', 'bldg:', 'department:'])
# Print the content
# print("Содержимое файла:\n", data_2)

# row_1 = data_1.iloc[1]
# row_2 = data_2.iloc[1] #index=1 => second row Получить определенную строку, используя индекс
# row = [row_1, row_2]
# print(row)

row = excel_data_1.loc [:, 'phone:':'name:']
row.to_csv('WHR_2019.csv')
print(row)

import pandas as pd
# Load the xlsx file
excel_data = pd.read_excel(r'E:\GeekBrains\08\python\Seminar\Sem\Sem_001.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['UID', 'phone:', 'surname:', 'name:', 'patronymic:'])
# Print the content
print("The content of the file is:\n", data)

# row = data.iloc[1] #index=1 => second row Получить определенную строку, используя индекс
# print(row)

index = data.index

for i in index:
    print(i)
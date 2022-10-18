import pandas as pd
# Load the xlsx file
excel_data = pd.read_excel(r'E:\GeekBrains\08\python\Seminar\Sem\Sem_001.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['Sales Date', 'Sales Person', 'Amount'])
# Print the content
print("The content of the file is:\n", data)
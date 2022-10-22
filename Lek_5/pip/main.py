# from isOdd import isOdd
# # простая библиотека для проверки нечетности числа.
#
# print(isOdd(1))
# print(isOdd(4))

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt
# import numpy as np

# lists = [1, 2, 3, 2, 7]
# plt.plot(lists)

# plt.show()

# Прогресс
# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1) # Таймер ториожения, не забываем import time
#     # Do some work
#     bar.next()
# bar.finish()

# Использование Эмоджи
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))



# Отрисрвка графика

# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

# Телеграмм бот oh_my_pythen_bot_99 (oh_my_pythen_bot_99_bot)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5713892468:AAGR6Dhsmo6q3DToNEpFYXCePd5UTXx1iBw").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()


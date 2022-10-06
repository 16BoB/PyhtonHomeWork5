# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"
def filter_text(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

user_text = 'абвгдейка - абвэто передача'

print(filter_text(user_text))
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.



# str_split = input('Enter some text: ').lower().split()

# str_cnt = {}

# for i in str_split:
#     str_cnt[i] = str_cnt.get(i, 0) + 1

# print(f'Number of words in the text is: {len(str_cnt)}')    

str_split = input('Enter some text: ').lower().split()
str_cnt = set(str_split)
print(f'Number of words in the text is: {len(str_cnt)}')   
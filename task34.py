# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод: ** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам 


#check if the letter is vowel
def is_vowel(ch) -> bool: 
    vowels = "уеыаоэяиюУЕЫАОЭЯИЮeaeiouAEIOU"
    return vowels.find(ch) != -1

#number of vowels in the word input
def num_of_vowels(word: str) -> int: 
    return len([letter for letter in list(word) if is_vowel(letter)])

#checks the rythm
def is_rythm(phrases: list) -> bool: 
    return len(set([num_of_vowels(word) for word in phrases])) <= 1


phrase = input("Enter the text: ").replace("-", "").split()

if is_rythm(phrase):
    print("Парам пам-пам")
else:
    print("Пам парам")


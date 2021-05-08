def num_translate(user_num):
    """Translate user input string number from English to Russian word"""
    print(num_dictionary.get(user_num))


num_dictionary = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'
                  }
user_num = input('Enter a number from zero to ten in English: ')
num_translate(user_num)

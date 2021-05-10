def num_translate_adv(user_num):
    """Translate user input string number from English to Russian word. Advanced version"""
    print(num_dictionary.get(user_num.lower())) \
        if user_num.capitalize() != user_num \
        else print(num_dictionary.get(user_num.lower()).capitalize())


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
num_translate_adv(user_num)

from random import choice


def get_jokes(n):
    """
    the function displays jokes from three lists, a given number of times
    :param n: int
    """
    for i in range(n):
        print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input('Enter the number of jokes you want to receive: '))
get_jokes(n)

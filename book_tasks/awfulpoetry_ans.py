import sys
import random

articles = ['the', 'a']
subjects = ['cat', 'dog', 'man', 'woman']
verbs = ['sang', 'rang', 'jumped']
adverbs = ['loudly', 'quitley', 'well', 'badly']


def print_a_string(first_word, second_word, third_word):
    print(random.choice(first_word) + ' ' + random.choice(second_word) + ' ' +
                  random.choice(third_word))


try:
    number_of_strings = int(sys.argv[1])
except IndexError:
    number_of_strings = 5


for _ in range(number_of_strings):
    if random.randint(0, 1):
        print_a_string(articles, subjects, verbs)
    else:
        print_a_string(articles, verbs, adverbs)
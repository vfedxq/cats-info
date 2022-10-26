class Cats:

    species = 'cat'

    def __init__(self, name, age,color):
        self.name = name
        self.age = age
        self.color = color

jack = Cats('Jack', 10, 'White')
kevin = Cats('Kevin', 12, 'Black')
tom = Cats('Tom', 9, 'Grey')

question = int(input(
    'Please enter what you want to know?\n'
    '1. species\n'
    '2. age\n'
    '3. color\n'
    'Please enter only number: \t'
    '\n'
))

def answer():
    if question == 1:
        print('Jack is a {}'.format(jack.__class__.species))
        print('Kevin is a {}'.format(kevin.__class__.species))
        print('Tom is a {}'.format(tom.__class__.species))
    if question == 2:
        print('{} is {}'.format(jack.name, jack.age))
        print('{} is {}'.format(kevin.name, kevin.age))
        print('{} is {}'.format(tom.name, tom.age))
    if question == 3:
        print('{} is a {}'.format(jack.name, jack.color))
        print('{} is a {}'.format(kevin.name, kevin.color))
        print('{} is a {}'.format(tom.name, tom.color))
answer()

exit_ques = input(
    '\n'
    'Do you want to know anything else?\n'
    'Please write yes or no\t'
    '\n'
)

if exit_ques == 'yes':
    question = int(input(
        '\n'
        'Please enter what you want to know?\n'
        '1. species\n'
        '2. age\n'
        '3. color\n'
        'Please enter only number: \t'
        '\n'
    ))
    answer()

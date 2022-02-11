# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# #Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...


from itertools import  zip_longest


def check_gen(tutors: list, klasses: list):
    klasses_tutors = ((tutors, klasses) for (tutors, klasses) in zip_longest(tutors, klasses))
    return klasses_tutors


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
generator = check_gen(tutors, klasses)

print(generator, sep='\n')
# добавьте здесь доказательство, что создали именно генератор
      # добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
        print(next(generator))

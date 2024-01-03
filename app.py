# my_file = open("C:\\Users\\eldridge\\Documents\\private.txt" , "r")
# print(my_file.read())
# my_file.close()

from Questions import Questions

question_promts = ['What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
                   'What color are bananas?\n(a) Blue\n(b) Magenta\n(c) Yellow\n\n',
                   'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
                   ]

questions = [
    Questions(question_promts[0], 'a'),
    Questions(question_promts[1], 'c'),
    Questions(question_promts[2], 'b')
]


def run_tests(questions):
    score = 0

    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1

    print(score)


run_tests(questions)

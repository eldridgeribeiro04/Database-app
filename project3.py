import random
import time

OPERATORS = ["+", "-", "*"]
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(3, 12)
    right = random.randint(3, 12)
    operator = random.choice(OPERATORS)

    expr = str(left) + operator + str(right)
    answer = eval(expr)
    return expr, answer


input("Press any key to begin")
print("----------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-----------------------")
print("Nice job! You finished in ", total_time, "seconds!")

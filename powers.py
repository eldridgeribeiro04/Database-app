# def power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
#
# print(power(3, 2))
# username = "Eldridge, Ribeiro"
# user, _, domain = username.strip().partition(",")
#
# print("Your First name is {} and your Last name is {}".format(user, domain))
# import random
#
# number = random.randint(0, 10)
# tries = 0
#
# while tries < 3:
#     your_guess = float(input("Enter a number: "))
#     tries += 1
#
#     if your_guess > number:
#         print("A bit high, try a lower number")
#     if your_guess < number:
#         print("A little low, go higher!")
#
#     if your_guess == number:
#         break
# if your_guess == number:
#     print("Well done! Youve got it")
#
# else:
#     print("Unlucky! Try again next time.")

n = 1
i = 0
end = int(input("please give a number: "))

for i in range(0, end):
    n += i
    print(n)















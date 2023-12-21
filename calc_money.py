name = input("Enter candidates name:")
print("Rate the candidate on a scale of 1 to 10 on different aspects")
coms = float(input("How was the candidates communication skills: "))
conf = float(input("How confident was the candidate: "))
know = float(input("How much information of the job did the candidate have?: "))

total = coms+conf+know
avg = 30/2

if total > avg:
    print("Candidate suitable for the role")
else:
    print("Candidate is not suitable for the role")
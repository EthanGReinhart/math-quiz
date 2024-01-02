import random
import time

#define the variables
MIN_VALUE = 1
MAX_VALUE = 12
OPERATORS = ["+", "-", "*"]
TOTAL_PROBLEMS = 10
def generate_problem():
    first_number = random.randint(MIN_VALUE, MAX_VALUE)
    second_number = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(OPERATORS)
    equation = f"{first_number} {operator} {second_number}"
    answer = eval(equation)
    return equation, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    equation, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + str(equation) + "= ")
        if guess == str(answer):
            print("Correct!")
            break
        else:
            print("Wrong!")
            wrong += 1

end_time = time.time()
total_time = end_time - start_time
print(f"{round(total_time, 2)}s")
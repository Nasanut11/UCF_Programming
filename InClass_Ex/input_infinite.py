import random
def quiz_question():
    a = random.randint(0,100)
    b = random.randint(0,100)
    correct = False
    try:
        answer = input("What is the sum of " + str(a) + " and " + str(b) + "? (Enter 'Q' to quit) \n")
        answer = int(answer)
    except ValueError:
        if(answer == 'Q' or answer == 'q'):
            raise StopIteration
        else:
            print("Invalid input, try again")
            return quiz_question()
    if(answer == a + b):
        print("Great job")
        correct = True
    else:
        print("Try again!")
    return correct

score = 0
total = 0
while(True):
    try:
        if(quiz_question()):
            score += 1
    except StopIteration: 
        break        
    total += 1
print("You scored " + str(score) + " out of " + str(total) + " or " + str(float(score)/float(total)*100.0) + "%")
#If len(answerlist) > 3 print "YOU WIN" else "Better luck next time"
answerlist = []
correct_answer_list = []
#Q1:
def space():
    print("--------------------------------------")
def question_1():
    space()
    answer = input("Is Greenville the captiol of South Carolina? Please enter 1 for Yes or 0 for No.?")
    space()
    if answer == "1":
        answerlist.append("Question one: Sorry inorrect!")
        correct_answer_list.append("1")
        print('Correct!')
        print(answerlist)
    elif answer == "0":
        answerlist.append("Question one: Correct")
        print('wrong')
        print(answerlist)
    else:
        question_1()

question_1()
space()

#Q2:
def question_2():
    print("What continant is the larget continent in the world")
    space()
    print("A: Africal\nB: Europel\nC: North America\nD: Antarctica\nE: Asia")
    space()
    answer = input("Enter answer here: ")

    if answer == "A":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "a":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "B":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "b":
        answerlist.append("Question two: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "C":
        answerlist.append("Question two: wrong!")
        correct_answer_list.append("2")
        print("Correct!")
        print(answerlist)
    elif answer == "c":
        answerlist.append("Question two: wrong")
        correct_answer_list.append("2")
        print("Correct!")
        print(answerlist)
    elif answer == "D":
        answerlist.append("Question two: Correct!")
        print("wrong")
        print(answerlist)
    elif answer == "d":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)
    elif answer ==  "E":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)
    elif answer ==  "e":
        answerlist.append("Question two: wrong")
        print("wrong")
        print(answerlist)

    else:
        question_2()

question_2()
space()


space()

#Q3:
def question_3():
    print("What state is known as the Golden Gate State?")
    space()
    print("A: New York\nB: Florida\nC: Hawaii\nD: California ")
    answer = input("Enter answer here: ")

    if answer == "A":
        
        answerlist.append("Q3: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "a":
        answerlist.append("Q3: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "B":
        answerlist.append("Q3: f: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "b":
        answerlist.append("Q3: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "C":
        answerlist.append("Q3: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "c":
        answerlist.append("Q3: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "D":
        answerlist.append("Q3: Correct")
        correct_answer_list.append("4")
        print("Correct!")
        print(answerlist)
    elif answer == "d":
        answerlist.append("Q3: Correct!")
        correct_answer_list.append("4")
        print("Correct!")
        print(answerlist)

#Q4:
def question_4():
    print("what jungle is the largest desert in the world?")
    space()
    print("A: Baylonian\nB: Amazon\nC: Savannah\nD: Sahara")
    space()
    answer = input("Enter answer here: ")

    if answer == "A":
        answerlist.append("Q4: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "a":
        answerlist.append("Q4: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "B":
        answerlist.append("Q4: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "b":
        answerlist.append("Q4: wrong")
        print('wrong')
        print(answerlist)
    elif answer == "C":
        answerlist.append("Q4: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "c":
        answerlist.append("Q4: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "D":
        answerlist.append("Q4: wrong")
        print("wrong")
        print(answerlist)
    elif answer == "d":
        answerlist.append("Q4: wrong")
        print("wrong")
        print(answerlist)
    elif answer ==  "D":
        answerlist.append("Q4: Correct!")
        correct_answer_list.append("5")
        print("Correct!")
        print(answerlist)
    else:
        question_4()
question_4()

space()

#Q5:
def question_5():
    print("Is this how you spell MISSISSIPI? \n")
    space()
    answer = input("Enter 1 for yes or 0 for no: ")
    if answer == "1":
        answerlist.append("Q5: wrong")
        print("Incorrect")
        print(answerlist)
    elif answer == "0":
        answerlist.append("Q5:Incorrect, B!")
        correct_answer_list.append("3")
        print("Correct!")
        print(answerlist)
    else:
        question_5()

question_5()
space()





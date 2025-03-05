question=["Who was the first President of the United States?","Which planet is known as the Red Planet?","What is the capital of France?","Who wrote the play 'Romeo and Juliet'?","What is the largest ocean on Earth?","Who was the first woman to win a Nobel Prize?"]
print(question[0:1])
print("a) Abraham Lincoln\nb) George Washington\nc) John F. Kennedy\nd) Thomas Jefferson")
a= input("Select one option:\n")
if(a=="b"):
    print("The answer is correct")
    print("Lets begin to next question")
else:
    print("Wrong answer")
    print("Answer the next question")

print(question[1:2])
print("a) Earth\nb) Jupiter\nc) Mars\nd) Venus")
f= input("Select one option:\n")
if(f=="c"):
    print("The answer is correct")
    print("Lets begin to next question")
else:
    print("Wrong answer")
    print("Answer the next question")

print(question[2:3])
print("a) London\nb) Rome\nc) Berlin\nd) Paris")
b= input("Select one option:\n")
if(b=="d"):
    print("The answer is correct")
    print("Lets begin to next question")
else:
    print("Wrong answer")
    print("Answer the next question")

print(question[3:4])
print("a) Charles Dickens\nb) William Shakespeare\nc) George Orwell\nd) Mark Twain")
c= input("Select one option:\n")
if(c=="b"):
    print("The answer is correct")
    print("Lets begin to next question")
else:
    print("Wrong answer")
    print("Answer the next question")

print(question[4:5])
print("a) Atlantic Ocean\nb)Indian Ocean\nc) Arctic Ocean\nd) Pacific Ocean")
d= input("Select one option:\n")
if(d=="d"):
    print("The answer is correct")
    print("Lets begin to next question")
else:
    print("Wrong answer")
    print("Answer the next question")

print(question[5:6])
print("a) Marie Curie\nb)Florence Nightingale\nc) Mother Teresa\nd) Ada Lovelace")
e= input("Select one option:\n")
if(e=="a"):
    print("The answer is correct")
    print("And The end of quiz")
else:
    print("Wrong answer")
    print("The end of quiz")
    
if(a=="b"and f=="c"and b=="d" and c=="b" and d=="d" and e=="a"):
    print("You are the winner of \"kaun bny ga Kaoor Patti\"\nYou have won 7 Crore")
elif(a=="b"or f=="c"or b=="d" or c=="b" or d=="d" or e=="a"):
    print("You are not the winner of \"kaun bny ga Kaoor Patti\"\nBut you have given correct answers of some questions so You have won 1 Crore")
else:
    print("Aby ja BSDk tery bs ki baat ni crore patti bnnna!")
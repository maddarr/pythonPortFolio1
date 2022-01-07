import random
question = 0
correct_answers = 0


def title():
    

    title = """
  ====     ===========   ===   ===   =======     ===   ====         ===   ==   ===     ===     ==     ==     ====
 =======   ===========   ===   ===   =========   ===   ======       ===   ==   ===     ===     ==     ==    ======
==     ==      ===       ===   ===   ===   ===   ===   ===  ==      ===  ====  ===    == ==    ==     ==   ==     ==
==     ==      ===       ===   ===   ===    ==   ===   ===  ===     ===  ====  ===    == ==    ==     ==    ==    ==
  ===          ===       ===   ===   ===   ===   ===   ===   ===    ===  ====  ===   ==   ==    =======      ===
   ===         ===       ===   ===   =======     ===   ===   ===    === ====== ===  =========   =======       ===
    ===        ===       ===   ===   ======      ===   ===   ===    ==============  =========     ===           ===
     ===       ===       ===   ===   ===         ===   ===   ===    ==============  ===   ===     ===            ===
==    ===      ===       ===   ===   ===         ===   ===  ===     =====    =====  ===   ===     ===      ==     ===
==    ===      ===       =========   ===         ===   ===  ==      ====      ====  ===   ===     ===      ==    ===
 =======       ===        =======    ===         ===   ======       ===        ===  ===   ===     ===       =======
  ====         ===         =====     ===         ===   ====         ===        ===  ===   ===     ===         ====
  
                               ===========     ====         =====       ===     ==========
                               ===========    ======        ======      ===     ==========
                                   ===       ===  ===       ===  ==     ===     ===
                                   ===      ===    ===      ===  ===    ===     ===
                                   ===      ===    ===      ===   ===   ===     ========
                                   ===      ===    ===      ===   ===   ===     ========
                                   ===      ===    ===      ===   ===   ===     ===
                                   ===       ===  ===       ===  ===    ===     ===
                                   ===       =======        ===  ==     ===     ===========
                                   ===        =====         =====       ===     ===========
                                    
                                    

"""
    
    print(title)
    
title()

name = input("What is your name: ")
print("Welcome to the game Stupid Ways To Die, " + name + ".")
print("""
In this game you will be presented with 5 statements on a person and the way they supposedly died, it is your job to guess it the way described is True or False. If you get all of the answers correct you WIN, if you get either 3 or 4 correct you PASS but if you get less than 3 correct you FAIL.

Are you ready?

Here is your First Question...


""")

questions = {"Robert Taylor died in the grave he was digging at work?": True, "Wolfgang Amadeus Mozart died of Strep Throat?": True, "Tennessee Williams choked to death after inhaling a small plastic bottle cap": True, "Gordon L Harwell, aka Unckle Ben fell into a silo of his own rice and suffocated?": False, "Maria Connor died after a camel bit her on the face and its saliva entered the wound making it deadly toxic": False, "Jasper Vinall died by being struck in the forehead by a cricket bat being swung by the batsman trying to hit the ball a second time": True, "Alex Josey died by taking a drink servers tray as a snow sled and sliding off a 200ft cliff": False, "Adam Ricket died by choking on ramen noodles he stole from another in-mate, after his death penalty was commuted to life in prison": False, "Arius, died in 336AD after suffering from intense diarrhea, hemoraging and then expulsion of his lower intestines": True, "Cristopher Cole, a UK pop singer died by lighting stike on a golf coarse": False, "Sylvester Paul was a fruit and veggie vendor that died by being pummeled to death by a veggie pyramid display": False, "Catherine Macnamara died in after asking , Wonder who will be next, at a funeral. And was then overcome with a fatal seizure": True} 



def random_questions():
   # question += 1
    correct_answers = 0
    quest = random.choice(list(questions.items()))
    print(quest[0])
    answer = quest[1]
    question_answer = input("Type (True) or (False) below for your answer: ")
    if question_answer == answer:
       correct_answers += 1
       print("You are correct!!  great job!!")
        #question += 1
    else: correct_answers += 0
    print("Oh Im sorry that was incorrect")
        
        #    question += 1
        
 
    
random_questions()


print("You have " + str(correct_answers))

next_question = input("ready to move on?: ")
if next_question == "Yes":
    random_questions()
else: print("OK")

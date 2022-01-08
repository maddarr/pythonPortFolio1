import random
import sys

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

questions = {"""Robert Taylor died in the grave he was digging at work?""": True, """Wolfgang Amadeus Mozart died of Strep Throat?""": True, """Tennessee Williams choked to death after inhaling a small plastic bottle cap""": True, """Gordon L Harwell, aka Unckle Ben fell into a silo of his own rice and suffocated?""": False, """Maria Connor died after a camel bit her on the face and its saliva entered the wound making it deadly toxic""": False, """Jasper Vinall died by being struck in the forehead by a cricket bat being swung by the batsman trying to hit the ball a second time""": True, """Alex Josey died by taking a drink servers tray as a snow sled and sliding off a 200ft cliff""": False, """Adam Ricket died by choking on ramen noodles he stole from another in-mate, after his death penalty was commuted to life in prison""": False, """Arius, died in 336AD after suffering from intense diarrhea, hemoraging and then expulsion of his lower intestines""": True, """Cristopher Cole, a UK pop singer died by lighting stike on a golf coarse""": False, """Sylvester Paul was a fruit and veggie vendor that died by being pummeled to death by a veggie pyramid display""": False, """Catherine Macnamara died in after asking , Wonder who will be next, at a funeral. And was then overcome with a fatal seizure""": True, """Nikolai Yezhov imprisoned and executed hundreds of Russians for just speaking poorly of Stalin, but was then himself executed for the same thing""": True, """Ray Murhy died by choking on a banana during a Banana eating competition""": False, """Tim Hoyle was a fire eater in the UK who had recently taken up sword swallowing. He died when he cut a main artery while swallowing a sword infront of 350 people in Bridlington, England""": False, """Dan Anderson, an acclaimed author in Sweeden died from a hotel cleaning. After checking into a room that had just been cleaned for bed bugs with hydrogen cyanide""": True, """Carlos Nyuri lived in Mozambique, after hearing from the locals crocodile bile was a natural aphrodisiac he brewed his own homemade beer. He shared the beer at a local festival, not realizing that the crocodile bile was poisonous. His beer killed 37 people, including himself.""": False, """Judy Sheppard suffered from trichophagia, (the compulsive eating of ones own hair). On her 21st birthday, she was rushed to the hospital with severe stomach pains, only to die in surgery that day. Surgeons had removed a 9lb hairball from her stomach.""": False, """Sprinkles The Clown loved making people laugh, but the day his after teasing an older Tigress in his act for too long, Sprinkles was mauled to death in front of a live crowd.""": False 
} 











def move_on():
    global question
    if question < 5:
        next_question = input("ready to move on?: ")
        print("")
        if next_question == "Yes" or next_question == "Y" or next_question == "y" or next_question == "yes":
            random_questions()
        else:
            print("OK") 
            print("")
            print("Thanks for playing Stupid Ways To Die")
            print(
            """
            
            Would you Like to Play again? 
            
            
                  """)
            play_again = input("Type Y or N: ")
            if play_again == "Y" or play_again == "y":
               print("Type - run StupidWays.py - in the console")
               sys.exit()
            else: 
                sys.exit()
            
    else:
        if correct_answers < 3:
            fail_quiz()
            sys.exit()
        elif correct_answers <= 4:
            pass_quiz()
            sys.exit()
        elif correct_answers == 5:
            win_quiz()
            sys.exit()
        else: 
            sys.exit()         
            
            

def fail_quiz():
    global correct_answers
    print("Sorry you didnt get enough to even Pass, you only got " + str(correct_answers) + " out of 5")
    print(
"""
     ==========     =====      ===     ===
     ==========    =======     ===     ===
     ===          ==== ====    ===     ===
     ===         ====   ====   ===     ===
     ======      ===========   ===     ===
     ======      ===========   ===     ===
     ===         ===     ===   ===     ===
     ===         ===     ===   ===     ===========
     ===         ===     ===   ===     ===========
     
     
""")
    sys.exit()


def pass_quiz():
    global correct_answers
    print("Not too bad, you Passed but only got " + str(correct_answers) + " out of 5")
    print(
"""
     ==========        =====          =====          =====
     ===========      =======        ========       ========
     ===     ===     ==== ====      ===    ==      ===    ==
     ===     ===    ====   ====     ===            ===
     ==========     ===========       ===            === 
     =========      ===========         ===            ===
     ===            ===     ===     ==    ===      ==    ===
     ===            ===     ===     ========       ========
     ===            ===     ===      =====           =====

""")
    sys.exit()
    
    
def win_quiz():
    global correct_answers
    print("CONGRATULATIONS!!! you Won!!! , you got " + str(correct_answers) + " out of 5 ")
    print(
"""
     ===   ==   ===    ===    =====      ===    ===
     ===  ====  ===    ===    ======     ===    ===
     ===  ====  ===    ===    === ===    ===    ===
     === ====== ===    ===    ===  ===   ===    ===
     ======  ======    ===    ===   ===  ===    ===
     =====    =====    ===    ===    === ===
     ====      ====    ===    ===     ======    ===
     ===        ===    ===    ===      =====    ===
        
"""
        )
    sys.exit()
    

def random_questions():
    global question
    global correct_answers
    question += 1
    while question <= 5:
        quest = random.choice(list(questions.items()))
        print(quest[0])
        answer = str(quest[1])
        question_answer = input("Type (True) or (False) below for your answer: ")
        if question_answer == "True" or question_answer == "true" or question_answer == "T" or question_answer == "t":
            question_answer = "True"
        elif question_answer == "False" or question_answer == "false" or question_answer == "F" or question_answer == "f":
            question_answer = "False"
        else:
            question_answer = "Wrong"
        
        if question_answer == answer:
            correct_answers += 1
            print("You are correct!!  great job!!")
            print("You have " + str(correct_answers) + " correct answers")
            move_on()
        else:
            print("Oh Im sorry that was incorrect")
            move_on()
    if correct_answers < 3:
        fail_quiz()
        sys.exit()
    elif correct_answers <= 4:
        pass_quiz()
        sys.exit()
    elif correct_answers == 5:
        win_quiz()
        sys.exit()
    else: sys.exit()
 
    
random_questions()





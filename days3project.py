#days 3 create treasure island with ascii
print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************'''
)

print("Welcome to the golden dungeon")
print(
    '''Suddenly there was a guide with an ascetic-like form wearing a black robe with his face covered by a robe and he said:
Welcome to the chosen one ...and congratulations to you because you have the opportunity to get the treasure. to get it you have to answer 3 questions and where there can be no wrong answers if you are wrong then you will die ...
'''
)
question = input("do you still want to continue [Y/N]? ")
if question == "y" or question == "Y":
    # Question number one
    print("\nQUESTION NUMBER ONE:")
    question_one = input("what is opposite of benzino? ")
    
    if question_one == "a giraffe" or question_one == "giraffe":
        print("cheongdamm!!")
        
        # Question number two - akan dijalankan hanya jika jawaban pertanyaan pertama benar
        print("\nQUESTION NUMBER TWO:")
        question_two = input("agus dibalik jadi?: ")
        
        if question_two == "ketapel" or question_two == "Ketapel":  
            print("Correct!!")
    
        # Question number three - akan dijalankan hanya jika jawaban pertanyaan kedua benar   
            print("\nQUESTION NUMBER THREE:")
            question_three = input("name 10 pi numbers? ") 

            if question_three == "3.1415926535" or question_three == "3.1415926535":
                print("Correct!!")
                print("Congratulations you have passed all the questions and you have the right to get the treasure")
            else:
                print("wrong..you will die!!")
        else:
            print("Wrong answer for question!..you will die!!")

    else:
        print("wrong..you will die!!")
else:
    print("you are coward!")


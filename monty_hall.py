import random,sys
ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""
SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""
THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""
FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""


swapWins = 0
swapLosses = 0
ogWins = 0
ogLosses = 0

while True:
    doorwithcar=random.randint(1,3)
    print(ALL_CLOSED)
    while True:
        input_number=int(input("Enter a door number 1,2,3 or 0 to exit : "))
        if input_number in range (1,4) :
            user_door=input_number
        else:
            print("Thanks for playing")
            sys.exit()
        if doorwithcar==1 and user_door==1:
            doorshown=random.choice([2,3])
            if doorshown==2:
                print(SECOND_GOAT)
            else:
                print(THIRD_GOAT)
        elif doorwithcar==1 and user_door==2:
            doorshown=3
            print(THIRD_GOAT)
        elif doorwithcar==1 and user_door==3:
            doorshown=2
            print(SECOND_GOAT)
        elif doorwithcar==2 and user_door==1:
            doorshown=3
            print(THIRD_GOAT)
        elif doorwithcar==2 and user_door==2:
            doorshown=random.choice([1,3])
            if doorshown==1:
                print(FIRST_GOAT)
            else:
                print(THIRD_GOAT)
        elif doorwithcar==2 and user_door==3:
            doorshown=1
            print(FIRST_GOAT)
        elif doorwithcar==3 and user_door==1:
            doorshown=2
            print(SECOND_GOAT)
        elif doorwithcar==3 and user_door==2:
            doorshown=1
            print(FIRST_GOAT)
        elif doorwithcar==3 and user_door==3:
            doorshown=random.choice([1,2])
            if doorshown==1:
                print(FIRST_GOAT)
            else:
                print(SECOND_GOAT)
        else:
            print("ERROR")

        swap=input("Do you want to swap (Y?N)")
        if swap.upper()=="Y":
            if user_door==1 and doorshown==2:
                user_door=3
            elif user_door==1 and doorshown==3:
                user_door=2
            elif user_door==2 and doorshown==1:
                user_door=3
            elif user_door==2 and doorshown==3:
                user_door=2
            elif user_door==3 and doorshown==1:
                user_door=2
            elif user_door==3 and doorshown==2:
                user_door=1
            else:
                print("ERROR")

        if doorwithcar==user_door and swap.upper()=='Y':
            swapWins+=1
            print("You won!")
        elif doorwithcar==user_door and swap.upper()=='N':
            ogWins+=1
            print("You won!")
        elif doorwithcar!=user_door and swap.upper()=="Y":
            swapLosses+=1
        elif doorwithcar!=user_door and swap.upper()=="N":
            ogLosses +=1

        print("""Thanks for playing !\n
wins after swapping: {}
wins without swapping:{}
losses with swapping:{}
losses without swapping:{}\n""".format(swapWins,ogWins,swapLosses,ogLosses))

        if swapWins !=0 or swapLosses!=0:
            successrateswaps=round((swapWins/(swapWins+swapLosses))*100,1)
        else:
            successrateswaps=0
        if ogWins !=0 or ogLosses !=0:
            successrateog=round((ogWins/(ogWins+ogLosses))*100,1)
        else:
            successrateog=0

        print("""Success rate for swap {}
Success rate without swapping {}""".format(successrateswaps,successrateog))
        
        
        
        if doorwithcar==1:
            
            print(FIRST_CAR_OTHERS_GOAT)
            print("The car was in room 1")
        elif doorwithcar==2:
            
            print(SECOND_CAR_OTHERS_GOAT)
            print("The car was in room 2")
        else:
            print(THIRD_CAR_OTHERS_GOAT)
            print("The car was in room 3")
            

        
        

    
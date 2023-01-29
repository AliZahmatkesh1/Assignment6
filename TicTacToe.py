from colorama import *
init()
""" You need to install the colorama library
    Install the library
    Type in CMD ( pip install colorama )
"""

list = [ ["-" , "-" , "-"] ,
         ["-" , "-" , "-"] ,
         ["-" , "-" , "-"] ]


#show print
def show() :
    print()
    for i in list :
        for o in i :
            if o == "-" : 
                print (o, end= "   ")
            elif o == "X" :
                print (Fore.BLUE+o, Fore.RESET, end= "  ")
            elif o == "O" :
                print (Fore.RED+o, Fore.RESET, end= "  ")


        print("\n")
    print()

#chek X $ O
def chek (a,c) :
    if a > 0 and a < 10 :
        if a == 1 :
            a , b = 0 , 0
        elif a == 2 :
            a , b = 0 , 1
        elif a == 3 :
            a , b = 0 , 2
        elif a == 4 :
            a , b = 1 , 0
        elif a == 5 :
            a , b = 1 , 1
        elif a == 6 :
            a , b = 1 , 2
        elif a == 7 :
            a , b = 2 , 0
        elif a == 8 :
            a , b = 2 , 1
        elif a == 9 :
            a , b = 2 , 2
        if list[a][b] == "-" :
            if c == 1 :
                list[a][b] = "X"
                return True
            elif c == 2 :
                list[a][b] = "O"
                return True
        else :
            return False
    else :
        return "n"


#chek 3 line
def chek_doz():

    c = 0

    for i in range(0 ,3) :
        l = list[i][0]
        l1 = list[i][1]
        l2 = list[i][2]
        if (l == "X" and l1 == "X" and l2 == "X") or (l == "O" and l1 == "O" and l2 == "O") :
            return True

    for j in range(0 ,3) :
        l = list[0][j]
        l1 = list[1][j]
        l2 = list[2][j]
        if (l == "X" and l1 == "X" and l2 == "X") or (l == "O" and l1 == "O" and l2 == "O" ) :
            return True

    if (list[0][0] == "X" and list[1][1] == "X" and list[2][2] == "X") or (list[0][0] == "O" and list[1][1] == "O" and list[2][2] == "O"):
        return True
    elif (list[0][2] == "X" and list[1][1] == "X" and list[2][0] == "X") or (list[0][2] == "O" and list[1][1] == "O" and list[2][0] == "O") :
        return True
    
    for a in list :
        for b in a :
            if b != "-" :
                c += 1
            if c == 9 :
                return "baz"

#player1
def player1 () :

    print (Fore.BLUE+"player 1", Fore.RESET)
    p1 = int(input("Enter namber : "))
    
    
    if chek(p1 , 1) == True:
        if chek_doz() == True:
            print("\n")
            print(Style.BRIGHT+Back.BLUE+Fore.WHITE+"========barande========"+Style.RESET_ALL +Back.RESET+ Fore.RESET)
            print("\n")
            show()
            return True

        elif chek_doz() == "baz" :
            print("\n")
            print(Style.BRIGHT+Back.YELLOW+Fore.WHITE+"kasi barande nashod ! "+Style.RESET_ALL +Back.RESET+ Fore.RESET)
            print("\n")
            show()
            return True
        show()
    elif chek(p1 , 1) == "n":
        print (Fore.YELLOW+"\nadad bayad beyne 1 ta 9 bashad .\ndobare !\n", Fore.RESET)
        player1()

    else:
        print (Fore.YELLOW+"\nIn khone ghablan entekhab shode.\ndobare !\n", Fore.RESET)
        player1()



#player2
def player2 () :
    print (Fore.RED+"player 2", Fore.RESET)
    p1 = int(input("Enter namber : "))

    if chek(p1 , 2) == True :
        if chek_doz() == True :
            print("\n")
            print(Style.BRIGHT+Back.RED+Fore.WHITE+"========barande========"+Style.RESET_ALL +Back.RESET+ Fore.RESET)
            print("\n")
            show()
            return True

        elif chek_doz() == "baz" :
            print("\n")
            print(Style.BRIGHT+Back.YELLOW+Fore.WHITE+"kasi barande nashod ! "+Style.RESET_ALL +Back.RESET+ Fore.RESET)
            print("\n")
            show()
            return True
        show()
    elif chek(p1 , 1) == "n":
        print (Fore.YELLOW+"\nadad bayad beyne 1 ta 9 bashad .\ndobare !\n", Fore.RESET)
        player2()

    else :
        print (Fore.YELLOW+"\nIn khone ghablan entekhab shode.\ndobare !\n", Fore.RESET)
        player2()

# Question Exit
def exit_cont () :
    print(Style.BRIGHT+Back.LIGHTRED_EX+"aya edame midahid? ( y/n )",Style.RESET_ALL ,Back.RESET , end= " ")
    a = input().lower().strip()
    return a
    
show()
while True :

    if player1() :
        list = [["-" , "-" , "-"] ,
                ["-" , "-" , "-"] ,
                ["-" , "-" , "-"] ]
        if exit_cont() == "y" :
            show()
            continue
        else : break
        
    if player2() :
        list = [["-" , "-" , "-"] ,
                ["-" , "-" , "-"] ,
                ["-" , "-" , "-"] ]
        if exit_cont() == "y" :
            show()
            continue
        else : break

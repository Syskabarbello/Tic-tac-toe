import random
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []
d={}

for key in theBoard:
    board_keys.append(key)



def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():
    play1=str(input('PLAYER1 NAME-'))
    print('GREETINGS!',play1)
    play2=str(input('PLAYER2 NAME-'))
    print('GREETINGS!',play2)
    lst=['X','O']
    r=random.choice(lst)
    print(play1,'You are',str(r),'FROM NOW ON YOU WOULD BE DENOTED BY THIS CHARACTER')
    d[play1]=str(r)
    lst.remove(r)
    print(play2,'You are',(lst[0]),'FROM NOW ON YOU WOULD BE DENOTED BY THIS CHARACTER')
    d[play2]=lst[0]
    turn = 'X'
    count = 0
    flag=1


    while flag==1:
        printBoard(theBoard)
        print("""
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9
THE NUMBERS IN THE ABOVE GRID DENOTE THE POSITIONS""")
        print("It's your turn",turn,".Move to which place?")

        move = input('Position-')
        if int(move)<=0 or int(move)>9:
            print('WRONG INPUT!!!')
            continue

        if theBoard[move] == ' ':
             theBoard[move] = turn
             count += 1
        else:
            print("That place is already filled.")
            continue

        
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

        
        if count==9:
           print("\nGame Over.\n")                
           print("It's a Tie!!")
           break


        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
   

    restart = input("Do want to play Again?(y/n)")
    if restart=='n' or restart=='N':
        print("THANK YOU!!HAVE A NICE DAY...")
       
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

   
if __name__ == "__main__":
    game()

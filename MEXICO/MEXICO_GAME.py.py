from mexico_pkg.users import Players
from mexico_pkg.dice import Die
from mexico_pkg.game_logic_funcs import four_players, three_players, two_players 


#intro
print("+-----+  +-----+  +-----+  +-----+  +-----+  +-----+ " )
print("|     |  | o   |  | o   |  | o o |  | o o |  | o o | " )
print("|  o  |  |     |  |  o  |  |     |  |  o  |  | o o | " )
print("|     |  |   o |  |   o |  | o o |  | o o |  | o o | ")
print("+-----+  +-----+  +-----+  +-----+  +-----+  +-----+ ")
print("***************************************************")
print("**Hello and welcome to Jordon's 'Mexico' dice game**")
print("****************************************************")
print("***********Each turn all players roll***************")
print("***********Players start with 6 lives***************")
print("***********Lowest roller of each round**************")
print("******************Loses a life**********************")
print("***********Players start with 6 lives***************")
print("**********************Enjoy*************************")
print("****************************************************")
print("How many players will be playing?*******************")

#while loop for player selection
while True:
    print("****************************************************")
    player_choice = input("Please enter 1, 2, 3 or 4 only")
    if player_choice == '1' or player_choice == '2' or player_choice == '3' or player_choice == '4':
        amount_of_players = int(player_choice)

      
        if amount_of_players == 1: #for one player, playing against the computer
            comp_player = Players("Computadora", 6)
            print("*************************************************")
            player1 = Players(input("Player 1 enter your name:"), 6) #calling the player class adding
            print("*************************************************") #6 lives
            print(f'{player1.name} will be playing against {comp_player.name}')
            break

        if amount_of_players == 2: #for two players
            player1 = Players(input("Player 1 enter your name:"), 6)
            player2 = Players(input("Player 2 enter your name:"), 6)
            print("*************************************************")
            print(f'{player1.name}, {player2.name} Good luck to you both!')
            print("*************************************************")
            break

        if amount_of_players == 3: #for 3 players
            player1 = Players(input("Player 1 enter your name:"), 6)
            player2 = Players(input("Player 2 enter your name:"), 6)
            player3 = Players(input("Player 3 enter your name:"), 6)
            print("*************************************************")
            print(f'{player1.name}, {player2.name}, {player3.name}, Good luck Players!')
            print("*************************************************")
            break

        if amount_of_players == 4: #for 4 players
            player1 = Players(input("Player 1 enter your name:"), 6)
            player2 = Players(input("Player 2 enter your name:"), 6)
            player3 = Players(input("Player 3 enter your name:"), 6)
            player4 = Players(input("Player 4 enter your name:"), 6)
            print("*************************************************")
            print(
                f'{player1.name}, {player2.name}, {player3.name}, {player4.name}, Good luck Players!')
            print("*************************************************")
            break

        else:
            print("*************************************************")
            print("Game only supports 4 players")                     #prints invalid input 
            print("Please enter 1 , 2 , 3 or 4")                      #instructions 
            print("*************************************************")

print("All Players Roll. Highest dice goes first")
print("*************************************************")
play = input("Press Enter to start the game or 'q' to quit")
print("*************************************************")

while play.lower() != 'Q': #while loop to see who goes first.


    if amount_of_players == 1:
        player1_roll = Die.roll(player1) #calling dice class
        comp_player_roll = Die.roll(comp_player) 

        while player1_roll == comp_player_roll: #while loop to handle equal value rolls
            player1_roll = Die.roll(player1)    #game will not show equal values
            comp_player_roll = Die.roll(comp_player)
            break

        if player1_roll > comp_player_roll: #conditional to show who wins the first roll and goes first
            print("************************************************************")
            print(f'{player1.name} you rolled a {player1_roll} \n{comp_player.name} you rolled a {comp_player_roll}.')
            print("************************************************************")
            print(f'{player1.name} you go first.')
            two_players(player1,6, comp_player,6) #function call for game logic
            print("Goodbye! ;)")
            break
            
        else:
            print("************************************************************")
            print(f'{comp_player.name} you rolled a {comp_player_roll} \n{player1.name} you rolled a {player1_roll}.')
            print("************************************************************")
            print(f'{comp_player.name} you go first.')
            two_players(player1,6, comp_player,6) #function call for game logic
            print("Goodbye! ;)") 
            break
            
    if amount_of_players == 2: #conditional to show who wins the first roll and goes first
        player1_roll = Die.roll(player1) #calling dice class
        player2_roll = Die.roll(player2)

        while player1_roll == player2_roll: #while loop to handle equal value rolls
            player1_roll = Die.roll(player1)#calling dice class
            player2_roll = Die.roll(player2)
        

        if player1_roll > player2_roll: # conditional for who goes first

            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player1.name} you go first.')
            two_players(player1,6, player2,6) #function call for game logic
            break
        else:
            print(
                f'{player2.name} you rolled a {player2_roll} \n{player1.name} you rolled a {player1_roll}.\n {player2.name} you go first.')
            two_players(player1,6, player2,6) #function call for game logic
            break

    if amount_of_players == 3: #conditional to show who wins the first roll and goes first
        player1_roll = Die.roll(player1)#calling dice class
        player2_roll = Die.roll(player2)
        player3_roll = Die.roll(player3)

        while player1_roll == player2_roll or player1_roll == player3_roll or player2_roll == player3_roll:
            player1_roll = Die.roll(player1)#calling dice class
            player2_roll = Die.roll(player2)
            player3_roll = Die.roll(player3)
            

        if player1_roll > player2_roll and player1_roll > player3_roll:

            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.')
            print(f'{player1.name} you roll first')
            three_players(player1,6,player2,6,player3,6) #function call for game logic
            print("GoodBye!!")
            break
        elif player2_roll > player1_roll and player2_roll > player3_roll:
            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.')
            print(f'{player2.name} you roll first')
            three_players(player1,6,player2,6,player3,6) #function call for game logic
            break
        else:
            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.')
            print(f'{player3.name} you roll first')
            three_players(player1,6,player2,6,player3,6) #function call for game logic
            break

    if amount_of_players == 4:
        player1_roll = Die.roll(player1)#calling dice class
        player2_roll = Die.roll(player2)
        player3_roll = Die.roll(player3)
        player4_roll = Die.roll(player4)

        while player1_roll == player2_roll or player1_roll == player3_roll or player2_roll == player3_roll or player4_roll == player1_roll or player4_roll == player2_roll or player4_roll == player3_roll:
            player1_roll = Die.roll(player1)#calling dice class
            player2_roll = Die.roll(player2)
            player3_roll = Die.roll(player3)
            player4_roll = Die.roll(player4)
            

        if player1_roll > player2_roll and player1_roll > player3_roll and player1_roll > player4_roll:
            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.\n {player4.name} you rolled a {player4_roll}')
            print(f'{player1.name} you roll first')
            four_players(player1, 6, player2, 6, player3, 6, player4, 6) #function call for game logic
            break
        

        elif player2_roll > player1_roll and player2_roll > player3_roll and player2_roll > player4_roll:
            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.\n {player4.name} you rolled a {player4_roll}')
            print(f'{player2.name} you roll first')
            four_players(player1, 6, player2, 6, player3, 6, player4, 6) #function call for game logic
            break
            

        elif player3_roll > player1_roll and player3_roll > player2_roll and player3_roll > player4_roll:
            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.\n {player4.name} you rolled a {player4_roll}')
            print(f'{player3.name} you roll first')
            four_players(player1, 6, player2, 6, player3, 6, player4, 6) #function call for game logic
            break
            

        elif player4_roll > player1_roll and player4_roll > player2_roll and player4_roll > player3_roll:
            print(
                f'{player1.name} you rolled a {player1_roll} \n{player2.name} you rolled a {player2_roll}.\n {player3.name} you rolled a {player3_roll}.\n {player4.name} you rolled a {player4_roll}')
            print(f'{player4.name} you roll first')
            four_players(player1, 6, player2, 6, player3, 6, player4, 6) #function call for game logic
            break



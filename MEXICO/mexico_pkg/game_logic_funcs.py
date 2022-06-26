
from mexico_pkg.dice import Die


def two_players(player1,p1lives, player2,p2lives): #passes in players names + default lives
    players_lives = {player1.name : p1lives, player2.name : p2lives}    
    

    while len(players_lives) != 1:
        
        player1_roll = Die.roll(player1)
        player2_roll = Die.roll(player2)

        if player1_roll == player2_roll:   # continues to roll so no dublicate values
            player1_roll = Die.roll(player1)
            player2_roll = Die.roll(player2)

        if player1_roll != player2_roll: 
            
            game_on = (input("Press Enter to roll"))
            
            print("************************************************************")
            print(f'{player1.name} you rolled a {player1_roll}. \n{player2.name} you rolled a {player2_roll}.')
            print("************************************************************")
            turn_rolls = {player1.name : player1_roll, player2.name : player2_roll}
            
        
            for key , value in turn_rolls.items():
                if value == min(turn_rolls.values()): #this checks for the minimum roll amount
                    for k , v in list(players_lives.items()):
                        if k == key:
                            players_lives[key] -= 1
                            
                            print(f'{player1.name} LIVES = {players_lives[player1.name]} \n{player2.name} LIVES = {players_lives[player2.name]}.')
                            print("************************************************************")
                            if v < 2:
                                print(key, "You are out! Good Bye")
                                print("************************************************************")
                                players_lives.pop(key, None)
                                
                                    
                            if len(players_lives) == 1:
                                for last_player in players_lives.keys():
                                    print(last_player, "You have Won Congratulations")
                                    return
                                break
                                               
                


def three_players(player1 , p1lives , player2 , p2lives , player3 , p3lives): #passes in players names + default lives
    players_lives = {player1.name : p1lives, player2.name : p2lives, player3.name : p3lives}    
   
  
    while len(players_lives) == 3:
    
        player1_roll = Die.roll(player1)
        player2_roll = Die.roll(player2)
        player3_roll = Die.roll(player3)

        while player1_roll == player2_roll or player3_roll == player1_roll or player2_roll == player3_roll:
            player1_roll = Die.roll(player1)
            player2_roll = Die.roll(player2)
            player3_roll = Die.roll(player3)

        if player1_roll != player2_roll and player1_roll != player3_roll and player2_roll != player3_roll: 
            
            game_on = (input("Press Enter to roll"))
            
            print("************************************************************")
            print(f'{player1.name} you rolled a {player1_roll}. \n{player2.name} you rolled a {player2_roll}. {player3.name} you rolled a {player3_roll}.')
            print("************************************************************")
            turn_rolls = {player1.name : player1_roll, player2.name : player2_roll, player3.name : player3_roll}
            

            for key , value in turn_rolls.items():
                if value == min(turn_rolls.values()): #this checks for the minimum roll amount
                    for k , v in list(players_lives.items()):
                        if k == key:
                            players_lives[key] -= 1
                            
                            print(f'{player1.name} LIVES = {players_lives[player1.name]}. \n{player2.name} LIVES = {players_lives[player2.name]}. {player3.name} LIVES = {players_lives[player3.name]}.')
                            print("************************************************************")
                            if v < 2:
                                print(key, "You are out! Good Bye")
                                print("************************************************************")
                                players_lives.pop(key, None)
    
               
    while len(players_lives) == 2:
        if player1.name in players_lives and player2.name in players_lives:
            two_players(player1,players_lives[player1.name],player2,players_lives[player2.name])
            break
                                       
        if player1.name in players_lives and player3.name in players_lives:
            two_players(player1,players_lives[player1.name],player3,players_lives[player3.name])                                    
            break

        if player2.name in players_lives and player3.name in players_lives:
            two_players(player2,players_lives[player2.name],player3,players_lives[player3.name])
            break







def four_players(player1 , p1lives , player2 , p2lives , player3 , p3lives , player4, p4lives): #passes in players names + default lives
    players_lives = {player1.name : p1lives, player2.name : p2lives, player3.name : p3lives, player4.name : p4lives}    
    
    
        
    while len(players_lives) == 4:
    
        player1_roll = Die.roll(player1)
        player2_roll = Die.roll(player2)
        player3_roll = Die.roll(player3)
        player4_roll = Die.roll(player4)

        while player1_roll == player2_roll or player1_roll == player3_roll or player2_roll == player3_roll or player4_roll == player1_roll or player4_roll == player2_roll or player4_roll == player3_roll: #continues to re roll so now duplicate values
            player1_roll = Die.roll(player1)
            player2_roll = Die.roll(player2)
            player3_roll = Die.roll(player3)
            player4_roll = Die.roll(player4)

            if player1_roll != player2_roll and player1_roll != player3_roll and player2_roll != player3_roll and player4_roll != player1_roll and player4_roll != player2_roll and player4_roll != player3_roll: 
                
                game_on = (input("Press Enter to roll"))
                
                print("************************************************************")
                print(f'{player1.name} you rolled a {player1_roll}. {player2.name} you rolled a {player2_roll}.')
                print(f'{player3.name} you rolled a {player3_roll}. {player4.name} you rolled a {player4_roll}')
                print("************************************************************")
                turn_rolls = {player1.name : player1_roll, player2.name : player2_roll, player3.name : player3_roll, player4.name : player4_roll}
                

                for key , value in turn_rolls.items():
                    if value == min(turn_rolls.values()): #this checks for the minimum roll amount
                        for k , v in list(players_lives.items()):
                            if k == key:
                                players_lives[key] -= 1
                                
                                print(f'{player1.name} LIVES = {players_lives[player1.name]}. {player2.name} LIVES = {players_lives[player2.name]}.') 
                                print(f'{player3.name} LIVES = {players_lives[player3.name]}.{player4.name} LIVES = {players_lives[player4.name]}')
                                print("************************************************************")
                                if v < 2:
                                    print(key, "You are out! Good Bye")
                                    print("************************************************************")
                                    players_lives.pop(key, None)
                                    break
                                break        

            
        while len(players_lives) == 3:
            if player1.name in players_lives and player2.name in players_lives and player3.name in players_lives:
                three_players(player1,players_lives[player1.name], player2,players_lives[player2.name], player3, players_lives[player3.name])
                break
                          
            if player1.name in players_lives and player3.name in players_lives and player4.name in players_lives:
                three_players(player1, players_lives[player1.name],player3, players_lives[player3.name],player4, players_lives[player4.name])                                    
                break

            if player2.name in players_lives and player3.name in players_lives and player4.name in players_lives:
                three_players(player2, players_lives[player2.name],player3,players_lives[player3.name],player4,players_lives[player4.name])
                break
            if player1.name in players_lives and player2.name in players_lives and player4.name in players_lives:
                three_players(player1, players_lives[player1.name],player2, players_lives[player2.name],player4,players_lives[player4.name]) 
                break
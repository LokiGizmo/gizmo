from random import randint

game_running = True
game_results = []



def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

def game_ends(winner_name):
    print(f'{winner_name} won the game')


while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'loki', 'attack': 13, 'heal': 17, 'health': 100}
    monster = {'name': 'max', 'attack_min': 10 ,'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('enter player name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health'] ) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print('please select action')
        print('---' * 7)
        print('1) attack')
        print('---' * 7)
        print('2) Heal')
        print('---' * 7)
        print('3) exit game')
        print('---' * 7)
        print('4)show results')
        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster ['health'] <= 0:
                player_won = True


            else:

                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])
            player['health'] = player['health'] - monster_attack
        if player['health'] <= 0:
            monster_won = True


        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for stats in game_results:
                print(stats)

        else:
            print('fight')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) +' hp left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' hp left')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name':player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False



        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False


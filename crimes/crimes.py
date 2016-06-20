import random
import os

def clear_screen():
    try:
        os.system('cls')#windows
    except:
        os.system('clear')#linux

def press_any_key():
    #from http://stackoverflow.com/questions/1394956/
    # how-to-do-hit-any-key-in-python
    try:
        os.system('pause')  #windows, doesn't require enter
        #manually tested as functional in
        #cmd line on Windows 7 on 9/19/2015 with Python 3.5.0
    except:
        os.system('read -p "Press any key to continue"') #linux
    clear_screen()
          
def create_crimes():
    crimes = [ 'move Daddy\'s tennis shoes to Xander\'s room',
             'move pencil sharpener to the blue recyle bin in garage',
             'draw a picture of a car and tape it to wall on the stairs',
             'flush the toilet in the Butterfly bathroom',
             'Move the red chair to the glass room'
             ]
    return crimes

def dict_of_roles():
    return { 1: 'detective',
             2: 'crime committer'
             }

def get_one_players_name(index):
    print('What is the name of player {}? '.format(index), end='')
    player_name = input()
    return player_name

def get_names_of_players():
    print('How many players (minimum of 4)?: ', end='')
    num_of_play = input()
    num_of_play = int(num_of_play)
    players = []
    for i in range(num_of_play):
        players.append(get_one_players_name(i + 1))
    return players

def divide_roles(num_of_players, roles):
    roles_included = [ roles[1], roles[2], roles[2], roles[2] ]
    if num_of_players > 4:
        for i in range(1, num_of_players - 3):
            roles_included.append(roles[2])
    return roles_included

def assign_roles_to_players(player_list):
    possible_roles = dict_of_roles()
    roles = []
    roles = divide_roles(len(player_list), possible_roles)
    random.shuffle(player_list)
    assigned_roles = {}
    for i in range(len(player_list)):
        assigned_roles[player_list[i]] = roles[i]
    return assigned_roles

def tell_criminal_what_the_crime_and_time_is(player, crimes):
    choice = random.randint(0, len(crimes)-1)
    crime = crimes[choice]
    time = 'next ten minutes'
    line = ('{}, your crime is {} and '
          'you will commit it in the {}.'.format(player, crime, time))
    print(line)
    with open('crimes.txt', 'at') as casebook:
        casebook.write(line)
        casebook.write('\n')
    crimes.remove(crime)
    
def tell_each_player_what_their_role_is(assigned_roles):
    crimes = create_crimes()
    for player in assigned_roles:
        print('Only {} should looking at screen now.'.format(player))
        press_any_key()
        print('Your role is {}'.format(assigned_roles[player]))
        if assigned_roles[player] == 'crime committer':
            tell_criminal_what_the_crime_and_time_is(player, crimes)
        if assigned_roles[player] == 'detective':
            with open('crimes.txt', 'at') as casebook:
                line = ('{} is the detective.'.format(player))
                casebook.write(line)
                casebook.write('\n')
        press_any_key()
    

if __name__ == '__main__':
    player_list = get_names_of_players()
    assigned_roles = assign_roles_to_players(player_list)
    tell_each_player_what_their_role_is(assigned_roles)
    
    
        


import random

# Food values
food = random.randint(0,2)
CANDY = 0
STEAK = 1
POTION = 2
CANDY_RESTORE = 10
STEAK_RESTORE = 15
POTION_RESTORE = 35

# Creature values
BUNNY = 0
DWARF = 1
TROLL = 2
WYVERN = 3
GAMBLER = 4
BAT = 6
TROGG = 7
BUNNY_DAMAGE = 10
DWARF_DAMAGE = 15
BAT_DAMAGE = 25
TROLL_DAMAGE = 30
WYVERN_DAMAGE = 50
GAMBLER_DAMAGE = 40
TROGG_DAMAGE = 60

# Misc values
TUITION = 50
BEER = 50
invalid_direction_msg = ('You fumble around in the darkness...your hands meet familiar structures as you feel your way around. You realize you\'re back where you started before you moved.')
cardinal_directions = ['N', 'E', 'S', 'W']

# Dictionary for player values -- stored in global scope.
player = {
    'name': '',
    'gold': 0,
    'health': 125,
    'room_num': 1
}

# Rooms dictionary -- the purpose will be to store the contents of each room.
Rooms_list = [
    # Room 1
    {
        'room_num': 1,
        'message':  
        '''
    ----------
    | Room 1 |
    |----------------------------------------------------------------
    | You stumble into a hole in the ground. When you               |
    | shake off the dirt and leaves you realize you are in          |
    | the entrance to a cave that looks man made. As you            |
    | take a look around, you decide it might be fun to explore.    |
    -----------------------------------------------------------------
        ''',
        'valid_directions': ['E', 'S'],
        'north_destination': lambda: print(invalid_direction_msg),
        'east_destination': lambda: update_player_room(4),
        'south_destination': lambda: update_player_room(2),
        'west_destination': lambda: print(invalid_direction_msg)
    },
    
    # Room 2
    {
        'room_num': 2,
        'message': 
        '''
    ----------
    | Room 2 |
    |------------------------------------------------------------
    | You have entered the throne room. In the middle           |
    | of the room there is a giant wooden throne with           |
    | intricate carvings. As you take a closer look at the      |
    | carvings, you see that they show trolls chasing humans.   |
    | Hmmm, maybe this is not a great place to stop for a rest. |
    -------------------------------------------------------------
        ''',
        'valid_directions': ['N', 'E'],
        'north_destination': lambda: update_player_room(1),
        'east_destination': lambda: update_player_room(3),
        'south_destination': lambda: print(invalid_direction_msg),
        'west_destination': lambda: print(invalid_direction_msg)
    },
    
    # Room 3
    {
        'room_num': 3,
        'message': 
        '''
    ----------
    | Room 3 |
    |------------------------------------------------------------
    | You have entered an abandoned pub. There are piles        |
    | of dirty dishes and empty beer mugs all over the place.   |
    | You hear someone coming and duck behind a table to hide.  |
    -------------------------------------------------------------        
        ''',
        'valid_directions': ['S', 'E'],
        'north_destination': lambda: print(invalid_direction_msg),
        'east_destination': lambda: update_player_room(5),
        'south_destination': lambda: update_player_room(2),
        'west_destination': lambda: print(invalid_direction_msg)
    },
    
    # Room 4
    {
        'room_num': 4,
        'message': 
        '''
    ----------
    | Room 4 |
    |----------------------------------------------------------------
    | You have entered a huge storage room filled with empty boxes. |
    | Looking at the side of one box, you see ACME Wyvern food      |
    | You better get out of here before you end up on the menu.     |
    -----------------------------------------------------------------
        ''',
        'valid_directions': ['E', 'S', 'W'],
        'north_destination': lambda: print(invalid_direction_msg),
        'east_destination': lambda: update_player_room(6),
        'south_destination': lambda: update_player_room(5),
        'west_destination': lambda: update_player_room(1)
    },

    # Room 5
    {
        'room_num': 5,
        'message': 
        '''
    ----------
    | Room 5 |
    |----------------------------------------------------------------------------------------
    | You have no idea where you are -- you know for sure you\'ve come across another room   |
    | Stumbling in the darkness, the only stimulus you have is a cool, damp breeze blowing  | 
    | towards you, through what must be multiple exits. This will be a hard decision...     |
    -----------------------------------------------------------------------------------------
        ''',
        'valid_directions': ['N', 'E', 'W'],
        'north_destination': lambda: update_player_room(4),
        'east_destination': lambda: update_player_room(6),
        'south_destination': lambda: print(invalid_direction_msg),
        'west_destination': lambda: update_player_room(3)
    },

    # Room 6
    {
        'room_num': 6,
        'message': 
        '''
    ----------
    | Room 6 |
    |------------------------------------------------------------------------
    | You hurriedly escape into what appears to be a panic room.            |
    | Looking at your surroundings, it\'s obvious someone left in a hurry.   |
    | This seems to be near the end of the cave...it\'s clear there\'s a      |
    | door at the end of the corridor.                                      |
    -------------------------------------------------------------------------
        ''',
        'valid_directions': ['E', 'W'],
        'north_destination': lambda: print(invalid_direction_msg),
        'east_destination': lambda: update_player_room(4),
        'south_destination': lambda: print(invalid_direction_msg),
        'west_destination': lambda: update_player_room(5)
    }
]


def update_player_gold(gold: int):
    player['gold'] = gold


def update_player_health(health: int):
    player['health'] = health


def update_player_room(room_num: int):
    player['room_num'] = room_num


def add_player_gold(gold: int):
    update_player_gold(player['gold'] + gold)


def damage_player(damage: int):
    new_health = player['health'] - damage
    new_health = 0 if new_health < 0 else new_health
    update_player_health(new_health)
    is_game_over()


def print_status():
    '''
    This function print's the players current status.
    
    Params
    ------
    player: dict
        A dictionary for the player that stores the player's current attributes
    '''
    gold = player['gold']
    health = player['health']

    if gold > 2 * health:
        print('\nYou are rich with ' + str(gold) + ' gold, but your health is only ' + str(health) + '\n')
    elif health > 2 * gold:
        print('\nYou are strong with ' + str(health) + ' health, but you only have ' + str(gold) + ' gold\n')
    else:
        print('\nYour health is ' + str(health) + ' and you have ' + str(gold) + ' gold\n')
        

def find_treasure(max_gold: int) -> int:
    '''
    This function calculates how much treasure is found by generating a random gold amount between 1 and the max number of gold coins.
    
    Params
    ------
    max_gold : int
        The maximum amount of gold possible to find.
    
    Returns
    -------
    int
        The actual amount of gold the user found.
    ''' 
    gold = random.randint(1, max_gold)
    add_player_gold(gold)
    
    if gold < max_gold / 2:
        print('\nYou find ' + str(gold) + ' gold pieces on the floor.\n')
    else:
        print('\nYou find a huge mound of ' + str(gold) + ' gold pieces!\n')


def search_for_treasure() -> bool:
    valid_responses = ['yes', 'no', 'y', 'n']
    
    user_choice = input('You see something shiny, would you like to search for treasure? (Y/N)\n').lower()

    while user_choice not in valid_responses:
        user_choice = input('Sorry that\'s not a valid response, please type either (Y/N):\n')

    return user_choice == 'yes' or user_choice == 'y'
    

def eat_food(food):
    '''
    This function allows the player to eat one of the optional food items which will update their health and print a message.
    
    Params
    ------
    food : int
        The food item being chosen. This number corresponds to the global variables we've created, however, there is a base case if the user attempts to eat
        nothing.
    health : int
        The player's current health prior to eating.
    '''
    health = player['health']
    # Check which food the user is eating then update their health and print a message about what they ate
    if food == CANDY:
        health += CANDY_RESTORE
        print('\nYou find a half eaten energy bar on the floor which restores your health by ' + str(CANDY_RESTORE) + '\n')
        
    elif food == STEAK:
        health += STEAK_RESTORE
        print('\nYou find a warm and juicy steak on the table which restores your health by ' + str(STEAK_RESTORE) + '\n')
        
    elif food == POTION:
        health += POTION_RESTORE
        print('\nYou find a green glowing potion on a shelf which restores your health by ' + str(POTION_RESTORE) + '\n')
        
    else:
        print('\nYour stomach is rumbling, but there is nothing to eat\n')
        
    if health > 100:
        health = 100

    update_player_health(health)
        

def fight_battle(creature: int):
    '''
    This function simulates battle with one of the optional creatures. A damage value will be generated based on each creatures max damage and a message will
    be given to the user regarding their battle.
    
    Params
    ------
    creature : int
        The creature that you are fighting. This number corresponds to the global variables we've created, however, there is a base case if the user attempts
        to fight nothing.
        
    Returns
    -------
    int
        The damage dealt to the player during the battle.
    ''' 
    
    damage = 0
    if creature == BUNNY:
        damage = random.randint(1, BUNNY_DAMAGE)
        print('\nYou trip over a cute bunny, dealing ' + str(damage) + ' damage to your health.\n')
        
    elif creature == DWARF:
        damage = random.randint(1, DWARF_DAMAGE)
        print('\nA drunken dwarf hits you with a beer mug and does ' + str(damage) + ' damage to your health.\n')
    
    elif creature == TROLL:
        damage = random.randint(1, TROLL_DAMAGE)
        print('\nAn angry troll takes a swing at you and does ' + str(damage) + ' damage to your health.\n')
    elif creature == WYVERN:
        damage = random.randint(1, WYVERN_DAMAGE)
        print('Chills run down your spine as you notice a polymorphic creature standing in your way --')
        print('it has wings like a bat and a tail like a scorpion -- the head is that of a lion.')
        print('\nThe Wyvern pierces you with their stinger, dealing ' + str(damage) + ' damage to your health.\n')    
    elif creature == BAT:
        damage = random.randint(1, BAT_DAMAGE)
        print('A high-pitched shriek indicates the presence of a bat! This creature seems unsure of itself...')
        print('\nThe Bat dives blindly towards you, dealing ' + str(damage) + ' damage to your health.\n')    
    elif creature == GAMBLER:
        damage = random.randint(0, GAMBLER_DAMAGE)
        print('A dwarf-like creature with beady eyes smiles at you -- you hear him snicker menacingly as he begins to shake a pair of magical dice.')
        print('\nThe Gambler rolls his dice -- throwing them at you to deal ' + str(damage) + ' damage to your health.\n')  
    elif creature == TROGG:
        damage = random.randint(20, TROGG_DAMAGE)
        print('A nasty, short, hairy little monster with razor sharp incisors hisses at you from across the room')
        print('\nIt lunges at you -- powerful claws tear into your skin, dealing ' + str(damage) + ' damage to your health.\n')
    else:
        print('\nIt is ghostly quiet here, you must be alone\n')
        
    # Damage the player
    if damage > 0:
        damage_player(damage)
    elif damage == 0:
        print('Well...gambling doesn\'t always pay off, now does it?')
    
    
def get_direction() -> str:
    '''
    This function gets what direction the user would like to travel.
    
    Returns
    -------
    str
        User choice of direction between one of the following values (N, S, E, W)
    ''' 
    optional_directions = ['N', 'S', 'E', 'W']
    direction = input('\nWhat direction would you like to go? (N, S, E, W): ').upper()
    
    while direction not in optional_directions:
        print('Sorry, you can not go that way...\n')
        direction = input('What direction would you like to go? (N, S, E, W): ').upper()
        
    return direction


def death_event():
    print('You feel the life leaving your body as your health reaches ' + str(player['health']) + ' -- this is the end of ' + (player['name']))
    exit()


def win_event():
    print('You empty your pockets and discover ' + str(player['gold']) + ' gold coins!')
    print('This will pay for your tuition, and your beer! w00t!')
    print('You crawl out of the cave and blink your eyes to')
    print('adjust to the bright sunshine. Congratulations!')
    print('Try not to spend it all in one place!')
    exit()    


def is_game_over():
    gold = player['gold']
    health = player['health']

    if gold >= 100:
        game_over = True
        did_player_win = True
        
    elif health == 0:
        game_over = True
        did_player_win = False

    else:
        game_over = False
        did_player_win = False


    return game_over, did_player_win

    
def room_1():
    '''
    This function visits the first room in the game and starts off the story.
    ''' 
    
    fight_battle(0)

    if player['health'] > 0:
        if search_for_treasure():
            find_treasure(10)
        
    print_status()


def room_2():
    '''
    This function visits the second room in the game.
    ''' 
    fight_battle(TROLL)
    
    if player['health'] > 0:
        if search_for_treasure():
            fight_battle(GAMBLER)
        else:
            print('Instead of treasure.....\n')
            eat_food(CANDY)
            
    print_status()


def room_3():
    '''
    This function visits the third room in the game.
    ''' 
    fight_battle(DWARF)

    if player['health'] > 0:
        if search_for_treasure():
            find_treasure(15)
    
    print_status()


def room_4():
    '''
    This function visits the fourth room in the game.
    ''' 
    
    rand = random.randint(1,100)
    if rand >= 50:
        fight_battle(WYVERN)
    else:
        eat_food(STEAK)

    if player['health'] > 0:
        
        if search_for_treasure():
            find_treasure(20)
        else:
            fight_battle(GAMBLER)

    print_status()
    
    
def room_5():
    '''
    This function visits the fifth room in the game.
    ''' 
    rand = random.randint(1, 100)
    if rand >= 50:
        fight_battle(BAT)
    else:
        eat_food(food)        
        
    if player['health'] > 0:
        if search_for_treasure():
            find_treasure(30)

    print_status()


def room_6():
    '''
    This function visits the sixth room in the game.
    ''' 
    
    door_value = 7
    

    # ONLY IF 0
    if door_value == 0:
        print('...you are extremely lucky and find that it opens, behind it is everything you were searching for!\n')
        add_player_gold(TUITION)
        win_event()

    # Range [1, 3]
    elif door_value <= 3:
        print('...there appears to be something shiny and heavy blocking it...\n')
        find_treasure(30)
        
    # Range [4, 6]
    elif door_value <= 6:
        print('Your stomach growls...somehow the door understands this and inexplicably spits out some food.')
        eat_food(food)
    
    # Everything else [7, 9]
    else:
        print('...it\'s guarded by a trogg!')
        fight_battle(TROGG)
    

def get_current_room(room_num: int):
    for room in Rooms_list:
        if room['room_num'] == room_num:
            return room
    return None


def validate_direction(direction: str, valid_directions_list) -> bool:
    if direction in valid_directions_list:
        return True
    else:
        return False


def move_to_destination(direction: str, room):
    if direction == 'N':
        room['north_destination']()
    elif direction == 'E':
        room['east_destination']()
    elif direction == 'S':
        room['south_destination']()
    elif direction == 'W':
        room['west_destination']()


room_map = {
    1: lambda : room_1(),
    2: lambda : room_2(),
    3: lambda : room_3(),
    4: lambda : room_4(),
    5: lambda : room_5(),
    6: lambda : room_6(),
}


if __name__ == '__main__':
        
    player['name'] = input('Before we begin...what is your name, traveler?\n')

    # Main game loop
    game_over = False
    did_player_win = False
    while not game_over:
        
        # Get the current room
        current_room = get_current_room(player['room_num'])

        # Print room message
        print(current_room['message'])

        # run the event for that room
        room_map[current_room['room_num']]()

        # Check if game is over
        game_over, did_player_win = is_game_over()

        if not game_over:

            is_valid_direction = False
            direction = ''

            while not is_valid_direction:

                # Get player's choice for the next room
                direction = get_direction()

                # Validate the direction
                is_valid_direction = validate_direction(direction, current_room['valid_directions'])

                if not is_valid_direction:
                    if direction in cardinal_directions:
                        move_to_destination(direction, current_room)
                    else:
                        print('Try again, except this time choose a cardinal direction...(N, E, S, W).\n')
                    

            # Move the player to the next room
            move_to_destination(direction, current_room)

    # End the game
    if is_game_over():
        win_event()
    else:
        death_event()

        




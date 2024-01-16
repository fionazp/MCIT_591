"""Name: Fan Zhang
Penn ID: 70912620
Statement of work: I received help from my friend Jiashuai Lu"""

def setup_bricks():
    ''' Set up the main pile of 60 bricks
        and discard pile of 0 bricks'''
    
    # define main pile which currently has 60 bricks and is not shuffled
    main_pile = []
    for i in range(1, 61):
        main_pile.append(i)
        
    # define discard pile which currently is empty
    discard = []

    # return both lists as a tuple, with main pile as the first item and discard pile as the second item
    return (main_pile, discard)



def shuffle_bricks(bricks):
    ''' Shuffle the given bricks '''
    
    # import the random module
    import random
    random.shuffle(bricks)



def check_bricks(main_pile, discard):
    ''' Check if there are any cards left in the given main pile of bricks.
        If not, shuffle the discard pile and move those bricks to the main pile.
        At last, turn over the top card to be the start of the new discard pile'''
    
    # check if no card is left in main pile
    if main_pile == []:
        # if no card is left, shuffle the discard pile
        shuffle_bricks(discard)
        # move the bricks to the main pile
        while len(discard) > 0:
            main_pile.append(discard.pop(-1))

        # turn over the top card to be the start of the new discard pile
        discard.append(main_pile[0])
        main_pile.pop(0)
        print("Oops! The main pile is empty!")
        print("The discard pile has been shuffled and moved to the main pile.")
        print("Now the top card of the new discard pile is", discard, ".")       
    else:
        pass
    



def check_tower_blaster(tower):
    ''' Check if the given tower has achieved stability'''

    # define a varaible sorted_tower to show what the tower would look like if achieved stability
    sorted_tower = sorted(tower)

    # if the tower is stable, return True 
    if sorted_tower == tower:
        print("The tower has achieved stability.")
        return True

    # if the tower is not stable, return False
    else:
        return False
    
   

def get_top_brick(brick_pile):
    ''' Remove and return the top brick from any given pile of bricks'''

    # create a new variable and cast the top brick from the given pile to the new variable
    top_brick = brick_pile[0]
    
    # remove the top brick from the given pile of bricks
    brick_pile.pop(0)
    
    # return the top brick from the given pile of bricks
    print("The brick", top_brick, "is picked. ")
    return top_brick



def deal_initial_bricks(main_pile):
    ''' Start the game by dealing two sets of 10 bricks each from the given main_pile'''
    # define two empty lists for the initial tower for computer and human
    computer_initial_tower = []
    human_initial_tower = []

    # to deal 10 bricks to each player. Computer first.
    for i in main_pile:
        # if the index of the elements in main pile is aneven number, starting 0, the element will be added to the computer's tower
        if int(main_pile.index(i)) % 2 ==0:
            # when the computer's tower has 10 elements, the function will stop adding more element
            if len(computer_initial_tower) <10:
                computer_initial_tower.insert(0,i)
            else:
                pass
       
        else:
            # when the human's tower has 10 elements, the function will stop adding more element
            if len(human_initial_tower) < 10:
                human_initial_tower.insert(0,i)

    # remove the bricks dealt to the players from main pile
    i=0
    while i < 20:
        main_pile.pop(0)
        i = i + 1
      
    return (computer_initial_tower, human_initial_tower)




def add_brick_to_discard(brick, discard):
    ''' Add the given brick to the top of the given discard pile'''
    discard.insert(0,brick)
    


def find_and_replace(new_brick, brick_to_be_replaced,tower,discard):
    ''' Find the given brick to be replaced in the given tower and replace it with the given new brick'''

    # check the given brick to be replaced is truly a brick in the given tower
    if brick_to_be_replaced in tower:
        
        # if it is in the given tower, then replace the given brick to be replaced with the given new brick
        tower[tower.index(brick_to_be_replaced)] = new_brick

        # given brick to be replaced then gets put on top of the given discard pile
        add_brick_to_discard(brick_to_be_replaced, discard)
  
    else:
        print("The brick to be replaced is not currently in the tower. Please pick again.")

    if new_brick in tower:
        return True
    else:
        return False 
    
# 
def reject(brick, discard, player):
    ''' Reject the brick picked by a player from main pile, and put it on top of discard pile'''
    add_brick_to_discard(brick, discard)
    print(player, "has rejected the brick to her tower.")

def count_conflicts(tower):
    ''' Count how many conflicts are there in a tower.
        A conflict happens when the first element's index is smaller than the second element but
        the first element's value is larger than the second element.
        The fewer the conflicts, the more stable the tower is.
        A stable tower that wins the game should have zero conflict.'''
    brick_conflicts = 0
                
    for i in range(len(tower)):
        for j in range(i):
            if tower[j] > tower[i]:
                brick_conflicts += 1

    return brick_conflicts

def decide_brick_to_be_replaced(new_brick, tower):
    ''' Decide which brick should be replaced to move the game towards winning.
        Iterate over the tower and calculate the conflicts after replacing each brick.
        The brick resulting in the least conflicts after being replaces is the one that should be replaced.
        If multiple bricks would satisfy as the brick that should be replaced, the last one would be picked.'''

    # copy the tower to a new list
    tower_trial = tower.copy()
    
    # set the index of the brick to be replaced to -1 so we would cover all the index in the list 
    brick_to_be_replaced_index = -1
    
    # create the variable for the conflicts in the tower
    tower_conflicts = count_conflicts(tower_trial)
    
    # iterate the new list that has the same value with tower
    for i in range(len(tower_trial)):
        
        # calculate the amount of conflicts after replacing each of the brick, from top to bottom
        tower_trial[i] = new_brick
        updated_tower_conflicts = count_conflicts(tower_trial)
        
        # decide which brick would result in the least conflicts
        if updated_tower_conflicts < tower_conflicts:
            tower_conflicts = updated_tower_conflicts
            brick_to_be_replaced_index = i
            
        tower_trial[i]= tower[i]
        
    return brick_to_be_replaced_index
    


def computer_play(tower, main_pile, discard):
    ''' This is the computer's turn.
        The computer will try to decide which brick in the tower to be replaced by the top brick in the discard pile,
        then replace the brick resulting the lest conflicts with the top brick from discard pile.
        If picking the top brick in the discard pile would not decrease the amount of conflicts in the tower (can not make the tower more stable),
        then the computer would pick the new brick from main pile, and decide which brick in the tower to be replaced. 
        If the brick from main pile can not make the tower more stable either,
        then the computer would reject the card and end the turn.'''
    

    print("Now is the computer's turn.")
    brick_to_be_replaced_index = -1

    # make sure the discard pile has bricks in it
    if len(discard) > 0:
        brick_to_be_replaced_index = decide_brick_to_be_replaced(discard[0], tower)

    # if the top brick in discard pile can not make the tower more stable 
    if brick_to_be_replaced_index == -1:
        
        # the computer would pick from main pile 
        new_brick = get_top_brick(main_pile)
        brick_to_be_replaced_index = decide_brick_to_be_replaced(new_brick, tower)
        
        # if the brick from main pile can not make the tower more stable
        if brick_to_be_replaced_index == -1:
            
            # the computer rejects the brick from main pile and the tower stays the same
            reject(new_brick, discard,"The computer")
            return
        
        # if the brick from main pile can make the tower more stable
        else:
            print("The brick was picked from the main pile.")
            # the computer calculates and decides which brick should be replaced to make the tower has least conflicts and replace it
            brick_to_be_replaced = tower[brick_to_be_replaced_index]
            find_and_replace(new_brick, brick_to_be_replaced, tower, discard)

    # if the top brick in discard pile can make the tower more stable
    else:
        new_brick = get_top_brick(discard)
        print("The brick was picked from the discard pile.")
        # the computer calculates and decides which brick should be replaced to make the tower has least conflicts and replace it
        brick_to_be_replaced = tower[brick_to_be_replaced_index]
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)
        
    print("The computer has replaced a brick in its tower. The computer's turn is over.")



def instruction():
    ''' To print out the instruction at the beginning of the game.'''

    print('''Welcome to Tower Blaster! Here is the play rules:
          The game starts with 60 bricks, each numbered from 1 to 60.
          Thik of the numbers on the bricks as the width of the bricks.
          The goal is to arrange the ten bricks from lowest to highest, like a pyramid.
          At the beginning of the game, each player will be dealt 10 bricks, and there will be 40 bricks remaining in the main pile.
          The top brick of the main pile will be turn over to begin the discarded brick pile.
          On each player's turn, the player chooses to pick up the top brick from either the discard pile or main pile.
          The top brick from the discard pile is known,but the main pile is not so picking from main pile can be risky.
          Once a player chooses a brick, the player will decide where in the tower to put the brick.
          The tower is always 10 bricks high so placing a new bricks menas that an existing brick in the tower will
          be removed and put on top of discard pile.
          If the player takes a brick from the main pile, the player can reject it and place it in the discard pile.
          If the player picks the top brick of the discard pile which is known to the player, she must use it.
          The first player to get their 10 bricks in order wins.
          Ready? Good luck!''')


def ask_D_or_M_or_H(prompt): 
    ''' Prints the given prompt as a question to the human player,
        and ask her to chose if she wants to draw the top brick on the discard pile or the main pile, or help.'''

    # set up a list for all the acceptable answers
    choices = ["d", "D", "m", "M", "h", "H"]
    
    # define a vairable to store the input of the acceptable answer to the prompt question
    human_decision = input(prompt)

    # if the input answer starts with a letter other than "d", "D", "m", "M", "h", "H", or empty, the answer is not acceptable and the question will be asked again
    while len(human_decision) == 0 or human_decision[0] not in choices:
        print("Your response is not acceptable. Please only enter D/M/H (not case sensitive)")
        human_decision = input(prompt)

    # return the answer into an int. "d" and "D" will return 0,"m" and "M" will return 1, "h" and "H" will return 2
    return int(choices.index(human_decision[0])/2)

def ask_brick_to_be_replaced(prompt):
    ''' Ask which brick in the towew that the player wants to replace'''
    return int(input(prompt))


def ask_yes_or_no(prompt):
    '''Prints the given prompt as a question to the user.'''
    
    # define a vairable to store the input of the answer to the prompt question
    play_decision = input(prompt)

    # if the input answer starts with a letter other than "y", "Y", "n", "N", or empty, the answer is not acceptable and the question will be asked again
    while len(play_decision) == 0 or play_decision[0] not in ["y", "Y", "n", "N"]:
        print("Your response is not acceptable. Please only enter y or n")
        play_decision = input(prompt)

    # if the answer starts with "y", or "Y", return True
    if play_decision[0]== "y" or play_decision[0] == "Y":
        return True

    # if the answer starts with "n", or "N", return False
    elif play_decision[0]== "n" or play_decision[0] == "N":
        return False


def human_play(human_tower, main_pile, discard):
    '''The human player will be asked which pile she wants to pick the brick.
        If she picks from discard pile, she then will be asked which brick in her tower she wants to replace, and enter a number.
        If she enters a number that is not in her tower, she will be asked again.
        The number that the player enters will be replaced.
        If she picks from the main pile, she then will be asked if she wants to use this brick or no.
        If she decides yes, then she will be asked which brick she wants to replace and enter a number.
        If she enters a number that is not in her tower, she will be asked again.
        The number that the player enters will be replaced.
        If she decides not to use the brick, she can say no and the brick will be rejected.'''
    
    print("NOW IT'S YOUR TURN!")
    print("Your tower is", human_tower, ".")
    print("The top brick of the discard pile is", discard[0],".")

    # ask the player if she wants to pick the brick from discard pile or main pile, or she needs help
    pile_decision = ask_D_or_M_or_H("Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help")
    brick_to_be_replaced = -1

    # if she entered 'h' or "H", she will be shown the instruction again
    while pile_decision == 2:
        instruction()
        
        # after the instruction, she will be asked to choose the pile again
        pile_decision = ask_D_or_M_or_H("Type 'D' to take the discard brick, 'M' for a mystery brick, or 'H' for help")
        
    # if the answer starts with "d", or "D", the player picks the brick from discard pile
    if pile_decision == 0:
        new_brick = get_top_brick(discard)
        replace_result = False
        while replace_result is False:

            # ask the player which brick she wants to replace in her tower
            brick_to_be_replaced = ask_brick_to_be_replaced("Which number would you like to replace? Please enter a number.")

            # replace the brick the player picked
            replace_result = find_and_replace(new_brick, brick_to_be_replaced, human_tower,discard)
            
        # show the player which brick has been replaced and which new brick and where it has been added to the tower
        print("You replaced", brick_to_be_replaced, "with", new_brick,".")
        
    # if the answer starts with "m", or "M", the player picks the brick from main pile
    else:
        new_brick = get_top_brick(main_pile)

        # ask the player if she wants to use this brick
        play_decision = ask_yes_or_no("Do you want to use this brick? y or n")
        if play_decision == True:
            replace_result = False
            # if the player chooses to replace a brick that is not in the current tower, she will be asked again to enter a number
            while replace_result is False:
                brick_to_be_replaced = ask_brick_to_be_replaced("Which number would you like to replace? Please enter a number.")

                # replace the number the player entered with the new brick from main pile
                replace_result = find_and_replace(new_brick, brick_to_be_replaced, human_tower,discard)
            print("You replaced brick", brick_to_be_replaced, "with", new_brick,".")

        # if the player does not want to use the brick from main pile, the brick will be rejected and this turn is over
        else:
            reject(new_brick, discard, "You")
            return
            
    print("Your tower:", human_tower)


def main():
    ''' set up the game to play. See instructions for rules'''

    # print instruction at the beginning of the game
    instruction()

    # set up main pile and discard pile
    main_pile, discard = setup_bricks()
    computer_tower = []
    human_tower = []
    computer_win = True
    human_win = True

    # the game only starts when none of the player's tower is already in order
    while computer_win == True or human_win == True:

        # shuffle the bricks in main pile 
        shuffle_bricks(main_pile)

        # deal the initial 10 bricks to each player
        computer_tower, human_tower = deal_initial_bricks(main_pile)
        computer_win = check_tower_blaster(computer_tower)
        human_win = check_tower_blaster(human_tower)
    
    print("The computer's initial tower is", computer_tower, ".")
    while True:
        check_bricks(main_pile, discard)
        computer_play(computer_tower, main_pile, discard)

        # check if the computer's tower is in order through the game
        if check_tower_blaster(computer_tower):
            print("The computer won! Good luck next time!")
            break

        # check if the main pile is empty through the game
        check_bricks(main_pile, discard)
        
        # check if the human player's tower is in order through the game
        human_play(human_tower, main_pile, discard)

        if check_tower_blaster(human_tower):
            print("Congrats! You won!")
            break

                



if __name__ == "__main__":
    main()

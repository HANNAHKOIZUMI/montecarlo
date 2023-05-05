# montecarlo

# METADATA
# Author Name: Hannah Koizumi
# Project Name: Monte Carlo Simulator

# SYNOPSIS: HOW TO USE THIS CODE
# Install and import: Use git to clone the repository on your local machine and use import montecarlo_folder.montecarlo 
# 1: Create a die with the Die class
die1 = Die([1,2,3,4,5,6])
# 2 : Change the weight of one of the faces, all faces are weighted at 1 by default
die1.change_weight(2,2)
# 3: Roll the die a specified amount of times and output the result
die1.roll_die(3)
# 4: Show your current die's faces and weights
die1.current_die()
# 5: Create a list die objects to create a game object
dice = ([die1, die1, die1])
dicegame = Game(dice)
# 6: Play a game by rolling all of the dice and specify the number of rolls
dicegame.play(5)
# 7: Output the results of the game in either a narrow or wide dataframe
dicegame.show('narrow')
# 8: Create an Analyzer object 
results = Analyzer(dicegame)
# 9: Analyze the results for the number of jackpots
results.jackpot()
# 10: Analyze the results for the count of unique combinations
results.combo()
# 11: Analyze the results for the face count for each face value per roll
results.face_count()

# API DESCRIPTION
    #Die Class """This class creates a die with face values and weights, offers you the ability to change the weights, and rolls the die and outputs the value"""
       # __init__(faces)
       """
        PURPOSE: Instantiates a die object with face values and weights for each value. 
        
        INPUTS: faces-- list or array of face values. 
        
        ATTRIBUTES: faces(list of ints), weights(list of ints, default is 1)
        """
       # change_weight(side, new_weight)
       """
        PURPOSE: Change a face value's weight, which is defaulted to 1. 
    
        INPUTS
        side: the face value whose weight you would like changed, same data type used to initialize the die
        new_weight: the value of the new weight, int
    
        OUTPUT
        self._die: a private dataframe of the die's face values and their corresponding weights in each row
        """
       # roll_die(rolls)
       """
        PURPOSE: Roll the die and show the result 
    
        INPUTS
        rolls = int, number of times to roll the die with a default of 1
    
        OUTPUT
        outcomes: a dataframe of the roll number and the results of the die
        """
       # current_die()
       """
        PURPOSE: Return the values of the current die
    
        INPUTS
        none
    
        OUTPUT
        self_die: a private dataframe of die's face values and their corresponding weights in each row
        """
    # Game Class: """This class takes a list of dice, rolls them, and outputs the results of the rolls"""
        # __init__(dice)
        """
        PURPOSE: Instantiate a list of die objects
        
        INPUT/ATTRIBUTE
        dice = list of dice objects
        """
        # play(rolls)
        """
        PURPOSE: Roll all of the dice objects and show the results
    
        INPUTS
        rolls: number of times to roll the dice objects, int
    
        OUTPUT
        self._result: the result of the game in a private data frame, roll number by die object
        """
        # show(form)
        """
        PURPOSE: Display the results of the game by either a narrow or wide dataframe
    
        INPUTS
        form: either "wide" or "narrow", str
    
        OUTPUT
        a dataframe in either wide or narrow form, showing the result of the roll for each die object and the roll number
        """
    # Analyzer Class: """This class takes the result of a game and analyzes it for jackpots, unique combinations, and frequency of face values"""
        # __init__(game)
        """
        PURPOSE: Instantiate a dataframe of game results
        
        INPUT/ATTRIBUTE: game(dataframe of game results)
        """
        # jackpot()
        """
        PURPOSE: Calculates the number of jackpots in all of the games played
    
        ATTRIBUTE
        .jackpot = dataframe of results by roll number and a column of T/F if a jackpot
    
        OUTPUT
        count: int of total number of jackpots
        """
        # combo()
        """
        PURPOSE: To count and display the number of unique combinations of dice objects
    
        INPUTS
        none
    
        OUTPUT
        output: a
        # face_count()
        """
        PURPOSE: Display the frequency of die object face values per roll number
    
        INPUTS
        none
    
        OUTPUT
        face_count_df: a dataframe with each face value as a column and its frequency for each roll number
        """


# Die Class
    # change_weight(): 
        # 
    # roll_die():
    # current_die():
# Game Class
    # play():
    # show():
# Analyzer Class
    # jackpot():
    # combo():
    # face_count():

# MANIFEST
montecarlo_folder
    montecarlo.py
    __init__.py
get-pip.py
LICENSE
montecarlo_demo
montecarlo_test.py
README.md
setup.py

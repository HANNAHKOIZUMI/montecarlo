import numpy as np
import pandas as pd
import random as rndm
from scipy import * 
import array as arr

class Die():
    """This class creates a die with face values and weights, offers you the ability to change the weights, 
    and rolls the die and outputs the value"""

    def __init__(self,faces):
        """
        PURPOSE: Instantiates a die object with face values and weights for each value. 
        
        INPUTS: faces: list or array of face values. 
        
        ATTRIBUTES: faces(list of ints), weights(list of ints, default is 1)
        """
        self.faces = faces
        self.weights = [1] * len(faces)
        self._die = pd.DataFrame({'faces': self.faces, 'weights': self.weights})
    
    def change_weight(self, side, new_weight):
        """
        PURPOSE: Change a face value's weight, which is defaulted to 1. 
    
        INPUTS
        side: the face value whose weight you would like changed, same data type used to initialize the die
        new_weight: the value of the new weight, int
    
        OUTPUT
        self._die: a private dataframe of the die's face values and their corresponding weights in each row
        """
        self.side=side
        self.new_weight=new_weight
        for i in self._die.faces:
            if i == self.side: 
                location = self._die.faces[self._die.faces == i].index.values
                self._die.loc[location,'weights'] = new_weight
            return self._die                
            
    def roll_die(self, rolls=1):
        """
        PURPOSE: Roll the die and show the result 
    
        INPUTS
        rolls = int, number of times to roll the die with a default of 1
    
        OUTPUT
        outcomes: a dataframe of the roll number and the results of the die
        """
        self.rolls = rolls
        outcomes = []
        for i in range(self.rolls):
            result = self._die.faces.sample(weights=self._die.weights).values[0]
            outcomes.append(result)
        return outcomes
    
    def current_die(self):
        """
        PURPOSE: Return the values of the current die
    
        INPUTS
        none
    
        OUTPUT
        self_die: a private dataframe of die's face values and their corresponding weights in each row
        """
        return self._die
    
class Game():
    """This class takes a list of dice, rolls them, and outputs the results of the rolls"""
    
    def __init__(self, dice):
        """
        PURPOSE: Instantiate a list of die objects
        
        INPUT/ATTRIBUTE
        dice = list of dice objects
        """
        self.dice=dice
    
    def play(self, rolls):
        """
        PURPOSE: Roll all of the dice objects and show the results
    
        INPUTS
        rolls: number of times to roll the dice objects, int
    
        OUTPUT
        self._result: the result of the game in a private data frame, roll number by die object
        """
        self.rolls = rolls
        results = []
        a=0
        roll_count=[]
        for y in self.dice:
            for x in range(self.rolls):
                die_result=() 
                z = len(self.dice)-1
                die_result = numpy.random.choice(self.dice[z].faces, weights = self.dice[z].weights)
                z+=1
        outcomes = pd.Series(results)
        vals = outcomes.values 
        final_outcome = vals.reshape(self.rolls,len(self.dice)) 
        self._result = pd.DataFrame(final_outcome)
        self._result.columns = [f'die_{i}' for i in self._result.columns]
        for h in range(len(self._result)):
            a+=1
            roll_count.append(a)
        self._result['Roll Number']=roll_count
        self._result.set_index('Roll Number', inplace=True)
        return self._result
    
    def show(self, form):
        """
        PURPOSE: Display the results of the game by either a narrow or wide dataframe
    
        INPUTS
        form: either "wide" or "narrow", str
    
        OUTPUT
        a dataframe in either wide or narrow form, showing the result of the roll for each die object and the roll number
        """
        self.form = form
        if self.form == 'wide':
            return self._result
        elif self.form == 'narrow':
            df = pd.DataFrame()
            for y in self._result:
                df = pd.DataFrame(self._result.stack())
                df.columns = ['Face Rolled']
            return df
        else:
            print('please only input narrow or wide to indicate which form to receive the results of the game')

class Analyzer():
    """This class takes the result of a game and analyzes it for jackpots, unique combinations, and frequency of face values"""
    
    def __init__(self, game):
        """
        PURPOSE: Instantiate a dataframe of game results
        
        INPUT/ATTRIBUTE: game(dataframe of game results)
        """
        self.game = pd.DataFrame(game.show('wide'))
        
    def jackpot(self):
        """
        PURPOSE: Calculates the number of jackpots in all of the games played
    
        ATTRIBUTE
        .jackpot = dataframe of results by roll number and a column of T/F if a jackpot
    
        OUTPUT
        count: int of total number of jackpots
        """
        self.game.eq(self.game.iloc[:, 0], axis=0)
        self.jackpot = self.game.copy()
        self.jackpot['Jackpot'] = self.jackpot.eq(self.jackpot.iloc[:, 0], axis=0).all(1)
        try:
            count = self.jackpot['Jackpot'].value_counts()[True]
            return count
        except:
            return 0
    
    def combo(self):
        """
        PURPOSE: To count and display the number of unique combinations of dice objects
    
        INPUTS
        none
    
        OUTPUT
        output: a dataframe with an index of the unique combinations and a column with a count of their frequency 
        """
        combo_df = self.game.copy()
        output = pd.DataFrame(np.sort(combo_df.values, axis=1), columns=combo_df.columns).value_counts().reset_index(name='counts')
        return output
    
    def face_count(self):
        """
        PURPOSE: Display the frequency of die object face values per roll number
    
        INPUTS
        none
    
        OUTPUT
        face_count_df: a dataframe with each face value as a column and its frequency for each roll number
        """
        columns = []
        for x in self.game.columns:
            columns.append(x)
        self.game=pd.DataFrame(self.game.stack())
        self.game.columns = ['Face Rolled' for i in self.game.columns]
        face_count_df = pd.DataFrame(self.game)
        face_count_df = face_count_df.reset_index().pivot_table(index='Roll Number', columns='Face Rolled', aggfunc='count').fillna(0)
        return face_count_df
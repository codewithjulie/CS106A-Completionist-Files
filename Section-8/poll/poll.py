"""
File: poll.py
-------------

Contains the Poll class, which powers a poll where people vote for options and
the poll computes a winner.
"""
import math

class Poll:
    def __init__(self):
        self.poll={}


    def add_option(self, option):
        """
        Adds option as a valid poll choice.

        Arguments
        ---------
        option (str) -- The option value to add to the poll.
        """
        if option not in self.poll:
            self.poll[option]=0


    def vote_for(self, option):
        """
        Processes a vote for option.

        Argument
        --------
        option (str) -- The option to vote for.
        """
        self.poll[option]+=1


    def get_winner(self):
        """
        Returns the winner in the poll.

        Returns
        -------
        str -- The poll option that received the most votes.
        """
        winner = None       # To display the name of the winner
        Maxvotes = 0        # Votes the winner has
        # For each candidate in poll dictinary, 
        for option in self.poll:
            # we'll check for no. of votes placed in his/her name
            num_of_votes = self.poll[option]
            # Next we check if the no. of votes we just read are max value or not
            if num_of_votes > Maxvotes:
                # If yes, then we proceed to announce the winner as key of poll dictionary
                winner = option
                Maxvotes = num_of_votes
            # Continue the loop until the end of dictionary
        
        # Finally announce the winner
        return winner
        
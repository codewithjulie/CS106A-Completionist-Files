"""
File: main.py
-------------

Uses the Poll class to run some sample polls.
"""
from poll import Poll


def main():
    """
    >>> main()
    Professor McGonagall wins!
    """
    print("Which Hogwarts professor would win in a battle?")
    poll = Poll()

    # Custom add candidates:->
    # candidate = input("Add a candidate to the poll: ")
    # poll.add_option(candidate)
    poll.add_option('Professor McGonagall')
    poll.add_option('Professor Snape')
    poll.add_option('Professor Umbridge')
    poll.add_option('Professor Lupin')

    # 4 votes for McGonagall
    poll.vote_for('Professor McGonagall')
    poll.vote_for('Professor McGonagall')
    poll.vote_for('Professor McGonagall')
    poll.vote_for('Professor McGonagall')

    # Custom place votes using terminal:->
    # Vote_Candidate_Name = input("Place the vote for candidate (name): ")
    # poll.vote_for(Vote_Candidate_Name)

    # 3 votes for Snape
    poll.vote_for('Professor Snape')
    poll.vote_for('Professor Snape')
    poll.vote_for('Professor Snape')

    # No votes for Umbridge (*boo*)

    # One faithful vote for our favorite werewolf
    poll.vote_for('Professor Lupin')

    print(poll.get_winner() + " wins!")



if __name__ == '__main__':
    main()
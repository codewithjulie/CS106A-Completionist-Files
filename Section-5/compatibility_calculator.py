def percent_in_common(l1, l2):
    counter = 0
    for i in range(len(l1)):
        if l1[i] in l2:
            counter += 1
    length = len(l1) + len(l2)
    compatability_score = counter / length
    return compatability_score


def calc_score(netflix_history1, netflix_history2, fav_books1, fav_books2):
    """
    >>> percent_in_common(['a', 'b', 'c', 'd'], ['c', 'd', 'm', 'n', 'x', 'z'])
    0.2
    """
    netflix = percent_in_common(netflix_history1, netflix_history2)
    books = percent_in_common(fav_books1, fav_books2)
    compatibility = netflix + books
    return compatibility


def new_friend(name_list, compatibility_scores):
    """
    >>> name_list = ['Michelle', 'Joe']
    >>> compatibility_scores = [1, 0.8]
    >>> new_friend(name_list, compatibility_scores)
    ['Michelle', 1]
    """
    max1 = compatibility_scores.index(max(compatibility_scores))
    name1 = name_list[max1]
    return [name1, compatibility_scores[max1]]

"""netflix_history1 = ["You", "pretty little liars", "friends"]
netflix_history2 = ["dark", "friends", "You"]
fav_books1 = ["a", "b", "c", "Karel Kares"]
fav_books2 = ["Karel Kares", "The Hate U Give", "Jedi Master Mehran"]
score = calc_score(netflix_history1, netflix_history2, fav_books1, fav_books2)
print(score)"""
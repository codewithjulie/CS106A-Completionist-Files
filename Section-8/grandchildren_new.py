SAMPLE_INPUT = {
    'Alice': ['Bob', 'Catherine'],
    'Daniel': ['Alice', 'Eve'],
    'Catherine': ['Frank'],
    'Eve': ['Grace']
}


def find_grandchildren(parents_dictionary):
    """
    >>> find_grandchildren(SAMPLE_INPUT)
    {'Alice': ['Frank'], 'Daniel': ['Bob', 'Catherine', 'Grace']}
    """
    granparent_dict = {}
    for parent in parents_dictionary:
        children = parents_dictionary[parent]
        for child in children:
            if child in parents_dictionary:
                grandchildren = parents_dictionary[child]
                print(parent, grandchildren)
                add_grandchildren(granparent_dict, parent, grandchildren)


    return granparent_dict


def add_grandchildren(grandparent_dict, grandparent, grandchildren):
    if grandparent not in grandparent_dict:
        grandparent_dict[grandparent] = []

    current_grandchildren = grandparent_dict[grandparent]
    current_grandchildren += grandchildren



def main():
    gr_dict = find_grandchildren(SAMPLE_INPUT)
    print(gr_dict)


if __name__ == '__main__':
    main()

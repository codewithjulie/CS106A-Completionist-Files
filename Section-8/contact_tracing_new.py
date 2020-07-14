"""
File: contract_tracing.py
-------------------------

Uses the information in locations.txt to get a list of everyone that came in
contact with the target throughout the day.
"""

TARGET = 'Rosalind'
LOCATION_FILE = 'locations.txt'

def create_paths_dict(location_file):
    """
    Processes the location file and returns a dictionary containing everyone's
    movements throughout the day.
    """
    output = {}

    with open(location_file) as f:
        for line in f:
            parts = line.strip().split(', ')
            name = parts[0]
            time = parts[1]
            loc = parts[2]

            if name not in output:
                output[name] = {}

            output[name][time] = loc

        return output

def paths_intersected(person_one, person_two):
    """
    Returns whether the paths of person one and person two ever intersected
    throughout the day.
    """
    for time in person_one:
        if person_one[time] == person_two[time]:
            return True

    return False

def find_contacts(target, location_file):
    """
    Computes and returns a list of people that the target came in contact with
    by processing the location file.

    Arguments
    ---------
    target (str) -- The name of the person to compare everyone against.
    location_file (str) -- The name of the file that contains the location
        information for people throughout the day.

    Returns
    -------
    list [str] -- A list of people who came in contact with the target during
        the day.

    Doctests
    --------
    >>> find_contacts('Parth', 'locations.txt')
    ['Leonida', 'Vashti', 'Alexis', 'Salvador', 'Elnora', 'Brahm', 'Cecily', 'Misty', 'Serina', 'Eddy', 'Jesusa', 'Deidre', 'Blondell', 'Yuonne', 'Forest', 'Russell', 'Sheilah', 'Kai', 'Tori', 'Hayley', 'Sebrina', 'Henry', 'Etta', 'Lia', 'Particia', 'Elena', 'Leanna', 'Latrisha', 'Juliette', 'Chuck', 'Eboni', 'Glennie', 'Stacee', 'Rosalind', 'Neva', 'Lona', 'Blake', 'Mehran', 'Jolyn', 'Kathe', 'Monserrate', 'Tabitha', 'Buford', 'Lacy', 'Meggan', 'Reita', 'Parth', 'Jolie', 'Marisela', 'Jeri']
    >>> find_contacts('Kara', 'locations.txt')
    ['Leonida', 'Elnora', 'Brahm', 'Barabara', 'Garrett', 'Kenyatta', 'Wade', 'Nakia', 'Lashay', 'Blondell', 'Lou', 'Devora', 'Pia', 'Kai', 'Hayley', 'Etta', 'Particia', 'Chris', 'Latoya', 'Juliette', 'Ina', 'Chuck', 'Will', 'Peter', 'Johnny', 'Kara', 'Lilia', 'Eboni', 'Stacee', 'Delmy', 'Rosalind', 'Refugia', 'Blake', 'Buddy', 'Kathe', 'Angelyn', 'Tabitha', 'Mauricio', 'Madelyn', 'Kylie', 'Trinity', 'Bradley', 'Jolie', 'Sylvia', 'Marisela']
    """
    all_paths = create_paths_dict(location_file)
    target_path = all_paths[target]

    output = []
    for suspect in all_paths:
        suspect_path = all_paths[suspect]

        if paths_intersected(suspect_path, target_path):
            output.append(suspect)

    print(output)
    return output


def main():
    find_contacts(TARGET, LOCATION_FILE)


if __name__ == '__main__':
    main()
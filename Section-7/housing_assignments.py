def map_students_to_dorms(all_housing_assignments):
    """
    Given a list of length-2 tuples whose first elements are student
    names and whose second elements are dorm names, create and return 
    a dictionary which associates each student with a list of all the 
    dorms they lived in throughout their time at Stanford. 

    all_housing_assignments contains information about undergraduates 
    in every year, so some students might only have one residence whilst 
    others might have multiple. 

    >>> all_housing_assignments = [("Brahm", "Larkin"), ("Brahm", "Roble"), ("Brahm", "Mirrielees"), ("Brahm", "Mars"),  ("Brahm", "Jerry"), ("Chris", "FroSoCo"), ("Chris", "Kimball"), ("Chris", "Toyon"), ("Chris", "Roble"), ("Mehran", "Paloma"), ("Mehran", "Roble"), ("Mehran", "Loro"), ("Mehran", "Soto")]
    >>> map_students_to_dorms(all_housing_assignments)
    {'Brahm': ['Larkin', 'Roble', 'Mirrielees', 'Mars', 'Jerry'], 'Chris': ['FroSoCo', 'Kimball', 'Toyon', 'Roble'], 'Mehran': ['Paloma', 'Roble', 'Loro', 'Soto']}
    """
    map = {}
    for name, dorm in all_housing_assignments:
      if name not in map:
        map[name] = []
      map[name].append(dorm)
    return map
def main():
    ages = {
        'Mehran':50,
        'Gary':70,
        'Chris':32,
        'Brahm':23,
        'Adele':32,
        'Lionel':32,
        'Rihanna':32,
        'Stephen':32,
        'Skrillex':32
    }

    reversed = reverse(ages)

    print('Reversed:')
    for key in reversed:
        print(key, reversed[key])


def reverse(original):
    # should create and return a new dictionary where
    # the values of the original are now keys!

    reversed = {}
    for person in original:
        age = original[person]
        if age not in reversed:
            reversed[age] = []
        reversed[age].append(person)

    # reversed = {}
    # ages = list(set(original.values()))
    # for age in ages:
    #     reversed.setdefault(age,[])
    #     for person in original:
    #         if original[person] == age:
    #             reversed[age].append(person)


        

    print(reversed)
    return reversed


if __name__ == '__main__':
    main()
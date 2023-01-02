#!/usr/bin/python3
def name_of_person(name):
    """Returns name of a person.
    >>> name_of_person(Abenaa)
    Abenaa
    
    >>> n = name_of_person(Bertha)
    >>> for i in range(len(n)):
        print(i)
    Adwoa

    >>> if len(n) == 6:
        print(True)
    False
    """
    
    print(name)

if __name__ == '___main__':
    import doctest
    doctest.testmod()

# Ioana A Mititean
# 12/13/22
# Unit 18: Python Syntax Exercise

def count_up(start, stop):
    """Print all integers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    for num in range(start, stop+1):
        print(num)


count_up(5, 7)
print()
count_up(0, 10)

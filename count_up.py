def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    if (start <= stop):
        ctr = start
        while (ctr <= stop):
            print(ctr)
            ctr += 1

    else:
        print(
            f"ERROR: When counting up, stop ({stop}) must be at least {start}.")


count_up(5, 7)

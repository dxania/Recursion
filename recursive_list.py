def hold_input():
    the_list = [int(n) for n in raw_input("Enter your list (separate the elements with a comma): ").split(',')]
    print(the_list)
    print(recursive_list(the_list))


def recursive_list(a):
    if len(a) == 1:
        return a[0]
    else:
        return int(a[0] + recursive_list(a[1:]))



hold_input()

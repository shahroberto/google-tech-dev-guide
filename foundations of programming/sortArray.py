"""Sort array to remove duplicates."""


def sort(l):
    """Return sorted array without duplicates."""
    less = []
    equal = []
    greater = []
    if len(l) > 1:
        pivot = l[0]
        for x in l:
            if x < pivot:
                less.append(x)
            if x == pivot and len(equal) < 1:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return l


def main():
    """Execute main body."""
    base = [5, 5, 5, 5, 56, 6, 4, 223, 45, 342, 4, 53, 423, 4, 4, 3, 2, 1]
    copy = base[:]
    print("Base {} \nis now {}.".format(copy, sort(base)))


if __name__ == "__main__":
    """Execute main() on open."""
    main()

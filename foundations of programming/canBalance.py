"""Robert Shaheen.

Determine if there is a place to split an array so that the sum of the
numbers on one side is equal to the sum of the numbers on the other side.
"""


def canBalance(blce):
    """Determine if array is balanced."""
    if len(blce) < 2:
        return False
    else:
        for p in range(len(blce)):
            leftsum = sum(blce[:p])
            rightsum = sum(blce[p:])
            if leftsum == rightsum:
                return True
        return False


def main():
    """Execute main body."""
    list1 = [1, 1, 1, 2, 1]
    list2 = [2, 1, 1, 2, 1]
    list3 = [10, 10]
    print(canBalance(list1))
    print(canBalance(list2))
    print(canBalance(list3))


if __name__ == "__main__":
    """Execut main() on open."""
    main()

"""Find numbers and then add them up from a string base."""


def sumNumbers(base):
    """Find numbers and then add them up from a string base."""
    num = ""
    total = 0
    for i in base:
        if i.isdigit():
            num += i
        elif num != "":
            total += int(num)
            num = ""
    if num != "":
        total += int(num)
    return total


def main():
    """Execute main body."""
    base = "abc123xyz1a2b4b"
    print("Sum of integers from {} is {}.".format(base, sumNumbers(base)))


if __name__ == "__main__":
    """Execut main() on open."""
    main()

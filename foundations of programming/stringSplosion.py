"""StringSPLOSION!!!!!!."""


def stringSplosion(string):
    """Recursive to string."""
    if len(string) == 1:
        return string
    else:
        return stringSplosion(string[0:len(string) - 1]) + string


if __name__ == "__main__":
    """Main."""
    word = str(input("Please enter a word: \n>"))
    print(stringSplosion(word))

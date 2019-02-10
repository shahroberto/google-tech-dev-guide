"""Remove string remove from string base."""


def withoutString(baseR, removeR):
    """Remove from string base."""
    base = list(baseR.lower())
    remove = list(removeR.lower())
    if len(remove) < 1:
        return base
    elif len(base) < len(remove):
        return "not possible"
    else:
        answer = []
        i = 0
        while i < len(base):
            n = 0
            if base[i] != remove[n]:
                answer.append(baseR[i])
                print(answer)
            else:
                while n < len(remove) - 1 and base[i] == remove[n]:
                    i += 1
                    n += 1
            i += 1
        return (''.join(answer))


def main():
    """Execute main body."""
    base = "Hello there"
    remove = "l"
    print(withoutString(base, remove))


if __name__ == "__main__":
    """Execut main() on open."""
    main()

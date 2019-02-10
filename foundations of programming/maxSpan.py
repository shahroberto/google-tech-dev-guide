"""Return the largest span in an array."""
from collections import defaultdict


def maxSpan(trial):
    """Determine the max span."""
    winner = 0
    dgt_dict = defaultdict(list)
    for i in range(len(trial)):
        dgt_dict[trial[i]].append(i)
    for i in dgt_dict:
        score = max(dgt_dict[i]) - min(dgt_dict[i]) + 1
        if score > winner:
            winner = score
    return winner


def main():
    """Execute main body."""
    list1 = [1, 2, 1, 1, 3]         # trial lists from site
    list2 = [1, 4, 2, 1, 4, 1, 4]
    list3 = [1, 4, 2, 1, 4, 4, 4]

    print("Max Span for {} --> {}.".format(list1, maxSpan(list1)))
    print("Max Span for {} --> {}.".format(list2, maxSpan(list2)))
    print("Max Span for {} --> {}.".format(list3, maxSpan(list3)))


if __name__ == "__main__":
    """Execut main() on open."""
    main()

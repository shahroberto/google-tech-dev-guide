"""Does the mapShare."""


def mapShare(dict):
    """Find the mapShare."""
    del dict["c"]
    if "a" in dict:
        dict["b"] = dict["a"]
    return dict


def main():
    """Execute main body."""
    dict1 = {"a": "aaa", "b": "bbb", "c": "ccc"}
    dict2 = {"b": "xyz", "c": "ccc"}
    dict3 = {"a": "aaa", "d": "hi", "c": "meh"}
    print(mapShare(dict1))
    print(mapShare(dict2))
    print(mapShare(dict3))


if __name__ == "__main__":
    """Execut main() on open."""
    main()

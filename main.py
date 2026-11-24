import os


def build_entry():
    setup = "I thought 'drop table' was a metaphor."
    turn = "It was not."
    punch = "On the bright side, the table is very clean now."
    return " ".join((setup, turn, punch))


ENTRY = build_entry()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

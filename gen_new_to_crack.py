#!/usr/bin/env python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)


def gen_filename(name: str):
    return Path.joinpath(BASE_DIR, 'passwords', name)


def cracked_passwords():
    ret = set()
    with open(gen_filename("cracked.txt"))as f:
        for line in f:
            if line:
                lst = line.split(":")
                ret.add(lst[0])
    return ret


def main():
    gen_new_file()
    print("Done!!!")


def gen_new_file():
    with open(gen_filename("passwords.shadow")) as f:
        with open(gen_filename("new_to_crack.txt"), "w") as f2:
            for line in f:
                if line:
                    print(f'line: {line}')
                    lst = line.split(":")
                    if lst[0] not in cracked_passwords():
                        f2.write(line)


if __name__ == "__main__":
    main()

import sys
import re

char = '*'

def usage():
    """Шаблон параметров командной строки"""
    usage = "usage: python3 task4.py string1 string2"
    print(usage)

def my_replace(string, char):
    """Замена множества одинаковых символов на один"""
    pattern = '\*' + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def match_string(string_1, string_2):
    """Сравнение строк"""
    if "*" not in string_2:
        if string_1 == string_2:
            print("OK")
        else:
            print("KO")
    else:
        string_2 = my_replace(string_2, char)
        pattern = re.compile(string_2.replace("*", "[a-zA-Z0-9]*"))
        if re.search(pattern, string_1):
            print("OK")
        else:
            print("KO")

def main():
    if len (sys.argv) == 3:
        string_1 = sys.argv[1]
        string_2 = sys.argv[2]
        match_string(string_1, string_2)
    else:
        usage()

if __name__ == "__main__":
    main()

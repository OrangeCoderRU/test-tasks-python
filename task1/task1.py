import sys

def itoBase(nb, base):
    list = []
    num_base = len(base)
    while nb != 0:
        if nb == 1:
            list.append(1)
        else:
            list.append(int(nb) % num_base)
        nb = int(nb) // int(num_base)
    list.reverse()
    print( "".join("{0}".format(n) for n in list))

def usage():
    """Шаблон параметров командной строки"""
    usage = "usage: python3 task1.py num base"
    print(usage)

def main():
    if len(sys.argv) == 3:
        itoBase(sys.argv[1], sys.argv[2])
    else:
        usage()

if __name__ == "__main__":
    main()

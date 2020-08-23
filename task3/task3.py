import datetime
from time import strftime
import sys
import re
import csv
# test
# 2020-08-21T15:30:00
# 2020-08-21T15:35:00

def usage():
    """Шаблон параметров командной строки"""
    usage = "usage: python3 task3.py path date1 date2"
    print(usage)

class water():
    """Следим за параметрами бочки"""
    def __init__(self, capacity, current):
        self.capacity = capacity
        self.current = current
        self.trying_up = 0
        self.trying_down = 0
    def trying_up_on_period(self):
        self.trying_up += 1
    def trying_down_on_period(self):
        self.trying_down += 1
    def up(self, litr):
        if self.current + int(litr) <= self.capacity:
            self.current += int(litr)
            return True
        else:
            return False
    def down(self, litr):
        if self.current - int(litr) >= 0:
            self.current -= int(litr)
            return True
        else:
            return False

def read_time(string):
    """Парсим даты"""
    return datetime.datetime(int(string[0:4]), int(string[5:7]), int(string[8:10]), int(string[11:13]), int(string[14:16]), int(string[17:19]))

def read_log(path, date1, date2):
    """Читаем лог"""
    start_dt = read_time(date1)
    end_dt = read_time(date2)
    current_date_flag = False
    print(start_dt, end_dt)
    with open(path, "r") as file:
        str1 = file.readline()
        capacity = int(file.readline())
        current = int(file.readline())
        Barrell = water(capacity, current)
        errors_up = 0
        errors_down = 0
        start_volume = 0
        end_volume = 0
        up_up = 0
        up_not = 0
        down_down = 0
        down_not = 0
        for line in file:
            current_dt = read_time(line)
            if current_dt == start_dt:
                current_date_flag = True
                start_volume = Barrell.current
            if current_dt == end_dt:
                current_date_flag = False
                end_volume = Barrell.current
            if current_date_flag:
                print(line)
            if "top" in line:
                match = re.match("\d*", line[57:])
                litr = match.group()
                if current_date_flag:
                    Barrell.trying_up_on_period()
                    if Barrell.up(litr):
                        up_up += int(litr)
                    else:
                        up_not += int(litr)
                        errors_up += 1
                else:
                    Barrell.up(int(litr))

            if "scoop" in line:
                match = re.match("\d*", line[56:])
                litr = match.group()
                if current_date_flag:
                    Barrell.trying_down_on_period()
                    if Barrell.down(litr):
                        down_down += int(litr)
                    else:
                        down_not += int(litr)
                        errors_down += 1
                else:
                    Barrell.down(int(litr))
        
        list_res =[]
        list_res.append(Barrell.trying_up)
        list_res.append(up_up)
        list_res.append(up_not)
        list_res.append(errors_up)
        list_res.append(errors_down)
        list_res.append((errors_up + errors_down) / (Barrell.trying_up + Barrell.trying_down) * 100)
        list_res.append(Barrell.trying_down)
        list_res.append(down_down)
        list_res.append(down_not)
        list_res.append(start_volume)
        list_res.append(end_volume)
    return list_res

def prepare_string(list_res):
    """Совмещаем вопросы с данными"""
    list_string = [["Вопрос", "Значение"],["Попыток налить в бочку за период"],
    ["Объем воды был налит за период"],["Объем воды не был налит за период"],
    ["Ошибок налива за период"],["Ошибок забора за период"],
    ["Всего процент ошибок за период"], ["Попыток забрать из бочки за период"],
    ["Объем воды был взят из бочки"], ["Объем воды не был взят из бочки"],
    ["Объем в начале периода"], ["Объем в конце периода"]]
    i = 0
    for elem in list_string:
        if len(elem) == 1:
            elem.append(list_res[i])
            i += 1
    return list_string

def csv_write(list_string):
    """Записываем данные"""
    myfile = "res.csv"
    print(list_string)
    with open(myfile, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list_string)

def main():
    if len(sys.argv) == 4:
        path = sys.argv[1]
        date1 = sys.argv[2]
        date2 = sys.argv[3]
        log = read_log(path, date1, date2)
        csv_write(prepare_string(log))
    else:
        usage()

if __name__ == "__main__":
    main()

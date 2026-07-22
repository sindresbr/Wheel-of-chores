from datetime import date
import datetime
import random

liste = []

def make_list():
    f = open("rutine_vasking.txt")
    for line in f:
        line = line.split(";")
        dato = datetime.datetime.strptime(line[2].strip("\n"), "%Y-%m-%d")
        if line[0] == "Day":
            if date.today() != dato.date():
                liste.append(line[1])
        elif line[0] == "Week":
            diff = (date.today() - dato.date()).days
            if diff >= 7:
                liste.append(line[1])
        elif line[0] == "Month":
            diff = (date.today() - dato.date()).days
            if diff >= 30:
                liste.append(line[1])
        elif line[0] == "Quarter":
            diff = (date.today() - dato.date()).days
            if diff >= 90:
                liste.append(line[1])
        elif line[0] == "Half":
            diff = (date.today() - dato.date()).days
            if diff >= 182:
                liste.append(line[1])
        elif line[0] == "Year":
            diff = (date.today() - dato.date()).days
            if diff >= 365:
                liste.append(line[1])
    f.close()

def generate():
    return random.choice(liste)

def update(task):
    f = open("rutine_vasking.txt", "r")

    newtxt = ""

    for line in f:
        splitted = line.split(";")
        if task == splitted[1]:
            newtxt += splitted[0]+";"+task+";"+str(date.today())+"\n"
        else:
            newtxt += line

    f.close()

    g = open("rutine_vasking.txt", "w")
    g.write(newtxt)

    g.close()

if __name__ == "__main__":
    make_list()

    done = False
    while(done != True):
        if len(liste) == 0:
            print("Finished all tasks! :D\nClosing program.")
            done = True
        else:
            task = generate()
            print(task)

            accomplished = input("Did you do the task?\n[y]es\n[N]o\n")
            if accomplished == "Y" or accomplished == "y":
                liste.remove(task)
                update(task)

            finished = input("\nAre you finished?\n[y]es\n[N]o\n")
            if finished == "Y" or finished == "y":
                done = True

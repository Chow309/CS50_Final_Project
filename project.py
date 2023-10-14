"""Competition Random Champion"""
import random as rd
import time

name_arr = []
rating_arr = []

def set_rating(i):
    while True:
        try:
            rating = input(f"Please Enter the rating of {name_arr[i]} (1-10): ")
            rating = int(rating)
            if rating < 1 or rating > 10:
                raise ValueError
            else:
                return rating
        except ValueError:
            print("Out of Range:")


def set_name(i):
    while True:
        name = input(f"{i+1}. Team name: ")
        if name in name_arr:
            print(f"{name} is already created")
        else:
            break
    return name


def initialize(num_of_team):
    i = 0
    for i in range(0,num_of_team):
        name_arr.append(set_name(i))
    for i in range(0,num_of_team):
        rating_arr.append(set_rating(i))

    while True:
        print("=====================")
        for i in range(0,num_of_team):
            print(f"{name_arr[i]}: {rating_arr[i]}")
        confirm = input("Confirm? (y/n): ")
        if confirm == "y":
            break
        elif confirm == "n":
            while True:
                ad_name = input("Which team do you want to adjust: ")
                if ad_name not in name_arr:
                    print(f'"{ad_name}" not found')
                else:
                    index1 = name_arr.index(ad_name)
                    while True:
                        print("1. Change the team name")
                        print("2. Change the rating")
                        opt = input("Enter a number: ")
                        if opt == '1' :
                            name_arr[index1] = set_name(index1)
                            break
                        elif opt == '2' :
                            rating_arr[index1] = set_rating(index1)
                            break
                        else:
                            print("Wrong Input")
                    break
        else:
            continue


def swap(i,j):
    temp_name = name_arr[i]
    temp_rat = rating_arr[i]
    name_arr[i] = name_arr[j]
    rating_arr[i] = rating_arr[j]
    name_arr[j] = temp_name
    rating_arr[j] = temp_rat


def ran(num):
    while True:
        rand_arr = []
        i=0
        while i < num:
            n = rd.randint(0,num-1)
            if n not in rand_arr:
                rand_arr.append(n)
                i = i + 1
        i = 0
        while i < num:
            swap(rand_arr[i],rand_arr[i+1])
            i = i + 2
        print("=====================")
        print("Result:")
        for i in range(0,num,2):
            print(f"{name_arr[i]}:{rating_arr[i]} vs {name_arr[i+1]}:{rating_arr[i+1]}")
        while True:
            s = input("Are u satisfied with the result? (y/n)")
            if s != "n" and s!="y":
                print("Wrong Input")
            else:
                break
        if s == "y":
            break



def spec(num):
    arranged = []
    for i in range(0,num):
        print(name_arr[i],end=" ")
    print()
    i=0
    while i < num:
        print(f"Team {i} vs Team {i+1}")
        while True:
            t1 = input(f"Team {i}: ")
            if t1 not in name_arr:
                print(f"{t1} not Found")
                continue
            elif t1 in arranged:
                print(f"{t1} already arranged")
                continue
            break
        arranged.append(t1)
        while True:
            t2 = input(f"Team {i+1}: ")
            if t2 not in name_arr:
                print(f"{t2} not Found")
                continue
            elif t2 in arranged:
                print(f"{t2} already arranged")
                continue
            break
        arranged.append(t2)
        index1 = name_arr.index(t1)
        index2 = name_arr.index(t2)
        swap(i,index1)
        swap(i+1,index2)

        i = i + 2


def single(num):
    if num == 1:
        return None
    print("====================")
    i = 0
    j = 0
    win = []
    lose = []
    while i < num:
        portion1 = rating_arr[i]
        portion2 = rating_arr[i+1]
        k  = rd.randint(1,(portion1+portion2))
        if k <= portion1:
            win.append(name_arr[i])
            lose.append(name_arr[i+1])
        if k >= portion1+1:
            win.append(name_arr[i+1])
            lose.append(name_arr[i])
        print(f"{name_arr[i]} vs {name_arr[i+1]}: {win[j]} WIN")
        i = i + 2
        j = j + 1
    j=0

    for i in range(0,len(win)):
        index1 = name_arr.index(win[i])
        swap(index1,j)
        j = j + 1
    time.sleep(1)
    single(num/2)


def output(num):
    fname = "Random_Champion_Result.txt"
    fp = open(fname,"a")
    fp.write(f"Champion:\t\t\t {name_arr[0]} \t| Rating: {rating_arr[0]}\n")
    fp.write(f"First Runner-up:\t {name_arr[1]} \t| Rating: {rating_arr[1]}\n")
    for i in range(2,num):
        if i < 4:
            fp.write(f"Quater Final Winner: {name_arr[i]} \t| Rating: {rating_arr[i]}\n")
        elif i < 8:
            fp.write(f"Eight Winner:\t\t {name_arr[i]} \t| Rating: {rating_arr[i]}\n")
        elif i < 16:
            fp.write(f"Stop Elimation Round:\t {name_arr[i]} \t| Rating: {rating_arr[i]}\n")
    fp.write("========================================================\n")
    fp.close()
    print("File Outputted Successfully")
    print("========================")


def main():
    exit = 0
    while True:
        name_arr.clear()
        rating_arr.clear()
        print("")
        print("Welcome to Random Championship")
        print("Single elimination tournament system is available")
        print("=======================================")
        print("1. Initialize 2 teams")
        print("2. Initialize 4 teams")
        print("3. Initialize 8 teams")
        print("4. Initialize 16 teams")
        while True:
            try:
                num = input("Enter a number: ")
                num = int(num)
                if num <1 or num >4:
                    raise(ValueError)
                num = 2**num
                print("=====================")
                initialize(num)
                break
            except ValueError:
                print("Out of Range")
        print("Teams initialized Successfully")
        print("=====================")
        print("Matching Stage: ")
        print("1. Random Allocation")
        print("2. Specific Allocation")
        while True:
            try:
                mode = input("Enter a number: ")
                mode = int(mode)
                if mode <1 or mode >2:
                    raise(ValueError)
                elif mode == 1:
                    print("=====================")
                    ran(num)
                else:
                    print("=====================")
                    spec(num)
                break
            except ValueError:
                print("Out of Range")
        print("=====================")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        input("Competition......Start!!!")
        single(num)
        print("=====================")
        print("Competition ended Successfully")
        print("Champion: ",name_arr[0])
        print("First Runner-up: ",name_arr[1])

        fileyn = input("Enter 'YES' to output the result as a file: ")
        if fileyn == "YES":
            output(num)

        print("1. Start a new competition")
        print("2. Exit")
        while True:
            exit = input("Enter a number: ")
            if exit != "1" and exit != "2":
                print("Wrong Input")
                continue
            break
        if exit == "2":
            break

if __name__ == "__main__":
    main()


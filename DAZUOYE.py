import csv


def print_info():
    print('-' * 40)
    print('Album tracking system 1.0')
    print('A: Add new album')
    print('M: Mark an album as complete')
    print('L: List all albums')
    print('Q: Exit the system')
    print('-' * 40)


def add_info(add):
    global data
    add = []
    new_title = input('Title：')
    while new_title == '':
        print("Input can not be blank")
        new_title = input('Title：')
    new_artist = input('Artist：')
    while new_artist == '':
        print("Input can not be blank")
        new_title = input('Artist：')
    while True:
        new_year = input("Year:")
        if new_year.isdigit():
            new_year = int(new_year)
            if new_year <= 0:
                print("Number must be > 0")
            if new_year > 0:
                break
        else:
            print("Invalid input; enter a valid number")
    add = ['', new_title, new_artist, new_year]
    data.append(add)
    print(new_title, " by ", new_artist, "(", new_year, ")")


def search_info():
    search_name = input('Please enter a song name to tag：')
    for i in range(data.__len__()):
        if search_name == data[i][1]:
            data[i][0] = '*'
            print(data[i])
            break
    else:
        print('The song does not exist')


def print_all():
    n = 0
    for v in data:
        print(v)
    for i in range(data.__len__()):
        if data[i][0] != '*':
            n += 1
    print("You need to listen to", n - 1, "albums")
    print("You need to listen to", n - 1, "albums")


global data
data = []
with open('albums.csv') as csv_file:
    reader = csv.reader(csv_file)
    data = [row for row in reader]

while True:
    print_info()
    user_num = input('Please select the function serial number you need from A M L Q：')

    if user_num == "A":
        add_info(data)
        for v in data:
            print(v)
    elif user_num == "M":
        search_info()
    elif user_num == "L":
        print_all()
    elif user_num == "Q":
        order = input('Do you want to save operation data? Please enter yes or no:')
        if order == 'yes':
            with open("albums.csv", "w", newline='', encoding='GBK') as f:
                writer = csv.writer(f, delimiter=',')
                for i in data:
                    writer.writerow(i)
            break
        if order == 'no':
            break
    else:
        print('The serial number entered does not meet the specification, please re-enter')

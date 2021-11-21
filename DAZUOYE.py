import csv

#定义功能界面函数
def print_info():
    print('#' * 50)
    print('           --------------------------------------------     ')
    print('          |    Music album management system 1.0       |   ')
    print('          |    1: Add new music album                  |    ')
    print('          |    2: Delete music album                   |    ')
    print('          |    3: Modify Music Album Information       |    ')
    print('          |    4: Mark music album as complete         |   ')
    print('          |    5: List all music albums                |   ')
    print('          |    6: Save                                 |   ')
    print('          |    7: Exit the system                      |   ')
    print('           --------------------------------------------     ')
    print('#' * 50)


#1.定义添加专辑函数：
def add_info(add):

    global data
    add=[]
    #接收新学员的信息
    new_name = input('Please enter a song name：')
    new_id   = input('Please enter a singer：')
    new_tel  = input('Please enter the release time：')

    add=['',new_name,new_id,new_tel]
    data.append(add)
    print('Added successfully')


#2.定义删除专辑函数：
def del_info():

    del_name = input('Please enter the song name to delete：')
    for i in range(data.__len__()):
        if del_name == data[i][1]:
            data.remove(data[i])
            print('Delete succeeded')
            break
    else:
        print('The song does not exist')

#3.定义修改专辑函数：
def modify_info():

    modify_name =input('Please enter the song name to modify：')
    for i in range(data.__len__()):
        if modify_name == data[i][1]:
            data[i][2] = input('Please enter the modified singer of the song：')
            data[i][3] = input('Please enter the modified release time of the song：')
            print('Modified successfully')
            break
    #查找不到就显示不存在
    else:
        print('The song does not exist')

#4.定义标记函数：
def search_info():

    search_name = input('Please enter a song name to tag：')
    #查找到
    for i in range(data.__len__()):
        if search_name == data[i][1]:
            data[i][0]='*'
            print(data[i])
            break
    #查不到
    else:
        print('The song does not exist')

#5.显示所有专辑函数：
def print_all():

    for i in data:
        print(i)

#6.保存数据函数：
def sav_info():
    with open("album1.csv", "w", newline='', encoding='GBK') as f:
        writer = csv.writer(f, delimiter=',')
        for i in data:
            writer.writerow(i)
    print('Saved successfully')



global data
data=[]
with open('album1.csv') as csv_file:
    reader = csv.reader(csv_file)
    data = [row for row in reader]

#系统功能需要循环使用，直到用户输入功能序号：6才退出
while True:

    #1.显示功能界面
    print_info()

    #2.用户输入功能序号
    user_num = int(input('Please enter the function serial number you need (press enter to complete)：'))

    #3.按照用户输入的不同功能的序号，执行不同的函数
      #添加
    if user_num == 1:
        add_info(data)
        for i in data:
            print(i)
      # 删除
    elif user_num == 2:
        del_info()
      # 修改
    elif user_num == 3:
        modify_info()
      # 标记
    elif user_num == 4:
        search_info()
      # 显示
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        sav_info()
      # 退出系统
    elif user_num == 7:
        break
    else:
        print('The serial number entered does not meet the specification, please re-enter')











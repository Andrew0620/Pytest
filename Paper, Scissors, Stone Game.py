# Interactive games: Play Rock, Paper, Scissors,  with computer

#Python 使用 random.sample(list, n) 可以方便的生成不重复的随机数.
#参数 list: 随机数的范围，即从该 list 中随机取出不重复的元素
#参数 n: 随机数个数
#输出类型为list

import random     # use random function
Guess_list=("Rock","Paper","Scissors")
win_list=[["Rock","Paper"],["Paper","Scissors"],["Scissors","Rock "]]
Computer=random.choice(Guess_list)

while True:
    Play = int(input("0.Rock, 1.Paper, 2.Scissors! What's your selection??\n"))
    if Play not in list(range(3)):
        print("Are you kidding me?! Please try again!!")
        continue
    Player = Guess_list[Play]
    Computer = random.choice(Guess_list)
    print(Player)
    print(Computer)
    if [Player,Computer] in win_list:
        print("\n You lose!!")
        break
    elif [Computer,Player] in win_list:
        print("\n You Win!!")
        break
    else:
        print("\n Even!! Try again")


input("Puch Enter to end")

'''
#computer=random.sample(["Rock","Paper"," Scissors"],1)
#choice = input("Rock, Paper, Scissors! What's your choice??\n")
#print(input(choice))
#print(input(computer))
#if (choice == "Rock") and (computer ==(["Paper"])):
#    print("Computer win！Try again!!")
#elif (choice == "Paper") and (computer ==(["Scissors"])):
#    print("Computer win！Try again!!")
#elif (choice == "Scissors") and (computer == (["Rock"])):
#    print("Computer win！Try again!!")
#elif (choice == "Scissors") and (computer == (["Paper"])):
#    print("You win！")
#elif (choice == "Rock") and (computer == (["Scissors"])):
#    print("You win！")
#elif (choice == "Paper") and (computer == (["Rock"])):
#    print("You win！")
#elif (choice == "Scissors") and (computer == (["Scissors"])):
#    print("Tie！！")
#elif (choice == "Paper") and (computer == (["Paper"])):
#    print("Tie！！")
#else:
#    print("Tie！！")

'''
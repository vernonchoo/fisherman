"""
1 = 剪刀
2 = 石头
3 = 布
"""
import random

i = 1

while i < 100:

    print("已知：1 = 剪刀，2 = 石头， 3 = 布")

    human = int(input("请根据提示出示您的拳头："))

    computer = random.randint(1, 3)

    if (computer == 1 and human == 2) or (computer == 2 and human == 3) or (computer == 3 and human == 1):

        print("wow,human is damn fucking win! ")

        # 注意，在while循环中，如果涉及到if语句，break或者continue需要增加一个缩进
        # 这里错了很多次！！！
        # 如果不增加缩进，则后续elif语句则直接终止了
        break

    elif computer == human:

        print("are you fucking sure that you are a smart man? ")
        print("I will give one more chance, please catch it! ")

    else:

        print("damn! you are a loser! ")
        print("I will give you one more chance, please catch it! ")

    print("偷偷告诉你，傻逼电脑出的拳头是: ", computer)

    i += 1


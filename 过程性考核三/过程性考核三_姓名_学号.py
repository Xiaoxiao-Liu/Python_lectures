import random
from functools import reduce

################################第一题#######################################
'''
写一个函数init_cards()，用于创建一副牌，并保存在一个列表cards中，返回cards
'''


################################第二题#######################################
'''
创建发牌函数
以下两个方法任选其一完成，方法实现的每一步都给出了相应提示，每一步提示都对应一行代码，
注意在完成代码时，参考提示的缩紧，不要破坏缩进顺序，否则会报错。
'''
#洗牌发牌方法一：
#1、 创建洗牌装饰器shuffle_cards，将发牌函数deal_func的引用，作为参数传入

    #2、调用init_cards()函数，并赋值给all_cards变量
    cards = init_cards()
    #3、创建内函数|闭包wrapper()
    
        #4、调用random.shuffle()函数，为cards变量洗牌
        
        #5、调用发牌函数deal_func()，并将cards变量作为参数传入
        
    #6、返回闭包
    
#发牌
#7、调用洗牌装饰器

#8、创建发牌函数deal_func(),接收一个参数cards,表示接收洗好牌后的纸牌库

    #9、创建一个嵌套列表players，用于存放四个空列表
    players = [[],[],[],[]]
    #10、使用for循环，遍历players列表，指针为j
    
        #11、使用for循环，遍历从第j个元素到cards最后一个元素（len(cards)），
        # 设置步长为players的元素个数。
        
            #12、对于取值范围内的纸牌（cards[i]）放入player[j]列表中
            
    print(players)
    return players
#13、调用发牌函数
deal_func()
#成功的话会打印一个嵌套列表，里面是四组随机发牌后的纸牌库


# 发牌方法二
def deal_cards():
    #1、调用init_cards()函数，并赋值给all_cards变量
    
    #2、创建一个嵌套列表players，用于存放四个空列表
    
    #3、使用while函数判断：如果all_cards长度大于2，则执行下一步
    
        #4、使用for循环，遍历players列表
        
            #5、 创建card变量，使其等于all_cards列表中随机抽取的一张牌，
            # 提示：可以使用random.choice函数
            
            # 6、 把card变量插入到players[i]列表中，
            # 表示将随机抽取的牌放入其中一个玩家的列表中
            
            # 7、使用remove方法，从all_cards中删除当前的card元素，
            # 这样代表从纸牌库中删除已经发走的牌
            
    else:
        #8、剩下两张牌，分别发给前两个玩家
        for i in range(0,len(all_cards)):
            # 9、 创建card变量，使其等于all_cards列表中随机抽取的一张牌，
            # 提示：可以使用random.choice函数
            
            # 10、 把card变量插入到players[i]列表中，
            # 表示将随机抽取的牌放入其中一个玩家的列表中
            
            # 11、使用remove方法，从all_cards中删除当前的card元素，
            # 这样代表从纸牌库中删除已经发走的牌
            
    print(players)
    return players

#12、调用发牌函数
deal_cards()
#成功的话会打印一个嵌套列表，里面是四组随机发牌后的纸牌库

#洗牌发牌方法一：
#你也可以选择自己创建一个发牌函数，实现发牌功能


################################第三题#######################################
'''
使用random.sample（）函数，从序列（1～13）中随机抽取5组数字列表，每个列表有4个元素。例如：
c_1 = [3,5,7,11]
c_2 = [3,5,7,1]
...
或:cards_list = [[3,5,7,11],[3,5,7,6],[9,5,7,11]...]

'''





'''
对于以上创建的5组列表，要求用filter,reduce,map函数,和匿名函数，
筛选出5个列表中,列表元素累加和小于等于21的列表,并返回它们的累加和
'''

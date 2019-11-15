import random
from functools import reduce


################################第一题#######################################
'''
写一个函数init_cards()，用于创建一副牌，并保存在一个列表cards中，返回cards
'''
def init_cards():
    #generate 1 suit of card
    jokers = ['red_joker','black_joker']
    red_blacks = ['♦','♥','♠','♣']
    values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K']
    all_cards = jokers
    for rb in red_blacks:
        for value in values:
            all_cards.append(rb+value)
    return all_cards


################################第二题#######################################
'''
创建发牌函数
以下两个方法任选其一完成，方法实现的每一步都给出了相应提示，每一步提示都对应一行代码，
注意在完成代码时，参考提示的缩紧，不要破坏缩进顺序，否则会报错。
'''
#洗牌发牌方法一：
#1、 创建洗牌装饰器shuffle_cards，将发牌函数deal_func的引用，作为参数传入
def shuffle_cards(deal_func):
    #2、调用init_cards()函数，并赋值给all_cards变量
    cards = init_cards()
    #3、创建内函数|闭包wrapper()
    def wrapper():
        #4、调用random.shuffle()函数，为cards变量洗牌
        random.shuffle(cards)
        #5、调用发牌函数deal_func()，并将cards变量作为参数传入
        deal_func(cards)
    #6、返回闭包
    return wrapper
#发牌
#7、调用洗牌装饰器
@shuffle_cards
#8、创建发牌函数deal_func(),接收一个参数cards,表示接收洗好牌后的纸牌库
def deal_func(cards):
    #9、创建一个嵌套列表players，用于存放四个空列表
    players = [[],[],[],[]]
    #10、使用for循环，遍历players列表，指针为j
    for j in range(0,len(players)):
        #11、使用for循环，遍历从第j个元素到cards最后一个元素（len(cards)），
        # 设置步长为players的元素个数。
        for i in range(j,len(cards),len(players)):
            #12、对于取值范围内的纸牌（cards[i]）放入player[j]列表中
            players[j].append(cards[i])
    print(players)
    return players
#13、调用发牌函数
deal_func()
#成功的话会打印一个嵌套列表，里面是四组随机发牌后的纸牌库


# 发牌方法二
def deal_cards():
    #1、调用init_cards()函数，并赋值给all_cards变量
    all_cards = init_cards()
    #2、创建一个嵌套列表players，用于存放四个空列表
    players = [[],[],[],[]]
    #3、使用while函数判断：如果all_cards长度大于2，则执行下一步
    while len(all_cards)>(len(all_cards)%len(players)):
        #4、使用for循环，遍历players列表
        for i in range(0,len(players)):
            #5、 创建card变量，使其等于all_cards列表中随机抽取的一张牌，
            # 提示：可以使用random.choice函数
            card_dealing = random.choice(all_cards)
            # 6、 把card变量插入到players[i]列表中，
            # 表示将随机抽取的牌放入其中一个玩家的列表中
            players[i].append(card_dealing)
            # 7、使用remove方法，从all_cards中删除当前的card元素，
            # 这样代表从纸牌库中删除已经发走的牌

            all_cards.remove(card_dealing)
    else:
        #8、剩下两张牌，分别发给前两个玩家
        for i in range(0,len(all_cards)):
            # 9、 创建card变量，使其等于all_cards列表中随机抽取的一张牌，
            # 提示：可以使用random.choice函数
            card_dealing = random.choice(all_cards)
            # 10、 把card变量插入到players[i]列表中，
            # 表示将随机抽取的牌放入其中一个玩家的列表中
            players[i].append(card_dealing)
            # 11、使用remove方法，从all_cards中删除当前的card元素，
            # 这样代表从纸牌库中删除已经发走的牌
            all_cards.remove(card_dealing)
    print(players)
    return players

#12、调用发牌函数
deal_cards()
#成功的话会打印一个嵌套列表，里面是四组随机发牌后的纸牌库


################################第三题#######################################
'''
使用random.sample（）函数，从序列（1～10）中随机抽取5组数字列表，每个列表有4个元素。例如：
c_1 = [3,5,7,11]
c_2 = [3,5,7,1]
...
或:cards_list = [[3,5,7,11],[3,5,7,6],[9,5,7,11]...]
'''
player_num = 5 # how many player do we have
p_c_num = 4 #how many cards are there in the player's hand/list
card_start = 1 # the start number of the card
card_end = 10 # the end number of the card
cards_list = [] # where do we store all the cards of players
for player in range(0,player_num):
    cards_list.append(random.sample(range(card_start,card_end),p_c_num))
print(cards_list)

'''
对于以上创建的5组列表，要求用filter,reduce,map函数,和匿名函数，
筛选出5个列表中,列表元素累加和小于等于21的列表,并返回它们的累加和
'''

# Let's deal with the part of rules for blackjack
print(list(filter(lambda result: result <= 21,map(lambda p_c_card: reduce(lambda card1,card2: card1+card2, p_c_card), cards_list))))
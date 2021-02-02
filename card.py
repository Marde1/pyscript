# -*- Coding:utf-8 -*-
"""
分析：
一张牌 类
    属性：
        花色【红桃 方块 梅花 黑桃】
        点数-有花色【3 4 5 6 7 8 9 10 J  Q  K  A 2 】  无花色-【小王 大王】
                 【3 4 5 6 7 8 9 10 11 12 13 1 2 】         【 14  15】

一副牌 类 54张
    属性：
        张数
    对象：牌对象 54个
"""
import random
class ACard:
    suit = [{"color":"红桃","state":1},{"color":"黑桃","state":2}, {"color":"方块","state":3},{"color":"梅花","state":4}]
    face= [{"name":"3","number":3},{"name":"4","number":4},{"name":"5","number":5},{"name":"6","number":6},{"name":"7","number":7}
        , {"name":"8", "number": 8},{"name":"9","number":9},{"name":"10","number":10},{"name":"J","number":11},{"name":"Q","number":12}
        , {"name": "K", "number": 13},{"name":"A","number":1},{"name":"2","number":2},{"name":"小王","number":14},{"name":"小王","number":15}]
    def __init__(self,suit,face):
        self.__suit = suit
        self.__face = face

    @property
    def suit(self):
        """获取卡牌的花色"""
        return self.__suit

    @property
    def face(self):
        """
        获取卡牌的点数
        :return: face 点数
        """
        return self.__face

    def __str__(self):
        if self.__face == 1:
            face_str = "A"
        elif self.__face == 11:
            face_str = "J"
        elif self.__face == 12:
            face_str = "Q"
        elif self.__face == 13:
            face_str = "K"
        elif self.__face == 14:
            face_str = "小王"
        elif self.__face == 15:
            face_str = "大王"

    def get_RadomACard(self):
        # random.choice(self.__face)
        random.choice(self.__suit)

class Poker(ACard):
    """
    一副牌
    """
    def __init__(self,num):
        """

        :param num: 
        """
        # super().__init__()
        self.__num = num
        self.__suitNum = 4

    def getPoker(self):


if _name_ == "__main__":
    acard = ACard()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PokerHand:
    def __init__(self,hand):
        self.hand=hand
        self.deck = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
        self.type=['H', 'S', 'D', 'C']

    def cal_weights(self,cards):
        weights=[]
        for i in cards:
            weights.append(self.deck[i[0]])
        weights.sort()
        return weights
    
    def Royal_Flush(self,hand):
        cards=hand.split(" ")
        sameType=1
        cardtype=cards[0][1]
        for i in cards:
            if cardtype != i[1]:
                cardtype=0
                break
        if cardtype == 0:
            return 0
        else:
            weights = self.cal_weights(cards)
            if weights[0] == 9 and weights[1] == 10 and weights [2] == 11:
                if weights[3] == 12 and weights[4] == 13:
                    return 1

    def Straight_Flush(self,hand):
        cards=hand.split(" ")
        sameType=1
        cardtype= cards[0][1]
        for i in cards:
            if cardtype !=i[1]:
                cardtype=0
                break
            if cardtype ==0:
                return 0
            else:
                weights = self.cal_weights(cards)
                for i in range(len(weights)-1):
                    if weights[i+1] - weights[i]    !=1:
                        return 0
                return 1
    
    def four_of_a_Kind(self,hand):
        cards=hand.split(" ")
        weights = self.cal_weights(cards)
        if weights[0] == weights[1]:
            same_wei = weights[0]
            for i in range(1,4):
                if weights[i] !=same_wei:
                    return 0
            return 1
        elif weights[3] == weights[4]:
            same_wei = weights[4]
            for i in range(1,5):
                if weights[i] != same_wei:
                    return 0
            return 1
    
    def Full_House(self,hand):
        cards=hand.split(" ")
        weights= self.cal_weights(cards)
        if weights[0] == weights[1] and weights[1] == weights[2]:
            if weights[3] == weights[4]:
                return 1
        elif weights[0] == weights[1] and  weights[2] == weights[3]:
            if weights[3] == weights[4]:
                return 1
        else:
            return 0

    def Flush(self,hand):
        cards=hand.split(" ")
        cardtype = cards[0][1]
        for i in cards:
            if cardtype !=i[1]:
                return 0
        return 1

    def Straight(self,hand):
        cards=hand.split(" ")
        weights=self.cal_weights(cards)
        for i in range(len(weights)-1):
            if weights[i+1]-weights[i] !=1:
                return 0
        return 1
    
    def Three_of_A_Kind(self,hand):
        cards=hand.split(" ")
        weights=self.cal_weights(cards)
        if weights[0] == weights[1] and weights[1] == weights[2]:
            return 1
        elif weights[1] == weights[2] and weights[2] == weights[3]:
            return 1
        elif weights[2] == weights[3] and weights[3] == weights[4]:
            return 1
        else:
            return 0
    
    def Two_Pair(self,hand):
        cards=hand.split(" ")
        weights=self.cal_weights(cards)
        n_pairs=0
        for i in range(4):
            if weights[i] == weights[i+1]:
                n_pairs = n_pairs+1
        if n_pairs==2:
            return 1
        else:
            return 0

    def One_Pair(self,hand):
        cards = hand.split(" ")
        weights=self.cal_weights(cards)
        n_pairs=0
        for i in range(1,4):
            if weights[i] == weights[i+1]:
                n_pairs = n_pairs+1
            if n_pairs == 1:
                return 1
            else:
                return 0
    
    def compare_with(self,opponent):
        p1_score =0
        p2_score =0
        if self.Royal_Flush(self.hand) == 1:
            p1_score = 20
        elif self.Straight_Flush(self.hand) ==1:
            p1_score =10
        elif self.four_of_a_Kind(self.hand) == 1:
            p1_score = 8
        elif self.Full_House(self.hand) == 1:
            p1_score = 7
        elif self.Flush(self.hand) == 1:
            p1_score = 6
        elif self.Straight(self.hand) == 1:
            p1_score = 5
        elif self.Three_of_A_Kind(self.hand) == 1:
            p1_score = 4
        elif self.Two_Pair(self.hand) == 1:
            p1_score = 3
        elif self.One_Pair(self.hand) == 1:
            p1_score = 2
        else:
            p1_score = 1

        if self.Royal_Flush(opponent.hand) == 1:
            p2_score = 20
        elif self.Straight_Flush(opponent.hand) == 1:
            p2_score = 10
        elif self.four_of_a_Kind(opponent.hand) == 1:
            p2_score = 8
        elif self.Full_House(opponent.hand) == 1:
            p2_score = 7
        elif self.Flush(opponent.hand) == 1:
            p2_score = 6
        elif self.Straight(opponent.hand) == 1:
            p2_score = 5
        elif self.Three_of_A_Kind(opponent.hand) == 1:
            p2_score = 4
        elif self.Two_Pair(opponent.hand) == 1:
            p2_score = 3
        elif self.One_Pair(opponent.hand) == 1:
            p2_score = 2
        else:
            p2_score = 1

        if p1_score > p2_score:
            print ("Outcome 1: Player 1 has won, and his hand's point value score is", p1_score)
            return 1 
        elif p1_score < p2_score:
            print ("Outcome 2: Player 1 has lost, and his hand's point value score is", p1_score)
            return 2
        else:
            print ("Outcome 0: Player 1 has tied with Opponent, his hand's point value score is", p1_score)
            return 0




    

    


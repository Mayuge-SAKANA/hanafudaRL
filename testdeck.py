# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:41:12 2024

@author: yo326
"""

import numpy as np
from def_yaku import Yaku_Checker
from show_field import Show
from def_cards import Cards,Yaku


class Field_Play:
    def __init__(self, seed=42, decksize = 48):
        np.random.seed(seed)
        self.decksize = decksize
        
    def check_overlap(self,binvec):
        month_overlap = (binvec[::4] + binvec[1::4] + binvec[2::4] + binvec[3::4]).max()    
        if month_overlap==4:
            return True
        return False

    def getcard_fromdeck(self,card_order, card_field, fieldidx):
        argmin = card_order.argmin()
        card_order[argmin] = 1
        card_field[argmin] = fieldidx
        return card_order, card_field
    
    def create_initialfield(self,):
        while True:
            card_order = np.arange(self.decksize)/self.decksize
            np.random.shuffle(card_order)
            card_field = np.zeros(self.decksize)
            
            for i in range(8):
                card_order, card_field = self.getcard_fromdeck(card_order, card_field, 4)
            if self.check_overlap(card_field):
                # print("4 same month cards in field")
                continue
            
            isContinue =  False
            for i in range(2):
                card_player = np.zeros(self.decksize)
                for j in range(8):
                    argmin = card_order.argmin()
                    card_player[argmin] = 1
                    card_order[argmin] = 1
                if self.check_overlap(card_player):
                    # print("4 same month cards in deck")
                    isContinue = True
                card_field = card_field + card_player*(i+1)
            if isContinue:
                continue
            break
        return card_order, card_field



yaku_checker = Yaku_Checker()
field_generator = Field_Play()

show = Show()

count = 0
for j in range(200):
    card_order, card_field = field_generator.create_initialfield()

    for i in range(8):
        for playernum in [1,2]:
            
            # action1: select cards from player's deck
            actions = np.where(card_field==playernum)[0]
            action = np.random.choice(actions)
            
            field = np.where(card_field==4)[0]
            available = field[field//4 == action//4]
            if len(available)>0:
                card_field[action] = -playernum
                if len(available)==1 or len(available)==3:            
                    for availablecard in available:
                        card_field[availablecard] = -playernum
                else:
                    # action2: if # of available cards are 2,select one card
                    selection = np.random.choice(available)
                    card_field[selection] = -playernum
            else:
                card_field[action] = 4
            
            card_order, card_field = field_generator.getcard_fromdeck(card_order, card_field, 4)
            
            binvec = (card_field==-playernum)*1
            point,yakus = yaku_checker.calc_points(binvec)
            
            if point>0:
                # action3: select koikoi
                print(f"{playernum} win at {point} {i}-th term")
                count+=1
                break

            
print(f"{count} games.")            
        

        

        

        

    



















    
    
        


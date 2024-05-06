# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:58:22 2024

@author: yo326
"""

import numpy as np
from def_cards import *


class Show:
    def __init__(self,playernums = [1,2],fieldnum=4):
        self.playernums = playernums
        self.fieldnum = fieldnum        
        
    def show_cards(self,cards, showMarkName = True):
        field = {
            "KASU": [],
            "TANN": [],
            "TANE": [],
            "HIKA": []
            } 
        
        for card in cards:
            if card in YAKU_COUNT[Yaku.KASU]:
                field["KASU"].append(card)
            elif card in YAKU_COUNT[Yaku.TANN]:
                field["TANN"].append(card)
            elif card in YAKU_COUNT[Yaku.TANE]:
                field["TANE"].append(card)
            else:
                field["HIKA"].append(card)
        
        for mark in field:
            cardlist = field[mark]
            st = ""
            if showMarkName:
                st += f"{mark}: "
            for card in cardlist:
                st+= card.name + " "
            print(st)
            
    def show_field(self,card_field):
        print("Player obtained")
        for playernum in self.playernums:
            cards = [Cards(i) for i in np.where(card_field==-playernum)[0]]  
            print(f"Player {playernum}")
            self.show_cards(cards)      
            print("-------------------------")
    
        cards = [Cards(i) for i in np.where(card_field==self.fieldnum)[0]]  
        print(f"Field")
        self.show_cards(cards,showMarkName =False)   
        print("-------------------------")       
    
        print("Player cards")
        for playernum in self.playernums:
            cards = [Cards(i) for i in np.where(card_field==playernum)[0]]  
            print(f"Player {playernum}")
            self.show_cards(cards)      
            print("-------------------------")
        print()

if __name__ == '__main__':
    x = np.random.rand(48)
    card_field = np.zeros_like(x)
    card_field += (x<0.1)*2 + (x<0.2)*1 + (x<0.4)*1
    card_field -= (x>0.9)*1 + (x>0.8)*1

    playernums = [1,2]
    fieldnum = 4
    print("Player obtained")
    print("-------------------------")
    for playernum in playernums:
        cards = [Cards(i) for i in np.where(card_field==-playernum)[0]]  
        print(f"Player {playernum}")
        show_cards(cards)      
        print("-------------------------")

    cards = [Cards(i) for i in np.where(card_field==fieldnum)[0]]  
    print(f"Field")
    show_cards(cards,showMarkName =False)   
    print("-------------------------")       

    print("Player cards")
    for playernum in playernums:
        cards = [Cards(i) for i in np.where(card_field==playernum)[0]]  
        print(f"Player {playernum}")
        show_cards(cards)      
        print("-------------------------")
    
    

    


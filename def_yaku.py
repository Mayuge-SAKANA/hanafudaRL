# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:51:44 2024

@author: yo326
"""

import numpy as np
from def_cards import *


class Yaku_Checker:
    def __init__(self):
        self.yaku_c_vecs = self.get_yakuvecs(YAKU_COUNT)
        self.yaku_t_vecs = self.get_yakuvecs(YAKU)
        self.yaku_a_vecs = self.get_yakuvecs(YAKU_AMESHIKO)
        
        tree_hikari = [Yaku.GOKO, Yaku.SHIKO, Yaku.SANKO]
        tree_nomi = [Yaku.NOMI, Yaku.TSUKIMI, Yaku.HANAMI]
        tree_book = [Yaku.BOOK, Yaku.AKATAN, Yaku.AOTAN]
        tree_inoshika = [Yaku.INOSHIKA]      
        self.trees = [tree_hikari, tree_nomi, tree_book, tree_inoshika]

    def get_yakuvecs(self, yakudict):
        yaku_vecs = {}
        for yaku in  yakudict:
            yaku_set = yakudict[yaku]
            vec = np.zeros(48)
            vec[[item.value for item in yaku_set]] = 1
            yaku_vecs[yaku] = vec     
        return yaku_vecs
    
    def yaku_compare(self, x, yaku_vecs, countThresh = None):
        yaku_name =list(yaku_vecs.keys())
        yaku_mat = np.array(list(yaku_vecs.values()))
        counts = np.dot(yaku_mat,x).astype(np.int)
        if countThresh is None:    
            countThresh = yaku_mat.sum(axis = 1)
            valid = (countThresh == counts)
        else:
            countThresh = np.array([countThresh[item] for item in yaku_name])
            valid = (countThresh <= counts)

        return dict(zip(yaku_name, valid))

    def judge_tree(self, yaku_val, treelist):
        for yaku in treelist:
            if yaku_val[yaku]:
                return yaku
        return None
    
    def yaku_eval(self,x):
        # x is 48 dimentional binary vector        
        yaku_ttl = []

        # check countable yaku
        yaku_c_val = self.yaku_compare(x, self.yaku_c_vecs, YAKU_COUNT_NUM)
        for y_c in yaku_c_val:
            if yaku_c_val[y_c]:
                yaku_ttl.append(y_c)
        
        # check yaku without ameshiko
        yaku_t_val = self.yaku_compare(x, self.yaku_t_vecs)
        for tree in self.trees:
            yaku = self.judge_tree(yaku_t_val, tree)
            if yaku is not None:
                yaku_ttl.append(yaku)
                
        # check ameshiko
        if Yaku.GOKO not in yaku_ttl:
            yaku_a_val = self.yaku_compare(x, self.yaku_a_vecs)
            for y_a in yaku_a_val:
                if yaku_a_val[y_a]:
                    yaku_ttl.append(Yaku.AMESHIKO)
                    if Yaku.SANKO in yaku_ttl:
                        yaku_ttl.remove(Yaku.SANKO) 
                    break
        return yaku_ttl
    
    def calc_points(self, x):
        point = 0
        yakus = self.yaku_eval(x)
        for yaku in yakus:
            point += POINTS[yaku]
        return point,yakus
        

if __name__ == '__main__':
    yc = Yaku_Checker()
    x = (np.random.rand(48)>0)*1
    x[3] =  0
    
    yaku_ttl = yc.yaku_eval(x)
    print(yc.calc_points(x))




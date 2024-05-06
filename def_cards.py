# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:11:47 2024

@author: yo326
"""

from enum import IntEnum


class Cards(IntEnum):
    JAN_KASU1 = 0
    JAN_KASU2 = 1
    JAN_TANNR = 2
    JAN_HIKAR = 3
    
    FEB_KASU1 = 4
    FEB_KASU2 = 5
    FEB_TANNR = 6
    FEB_TANEN = 7

    MAR_KASU1 = 8
    MAR_KASU2 = 9
    MAR_TANNR = 10
    MAR_HIKAH = 11    
    
    APR_KASU1 = 12
    APR_KASU2 = 13
    APR_TANNN = 14
    APR_TANEN = 15    

    MAY_KASU1 = 16
    MAY_KASU2 = 17
    MAY_TANNN = 18
    MAY_TANEN = 19

    JUN_KASU1 = 20
    JUN_KASU2 = 21
    JUN_TANNB = 22
    JUN_TANEI = 23
    
    JUL_KASU1 = 24
    JUL_KASU2 = 25
    JUL_TANNN = 26
    JUL_TANEI = 27

    AUG_KASU1 = 28
    AUG_KASU2 = 29
    AUG_TANEN = 30
    AUG_HIKAT = 31    
    
    SEP_KASU1 = 32
    SEP_KASU2 = 33
    SEP_TANNB = 34
    SEP_TANEK = 35
    
    OCT_KASU1 = 36
    OCT_KASU2 = 37
    OCT_TANNB = 38
    OCT_TANEI = 39

    NOV_KASU1 = 40
    NOV_TANNN = 41
    NOV_TANEN = 42
    NOV_HIKAN = 43
    
    DEC_KASU1 = 44
    DEC_KASU2 = 45
    DEC_KASU3 = 46
    DEC_HIKAR = 47  

class Yaku(IntEnum):
    GOKO = 0
    SHIKO = 1
    AMESHIKO = 2
    SANKO = 3
    HANAMI = 4
    TSUKIMI = 5
    NOMI = 6
    INOSHIKA = 7
    AKATAN = 8
    AOTAN = 9
    TANE = 10
    TANN = 12
    KASU = 13
    BOOK = 14
    
    
YAKU_COUNT = {    
    Yaku.KASU:{
        Cards.JAN_KASU1,
        Cards.JAN_KASU2,
        Cards.FEB_KASU1,
        Cards.FEB_KASU2,
        Cards.MAR_KASU1,
        Cards.MAR_KASU2,
        Cards.APR_KASU1,
        Cards.APR_KASU2,
        Cards.MAY_KASU1,
        Cards.MAY_KASU2,
        Cards.JUN_KASU1,
        Cards.JUN_KASU2,
        Cards.JUL_KASU1,
        Cards.JUL_KASU2,
        Cards.AUG_KASU1,
        Cards.AUG_KASU2,
        Cards.SEP_KASU1,
        Cards.SEP_KASU2,
        Cards.OCT_KASU1,
        Cards.OCT_KASU2,
        Cards.NOV_KASU1,
        Cards.DEC_KASU1,
        Cards.DEC_KASU2,
        Cards.DEC_KASU3,
        },
    Yaku.TANE:{
        Cards.FEB_TANEN,
        Cards.APR_TANEN,
        Cards.MAY_TANEN,
        Cards.JUN_TANEI,
        Cards.JUL_TANEI,
        Cards.AUG_TANEN,
        Cards.SEP_TANEK,
        Cards.OCT_TANEI,
        Cards.NOV_TANEN,
        },
    
    Yaku.TANN:{
        Cards.JAN_TANNR,
        Cards.FEB_TANNR,
        Cards.MAR_TANNR,
        Cards.APR_TANNN,
        Cards.MAY_TANNN,
        Cards.JUN_TANNB,
        Cards.JUL_TANNN,
        Cards.SEP_TANNB,
        Cards.OCT_TANNB,
        Cards.NOV_TANNN,
        },
    }

YAKU_COUNT_NUM = {
    Yaku.KASU: 10,
    Yaku.TANE: 5,
    Yaku.TANN: 5,
    
    
    }

YAKU = {
     Yaku.GOKO :{
         Cards.JAN_HIKAR,
         Cards.MAR_HIKAH,
         Cards.AUG_HIKAT,
         Cards.NOV_HIKAN,
         Cards.DEC_HIKAR
         },
       
     Yaku.SHIKO:{
         Cards.JAN_HIKAR,
         Cards.MAR_HIKAH,
         Cards.AUG_HIKAT,
         Cards.DEC_HIKAR
         },

     Yaku.SANKO:{
         Cards.JAN_HIKAR,
         Cards.MAR_HIKAH,
         Cards.AUG_HIKAT,
         },     

     Yaku.NOMI:{
         Cards.MAR_HIKAH,
         Cards.AUG_HIKAT,
         Cards.SEP_TANEK
         },         
     Yaku.HANAMI:{
         Cards.MAR_HIKAH,
         Cards.SEP_TANEK
         },
     Yaku.TSUKIMI:{
         Cards.AUG_HIKAT,
         Cards.SEP_TANEK
         },         

    Yaku.BOOK:{
         Cards.JAN_TANNR,
         Cards.FEB_TANNR,
         Cards.MAR_TANNR,
         Cards.JUN_TANNB,
         Cards.SEP_TANNB,
         Cards.OCT_TANNB,         
         },
     Yaku.AKATAN:{
         Cards.JAN_TANNR,
         Cards.FEB_TANNR,
         Cards.MAR_TANNR,
         },
     
     Yaku.AOTAN:{
         Cards.JUN_TANNB,
         Cards.SEP_TANNB,
         Cards.OCT_TANNB,
         },         

     Yaku.INOSHIKA:{
         Cards.JUN_TANEI,
         Cards.JUL_TANEI,
         Cards.OCT_TANEI,
         },
     }

YAKU_AMESHIKO ={
    0 :{
         Cards.JAN_HIKAR,
         Cards.MAR_HIKAH,
         Cards.AUG_HIKAT,
         Cards.NOV_HIKAN,
         },
    1 :{
         Cards.MAR_HIKAH,
         Cards.AUG_HIKAT,
         Cards.NOV_HIKAN,
         Cards.DEC_HIKAR
         },    
    2 :{
         Cards.JAN_HIKAR,
         Cards.AUG_HIKAT,
         Cards.NOV_HIKAN,
         Cards.DEC_HIKAR
         },    
    3 :{
         Cards.JAN_HIKAR,
         Cards.MAR_HIKAH,
         Cards.NOV_HIKAN,
         Cards.DEC_HIKAR
         },       
    }    

POINTS = {
    Yaku.GOKO : 10,
    Yaku.SHIKO : 8,
    Yaku.AMESHIKO : 7,
    Yaku.SANKO : 5,
    Yaku.HANAMI : 5,
    Yaku.TSUKIMI : 5,
    Yaku.NOMI : 10,
    Yaku.INOSHIKA : 6,
    Yaku.AKATAN : 6,
    Yaku.AOTAN : 6,
    Yaku.TANE : 1,
    Yaku.TANN : 1,
    Yaku.KASU : 1,
    Yaku.BOOK :  12, 
    }




    
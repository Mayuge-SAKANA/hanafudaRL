# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:26:36 2024

@author: yo326
"""

import torch
import torch.nn as nn


class Q(nn.Module):
    def __init__(self,in_channel = 48*2, out_channel = 48):
        super(Q, self).__init__()
        chs = [256,512,512,256]
        self.seq = nn.Sequential(
            nn.Linear(in_channel,chs[0]),
            nn.BatchNorm1d(chs[0]),
            nn.ReLU(inplace = True),
            
            nn.Linear(chs[0],chs[1]),
            nn.BatchNorm1d(chs[1]),
            nn.ReLU(inplace = True),

            nn.Linear(chs[1],chs[2]),
            nn.BatchNorm1d(chs[2]),
            nn.ReLU(inplace = True),

            nn.Linear(chs[2],chs[3]),
            nn.BatchNorm1d(chs[3]),
            nn.ReLU(inplace = True),
            
            nn.Linear(chs[3],out_channel),
            nn.Softmax(dim=1),            
            )
    
    def forward(self,x):
        
        return self.seq(x)


if __name__ == '__main__':
    q = Q()
    
    batch = torch.rand(20,48*2)
    
    y=q(batch)
    
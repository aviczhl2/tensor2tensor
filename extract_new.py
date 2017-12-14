import re
import os
import sys
import random
import string
import logging
import argparse
from shutil import copyfile
from datetime import datetime
from collections import Counter
import torch
import msgpack
import pandas as pd



file=open('context.txt','r',encoding='utf8')
w=file.readlines()
ignored=[]
tobe_translated=[]
for j in range(len(w)):
    line=w[j]
    if len(line)>0 and line[0]==' ':
        line=line[1:]
    split=line.split(' ')
    if len(split)>50:
        ignored.append(j)
    else:
        tobe_translated.append(line)

f2=open('translate.txt','w')
for sentence in tobe_translated:
    f2.write(sentence+'\n')
f3=open('ignorelist.txt','w')
for ii in ignored:
    print("%4d "%ii,file=f3)





"""
author: CMWY
date:2021.04.10
"""


import random
def ran(acc,lon):
    a=[]
    for k in range(acc):
        num=[chr(i) for i in range(48,58)]
        char=[chr(i) for i in range(97,123)]
        total=num+char
        a.append("".join(random.sample(total,lon)))
        k += 1
    return a

if __name__ == "__main__":
    s=ran(200,20)
    for b in range(200):
        print(s[b],end='\n')



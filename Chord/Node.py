#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import sys

totalNodes = 64

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash


class myNode:
    def __init__(self, hashT, keyValue, successor, predecessor,fingerTable):
        self.hash_ = hashT
        self.keyvalue_ = keyValue
        self.successor_ = successor
        self.predecessor_ = predecessor
        self.fingertable_ = fingerTable




if __name__ == "__main__":
    
    hash_ = converterSha1(1)
    hashT = {hash_:[43423,343]}
    hashT2 = {'dfdsss':[4342,3433]}
    fingerTable = [{'343443':'2343243'},{'32432':'23432423'}]
    predecessor = "asddfds"
    successor = "dfdsss"
    keyValue = [2,14,67,90]
    

    x = myNode(hashT,keyValue,successor,predecessor,fingerTable)
    print(x.hash_.keys())
    
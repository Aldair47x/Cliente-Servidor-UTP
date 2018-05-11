#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Node
import hashlib
import sys

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash

class chord():
    def __init__(self, nodeStart):
        self.nodes = [nodeStart]

    def fingerTableGenerator():
        pass
    
    def keyValueGenerator(node):
        pass

    def createNode(IdHash, idnumber_):
        hashKey = converterSha1(idnumber_)
        newIdHash = IdHash
        newHashT = {hashKey:[]}
        newNode = myNode(newIdHash,newHashT,)


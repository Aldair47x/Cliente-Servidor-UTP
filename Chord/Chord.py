#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Node
import hashlib
import sys
import random

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash


class chord():
    def __init__(self):
        self.nodes_ = {}

    def fingerTableGenerator(node):
        auxHashT = node.Node.getHashT()
        auxKeyHash = auxHashT.keys()
        pass
    
    def keyValueGenerator(node):
        pass

    def createNode(IdHash, idnumber_):
        hashKey = converterSha1(idnumber_)
        newIdHash = IdHash
        newHashT = {hashKey:[]}
        newNode = myNode(newIdHash,newHashT,)

    def addNode(node):
        auxHashT = node.Node.getHashT()
        auxKeyHash = auxHashT.keys()
        auxFlag = self.nodes.get(auxKeyHash)
        if auxFlag is none:
            nodesKeysList = list(self.nodes_.keys())
            auxNodeNumber = random.choice(nodesKeysList)





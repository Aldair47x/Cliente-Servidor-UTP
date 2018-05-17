#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Node
import hashlib
import sys
import random
import operator

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash


class chord():
    def __init__(self):
        self.nodes_ = {}  #Key IdNumber node, value Node


    def getChordKeys():
        nodesKeysList = list(self.nodes.keys())
        return nodesKeysList    

    def fingerTableGenerator(node):
        auxIdHash = node.getIdHash()
        fingerTable = {}
        nodesKeysList = sort(list(self.nodes_.keys()))
        for i in range (0,6):
            sum = auxIdHash + pow(2,i)
            if(self.nodes_.get(sum) != None):
                fingerTable[sum] = sum
            else:
                for i in nodesKeysList:
                    if i > sum :
                        aux = i
                        break
                fingerTable[sum] = aux
        return fingerTable               


    def getSuccessor(node):
        auxFingerTable = node.getFingerTable()

    def keyValueGenerator(node):
        pass

    def createNode(idnumber_):
        hashKey = converterSha1(idnumber_)
        newIdHash = idnumber_
        newHashT = {hashKey:[]}
        newNode = myNode(newIdHash,newHashT,[],[],{})

    def addNode(node):
        auxHashT = node.Node.getHashT()
        auxKeyHash = auxHashT.keys()
        auxFlag = self.nodes.get(auxKeyHash)
        if auxFlag is none:
            nodesKeysList = list(self.nodes_.keys())
            auxNodeNumber = random.choice(nodesKeysList)

    def startChord():
        t = Node.totalNodes
        firstIdNode = int(random.uniform(0,t))
        secondIdNode = int(random.uniform(0,t))






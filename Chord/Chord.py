#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Node import *
import hashlib
import sys
import random
import operator

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash


class chord(myNode):
    def __init__(self):
        myNode.__init__(self,int, {}, [],[] ,{})
        self.nodes_ = {}  #Key IdNumberNode, value Node
        self.fingerTableGenerator(myNode)
        self.createNode()
        self.getSuccessors()


    def getChordKeys(self):
        nodesKeysList = list(self.nodes.keys())
        return nodesKeysList

    def getNodes(self):
        return self.nodes_        

    def fingerTableGenerator(self,node):
        auxIdHash = node.getIdHash(self)
        print(auxIdHash)
        fingerTable = {} 
        nodesKeysList = list(self.nodes_.keys())
        for i in range (0,15):
            sum = pow(2,i)
            if(self.nodes_.get(sum) != None):
                fingerTable[sum] = sum
            else:
                for i in nodesKeysList:
                    if i > sum :
                        aux = i
                        break
                fingerTable[sum] = aux
        return fingerTable               


    def getSuccessors(node):
        auxFingerTable = node.getFingerTable()
        auxSuccessors = list(set(auxFingerTable.values()))
        return auxSuccessors


    def keyValueGenerator(node):
        pass

    def createNode(idnumber_):
        hashKey = converterSha1(idnumber_)
        newIdHash = idnumber_
        newHashT = {hashKey:[]}
        newNode = Node.myNode(newIdHash,newHashT,[],[],{})
        auxFingerTable = fingerTableGenerator(newNode)
        auxSuccessors = getSuccessors(newNode)
        newNode.setFingerTable(auxFingerTable)
        newNode.setSuccessor(auxSuccessors)
        return newNode

        

    def addNode(node):
        auxHashT = node.Node.getHashT()
        auxKeyHash = auxHashT.keys()
        auxFlag = self.nodes.get(auxKeyHash)
        if auxFlag is none:
            nodesKeysList = list(self.nodes_.keys())
            auxNodeNumber = random.choice(nodesKeysList)

    def startChord(self):
        t = Node.totalNodes
        firstIdNode = int(random.uniform(0,t))
        secondIdNode = int(random.uniform(0,t))
        n1 = createNode(firstIdNode)
        n2 = createNode(secondIdNode)
        self.nodes_[firstIdNode] = n1
        self.nodes_[secondIdNode] = n2



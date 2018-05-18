#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import sys
import random
import operator

totalNodes = 32768
nodes_ = {}

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash

class myNode:
    def __init__(self, IdHash, hashT, successor, predecessor,fingerTable):
        self.idhash_ = IdHash
        self.hash_ = hashT
        self.successor_ = successor
        self.predecessor_ = predecessor
        self.fingertable_ = fingerTable
        self.fingerTableGenerator()
        self.createNode()
        self.getSuccessors()


    def setHashT(self,hashT):
        self.hash_ = hashT

    def getHashT(self):
        return self.hash_

    def setSuccessor(self,successor):
        self.successor_ = successor

    def getSuccessor(self):
        return self.successor_

    def setPredecessor(self,predecessor):
        self.predecessor_ = predecessor

    def getPredecessor(self):
        return self.predecessor_

    def setFingerTable(self,fingerTable):
        self.fingertable_ = fingerTable

    def getFingerTable(self):
        return self.fingertable_

    def setIdHash(self,IdHash):
        self.idhash_ = IdHash

    def getIdHash(self):
        return self.idhash_
    
    def getChordKeys(self):
        nodesKeysList = list(self.nodes.keys())
        return nodesKeysList

    def getNodes(self):
        return self.nodes_        

    def fingerTableGenerator(node):
        auxIdHash = node.getIdHash()
        print (auxIdHash)
        fingerTable = {} 
        nodesKeysList = list(nodes_.keys())
        for i in range (0,15):
            sum =  auxIdHash + pow(2,i)
            if(nodes_.get(sum) != None):
                fingerTable[sum] = sum
            else:
                for i in nodesKeysList:
                    if i > sum :
                        aux = i
                        fingerTable[sum] = aux
                        break            
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
        newNode = myNode(newIdHash,newHashT,[],[],{})
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
        t = totalNodes
        firstIdNode = int(random.uniform(0,t))
        secondIdNode = int(random.uniform(0,t))
        n1 = createNode(firstIdNode)
        n2 = createNode(secondIdNode)
        self.nodes_[firstIdNode] = n1
        self.nodes_[secondIdNode] = n2
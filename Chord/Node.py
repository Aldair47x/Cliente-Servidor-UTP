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
    def __init__(self, IdHash, hashT, successor,fingerTable,keyValues):
        self.idhash_ = IdHash
        self.hash_ = hashT
        self.successor_ = successor
        self.fingertable_ = fingerTable
        self.keyvalues_ = keyValues


    def setHashT(self,hashT):
        self.hash_ = hashT

    def getHashT(self):
        return self.hash_

    def setSuccessor(self,successor):
        self.successor_ = successor

    def getSuccessor(self):
        return self.successor_

    def setFingerTable(self,fingerTable):
        self.fingertable_ = fingerTable

    def getFingerTable(self):
        return self.fingertable_

    def setIdHash(self,IdHash):
        self.idhash_ = IdHash

    def getIdHash(self):
        return self.idhash_

    def setKeyValues(self,keyValues):
        self.keyvalues_ = keyValues

    def getKeyValues(self):
        return self.keyvalues_
    
    def getChordKeys(self):
        nodesKeysList = list(self.nodes.keys())
        return nodesKeysList
    
    def toString(self):
        return print(self.getIdHash()," ",self.getHashT()," ",self.getSuccessor()," ",self.getFingerTable()," ",self.getKeyValues()," ")
        
    def fingerTableGenerator(self):
        auxIdHash = self.getIdHash()
        nodesKeysList = list(nodes_.keys())

        for i in range (0,14):
            sum =  auxIdHash + pow(2,i)

            if(not self.fingertable_):
                self.successor_ = [auxIdHash]

            elif(nodes_.get(sum) != None):
                self.fingertable_[sum] = sum
            
            else:
                for i in nodesKeysList:
                    if i > sum :
                        aux = i
                        self.fingertable_[sum] = aux
                        break                          


    def getSuccessors(self):
        auxFingerTable = self.getFingerTable()
        auxSuccessors = list(set(auxFingerTable.values()))
        self.successor_ = auxSuccessors
        pass


    def keyValueGenerator(self):
        auxIdHash = self.getIdHash()
        nodesKeysList = (list(nodes_.keys())).sort()
        for i in nodesKeysList:
            break


    def addNode(node):
        auxHashT = node.Node.getHashT()
        auxKeyHash = auxHashT.keys()
        auxFlag = self.nodes.get(auxKeyHash)
        if auxFlag is none:
            nodesKeysList = list(self.nodes_.keys())
            auxNodeNumber = random.choice(nodesKeysList)

    def startChord(self):
        firstIdNode = int(random.uniform(0,totalNodes))
        secondIdNode = int(random.uniform(0,totalNodes))
        n1 = createNode(firstIdNode)
        n2 = createNode(secondIdNode)
        for i in range (0,14):
            sum1 =  firstIdNode + pow(2,i)
            sum2 =  secondIdNode + pow(2,i)
            if(sum1>totalNodes):
                sum1 = sum1 % totalNodes
            elif(sum2>totalNodes):
                sum2 = sum2 % totalNodes
            n1.fingertable_[sum1] = secondIdNode
            n2.fingertable_[sum2] = firstIdNode
        n1.getSuccessors()
        n2.getSuccessors()

        n1.keyvalues_.append(secondIdNode+1)
        n1.keyvalues_.append(firstIdNode)
        n2.keyvalues_.append(firstIdNode+1)
        n2.keyvalues_.append(secondIdNode)

            

        nodes_[firstIdNode] = n1
        nodes_[secondIdNode] = n2

        

def createNode(idnumber_):
    hashKey = converterSha1(idnumber_)
    newIdHash = idnumber_
    newHashT = {hashKey:[]}
    newKeyValues = []
    newNode = myNode(newIdHash,newHashT,{},{},[])
    return newNode

def getNodes():
    return nodes_

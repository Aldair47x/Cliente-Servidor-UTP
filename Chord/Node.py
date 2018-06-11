#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import sys
import random
import operator

totalNodes = 32768
nodes_ = {}
firstIdNodeChord = []

def converterSha1(idnumber_):
    stringIdNumber = str(idnumber_)
    newIdHash = hashlib.sha1(stringIdNumber.encode('utf-8')).hexdigest()
    return newIdHash


class myNode:
    def __init__(self, IdHash, hashT, successor,fingerTable,keyValues):
        self.idhash_ = IdHash  # Diccionario donde la llave es el id_number del nodo y el valor el socket
        self.hash_ = hashT # Diccionario donde la llave es el hash del id_number y el valor una lista de {}
        self.successor_ = successor # Una lista de cada sucesor del nodo
        self.fingertable_ = fingerTable #Un diccionario con llave 2^i-1 + id_number y con valor el nodo asociado
        self.keyvalues_ = keyValues # Una lista con el intervalo de llaves


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
        
                    
    def addNode(self,idnumber_):
        auxNode = nodes_.get(firstIdNodeChord[0])
        auxIdHash = auxNode.getIdHash()
        if(idnumber_ > ):
            for i in auxNode.getSuccessor():
                           
        else:
            #self.addNode(auxNode.getSuccessor()[-1])
            pass
                




    def keyValueGenerator(self):
        auxIdHash = self.getIdHash()
        nodesKeysList = (list(nodes_.keys()))
        auxNode = nodes_.get()
        for x in auxNode.getSuccessors():
            auxKeyValues = x.getKeyValues()
            if((auxIdHash < auxKeyValues[0])&(auxIdHash >= auxKeyValues[1])):
                self.keyvalues_.append()


    def startChord(self):
        firstIdNode = int(random.uniform(0,totalNodes))
        secondIdNode = int(random.uniform(0,totalNodes))
        firstIdNodeChord.append(firstIdNode)
        n1 = createNode(firstIdNode)
        n2 = createNode(secondIdNode)
        for i in range (0,14):
            sum1 =  firstIdNode + pow(2,i)
            sum2 =  secondIdNode + pow(2,i)
            n1.fingertable_[sum1 % totalNodes] = secondIdNode
            n2.fingertable_[sum2 % totalNodes] = firstIdNode
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
    newNode = myNode(newIdHash,newHashT,[],{},[])
    return newNode

def getNodes():
    return nodes_


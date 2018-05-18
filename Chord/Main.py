from Chord import *
from Node import *
import random
import operator


def initValues(idnumber_):
    keyValue = {}
    for i in range(Node.totalNodes):
        if(i==idnumber_):
            pass
        else:
            auxHashKey = Chord.converterSha1(i)
            keyValue[i] = auxHashKey
            #auxKeyValue = {i:auxHashKey}
            #keyValue.append(auxKeyValue)
    return keyValue  

def fingerTableGenerator(node):
        auxIdHash = node.getIdHash()
        fingerTable = {}
        nodesKeysList = [1,3,5,9,12,20,25,30,40,45,50]
        for i in range (0,6):
            sum = auxIdHash + pow(2,i)
            k = True
            for i in nodesKeysList:
                if i == sum:
                    k = False

            if(k == False):
                fingerTable[sum] = sum
            else:
                for i in nodesKeysList:
                    if i > sum :
                        aux = i
                        break
                fingerTable[sum] = aux
        return fingerTable       

if __name__ == "__main__":
    
    """hash_ = Chord.converterSha1(1)
    hashT = {hash_:[43423,343]}
    hashT2 = {'dfdsss':[4342,3433],'343443':'2343243','32432':'23432423'}
    fingerTable = [{'343443':'2343243'},{'32432':'23432423'}]
    predecessor = "asddfds"
    successor = "dfdsss"
    keyValue = initValues(10)"""

    

    x = myNode(4,{"sddsdf33e3es":[]},[],[],{})
    z = fingerTableGenerator(x)
    #print(z)
    #nodesKeysList = list(x.keyvalue_.keys())
    m = [2,3,3,3,6,1,5,6]
    auxSuccessors = list(set(m))
    c = chord()
    c.startChord()
    print(c.getNodes())
    #print(auxSuccessors)
    #print(4 in m)
    #print(int(random.uniform(1,64)))
    #print(nodesKeysList)
    #print(m[2])
    #print (random.choice(m))
    
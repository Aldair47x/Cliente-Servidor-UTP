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
 

if __name__ == "__main__":
    
    """hash_ = Chord.converterSha1(1)
    hashT = {hash_:[43423,343]}
    hashT2 = {'dfdsss':[4342,3433],'343443':'2343243','32432':'23432423'}
    fingerTable = [{'343443':'2343243'},{'32432':'23432423'}]
    predecessor = "asddfds"
    successor = "dfdsss"
    keyValue = initValues(10)"""

    x = myNode(10,{"sddsdf33e3es":[]},[],{},[])
    #z = fingerTableGenerator(x)
    #print(z)
    #nodesKeysList = list(x.keyvalue_.keys())
    #m = [2,3,3,3,6,1,5,6,4,9,10,8]
    #auxSuccessors = list(set(m))
    x.startChord()
    p = list(getNodes().values())
    print(p[0].toString())
    print(p[1].toString())

    #print(x.lookup(1500))
    
    #print(auxSuccessors)
    #print(4 in m)
    #print(int(random.uniform(1,64)))
    #print(nodesKeysList)
    #print(m[2])
    #print (random.choice(m))

    
    
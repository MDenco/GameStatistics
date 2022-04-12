import copy
import random
from GameObjects.MainRAMVars import *
from DB.dbBazar import *

class Funcs(object):
    """description of class"""
    def __init__(self,vars,funcslist,varnumber, value):
        self.PV = copy.deepcopy(vars)
        self.playerFuncs = funcslist
        self.varnumber = varnumber
        self.value = value
        dbb = dbBazar()
        self.funcList = []
        self.funcName = []
        self.funcMainPrice = []
        self.funcSharedPrice = []
        bazarlist = dbb.selectAll()
        
       # for x in range (len(bazarlist)):
       #     print(bazarlist[x])
        self.funcList.append(bazarlist[0])
        self.funcList = self.funcList[0]
        self.funcName.append(bazarlist[1])
        self.funcName = self.funcName[0]
        self.funcMainPrice.append(bazarlist[2])
        self.funcMainPrice = self.funcMainPrice[0]
        self.funcSharedPrice.append(bazarlist[3])
        self.funcSharedPrice = self.funcSharedPrice[0]
        return
    #-------------------
    #player functions
    #1: zero instead of null
    #2: absolute value
    #3: add instead of reduce
    #4: add instead of assign
    #-------------------
    
    def updateRAMwithFunc(self,funcnumber):
        if funcnumber == 0:
            self.PV.Nullindex.clear()
        if funcnumber == 1:
            if(self.PV.varsValue[0]<0):
                self.PV.varsValue[0] = self.PV.varsValue[0] * (-1)
            if(self.PV.varsValue[1]<0):
                self.PV.varsValue[1] = self.PV.varsValue[1] * (-1)
            if(self.PV.varsValue[2]<0):
                self.PV.varsValue[2] = self.PV.varsValue[2] * (-1)
            if(self.PV.varsValue[3]<0):
                self.PV.varsValue[3] = self.PV.varsValue[3] * (-1)
        return

    def buyFunc(self):
        fnumber = -1
        x=4
        tempFuncList = []
        tempFuncMainPrice = []
        tempFuncSharedPrice = []
        # make list of functions which player can buy
        for f in range(len(self.funcList)):
            # f begins from 0 and id from 1
            f=f+1
            #1. player do not have it
            if (f not in self.playerFuncs):
                #player has money to buy
                ind = self.funcList.index(f)
                if self.PV.varsValue[3] >= self.funcMainPrice[ind]:
                    tempFuncMainPrice.append(self.funcMainPrice[ind])
                    tempFuncSharedPrice.append(-1)
                    tempFuncList.append(f)
                elif self.PV.sumvars >= self.funcSharedPrice[ind]:
                    tempFuncMainPrice.append(-1)
                    tempFuncSharedPrice.append(self.funcSharedPrice[ind])
                    tempFuncList.append(f)
        #end of for: list of functions player can buy
        #select to buy        
        if (len(tempFuncList)>0):
            fnumber = random.choice(tempFuncList)
            ind = tempFuncList.index(fnumber)
            tempPrice = tempFuncMainPrice[ind]
            tempSharedPrice = tempFuncSharedPrice[ind]
            
            #pay the price of function from total
            if tempPrice >0:
                self.PV.varsValue[3] = self.PV.varsValue[3]-tempPrice
                self.playerFuncs.append(fnumber)
                self.updateRAMwithFunc(fnumber)
            else:
                #pay from shared values
                if self.PV.varsValue[0]>0 and 0 not in self.PV.Nullindex:
                    tempSharedPrice = self.PV.varsValue[0]-tempSharedPrice
                    if tempSharedPrice == 0:
                        self.PV.varsValue[0]=0
                        self.playerFuncs.append(fnumber)
                        self.updateRAMwithFunc(fnumber)
                        return True
                    elif tempSharedPrice>0:
                        self.playerFuncs.append(fnumber)
                        self.PV.varsValue[0]= tempSharedPrice
                        self.updateRAMwithFunc(fnumber)
                        return True
                    else:
                        self.PV.varsValue[0] = 0
                        tempSharedPrice = (-1 * tempSharedPrice)
                if self.PV.varsValue[1]>0 and (1 not in self.PV.Nullindex):        
                        tempSharedPrice = self.PV.varsValue[1]-tempSharedPrice
                        if tempSharedPrice == 0:
                            self.PV.varsValue[1]=0
                            self.playerFuncs.append(fnumber)
                            self.updateRAMwithFunc(fnumber)
                            return True
                        elif tempSharedPrice>0:
                            self.playerFuncs.append(fnumber)
                            self.PV.varsValue[1]= tempSharedPrice
                            self.updateRAMwithFunc(fnumber)
                            return True
                        else:
                            self.PV.varsValue[1] = 0
                            tempSharedPrice = (-1 * tempSharedPrice)
                if self.PV.varsValue[2]>0 and (2 not in self.PV.Nullindex):        
                        tempSharedPrice = self.PV.varsValue[2]-tempSharedPrice
                        if tempSharedPrice == 0:
                            self.PV.varsValue[2]=0
                            self.playerFuncs.append(fnumber)
                            self.updateRAMwithFunc(fnumber)
                            return True
                        elif tempSharedPrice>0:
                            self.playerFuncs.append(fnumber)
                            self.PV.varsValue[2]= tempSharedPrice
                            self.updateRAMwithFunc(fnumber)
                            return True
        else:
            return False
        return True
    
    def playallFuncs(self):
        pf = self.playallFuncs
        while len(pf)>0:
            FuncName = 'ECFunc' + str(pf.pop())
            getattr(self, FuncName)()
        return self
   
    #zero instead of null
    def func1(self):
        if self.varnumber in self.PV.Nullindex:
            Nullindex.remove(varnumber)
        return 
   
    #Absolut value
    def func2(self):
        if self.value <0:
           self.value = -1 * self.value
        return 

    #Add isntead of asign
    def func3(self):    
        if self.varnumber not in self.PV.nullindex:
            self.PV.varsValue[self.varnumber] = self.PV.varsValue[self.varnumber] + self.value
        return 

    #add instead of reduce
    def func3(self):
        if self.value <0:
           self.value = -1 * self.value
        return 
    
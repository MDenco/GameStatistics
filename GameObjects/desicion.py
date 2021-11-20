from GameObjects.Player import *
from GameObjects.GameSettings import *
from random import randrange
import copy

class desicion(object):
#    gs = GameSettings()

#----------------------------
    """description of class"""
    def _init_(self,ply,GS):
     #deepcopy is extremly slow
     #   self.step = copy.deepcopy(s)
     #    self.player = copy.deepcopy(ply)
     #        self.GS = copy.deepcopy(GS)
        self.restart = GS.restart

        self.tempPCstatus = ply.PCStatus
        self.desicion = ply.mydesicion
        self.tempReservedEc = ply.PlayerReservedEC
        self.nofRoundPausing = ply.nofRoundPausing

        return self
#-------------------------------

    def makeRandomDecision(self):
        a = randrange(1000) % 2
        if a == 0:
           return True
        return False

#    def makeDecision(self):
 #           if self.GS.makeRandomDecision(): 
  #              if (self.GS.ResourceECTypes.Restart in (self.step.PlayerReservedEC)):
   #         
    #              self.step.P.PlayerReservedEC.remove(self.DE.ResourceECTypes.Restart)

    def playerdesicion(self):
        if 'CPU1Captured'  in (self.tempPCstatus):
            FuncName = 'rule1'
            funcresult = getattr(self, FuncName)()
        else:
            self.desicion = True        
        return self
    #rule 1= cpu is captured  
    def rule1(self): 
            if (self.restart in self.tempReservedEc):
                self.tempPCstatus.remove('CPU1Captured')
                self.tempReservedEc.remove(self.restart)
                self.desicion = True
                self.nofRoundPausing = 0
            else: 
                if (self.nofRoundPausing == 0):
                    self.tempPCstatus.remove('CPU1Captured')
                    #self.player.nofRoundPausing = 0
                    self.desicion = True
                else:
                    self.desicion = False      
                    self.nofRoundPausing = self.nofRoundPausing-1
            return self

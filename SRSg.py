# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import visa



class SRS830():
    def init(self,address):
        #print(self)
        #print(address)
        self.address=address
        rm=visa.ResourceManager()
        self.lockin = rm.open_resource("GPIB::{:n}".format(self.address))
        #lockin.write("*CLS?")
        print(self.lockin.query("FREQ?"))

        
        
    def getx(self):
        return (self.lockin.query("OUTP?1"))
        
    def gety(self):
        return (self.lockin.query("OUTP?2")) 
        
    def getf(self):
        return (self.lockin.query("FREQ?"))    
        
    def getvout(self):
        return (self.lockin.query("SLVL?"))         
        
    def getsens(self):
        return (self.lockin.query("SENS?"))
        
    def gettc(self):
        return (self.lockin.query("OFLT?")) 

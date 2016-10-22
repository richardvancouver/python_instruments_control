# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:34:45 2016

@author: Rui
"""

import time
import visa



class K2400():
    def init(self,address):
        #print(self)
        #print(address)
        self.address=address
        rm=visa.ResourceManager()
        self.inst = rm.open_resource("GPIB::{:n}".format(self.address))
        #lockin.write("*CLS?")
        #print(self.lockin.query("FREQ?"))

        
        
    def getx(self):
        self.inst.write(':form:elem volt')
        return float(self.inst.query(':read?'))

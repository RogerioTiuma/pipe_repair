import pandas as pd
import math

class repair_thickness:
    def __init__(self, P, D, E_c, S, t_s, P_live,E_s, epsl_c):
        self.P = P 
        self.D = D
        self.E_c = E_c
        self.S = S
        self.t_s = t_s
        self.P_live = P_live
        self.E_s = E_s
        self.epsl_c = epsl_c
    
    """def epsl_c(self):
        epsl_c = (self.P*self.D)/(2*self.E_c*self.t_min)-self.S*(self.t_s/(self.E_c*self.t_min)) - (self.P_live*self.D)/(2*self.E_c*self.t_min + self.E_s*self.t_s)
        return epsl_c"""
    
    def t_min(self):
        t_min = (1/(self.E_c*self.epsl_c))*(self.P*self.D/2 - self.S*self.t_s)
        return t_min
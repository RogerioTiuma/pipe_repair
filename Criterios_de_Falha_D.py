import math

class CorrodedPipeline:
    def __init__(self, D, t, d, l, w, ry, ru):
        self.D = D
        self.t = t
        self.d = d
        self.l = l
        self.w = w
        self.ry = ry
        self.ru = ru

    def stephens_leis(self):

        M = 1 - math.exp(-0.157 * self.l / math.sqrt(self.D * (self.t - self.d) / 2))
        Pb = (2 * self.t / self.D) * self.ru * (1 - M * (self.d / self.t))
        return Pb

    def choi(self):

        Rt = math.sqrt(self.D / 2 * self.t)
        
        if self.l / Rt < 6:

            C2 = 0.1163 * (self.d / self.t)**2 - 0.1053 * (self.d / self.t) + 0.0292
            C1 = -0.6913 * (self.d / self.t)**2 + 0.4548 * (self.d / self.t) - 0.1447
            C0 = 0.06 * (self.d / self.t)**2 - 0.1035 * (self.d / self.t) + 1.0
            Pb = 0.9 * (2 * self.t / self.D) * self.ru * (C2 * (self.l / Rt)**2 + C1 * (self.l / Rt) + C0)

        else:

            C1 = 0.0071 * (self.d / self.t) - 0.0126
            C0 = -0.9847 * (self.d / self.t) + 1.1101
            Pb = (2 * self.t / self.D) * self.ru * (C1 * (self.l / Rt) + C0)

        return Pb

    def netto(self):

        Pb = (2 * self.t / self.D) * self.ru * (1 - 0.9435 * (self.d / self.t)**1.6 * (self.l / self.D)**0.4)

        return Pb

    def ma(self):

        n = 1 / (0.3 * (1 - (self.ry / self.ru)))

        H = 2 / (math.sqrt(3) ** ((n + 1) / n))

        M = 1 - 0.7501 * math.exp(-0.4174 * (self.l / math.sqrt(self.D * self.t))) * (1 - (self.d / self.t))**-0.01151
        Pb = H * (2 * self.t / self.D) * self.ru * (1 - M * (self.d / self.t))

        return Pb

    def wang_zarghamee(self):

        if self.D < 610:
            Pb = (2 * self.t / self.D) * self.ru * (1 - 0.886 * (self.d / self.t)**1.0 * (self.l / self.D)**0.3)
        else:
            Pb = (2 * self.t / self.D) * self.ru * (1 - 1.120 * (self.d / self.t)**1.15 * (self.l / self.D)**0.3)

        return Pb

    def chen(self):

        ratio_w_D = self.w / (math.pi * self.D)
        ratio_l_Dt = self.l / math.sqrt(self.D * self.t)

        if ratio_w_D <= 0.3:
            
            if ratio_l_Dt <= 5:
                
                C0 = 0.000194 + 0.0135 * (self.d / self.t) + 0.0221 * (self.d / self.t)**2
                C1 = 0.00482 - 0.202 * (self.d / self.t) - 0.169 * (self.d / self.t)**2
                C2 = 1.0604 - 0.253 * (self.d / self.t) + 0.194 * (self.d / self.t)**2
                C3 = -4.016 + 13.195 * (self.d / self.t)
                C4 = 1.583 - 5.337 * (self.d / self.t)
                C5 = 0.975 + 0.00873 * (self.d / self.t)

                Pb = (2 * self.t / (self.D - self.t)) * self.ru * (C0 * ratio_l_Dt**2 + C1 * ratio_l_Dt + C2) * (C3 * ratio_w_D**2 + C4 * ratio_w_D + C5)
            
            else:
                
                C1 = 0.000238 - 0.0105 * (self.d / self.t)
                C2 = 1.108 - 0.974 * (self.d / self.t)
                C3 = -4.016 + 13.195 * (self.d / self.t)
                C4 = 1.583 - 5.337 * (self.d / self.t)
                C5 = 0.975 + 0.00873 * (self.d / self.t)
                
                Pb = (2 * self.t / (self.D - self.t)) * self.ru * (C1 * ratio_l_Dt + C2) * (C3 * ratio_w_D**2 + C4 * ratio_w_D + C5)  
        
        else:

            if ratio_l_Dt <= 5:
                C0 = -0.00239 + 0.0308 * (self.d / self.t) - 0.00382 * (self.d / self.t)**2
                C1 = 0.0314 - 0.381 * (self.d / self.t) + 0.101 * (self.d / self.t)**2
                C2 = 0.993 + 0.185 * (self.d / self.t) - 0.579 * (self.d / self.t)**2
                Pb = (2 * self.t / (self.D - self.t)) * self.ru * (C0 * ratio_l_Dt**2 + C1 * ratio_l_Dt + C2)
            else:
                C1 = -0.000586 - 0.00771 * (self.d / self.t)
                C2 = 1.129 - 1.0808 * (self.d / self.t)
                Pb = (2 * self.t / (self.D - self.t)) * self.ru * (C1 * ratio_l_Dt + C2)
        return Pb

    def zhu(self):

        n = 0.0763108

        H = ((2 + math.sqrt(3)) / (4 * math.sqrt(3))) * (n + 1) 

        ratio_l_Dt = self.l / math.sqrt(self.D * self.t)

        M = 1 - (1 / (1 + 0.1385 * ratio_l_Dt + 0.1357 * ratio_l_Dt**2))

        Pb = H * (4 * self.t / self.D) * self.ru * (1 - M * (self.d / self.t))

        return Pb

    def su(self):
        ratio_l_Dt = self.l / math.sqrt(self.D * self.t)
        ratio_b_p = self.w / math.pi  # b é representado como w aqui

        C0 = 0.8816 + 0.7942 * (self.d / self.t) - 0.05329 * (self.d / self.t)**2
        C1 = 0.03982 - 0.3946 * (self.d / self.t) - 0.1901 * (self.d / self.t)**2
        C2 = -0.004248 + 0.02983 * (self.d / self.t) + 0.03091 * (self.d / self.t)**2

        G0 = 1.065 - 0.2992 * (self.d / self.t) - 0.248 * (self.d / self.t)**2
        G1 = 0.06604 + 0.7039 * (self.d / self.t) - 2.027 * (self.d / self.t)**2
        G2 = -0.000185 - 1.211 * (self.d / self.t) + 2.356 * (self.d  / self.t)**2

        if self.l < math.sqrt(20*self.D*self.t):

            Pb = (2 * self.t / (self.D - self.t)) * self.ru * (C2 * ratio_l_Dt**2 + C1 * ratio_l_Dt + C0) *(G2 * ratio_b_p**2 + G1 * ratio_b_p + G0)
        else:

            Pb = (2 * self.t / (self.D - self.t)) * self.ru * (C2 * ratio_l_Dt**2 + C1 * ratio_l_Dt + C0)

        return Pb

    def belachew(self):

        l_D = self.l / self.D
        if l_D <= 1:
            Pb = (2 * self.t / (self.D - self.t)) * self.ru * (1 - 0.8 * (self.d / self.t) * (l_D)**0.4)
        elif 1 < l_D < 2:
            Pb = (2 * self.t / (self.D - self.t)) * self.ru * (1 - 0.8 * (self.d / self.t) * (l_D)**0.1)
        else:
            Pb = (2 * self.t / (self.D - self.t)) * self.ru * (1 - 0.85 * (self.d / self.t))

        return Pb

    def ghani(self):

        n = 0.239 * ( 1 + self.ry / self.ru)**0.596
        H = 2 * ((1/2)**(n + 1))
        M = 1 - 1 / (1 + (self.d / self.t) * (self.l / (math.sqrt(self.D * self.t))**2))

        Pb = H * (2 * self.t / (self.D - 2 * self.t)) * self.ru * (1 - M * (self.d / self.t))

        return Pb

    def phan(self):

        P0 = (2 * self.t * self.ru) / (self.D - self.t)

        Pb = P0 * (1 - 0.88555 * (self.d / self.t)**0.98077 * (self.l / self.D)**0.31053)
        
        return Pb

    def shuai(self):
        ratio_w_D = self.w / (math.pi * self.D)
        ratio_l_Dt = self.l / math.sqrt(self.D * self.t)
        M = (1 - 0.1075 * (1 - ratio_w_D**2)**6 + 0.8925 * math.exp(-0.4103 * ratio_l_Dt**2)) * (1 - self.d / self.t)**0.2504
        Pb = (2 * self.t / self.D) * self.ru * (1 - M * (self.d / self.t))
        return Pb
    
    def asme_b31g(self):
        """ASME B31G (original)"""
        R = 1 - self.d / self.t
        L_sqrt = math.sqrt(1 + 0.8 * self.l**2 / (self.D * self.t))
        F = R / L_sqrt
        Pb = 2 * self.t * self.ry * F / self.D
        return Pb

    def asme_b31g_mod(self):
        """ASME B31G* (modificado)"""
        R = 1 - self.d / self.t
        L_sqrt = math.sqrt(1 + 0.6275 * self.l**2 / (self.D * self.t))
        F = R / L_sqrt
        Pb = 2 * self.t * self.ry * F / self.D
        return Pb

    def rstreng(self):
        """RSTRENG (original)"""
        Lc = math.sqrt(self.D * self.t)
        if self.l < Lc:
            M = 1.001 - 0.31 * (self.l / Lc)
        else:
            M = 0.85 + 0.31 * (Lc / self.l)
        R = 1 - self.d / self.t
        Pb = 2 * self.t * self.ry * R * M / self.D
        return Pb

    def rstreng_mod(self):
        """RSTRENG* (modificado)"""
        Lc = math.sqrt(self.D * self.t)
        if self.l < Lc:
            M = max(1.001 - 0.31 * (self.l / Lc), 0.9)
        else:
            M = max(0.85 + 0.31 * (Lc / self.l), 0.9)
        R = 1 - self.d / self.t
        Pb = 2 * self.t * self.ry * R * M / self.D
        return Pb

    def dnv_rp_f101(self):
        """DNV RP-F101, Parte B"""
        a = self.d / self.t
        alpha = self.l / math.sqrt(self.D * self.t)
        beta = (1 - a)**2 / (1 + 0.8 * alpha)
        Pb = 2 * self.t * self.ry * beta / self.D
        return Pb

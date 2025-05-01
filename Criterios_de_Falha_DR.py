import math

class fail:
    def __init__(self,D,L,t,P_i,d,stress_y, stress_u):
        self.D = D # Diâmetro externo do duto
        self.L = L # Comprimento do duto
        self.t = t # Espessura do duto
        self.d = d # Espessura do defeito
        self.P_i = P_i # Pressão interna no duto
        self.stress_y = stress_y # Tensão de escoamento do material
        self.stress_u = stress_u # Tensão última do material
        self.stress_teta = P_i*D/(2*t) # Tensão circunferencial duto íntegro
        self.stress_a = P_i*D/(4*t) # Tensão longitudinal do duto íntegro


    def B31G(self,D,L,t,d, stress_y):

        #Bulging Factor
        A_f = 0.893*(L/(D*t)**(-1/2)) 

        # Damaged Factor/ Remaining Strength
        if A_f <= 4:
            alfa_teta = (1-2/3*(d/(t*(A_f*A_f+1))))/(1-(2/3)*(d/t))
        else:
            alfa_teta = t/(t-d)
        
        #Flow Stress
        stress_flow = 1.1*stress_y

        #Failure Pressure
        
        return alfa_teta, stress_flow
    
    def RSTRENG085(self,D,L,t,d, stress_y):

        #Bulging Factor
        A_f = L**2/D*t

        # Damaged Factor/ Remaining Strength
        if A_f <= 50:
            M_t = (1+0.6275*(L**2/D*t) - 0.00375*(L**2/D*t)**2)**(-1/2)
        else:
            M_t = 3.3+0.032*(L**2/D*t)
        

        alfa_teta = (1-0.85*(d/t)*(1/M_t))/(1-0.85*(d/t))

        #Flow Stress
        stress_flow = stress_y + 69

        #Failure Pressure
        
        return alfa_teta, stress_flow
    
    def DNV(self,D,L,t,d, stress_u):

        #Bulging Factor
        Q = (1+0.31*(L**2/D*t))**(-1/2)

        # Damaged Factor/ Remaining Strength
        alfa_teta = (1-(d/t)*(1/Q))/(1-(d/t))

        #Flow Stress
        stress_flow = stress_u

        #Failure Pressure
        
        return alfa_teta, stress_flow
    
    def RITCHIELAST(self,D,L,t,d, stress_u):

        #Bulging Factor
        M_t = (1.0+0.8*(L^2/D*t))**(-1/2)

        # Damaged Factor/ Remaining Strength
        alfa_teta = (1.0-(d/t)*(1/M_t))  /   (1-(d/t))

        #Flow Stress
        stress_flow = 0.9*stress_u

        #Failure Pressure
        
        return alfa_teta, stress_flow
    
    def CHELL(self,D,L,t,d, stress_u):

        R_d = D/2 - d # Raio médio do Defeito

        #Bulging Factor
        M_t = (1.0 + 1.61*((math.pi()/8)**2)*(L^2/R_d))**(-1/2)

        # Damaged Factor/ Remaining Strength
        alfa_teta = (1-(d/t) + (d/t)*(1/M_t))**(-1)

        #Flow Stress
        stress_flow = 1.16*stress_u

        #Failure Pressure
        
        return alfa_teta, stress_flow
    
    """def SIMS(self,D,L,t,d, stress_u):
        
        R_t = 1 - d/t 

        if 

        #Bulging Factor
        M_t = (1.0 + 1.61*((math.pi()/8)**2)*(L^2/R_d))**(-1/2)

        # Damaged Factor/ Remaining Strength
        alfa_teta = (1-(d/t) + (d/t)*(1/M_t))**(-1)

        #Flow Stress
        stress_flow = 1.16*stress_u

        #Failure Pressure
        
        return alfa_teta, stress_flow"""



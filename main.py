import asmepcc2 as pcc2

import Material

import Criterios_de_Falha_DR as CFDR

from Criterios_de_Falha_D import CorrodedPipeline

################ Duto #############

D = 458.8        # Diâmetro Externo
t = 41.9         # Espessura do Defeito
L = 900.0        # Comprimento do Duto

################ Material do Duto ##############

E_s = 1.         # Módulo de Elásticidade do Aço
ry = 464.6       # Tensão de Escoamento
ru = 599.3       # Tensão de Última de Escoamento

########## Defeito #########

d = 4.9          # Profundidade do Defeito
w = 132.0        # Largura do Defeito
l = 771.6        # Comprimento do Defeito
t_s = t-d        # t-d

########## Geometria do Reparo ##########

########## Material do Reparo ###########

E_c = 1          # Módulo de Elásticidade do Compósito
epsilon_c = 1.   # 


########## Condições de Contorno #######

P_i = 100
P_live = 0. # Pressão de operação do duto no momento do reparo
P = 100.


epsl_c = 1.

t_min = pcc2.repair_thickness(P, D, E_c, ry, t_s, P_live,E_s,epsl_c).t_min()

print(t_min)
#print(E_s)

aco_1020 = Material.taterial(nome="Aço 1020",
    elasticidade=2.1e11,
    poisson=0.29,
    densidade=7870,
    escoamento=3.5e8,
    ruptura=4.2e8
)

# print(aco_1020.to_dict())
print(aco_1020)
print(aco_1020.elasticidade)

B31G = CFDR.fail.B31G(D,L,t,d,aco_1020.escoamento, aco_1020.elasticidade)
print(B31G)

RSTRENG085 = CFDR.fail.RSTRENG085(D,L,t,d,aco_1020.escoamento, aco_1020.elasticidade)
print(RSTRENG085[1])

fail = CFDR.fail(D,L,t,P_i,d,aco_1020.escoamento, aco_1020.elasticidade)
print()

pipe = CorrodedPipeline(D, t, d, l, w, ry, ru)

print(f"Pressão de falha (Stephens & Leis): {pipe.stephens_leis():.2f} MPa")
print(f"Pressão de falha (Choi et al.): {pipe.choi():.2f} MPa")
print(f"Pressão de falha (Netto et al.): {pipe.netto():.2f} MPa")
print(f"Pressão de falha (Ma et al.): {pipe.ma():.2f} MPa")
print(f"Pressão de falha (Wang & Zarghamee): {pipe.wang_zarghamee():.2f} MPa")
print(f"Pressão de falha (Chen et al.): {pipe.chen():.2f} MPa")
print(f"Pressão de falha (Zhu): {pipe.zhu():.2f} MPa")
print(f"Pressão de falha (Su et al.): {pipe.su():.2f} MPa")
print(f"Pressão de falha (Belachew et al.): {pipe.belachew():.2f} MPa")
print(f"Pressão de falha (Ghani et al.): {pipe.ghani():.2f} MPa")
print(f"Pressão de falha (Phan et al.): {pipe.phan():.2f} MPa")
print(f"Pressão de falha (Shuai et al.): {pipe.shuai():.2f} MPa")

import asmepcc2 as pcc2

import Material

import Criterios_de_Falha as CF

P = 100.
D = 50.
E_c = 1.
S = 1.
t_s = 1.
P_live = 0. # Pressão de operação do duto no momento do reparo
E_s = 1.
epsl_c = 1.
P_i = 100
L = 10
d = 5


t = pcc2.repair_thickness(P, D, E_c, S, t_s, P_live,E_s,epsl_c).t_min()

#print(t.t_min())
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

B31G = CF.fail.B31G(D,L,t,d,aco_1020.escoamento, aco_1020.elasticidade)
print(B31G)

RSTRENG085 = CF.fail.RSTRENG085(D,L,t,d,aco_1020.escoamento, aco_1020.elasticidade)
print(RSTRENG085[1])
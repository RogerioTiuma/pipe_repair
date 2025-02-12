import determination_thickness as dt

P = 1.
D = 1.
E_c = 1.
t_min = 1.
S = 1.
t_s = 1.
P_live = 1.
E_s = 1.

t = dt.repair_thinckness(P, D, E_c, t_min, S, t_s, P_live,E_s)

print(t.epsl_c())
import numpy as np
import matplotlib.pyplot as plt
from utilities import trvalues, iptrack


# Constants
g = 9.82
N_STEPS = 1000
avg_tid1 = 0.83
avg_tid2 = 1.17
avg_tid3 = 0.72
m = 0.1 		# Vekt på kula: omtrent 100 g?????


p1, t_malt1, x_malt1, y_malt1 = iptrack('fysikk_lab/malinger_txt/bane1/Bane1-2.txt')
p2, t_malt2, x_malt2, y_malt2 = iptrack('fysikk_lab/malinger_txt/bane2/Bane2-7.txt')
p3, t_malt3, x_malt3, y_malt3 = iptrack('fysikk_lab/malinger_txt/bane3/Bane3-4.txt')

# eulersMethod returnerer numerisk beregnede verdier for x, y, v, a og t basert pa polynomet fra iptrack  og den
# malte tiden. n_steps angir noyaktigheten til beregningene.
def eulersMethod(n_steps, p, t_malt, x_malt):

	tn = t_malt[-1]
	t = np.linspace(0, tn, n_steps)
	dt = t[1] - t[0]
	v0 = (x_malt[1] - x_malt[0])/(t_malt[1] - t_malt[0])
	x0 = -0.05

	x = np.zeros(n_steps)
	v = np.zeros(n_steps)
	y = np.zeros(n_steps)
	a = np.zeros(n_steps)
	f = np.zeros(n_steps)
	R = np.zeros(n_steps)
	N = np.zeros(n_steps)

	x[0] = x0
	v[0] = v0

	y[0], dydx, d2ydx2, alpha, R[0] = trvalues(p, x[0])
	a[0] = (g * np.sin(alpha)) / (1 + (2. / 5.))
	f[0] = (2./5.) * a[0]
	N[0] = g * np.cos(alpha) + ((dydx ** 2) / R[0])

	for n in range(0, n_steps - 1):
		y[n + 1], dydx, d2ydx2, alpha, R[n + 1] = trvalues(p, x[n])
		a[n + 1] = (g * np.sin(alpha)) / (1 + (2. / 5.))
		x[n + 1] = x[n] + np.cos(alpha) * v[n] * dt
		v[n + 1] = v[n] + a[n] * dt
		f[n + 1] = (2./5.) * a[n + 1]
		N[n + 1] = g * np.cos(alpha) + ((dydx ** 2) / R[n])

	return x, y, v, a, t, f, R, N


# Henter ut numerisk beregnede verdier for de tre banene
x1, y1, v1, a1, t1, f1, R1 ,N1 = eulersMethod(N_STEPS, p1, t_malt1, x_malt1)
x2, y2, v2, a2, t2, f2, R2, N2 = eulersMethod(N_STEPS, p2, t_malt2, x_malt2)
x3, y3, v3, a3, t3, f3, R3, N3 = eulersMethod(N_STEPS, p3, t_malt3, x_malt3)


R2_avg = np.mean(R2)
R3_avg = np.mean(R3)

print('R2_avg:', R2_avg)
print('R3_avg:', R3_avg)


# Lager en sluttindex, men den blir kun brukt for bane 3 da den ser litt merkelig ut etter t = 0.72
b1_index_slutt = min(min(np.argwhere(t1 > avg_tid1)))
b2_index_slutt = min(min(np.argwhere(t2 > avg_tid2)))
b3_index_slutt = min(min(np.argwhere(t3 > avg_tid3)))

#
# # Plotter fart mot tid
# plt.plot(t1, v1, label='Bane 1', linestyle='-')
# plt.plot(t2, v2, label='Bane 2', linestyle='-')
# plt.plot(t3[0: b3_index_slutt], v3[0: b3_index_slutt], label='Bane 3', linestyle='-') # Slicer listen sa de passer pa grafen
# plt.title("Fart mot tid")
# plt.xlabel("Tid [t]")
# plt.ylabel("Fart [m/s]")
# plt.legend()
# plt.show()
#
# # Plotter akselerasjon mot tid
# plt.plot(t1, a1, label='Bane 1', linestyle='-')
# plt.plot(t2, a2, label='Bane 2', linestyle='-')
# plt.plot(t3[0: b3_index_slutt], a3[0: b3_index_slutt], label='Bane 3', linestyle='-') # Slicer listen sa de passer pa grafen
# plt.title("Akselerasjon mot tid")
# plt.xlabel("Tid [s]")
# plt.ylabel("Akselerasjon [m/$s^2$]")
# plt.legend()
# plt.show()
#
# # Plotter friksjonskraft per kilo mot tid
# plt.plot(t1, f1, label='Bane 1', linestyle='-')
# plt.plot(t2, f2, label='Bane 2', linestyle='-')
# plt.plot(t3[0: b3_index_slutt], f3[0: b3_index_slutt], label='Bane 3', linestyle='-') # Slicer listen sa de passer pa grafen
# plt.title("Friksjonskraft mot tid")
# plt.xlabel("Tid [s]")
# plt.ylabel("Friksjonskraft per kilo [N/kg]")
# plt.legend()
# plt.show()

# Plot av Normalkraft per kilo mot tid
#plt.plot(t1, N1, label='Bane 1', linestyle='-')
#plt.plot(t2, N2, label='Bane 2', linestyle='-')
#plt.plot(t3[0: b3_index_slutt], N3[0: b3_index_slutt], label='Bane 3', linestyle='-') # Slicer listen sa de passer pa grafen
# plt.plot(t3[0: b3_index_slutt], y3[0: b3_index_slutt], label='Bane 3 y-pos', linestyle=':')
# plt.title("Friksjonskraft mot tid")
# plt.xlabel("Tid [s]")
# plt.ylabel("Normalkraft per kilo [N/kg]")
# plt.legend()
# plt.show()

# Plot y-pos mot tid
plt.plot(x1, y1, label='Bane 1', linestyle='-')
plt.plot(x2, y2, label='Bane 2', linestyle='-')
plt.plot(x3[0: b3_index_slutt], y3[0: b3_index_slutt], label='Bane 3 y-pos', linestyle='-')
plt.title("Friksjonskraft mot tid")
plt.xlabel("Tid [s]")
plt.ylabel("Normalkraft per kilo [N/kg]")
plt.legend()
plt.show()
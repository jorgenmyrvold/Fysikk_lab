import numpy as np
import matplotlib.pyplot as plt
from utilities import trvalues, iptrack


# Constants
g = 9.82
N_STEPS = 100
avg_tid1 = 0.83
avg_tid2 = 1.17
avg_tid3 = 0.72


p1, t_malt1, x_malt1, y_malt1 = iptrack('fysikk_lab/malinger_txt/bane1/Bane1-2.txt')
p2, t_malt2, x_malt2, y_malt2 = iptrack('fysikk_lab/malinger_txt/bane2/Bane2-7.txt')
p3, t_malt3, x_malt3, y_malt3 = iptrack('fysikk_lab/malinger_txt/bane3/Bane3-4.txt')


# eulersMethod returnerer numerisk beregnede verdier for x, y, v, a og t basert på polynomet fra iptrack  og den
# målte tiden. n_steps angir nøyaktigheten til beregningene.
def eulersMethod(n_steps, p, t_malt):
    dt = t_malt[1] - t_malt[0]
    v0 = 0
    x0 = -0.03

    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    y = np.zeros(n_steps)
    a = np.zeros(n_steps)
    t = np.linspace(0, t_malt[len(t_malt) - 1], n_steps)

    x[0] = x0
    v[0] = v0

    y[0], dydx, d2ydx2, alpha, R = trvalues(p, x[0])
    a[0] = (g * np.sin(alpha)) / (1 + (2. / 5.))

    for n in range(0, n_steps - 1):
        y[n + 1], dydx, d2ydx2, alpha, R = trvalues(p, x[n])
        a[n + 1] = (g * np.sin(alpha)) / (1 + (2. / 5.))
        x[n + 1] = x[n] + np.cos(alpha) * v[n] * dt
        v[n + 1] = v[n] + a[n] * dt

    return x, y, v, a, t

# Henter ut numerisk beregnede verdier for de tre banene
x1, y1, v1, a1, t1 = eulersMethod(N_STEPS, p1, t_malt1)
x2, y2, v2, a2, t2 = eulersMethod(N_STEPS, p2, t_malt2)
x3, y3, v3, a3, t3 = eulersMethod(N_STEPS, p3, t_malt3)

# Lager en sluttindex, men den blir kun brukt for bane 3 da den ser litt merkelig ut etter t = 0.72
b1_index_slutt = min(min(np.argwhere(t1 > avg_tid1)))
b2_index_slutt = min(min(np.argwhere(t2 > avg_tid2)))
b3_index_slutt = min(min(np.argwhere(t3 > avg_tid3)))


# Plotter x mot y
plt.plot(x1, y1, label='Bane 1', linestyle='-')
plt.plot(x2, y2, label='Bane 2', linestyle='-')
plt.plot(x3[0: b3_index_slutt], y3[0: b3_index_slutt], label='Bane 3', linestyle='-') # Slicer listen så de passer på grafen
plt.plot(x_malt1, y_malt1, label='Bane 1 målt', linestyle=':')
plt.plot(x_malt2, y_malt2, label='Bane 2 målt', linestyle=':')
plt.plot(x_malt3, y_malt3, label='Bane 3 målt', linestyle=':')
plt.title("Posisjon")
plt.xlabel("x posisjon")
plt.ylabel("y posisjon")
plt.legend()
plt.show()

# Plotter tid mot x
plt.plot(t1, x1, label='Bane 1', linestyle='-')
plt.plot(t2, x2, label='Bane 2', linestyle='-')
plt.plot(t3[0: b3_index_slutt], x3[0: b3_index_slutt], label='Bane 3', linestyle='-') # Slicer listen så de passer på grafen
plt.plot(t_malt1, x_malt1, label='Bane 1 målt', linestyle=':')
plt.plot(t_malt2, x_malt2, label='Bane 2 målt', linestyle=':')
plt.plot(t_malt3, x_malt3, label='Bane 3 målt', linestyle=':')
plt.title("Tid mot x-posisjon")
plt.xlabel("Tid [s]")
plt.ylabel("x posisjon")
plt.legend()
plt.show()

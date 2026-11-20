import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from scipy.constants import c

Q = 18600

def dN_dE(E, mv):
    result = np.zeros(len(E))
    mask = E <= Q - mv**2
    result[mask] = E[mask]**0.5 * (Q - E[mask]) * np.maximum(((Q - E[mask])**2 - mv**2), 0)**0.5
    return result

E = np.arange(0, 18600, 0.01)
E_ = np.arange(18599.9, 18600, 0.0001)
mv = [0.01, 0.02, 0.025, 0.03, 0.035, 0.04, 0.05]

fig1, axs = plt.subplots(2, 3, figsize=(11, 6))

for i in range(6):
    N_E = dN_dE(E_, mv[i])
    axs.flat[i].plot(E_, N_E)
    axs.flat[i].xaxis.get_offset_text().set_visible(False)
    axs.flat[i].set_xlabel("E")
    axs.flat[i].set_ylabel("dN/dE")
    axs.flat[i].axvline(x=Q-mv[i], color='orange', linestyle='--')
    axs.flat[i].set_title(f"mv = {mv[i]}эВ", fontsize=13)
    axs.flat[i].grid(True)


fig1.suptitle("β-спектр в окрестности конечной точки при разных mv", fontsize=17)
fig1.tight_layout()
fig1.savefig("betta-spectrum(mv)")

fig2, ax = plt.subplots(figsize=(10, 6))
N_E = dN_dE(E, 0.01)
ax.plot(E, N_E)
ax.set_xlabel("E")
ax.set_ylabel("dN/dE")
ax.axvline(x=Q - mv[0], color='orange', linestyle='--')
ax.set_title("Полный β-спектр", fontsize=13)
ax.grid(True)
fig2.savefig("betta-spectrum_whole")


plt.show()

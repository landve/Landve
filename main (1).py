import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from scipy.interpolate import interp1d

monaco_x = [0, 100, 250, 400, 550, 700, 850, 900, 850, 750, 650, 700, 900, 1150, 1250, 1200, 1050, 850, 600, 300, 100, 0]
monaco_y = [0, 50, 180, 350, 450, 480, 380, 200, 50, -20, 20, 80, 120, 80, -40, -180, -280, -360, -380, -300, -120, 0]

t_old = np.linspace(0, 1, len(monaco_x))
t_new = np.linspace(0, 1, 1000)
x = interp1d(t_old, monaco_x, kind='cubic')(t_new)
y = interp1d(t_old, monaco_y, kind='cubic')(t_new)
speed = np.clip(80 + 180*(0.5+0.5*np.sin(t_new*3+1)), 60, 280)

fig, ax = plt.subplots(figsize=(10,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap='plasma', norm=plt.Normalize(60, 280), linewidth=5)
lc.set_array(speed)
ax.add_collection(lc)
ax.set_xlim(x.min()-100, x.max()+100)
ax.set_ylim(y.min()-100, y.max()+100)
ax.axis('equal')
ax.axis('off')
ax.set_title("VER - Monaco 2023 Q - Velocidad", color='white', fontsize=12, fontweight='bold', loc='left')
plt.colorbar(lc, ax=ax, shrink=0.6).set_label('Velocidad km/h', color='white')
plt.savefig("monaco_2023.png", dpi=300, bbox_inches='tight', facecolor='black')
print("LISTO") 
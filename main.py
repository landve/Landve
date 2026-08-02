import matplotlib.pyplot as plt
x = [0, 150, 300, 450, 550, 650, 700, 750, 700, 600, 500, 350, 300, 350, 500, 800, 1100, 1200, 1100, 900, 600, 300, 100, 0]
y = [0, -50, -100, -80, 0, 150, 300, 500, 650, 700, 680, 600, 450, 300, 200, 100, 150, 0, -150, -300, -350, -300, -150, 0]
plt.figure(figsize=(10,6))
plt.plot(x, y, color='#E10600', linewidth=5)
plt.scatter([0], [0], color='black', s=40)
plt.axis('equal')
plt.axis('off')
plt.title("Circuit de monaco - 2023", fontsize=16, fontweight='bold')
plt.savefig('monaco_2023.png', dpi=300, bbox_inches='tight')
print("LISTO:monaco_2023.png creado")

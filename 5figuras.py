import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(18, 10))

# 1 CUBO
ax1 = fig.add_subplot(2, 3, 1, projection="3d")

r = [-1, 1]
X, Y = np.meshgrid(r, r)
# Dibujar cada una de las 6 caras
ax1.plot_surface(X, Y, np.atleast_2d(1), color="cyan", alpha=0.6)
ax1.plot_surface(X, Y, np.atleast_2d(-1), color="cyan", alpha=0.6)
ax1.plot_surface(X, np.atleast_2d(1), Y, color="cyan", alpha=0.6)
ax1.plot_surface(X, np.atleast_2d(-1), Y, color="cyan", alpha=0.6)
ax1.plot_surface(np.atleast_2d(1), X, Y, color="cyan", alpha=0.6)
ax1.plot_surface(np.atleast_2d(-1), X, Y, color="cyan", alpha=0.6)
ax1.set_title("1. Cubo")

# 2 ESFERA
ax2 = fig.add_subplot(2, 3, 2, projection="3d")
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
ax2.plot_surface(x, y, z, cmap="magma", alpha=0.8)
ax2.set_title("2. Esfera")

# 3 CILINDRO
ax3 = fig.add_subplot(2, 3, 3, projection="3d")
z_cil = np.linspace(-1, 1, 30)
theta = np.linspace(0, 2 * np.pi, 30)
theta_grid, z_grid = np.meshgrid(theta, z_cil)
x_cil = np.cos(theta_grid)
y_cil = np.sin(theta_grid)
ax3.plot_surface(x_cil, y_cil, z_grid, cmap="viridis", alpha=0.8)
ax3.set_title("3. Cilindro")

# 4 CONO
ax4 = fig.add_subplot(2, 3, 4, projection="3d")
z_cono = np.linspace(0, 2, 30)
theta_cono = np.linspace(0, 2 * np.pi, 30)
theta_grid, z_grid = np.meshgrid(theta_cono, z_cono)
r_cono = 2 - z_grid  # El radio disminuye a medida que z aumenta
x_cono = r_cono * np.cos(theta_grid)
y_cono = r_cono * np.sin(theta_grid)
ax4.plot_surface(x_cono, y_cono, z_grid, cmap="plasma", alpha=0.8)
ax4.set_title("4. Cono")
# 5 
ax5 = fig.add_subplot(2, 3, 5, projection="3d")
R = 2  # Radio principal (distancia del centro al centro del tubo)
r_tubo = 0.7  # Radio del tubo
u_tor = np.linspace(0, 2 * np.pi, 30)
v_tor = np.linspace(0, 2 * np.pi, 30)
u_tor, v_tor = np.meshgrid(u_tor, v_tor)
x_tor = (R + r_tubo * np.cos(v_tor)) * np.cos(u_tor)
y_tor = (R + r_tubo * np.cos(v_tor)) * np.sin(u_tor)
z_tor = r_tubo * np.sin(v_tor)
ax5.plot_surface(x_tor, y_tor, z_tor, cmap="coolwarm", alpha=0.8)
ax5.set_title("5. Toroide")

plt.tight_layout()
plt.show()
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from mesh import*


#class Control_field:

#list of control vectors
control = []

print("Reading control file...")


doc = minidom.parse("../../Optim_VSTRAP/data/box_shifting/interpolated_control_field.xml");
field = doc.getElementsByTagName('field')[0]

#value = field.getElementsByTagName('value')[1]
#print(value.getAttribute('node_number'))


for v in field.getElementsByTagName('value'):
	#print(v.firstChild.data)
	u_x,u_y,u_z = v.firstChild.data.split(",")
	control.insert(len(control),[float(u_x),float(u_y),float(u_z)])


print("Generated control without errors.\n")

print("Reading mesh file...")

nodesMesh = []
endPoints = []

mesh = Mesh()
mesh.read_mesh_xml("../../Optim_VSTRAP/data/box_shifting/box_coarse.xml")

for n in mesh.nodes:
	#print(n)
	#print(mesh.nodes[n].x_coord)
	nodesMesh.insert(len(nodesMesh),[float(mesh.nodes[n].x_coord),mesh.nodes[n].y_coord,mesh.nodes[n].z_coord])

control_scaling = 1e-1

for n in mesh.nodes:
	endPoints.insert(len(endPoints),[nodesMesh[n-1][0]+control_scaling*control[n-1][0],nodesMesh[n-1][1]+control_scaling*control[n-1][1],nodesMesh[n-1][2]+control_scaling*control[n-1][2]])


print("Generating nodes and endpoints without errors.\n")

print("Plotting force field...")


from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d



class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


plt.style.use("ggplot")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set(xlim=(-0.5, 0.5), ylim=(0.5, -0.5),zlim=(-0.5,0.5))

for n in mesh.nodes:
	a = Arrow3D([nodesMesh[n-1][0], endPoints[n-1][0]], [nodesMesh[n-1][1], endPoints[n-1][1]], [nodesMesh[n-1][2], endPoints[n-1][2]], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
	ax.add_artist(a)

plt.title('Force field')
plt.grid(False)

t = np.arange(0.0, 2.0, 0.1)
s = np.sin(2 * np.pi * t)
s2 = np.cos(2 * np.pi * t)
plt.plot(t, s, "o-", lw=4.1)

plt.draw()
#plt.show()

print("Generating tikz file...")

import tikzplotlib

tikzplotlib.save("test_control_field.tex")


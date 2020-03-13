import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

from mesh import*

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

nodes = []

mesh = Mesh()
mesh.read_mesh_xml("../../Optim_VSTRAP/data/box_shifting/box_coarse.xml")

for n in mesh.nodes:
	#print(mesh.nodes[n].x_coord)
	nodes.insert(len(nodes),[float(mesh.nodes[n].x_coord),mesh.nodes[n].y_coord,mesh.nodes[n].z_coord])

print("Generating nodes without errors.\n")

print(nodes[0][0]+control[0][0])



from matplotlib import pyplot as plt

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')

plt.title('Force field')

plt.draw()
plt.show()


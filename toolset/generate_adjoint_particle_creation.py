import xml.etree.ElementTree as ET
import csv
import numpy.matlib
import numpy as np
import math

file = open("creation_adjoint_particles.xml", 'w+');

ntimesteps = 30;
mu_x = -0.35; 
mu_y = 0.0;
mu_z = 0.0;
s_x = 0.05;
s_y = 0.25;
s_z = 0.25;

v_x = 0.0;
v_y = 0.0;
v_z = 0.0;

v_s_x = 1e+3;
v_s_y = 1e+3;
v_s_z = 1e+3;


file.write("<parameraters>\n")

for timestep in range(0,ntimesteps-1):
	file.write("\t<set iteration=\"" + str(timestep) + "\">\n")
	file.write("\t\t<particle_values number_density=\"4e+13\" weight=\"1e+10\" charge_number=\"-1\" mass=\"1e-26\" species=\"e-\"/>\n")
	file.write("\t\t<position>\n \t\t\t<mu x_val = \"" + str(mu_x) + "\" y_val = \"" + str(mu_y) + "\" z_val = \"" + str(mu_z) + "\" />\n")
	file.write("\t\t\t<sigma x_val = \"" + str(s_x) +"\" y_val = \"" + str(s_y)+ "\" z_val = \"" + str(s_z) +"\"/> \n \t\t</position>\n")
	file.write("\t\t<velocity> \n \t\t\t<mu x_val = \"" + str(v_x) + " \" y_val = \"" + str(v_y) + "\" z_val = \"" + str(v_z) + "\" />\n")
	file.write("\t\t\t<sigma x_val = \"" + str(v_s_x) +"\" y_val = \"" + str(v_s_y)+ "\" z_val = \"" + str(v_s_z) +"\"/> \n \t\t</velocity>\n")
	file.write("\t</set>\n")
file.write("</parameraters>")
import ansys.fluent.core as pyfluent
import os
import json
from ansys.fluent.visualization import set_config, Graphics
from ansys.fluent.visualization.graphics import graphics_windows_manager
session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
session.file.read_case(
            file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5"
        )
itnum=int(input("Please Tell us how many times do you want to run the program\n"))
lst1=[]
print("list of allowable physics")
print({i:session.setup.models.viscous.model.allowed_values()[i] for i in range(len(session.setup.models.viscous.model.allowed_values()))})

for i in range(itnum):
    lst2=[]
    print(f"Please tell us which physics and rpm you want to use for iteration {i}\n")
    rpm=int(input("RPM:\t"))
    phyics=int(input("The number of the physics:\t"))
    lst2.append(rpm)
    lst2.append(session.setup.models.viscous.model.allowed_values()[phyics])
    lst1.append(lst2)
print("These are the setting You provided: ",lst1)
for i in range(itnum):
    session.setup.models.viscous.model.set_state(lst1[i][1])
    session.settings.setup.cell_zone_conditions.solid['fluid2'].solid_motion.solid_omega.value.set_state(lst1[i][0])
    session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state(lst1[i][0])
    session.solution.run_calculation.iterate(iter_count=1)
    graphics_session1 = Graphics(session)
    contour1 = graphics_session1.Contours["contour-1"]
    contour1.field = "temperature"
    contour1.surfaces = ['interior-rotor']
    graphics_windows_manager.save_graphic(f"minfow-{i+1}", "PDF")

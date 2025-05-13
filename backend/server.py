# from flask import Flask, request, jsonify, send_file
# import ansys.fluent.core as pyfluent
# import os
# import json
# # from ansys.fluent.core import examples
# from ansys.fluent.visualization import Graphics
# from ansys.fluent.visualization.graphics import graphics_windows_manager
# from ansys.fluent.visualization import set_config
# set_config(blocking=True,
# set_view_on_display="isometric")
# from ansys.fluent.visualization.graphics.graphics_objects import Graphics
# import pyautogui
# import pygetwindow as gw
# import time

# # from ansys.fluent.visualization.matplotlib import Plots
# # import pyvista
# # print(pyvista.__version__)
# # from ansys.fluent.core import PyFluentDeprecationWarning
# # import ansys.fluent.core
# # import ansys.fluent.core.pyfluent_warnings

# # print(ansys.fluent.core.__file__)  # This prints the installation path

# # import ansys.fluent.visualization.pyvista as pv
# # from ansys.fluent.visualization.pyvista import Graphics
# # from ansys.fluent.core.file_session import FileSession
# # fileSession=FileSession()
# # fileSession.read_case("ElectricMotorSteadyStationary.cas.h5")
# # from ansys.fluent.core.pyfluent_warnings import PyFluentDeprecationWarning
# # from ansys.fluent.core.file_session import FileSession
# # fileSession=FileSession()
# # fileSession.read_case("elbow1.cas.h5")
# # graphics = pv(session=fileSession)

# # import_filename = examples.download_file(
# #     "ElectricMotorSteadyStationary.cas.h5",
# #     "pyfluent/examples/Brake-Thermal-PyVista-Matplotlib",
# # )


# app = Flask(__name__)

# # Create results folder if not exists
# os.makedirs("results", exist_ok=True)

# @app.route('/run_simulation', methods=['POST'])
# def run_simulation():
#     try:
#         # Get JSON data from frontend
#         data = request.json
#         rpm = data.get("rpm")
#         # velocity_x = data.get("velocity_x")
#         # velocity_y = data.get("velocity_y")
#         # velocity_z = data.get("velocity_z")
# # , Velocity=({velocity_x}, {velocity_y}, {velocity_z})
#         print(dir(Graphics))
#         print(f"Received: RPM={rpm}")

#         # Start Fluent session
#         fluent_session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
        
#         # Load base case
#         # base_case_file = r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5"
#         fluent_session.file.read_case(file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5")

#         # Update RPM
#         # fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_omega.set_state(rpm)
#         print("DEBUG: Checking solid_omega.set_state function signature")
#         print(dir(fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_omega))
#         print("DEBUG: RPM Value =", rpm)
#         fluent_session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state(rpm)

        
        

#         # fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_omega.set_state(value=rpm)


#         # Update Translational Velocity
#         # fluent_session.setup.boundary_conditions.velocity["moving_part"].components = {
#         #     "x": velocity_x,
#         #     "y": velocity_y,
#         #     "z": velocity_z
#         # }

#         print(f"Set RPM: {rpm}")
#         # print(f"Set Translational Velocity: {velocity_x}, {velocity_y}, {velocity_z}")

#         # Run Simulation (200 iterations)
#         fluent_session.solution.run_calculation.iterate(iter_count=1)

#         # Extract Results
#         # temperature_result = fluent_session.results.get_state("temperature")
#         print("DEBUG: Checking results.get_state function signature")
#         print(dir(fluent_session.fields.solution_variable_data))

#         # temperature_result = fluent_session.results.get_state({"variable":"temperature"})
#         solution_variable_data = fluent_session.fields.solution_variable_data

#         temperature_result = solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["fluid1"])
#         fluid_temp = temperature_result['fluid1']
#         avg_fluid_temp=sum(fluid_temp)/len(fluid_temp)

#         # Save Contour Image
#         contour_filename = f"results/simulation_contour.png"
#         # fluent_session.results.graphics.contour("temperature").save_as(contour_filename)
#         # print("DEBUG: Checking contour function signature")
#         # print(dir(fluent_session.results.graphics))

#         # graphics_session1 = pv.Graphics(fluent_session)

#         # contour = fluent_session.results.graphics.contour()
#         # print("DEBUG: Contour object type:", type(contour))
#         # print("DEBUG: Contour object content:", contour)

#         # contour = fluent_session.results.graphics.contour()
#         # contour.field.set_state("SV_T")
#         # contour.save_as(contour_filename)
#         # contour1 = graphics.Contours["fluid-fluid-src"]
#         # contour1.node_values = False
#         # contour1.field = "SV_T"
#         # contour1.surfaces_list = ['fluid1']
#         # contour1.save_as(contour_filename)
#         # contour1.display('w2')
#         # graphics_session1 = pv.Graphics(fluent_session)
#         # graphics = pv(session=fluent_session)
#         # graphics = Graphics(session=fluent_session)
#         graphics = Graphics(session=fluent_session)
#         contour1 = graphics.Contours['periodic-phasec',
#                     'periodic-phaseb',
#                     'periodic-phasea',
#                     'fluid-fluid',
#                     'mag-rotor',
#                     'mag2-rotor',
#                     'fluid-stator',
#                     'statot-insulate1',
#                     'stator-insulate6',
#                     'stator-insulate5',
#                     'stator-insulate4',
#                     'stator-insulate3',
#                     'stator-insulate2',
#                     'rotor-fluid',
#                     'phasec-insulate1',
#                     'phaseb-insulate2',
#                     'phaseb-insulate1',
#                     'phasea-insulate1',
#                     'frame-stator',
#                     'frame-shaft-rotor-shaft',
#                     'phasea-insulate2',
#                     'phasec-insulate2']
#         # contour1 = graphics.Contours["mesh-1"]
#         # contour1.node_values = False
#         contour1.field = "temperature"
#         # contour1.surfaces_list = ['symmetry']
#         # contour1()
#         # contour1.field = "SV_T"
#         print("hello")
#         # print(dir(contour1))
#         # print(contour1.surfaces_list.allowed_values)
#         print(contour1.surfaces)
#         contour1.surfaces = [
#             "interior-rotor",
#         ]
#         # contour1.range.option = "auto-range-off"
#         # contour1()
#         # contour1.range.auto_range_off.minimum = 300
#         # contour1.range.auto_range_off.maximum = 400
#         contour1.display()
#         # contour1.save_as(contour_filename)
#         # graphics.fluent_session.graphics.save_picture(file_name=contour_filename, format="png")
#         # contour1.savefig(contour_filename)
        
#         # time.sleep(3)  # Adjust if needed

# # Step 4: Force Fluent window to fullscreen
#         # fluent_window = None
#         # for window in gw.getWindowsWithTitle("ANSYS Fluent"):  # Adjust if window title is different
#         #     fluent_window = window
#         #     window.maximize()
#         #     break

#         # time.sleep(2)
#         # screenshot = pyautogui.screenshot()
#         # screenshot.save(contour_filename)

#         # Save Results to JSON
#         result_data = {
#             "rpm": rpm,
#             # "velocity_x": velocity_x,
#             # "velocity_y": velocity_y,
#             # "velocity_z": velocity_z,
#             "temperature_result": avg_fluid_temp,
#             # "contour": contour_filename
#         }

#         # get the graphics objects for the session

#         graphics_session1 = Graphics(fluent_session)
#         contour1 = graphics_session1.Contours["contour-1"]

#         contour1.field = "temperature"
#         contour1.surfaces =['interior-magnet']
#         contour1.display("window-1")
#         graphics_windows_manager.save_graphic("window-1","PDF")
        
#         json_filename = f"results/simulation_results.json"
#         with open(json_filename, "w") as json_file:
#             json.dump(result_data, json_file)

#         print("Simulation Completed. Results saved.")

#         # Close Fluent session
#         fluent_session.exit()

#         return jsonify({"message": "Simulation completed", "results": result_data})

#     except Exception as e:
#         return jsonify({"error": str(e)})

# @app.route('/get_contour', methods=['GET'])
# def get_contour():
#     return send_file("results/simulation_contour.png", mimetype='image/png')

# if __name__ == '__main__':
#     app.run(debug=True)










# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS  # Import CORS
# import ansys.fluent.core as pyfluent
# import os
# import json
# from ansys.fluent.visualization import Graphics
# from ansys.fluent.visualization.graphics import graphics_windows_manager
# from ansys.fluent.visualization import set_config

# set_config(blocking=True, set_view_on_display="isometric")

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Create results folder if not exists
# os.makedirs("results", exist_ok=True)

# @app.route('/run_simulation', methods=['POST'])
# def run_simulation():
#     try:
#         data = request.json
#         # rpm=3000
#         rpm = data.get("rpm")
#         velocity_x = data.get("velocityX")
#         velocity_y = data.get("velocityY")
#         velocity_z = data.get("velocityZ")
# # , Velocity=({velocity_x}, {velocity_y}, {velocity_z})
#         print(dir(Graphics))
#         print(f"Received: RPM={rpm}")

#         # Start Fluent session
#         fluent_session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
        
#         # Load base case
#         # base_case_file = r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5"
#         fluent_session.file.read_case(file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5")

#         # Update RPM
#         # fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_omega.set_state(rpm)
#         print("DEBUG: Checking solid_omega.set_state function signature")
#         print(dir(fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion))
#         print("DEBUG: RPM Value =", rpm)
#         fluent_session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state(rpm)
#         fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_motion_velocity.set_state(
#             [velocity_x, velocity_y, velocity_z]
#         )


        
        

#         # fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_omega.set_state(value=rpm)


#         # Update Translational Velocity
#         # fluent_session.setup.cell_zone_conditions.solid['fluid1'].solid_motion = {
#         #     "x": velocity_x,
#         #     "y": velocity_y,
#         #     "z": velocity_z
#         # }

#         print(f"Set RPM: {rpm}")
#         # print(f"Set Translational Velocity: {velocity_x}, {velocity_y}, {velocity_z}")

#         # Run Simulation (200 iterations)
#         fluent_session.solution.run_calculation.iterate(iter_count=1)

#         # Extract Results
#         # temperature_result = fluent_session.results.get_state("temperature")
#         print("DEBUG: Checking results.get_state function signature")
#         print(dir(fluent_session.fields.solution_variable_data))

#         # temperature_result = fluent_session.results.get_state({"variable":"temperature"})
#         solution_variable_data = fluent_session.fields.solution_variable_data

#         temperature_result = solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["fluid1"])
#         fluid_temp = temperature_result['fluid1']
#         avg_fluid_temp=sum(fluid_temp)/len(fluid_temp)

#         # Save Contour Image
#         contour_filename = f"results/simulation_contour.png"
#         # fluent_session.results.graphics.contour("temperature").save_as(contour_filename)
#         # print("DEBUG: Checking contour function signature")
#         # print(dir(fluent_session.results.graphics))

#         # graphics_session1 = pv.Graphics(fluent_session)

#         # contour = fluent_session.results.graphics.contour()
#         # print("DEBUG: Contour object type:", type(contour))
#         # print("DEBUG: Contour object content:", contour)

#         # contour = fluent_session.results.graphics.contour()
#         # contour.field.set_state("SV_T")
#         # contour.save_as(contour_filename)
#         # contour1 = graphics.Contours["fluid-fluid-src"]
#         # contour1.node_values = False
#         # contour1.field = "SV_T"
#         # contour1.surfaces_list = ['fluid1']
#         # contour1.save_as(contour_filename)
#         # contour1.display('w2')
#         # graphics_session1 = pv.Graphics(fluent_session)
#         # graphics = pv(session=fluent_session)
#         # graphics = Graphics(session=fluent_session)
#         graphics = Graphics(session=fluent_session)
#         contour1 = graphics.Contours['periodic-phasec',
#                     'periodic-phaseb',
#                     'periodic-phasea',
#                     'fluid-fluid',
#                     'mag-rotor',
#                     'mag2-rotor',
#                     'fluid-stator',
#                     'statot-insulate1',
#                     'stator-insulate6',
#                     'stator-insulate5',
#                     'stator-insulate4',
#                     'stator-insulate3',
#                     'stator-insulate2',
#                     'rotor-fluid',
#                     'phasec-insulate1',
#                     'phaseb-insulate2',
#                     'phaseb-insulate1',
#                     'phasea-insulate1',
#                     'frame-stator',
#                     'frame-shaft-rotor-shaft',
#                     'phasea-insulate2',
#                     'phasec-insulate2']
#         # contour1 = graphics.Contours["mesh-1"]
#         # contour1.node_values = False
#         contour1.field = "temperature"
#         # contour1.surfaces_list = ['symmetry']
#         # contour1()
#         # contour1.field = "SV_T"
#         print("hello")
#         # print(dir(contour1))
#         # print(contour1.surfaces_list.allowed_values)
#         print(contour1.surfaces)
#         contour1.surfaces = [
#             "interior-rotor",
#         ]
#         # contour1.range.option = "auto-range-off"
#         # contour1()
#         # contour1.range.auto_range_off.minimum = 300
#         # contour1.range.auto_range_off.maximum = 400
#         contour1.display()
#         # contour1.save_as(contour_filename)
#         # graphics.fluent_session.graphics.save_picture(file_name=contour_filename, format="png")
#         # contour1.savefig(contour_filename)
        
#         # time.sleep(3)  # Adjust if needed

# # Step 4: Force Fluent window to fullscreen
#         # fluent_window = None
#         # for window in gw.getWindowsWithTitle("ANSYS Fluent"):  # Adjust if window title is different
#         #     fluent_window = window
#         #     window.maximize()
#         #     break

#         # time.sleep(2)
#         # screenshot = pyautogui.screenshot()
#         # screenshot.save(contour_filename)

#         # Save Results to JSON
#         result_data = {
#             "rpm": rpm,
#             # "velocity_x": velocity_x,
#             # "velocity_y": velocity_y,
#             # "velocity_z": velocity_z,
#             "temperature_result": avg_fluid_temp,
#             # "contour": contour_filename
#         }

#         # get the graphics objects for the session

#         graphics_session1 = Graphics(fluent_session)
#         contour1 = graphics_session1.Contours["contour-1"]

#         json_filename = f"results/simulation_results.json"
#         with open(json_filename, "w") as json_file:
#             json.dump(result_data, json_file)

#         contour1.field = "temperature"
#         contour1.surfaces =['interior-magnet']
#         contour1.display("window-1")
#         graphics_windows_manager.save_graphic("window-1","PDF")
        
        

#         print("Simulation Completed. Results saved.")

#         fluent_session.exit()

#         return jsonify({"message": "Simulation completed", "results": result_data})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/get_contour', methods=['GET'])
# def get_contour():
#     contour_path = os.path.join("results", "simulation_contour.png")
#     if os.path.exists(contour_path):
#         return send_file(contour_path, mimetype='image/png')
#     else:
#         return jsonify({"error": "Contour file not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)






# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import ansys.fluent.core as pyfluent
# import os
# import json
# from ansys.fluent.visualization import Graphics
# from ansys.fluent.visualization.graphics import graphics_windows_manager
# from ansys.fluent.visualization import set_config

# set_config(blocking=True, set_view_on_display="isometric")

# app = Flask(__name__)
# CORS(app)

# os.makedirs("results", exist_ok=True)

# @app.route('/run_simulation', methods=['POST'])
# def run_simulation():
#     try:
#         data = request.json
#         rpm = data.get("rpm")
#         # Make sure to match the frontend keys:
#         velocity_x = data.get("velocityX")
#         velocity_y = data.get("velocityY")
#         velocity_z = data.get("velocityZ")
        
#         print(f"Received: RPM={rpm}, Velocity: {velocity_x}, {velocity_y}, {velocity_z}")

#         # Start Fluent session
#         fluent_session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
        
#         fluent_session.file.read_case(file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5")

#         print("DEBUG: Fluent setup in progress...")
#         fluent_session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state(rpm)
#         fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_motion_velocity.set_state(
#             [velocity_x, velocity_y, velocity_z]
#         )
#         print(f"Set RPM: {rpm}")

#         # Run simulation iteration
#         fluent_session.solution.run_calculation.iterate(iter_count=1)

#         # Extract temperature result
#         solution_variable_data = fluent_session.fields.solution_variable_data
#         temperature_result = solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["fluid1"])
#         fluid_temp = temperature_result['fluid1']
#         avg_fluid_temp = sum(fluid_temp) / len(fluid_temp)
#         print(f"Average Fluid Temperature: {avg_fluid_temp}")

#         # Save contour plot only once
#         contour_filename = f"results/simulation_contour.png"
#         graphics = Graphics(session=fluent_session)
#         contour_obj = graphics.Contours['periodic-phasec',
#                     'periodic-phaseb',
#                     'periodic-phasea',
#                     'fluid-fluid',
#                     'mag-rotor',
#                     'mag2-rotor',
#                     'fluid-stator',
#                     'statot-insulate1',
#                     'stator-insulate6',
#                     'stator-insulate5',
#                     'stator-insulate4',
#                     'stator-insulate3',
#                     'stator-insulate2',
#                     'rotor-fluid',
#                     'phasec-insulate1',
#                     'phaseb-insulate2',
#                     'phaseb-insulate1',
#                     'phasea-insulate1',
#                     'frame-stator',
#                     'frame-shaft-rotor-shaft',
#                     'phasea-insulate2',
#                     'phasec-insulate2']
#         contour_obj.field = "temperature"
#         contour_obj.surfaces = ["interior-rotor"]
#         # Use only one display call; for example:
#         contour_obj.display("window-1")
#         try:
#             graphics_windows_manager.save_graphic("window-1", "PDF")
#         except Exception as e:
#             print("Warning: Could not save graphic -", str(e))
        
#         # Optionally, if you save an image file, do it here once:
#         # contour_obj.save_as(contour_filename)

#         result_data = {
#             "rpm": rpm,
#             "temperature_result": avg_fluid_temp,
#             # Optionally include a link to the contour file if you use it:
#             # "contour_file": f"http://localhost:5000/get_contour"
#         }

#         # Optionally, save results to JSON file (if needed)
#         json_filename = f"results/simulation_results.json"
#         with open(json_filename, "w") as json_file:
#             json.dump(result_data, json_file)

#         print("Simulation Completed. Results saved.")
#         fluent_session.exit()
#         return jsonify({"message": "Simulation completed", "results": result_data})
#     except Exception as e:
#         print(f"Error during simulation: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/get_contour', methods=['GET'])
# def get_contour():
#     contour_path = os.path.join("results", "simulation_contour.png")
#     if os.path.exists(contour_path):
#         return send_file(contour_path, mimetype='image/png')
#     else:
#         return jsonify({"error": "Contour file not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import ansys.fluent.core as pyfluent
# import os
# import json
# from ansys.fluent.visualization import Graphics
# from ansys.fluent.visualization.graphics import graphics_windows_manager
# from ansys.fluent.visualization import set_config

# set_config(blocking=True, set_view_on_display="isometric")

# app = Flask(__name__)
# CORS(app)

# os.makedirs("results", exist_ok=True)

# @app.route('/run_simulation', methods=['POST'])
# def run_simulation():
#     try:
#         data = request.json
#         rpm = data.get('rpms', [])
#         # Make sure to match the frontend keys:
#         velocity_x = data.get("velocityX")
#         velocity_y = data.get("velocityY")
#         velocity_z = data.get("velocityZ")
        
#         print(f"Received: RPM={rpm}, Velocity: {velocity_x}, {velocity_y}, {velocity_z}")

#         # Start Fluent session
#         fluent_session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
        
#         fluent_session.file.read_case(file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5")

#         print("DEBUG: Fluent setup in progress...")
#         result_data=[]
#         for i in rpm:
#             fluent_session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state(rpm)
#             fluent_session.setup.cell_zone_conditions.solid["fluid1"].solid_motion.solid_motion_velocity.set_state(
#                 [velocity_x, velocity_y, velocity_z]
#             )
#             print(f"Set RPM: {rpm}")

#             # Run simulation iteration
#             fluent_session.solution.run_calculation.iterate(iter_count=1)

#             # Extract temperature result
#             solution_variable_data = fluent_session.fields.solution_variable_data
#             temperature_result = solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["fluid1"])
#             fluid_temp = temperature_result['fluid1']
#             avg_fluid_temp = sum(fluid_temp) / len(fluid_temp)
#             print(f"Average Fluid Temperature: {avg_fluid_temp}")

#             # Save contour plot only once
#             contour_filename = f"results/simulation_contour.png"
#             graphics = Graphics(session=fluent_session)
#             contour_obj = graphics.Contours['periodic-phasec',
#                         'periodic-phaseb',
#                         'periodic-phasea',
#                         'fluid-fluid',
#                         'mag-rotor',
#                         'mag2-rotor',
#                         'fluid-stator',
#                         'statot-insulate1',
#                         'stator-insulate6',
#                         'stator-insulate5',
#                         'stator-insulate4',
#                         'stator-insulate3',
#                         'stator-insulate2',
#                         'rotor-fluid',
#                         'phasec-insulate1',
#                         'phaseb-insulate2',
#                         'phaseb-insulate1',
#                         'phasea-insulate1',
#                         'frame-stator',
#                         'frame-shaft-rotor-shaft',
#                         'phasea-insulate2',
#                         'phasec-insulate2']
#             contour_obj.field = "temperature"
#             contour_obj.surfaces = ["interior-rotor"]
#             # Use only one display call; for example:
#             contour_obj.display("window-1")
#             try:
#                 graphics_windows_manager.save_graphic("window-1", "PDF")
#             except Exception as e:
#                 print("Warning: Could not save graphic -", str(e))
            
#             # Optionally, if you save an image file, do it here once:
#             # contour_obj.save_as(contour_filename)

#             result_data.append({
#                 "rpm": rpm,
#                 "temperature_result": avg_fluid_temp,
#                 # Optionally include a link to the contour file if you use it:
#                 # "contour_file": f"http://localhost:5000/get_contour"
#             })

#         # Optionally, save results to JSON file (if needed)
#         json_filename = f"results/simulation_results.json"
#         with open(json_filename, "w") as json_file:
#             json.dump(result_data, json_file)

#         print("Simulation Completed. Results saved.")
#         fluent_session.exit()
#         return jsonify({"message": "Simulation completed", "results": result_data})
#     except Exception as e:
#         print(f"Error during simulation: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/get_contour', methods=['GET'])
# def get_contour():
#     contour_path = os.path.join("results", "simulation_contour.png")
#     if os.path.exists(contour_path):
#         return send_file(contour_path, mimetype='image/png')
#     else:
#         return jsonify({"error": "Contour file not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import ansys.fluent.core as pyfluent
# import os
# import json
# from ansys.fluent.visualization import set_config, Graphics
# from ansys.fluent.visualization.graphics import graphics_windows_manager

# # Configure Fluent visualization
# set_config(blocking=True, set_view_on_display="isometric")

# app = Flask(__name__)
# CORS(app)

# # Ensure results folders exist
# os.makedirs("results/contours", exist_ok=True)

# @app.route('/run_simulation', methods=['POST'])
# def run_simulation():
#     try:
#         data = request.get_json(force=True)
#         rpms = data.get('rpms', [])
#         velocity_x = data.get('velocityX', 0.0)
#         velocity_y = data.get('velocityY', 0.0)
#         velocity_z = data.get('velocityZ', 0.0)

#         # Launch Fluent session once
#         session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
#         session.file.read_case(
#             file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5"
#         )

#         results = []
#         for rpm in rpms:
#             # Set RPM and velocity
#             session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state(rpm)
#             session.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_motion_velocity.set_state([velocity_x, velocity_y, velocity_z])

#             # Run one iteration
#             session.solution.run_calculation.iterate(iter_count=1)

#             # Extract temperature data
#             # temp_data = session.fields.solution_variable_data.get_data(
#             #     solution_variable_name="SV_T",
#             #     zone_names=["fluid1"]
#             # )
#             # fluid_vals = temp_data.get('fluid1', [])
#             # avg_temp = sum(fluid_vals) / len(fluid_vals) if fluid_vals else None
#             solution_variable_data = session.fields.solution_variable_data
#             temperature_result = solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["fluid1"])
#             fluid_temp = temperature_result['fluid1']
#             avg_fluid_temp = sum(fluid_temp) / len(fluid_temp)

#             # Save contour image
#             # filename = f"contour_{int(rpm)}.png"
#             # filepath = os.path.join("results/contours", filename)
#             graphics = Graphics(session=session)
#             contour = graphics.Contours['fluid1']
#             contour.field = 'temperature'
#             contour.surfaces = ['interior-rotor']
#             window_name = f"window_{int(rpm)}"
#             contour.display(window_name)
#             try:
#                 graphics_windows_manager.save_graphic(window_name, "SVG")
                
#             except Exception as e:
#                 app.logger.warning(f"Failed saving graphic for RPM {rpm}: {e}")

#             results.append({
#                 'rpm': rpm,
#                 'temperature_result': avg_fluid_temp,
#                 'contour_file': f"http://localhost:5000/contours/{filename}"
#             })
#             filename=f"{window_name}.svg"

#         # Save JSON results
#         with open("results/simulation_results.json", "w") as jf:
#             json.dump(results, jf, indent=2)

#         session.exit()
#         return jsonify(message="Simulation completed", results=results)

#     except Exception as e:
#         app.logger.error(f"Simulation error: {e}")
#         return jsonify(error=str(e)), 500

# @app.route('/contours/<filename>')
# def get_contour(filename):
#     path = os.path.join("results/contours", filename)
#     if os.path.exists(path):
#         return send_file(path, mimetype='image/png')
#     return jsonify(error="File not found"), 404

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import ansys.fluent.core as pyfluent
import os
import json
from ansys.fluent.visualization import set_config, Graphics
from ansys.fluent.visualization.graphics import graphics_windows_manager

# Configure Fluent visualization
set_config(blocking=True, set_view_on_display="isometric")

app = Flask(__name__)
CORS(app)

# Ensure results folders exist
# os.makedirs("results/contours", exist_ok=True)

@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    try:
        data = request.get_json(force=True)
        rpms = data.get('rpms', [])
        pows = data.get('pows',[])
        ipows = data.get('ipows',[])
        # velocity_x = data.get('velocityX', 0.0)
        # velocity_y = data.get('velocityY', 0.0)
        # velocity_z = data.get('velocityZ', 0.0)

        # Launch Fluent session once
        session = pyfluent.launch_fluent(mode="solver", precision="double", dimension=3)
        session.file.read_case(
            file_name=r"C:\Users\Lenovo\Desktop\Fluent Simulation\ElectricMotorSteadyStationary.cas.h5"
        )

        results = []
        for i in range(len(rpms)):
            rpm=rpms[i]
            pow=pows[i]
            ipow=ipows[i]
            # Set RPM and velocity
            session.settings.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_omega.value.set_state((rpm*(2*3.14))/60)
            session.settings.setup.cell_zone_conditions.solid["phasea"].source_terms.source_terms["energy"][0].value.set_state(pow)
            session.settings.setup.cell_zone_conditions.solid["phaseb"].source_terms.source_terms["energy"][0].value.set_state(pow)
            session.settings.setup.cell_zone_conditions.solid["phasec"].source_terms.source_terms["energy"][0].value.set_state(pow)
            session.settings.setup.cell_zone_conditions.solid["rotor"].source_terms.source_terms["energy"][0].value.set_state(ipow)
            session.settings.setup.cell_zone_conditions.solid["stator"].source_terms.source_terms["energy"][0].value.set_state(ipow)
            
            # session.setup.cell_zone_conditions.solid['fluid1'].solid_motion.solid_motion_velocity.set_state([velocity_x, velocity_y, velocity_z])

            # Run one iteration
            session.solution.run_calculation.iterate(iter_count=8)

            # Extract temperature data
            # temp_data = session.fields.solution_variable_data.get_data(
            #     solution_variable_name="SV_T",
            #     zone_names=["fluid1"]
            # )
            # fluid_vals = temp_data.get('fluid1', [])
            # avg_temp = sum(fluid_vals) / len(fluid_vals) if fluid_vals else None
            # Extract temperature data
            # temp_data = session.fields.solution_variable_data.get_data(
            #     solution_variable_name="SV_T",
            #     zone_names=["fluid1"]
            # )
            # fluid_vals = temp_data.get('fluid1', [])
            # avg_temp = sum(fluid_vals) / len(fluid_vals) if fluid_vals else None
            solution_variable_data = session.fields.solution_variable_data
            temperature_result = solution_variable_data.get_data(solution_variable_name="SV_T", zone_names=["fluid1"])
            fluid_temp = temperature_result['fluid1']
            avg_fluid_temp = sum(fluid_temp) / len(fluid_temp)


            # Save contour image
            filename = f"contour_{int(rpm)}.png"
            filepath = os.path.join("results/contours", filename)
            graphics = Graphics(session=session)
            contour = graphics.Contours['fluid1']
            contour.field = 'temperature'
            contour.surfaces = ['interior-rotor','interior-magnet','interior-stator']
            contour.display("window-1")
            # try:
            #     graphics_windows_manager.save_graphic("window-1", "PDF")
            # except Exception as e:
            #     app.logger.warning(f"Failed saving graphic for RPM {rpm}: {e}")

            results.append({
                'rpm': rpm,
                'pow': pow,
                'ipow': ipow,
                'temperature_result': avg_fluid_temp,
                # 'contour_file': f"http://localhost:5000/contours/{filename}"
            })

        # Save JSON results
        with open("results/simulation_results.json", "w") as jf:
            json.dump(results, jf, indent=2)

        session.exit()
        return jsonify(message="Simulation completed", results=results)

    except Exception as e:
        app.logger.error(f"Simulation error: {e}")
        return jsonify(error=str(e)), 500

# @app.route('/contours/<filename>')
# def get_contour(filename):
#     path = os.path.join("results/contours", filename)
#     if os.path.exists(path):
#         return send_file(path, mimetype='image/png')
#     return jsonify(error="File not found"), 404

if __name__ == '__main__':
    app.run(debug=True)

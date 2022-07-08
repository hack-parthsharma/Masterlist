"""
Masterlist

A List Generator-typed Android application designed to be Quality-of-life focused.

GitHub URL: https://github.com/Thanatisia/masterlist-app
"""

# Import Internal Libraries
import os
import sys

# Import External Libraries
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Import self-defined user libraries
import modules.settings as settings
from modules.settings import app, database

class Handle_Widgets:
	"""
	Kivy Helper Library
	"""


class MyLayouts():
	"""
	Hold my design, layouts and elements
	"""
	class Grid():
		"""
		Grid Layout design
		"""
		def __init__(self, **kwargs):
			"""
			**kwargs: Variable Length Keywords Arguments
				Type: Dictionary
			"""
			super(MyLayouts().Grid, self).__init__(**kwargs)

			self.all_values = {
				# k : Widget ID
				# v : Records
				# 	k : ROW_ID
				# 	v : Value
				# Example:
				# {
				#	"[Widget ID]" : {
				#		0 : "Line 1",
				#		1 : "Line 2" ....
				#	}
				# }
			}

			# Add Widgets
			self.widget_design = [
				{
					"Class" : Label,
					"id" : "lb_user_Name",
					"Params" : {
						"text" : "Username: "
					}
				},
				{
					"Class" : TextInput,
					"id" : "tb_user_Name",
					"Params" : {
						"multiline" : False
					}
				},
				{
					"Class" : Label,
					"id" : "lb_Password",
					"Params" : {
						"text" : "Password: "
					}
				},
				{
					"Class" : TextInput,
					"id" : "tb_Password",
					"Params" : {
						"multiline" : False
					}
				},
				{
					"Class" : Label,
					"id" : "lb_first_Name",
					"Params" : {
						"text" : "First Name: "
					}
				},
				{
					"Class" : TextInput,
					"id" : "tb_first_Name",
					"Params" : {
						"multiline" : False
					}
				},
				{
					"Class" : Label,
					"id" : "lb_last_Name",
					"Params" : {
						"text" : "Last Name: "
					}
				},
				{
					"Class" : TextInput,
					"id" : "tb_last_Name",
					"Params" : {
						"multiline" : False
					}
				},
				{
					"Class" : Label,
					"id" : "lb_Email",
					"Params" : {
						"text" : "Email: "
					}
				},
				{
					"Class" : TextInput,
					"id" : "tb_Email",
					"Params" : {
						"multiline" : False
					}
				},
				{
					"Class" : Button,
					"id" : "btn_get_values",
					"action" : {
						"on_press" : self.get_values
					},
					"Params" : {
						"text" : "Get all entered values"
					}
				},
				{
					"Class" : Button,
					"id" : "btn_print_stored_values",
					"action" : {
						"on_press" : self.print_values
					},
					"Params" : {
						"text" : "Print all stored values"
					}
				},
				{
					"Class" : Button,
					"id" : "btn_export_stored_values",
					"action" : {
						"on_press" : self.export_to_file
					},
					"Params" : {
						"text" : "Export stored values to file"
					}
				},
				{
					"Class" : Button,
					"id" : "btn_import_stored_values",
					"action" : {
						"on_press" : self.import_from_file
					},
					"Params" : {
						"text" : "Import stored values from file"
					}
				},
			]

			self.widget_objs = {
				# Widget Objects
				# {
				#	# Like a variable
				#	"Widget ID Name" : {
				#		"Class" : Widget,
				#		"action" : action,
				#		"params" : **params,
				#		"object" : Widget-Object
				# 	}
				# }	
			}

			self.cols = len(self.widget_design)	# Number of columns in the grid
			self.rows = len(self.widget_design)	# Number of rows in the grid

			# for curr_row, widget_defn in self.widget_design.items():
			for i in range(self.cols):
				"""
				k : ROW_ID
				v : Widget Specifications
					k : Keywords
					v : Values
				"""
				curr_row = i
				widget_defn = self.widget_design[i]

				curr_class = widget_defn["Class"]
				curr_id = widget_defn["id"]
				curr_params = widget_defn["Params"]

				curr_widget = curr_class(**curr_params)

				# Check if action is included
				if "action" in widget_defn:
					# Get action
					curr_action = widget_defn["action"]

					# Bind
					curr_widget.bind(**curr_action)

				self.add_widget(curr_widget)

				# Add Widget to Widget Objects container
				self.widget_objs[curr_id] = {
					"Class" : curr_class,
					"object" : curr_widget
				}
				

		def get_values(self, instance):
			"""
			Get variable values
			"""
			# Get all texts from textboxes
			for curr_id, widget_defn in self.widget_objs.items():
				curr_class = widget_defn["Class"]
				curr_obj = widget_defn["object"]

				if(curr_class == TextInput):
					print("{} is TextBox".format(curr_id))
					curr_val = curr_obj.text

					# [Calculate next ROW_ID to populate]
					# Check if ID exists
					if( curr_id in self.all_values.keys() ):
						curr_id_stored_values = self.all_values[curr_id]	# Get all stored values
						curr_id_stored_values_size = len(curr_id_stored_values)
						curr_id_row = curr_id_stored_values_size
		
						# Add new value to new row
						self.all_values[curr_id][curr_id_row] = curr_val
					else:
						# Create Current ID Key in Dictionary
						self.all_values[curr_id] = {}

						# Reset at 0
						self.all_values[curr_id][0] = curr_val

		def print_values(self, instance):
			"""
			Print all stored values
			"""
			if(len(self.all_values.items())):
				for k,v in self.all_values.items():
					print("{} : {}".format(k,v))
			else:
				print("There are no data")

		def export_to_file(self, instance):
			"""
			Write all stored values into file
			"""
			f_name = "resources/data/accounts.txt"

			delimiter="\n"
			header_delimiter = ":"
			subvalue_delimiter = ";"
			with open(f_name, "a") as f_export:
				line = ""
				for curr_id, id_records in self.all_values.items():
					line = curr_id + header_delimiter
					for curr_row, value in id_records.items():
						line += value + subvalue_delimiter

					# Write to file
					f_export.write(line)
					f_export.write("\n")

					print("Finished writing line : {}".format(line))

				# Write newline
				f_export.write("\n")

				# Close file after using
				f_export.close()

		def import_from_file(self, instance):
			"""
			Read from file into 'all_values'
			"""
			f_name = "resources/data/accounts.txt"

			newline = "\n"
			header_delimiter = ":"
			subvalue_delimiter = ";"

			# Create file if doesnt exist
			if( not(os.path.exists(f_name)) ):
				with open(f_name, "a+") as f_create:
					f_create.close()

			with open(f_name, "r") as f_import:
				"""
				Open and read values file and write into all_values
				"""
				curr_line = f_import.readline()

				ROW_ID = 0
				curr_row = 0

				if(curr_line == ""):
					print("File has no data.")
				else:
					while(curr_line):
						# Split Current Line into Header and Values
						line_arr = curr_line.split(header_delimiter)

						if(len(line_arr) == 2): 
							header = line_arr[0]
							values = line_arr[1]

							# Split Values into individual rows in List
							values_arr = values.split(subvalue_delimiter)
	
							# Trim list and remove newline element
							values_arr = values_arr[::-1][1:][::-1]
							number_of_rows = len(values_arr)
						
							# Data Validation : self.all_values is not empty
							if( not(header in self.all_values.keys()) ):
								self.all_values[header] = {}

							# Import into 'self.all_values'
							for i in range(number_of_rows):
								# Get ROW_ID
								ROW_ID = len(self.all_values[header])
		
								# Append data to each row
								# print("{}[{}] : {} : {}".format(header, ROW_ID, i, values_arr[i]))
								self.all_values[header][ROW_ID] = values_arr[i]
	
						curr_line = f_import.readline()
						curr_row += 1

				# Close file after using
				f_import.close()


class GUI(App): # Automatically call constructor 'App'
	"""
	Main Mobile Application
	"""
	def build(self):
		# Return what you want to draw
		grids = MyLayouts().Grid()
		return grids

def init():
	"""
	Class Initialization
	"""
	PROJ_INFO = app.init("Masterlist", "v20220324_1", "https://github.com/Thanatisia/masterlist-app")
	DB_INFO = database.init("MyDB", "1", "root", "")
	
	print(PROJ_INFO)
	print(DB_INFO)
	
def main():
	"""
	Main Program
	"""
	gui = GUI()
	gui.run()	

if __name__ == "__main__":
	init()
	main()
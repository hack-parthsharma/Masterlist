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
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Import self-defined user libraries
import modules.settings as settings
from modules.settings import app, database


class MyLayouts:
	"""
	Hold my design, layouts and elements
	"""
	def __init__(self, *kv_file):
		self.layouts = {}
		self.gen_layouts(*kv_file)

	def gen_layouts(self, instance, *kv_file):
		"""
		Generate Layouts
		
		- Read Kivy File and Build
		
		:: Params
			kv_file
				Name : Kivy Design Files
				Type : Variable Length Arguments => List
				Structure:
					[
						{ "layout_name" : "name", "layout_path" : Layout_Path }
					]	
		"""
		number_of_items = len(kv_file)
		for layout_ID in range(number_of_items):
			layout_file = kv_file[layout_ID]

			layout_name = layout_file["layout_name"]
			layout_path = layout_file["layout_path"]

			root = Builder.load_file(layout_path)

			# Create Default Value for Keyword if doesnt exist
			if not (layout_name in self.layouts.values()):
				self.layouts[layout_name] = None	

			# Populate Key with Value
			self.layouts[layout_name] = root

	def build_root(self, instance, kv_file):
		root = Builder.load_file(kv_file)
		return self.root


class GUI(App): # Automatically call constructor 'App'
	"""
	Main Mobile Application
	"""
	def build(self):
		"""
		Return what you want to draw
		
		:: Params
			layouts
				Name : Layouts
				Type : Keyword Variable Length Argument (kwargs) - Dictionary
				Desc : Pass all layouts you want to generate
					- Keyword : Name of Layout
					- Value : Layout Object
		"""
		self.root = MyLayouts(
			{
				"layout_name" : "main",
				"layout_path" : "resources/layouts/main.kv"
			}
		)
		return self.root

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
"""
Project Settings
"""
import os
import sys

class app:
	"""
	Application settings here
	"""
	class init:
		"""
		Settings Initialization here
		"""
		def __init__(self, proj_name="TestProj", proj_vers="0.1", proj_url=""):
			"""
			Initialize Database info on class creation

			:: Parameters
				proj_name
					Name : Project Name
					Type : String	
					Desc : Name of your project

				proj_vers
					Name : Project Version
					Type : String
					Desc : Project version as of update

				proj_url
					Name : Project URL/Link
					Type : String
					Desc : The url/link of your project's website, github and/or showcase
			"""
			global PROJ_NAME, PROJ_VERS, PROJ_URL

			self.PROJ_NAME = proj_name
			self.PROJ_VERS = proj_vers
			self.PROJ_URL = proj_url

			self.APP_OBJ = {
				"NAME" : self.PROJ_NAME,
				"VERS" : self.PROJ_VERS,
				"URL" : self.PROJ_URL
			}

class database:
	"""
	Database settings here
	"""
	class init:
		"""
		Settings Initialization here
		"""
		def __init__(self, DATABASE_NAME, DATABASE_VERS, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_SERVER="localhost", DATABASE_PORT=22):
			"""
			Initialize Database info on class creation

			:: Parameters
				DATABASE_NAME
					Name : Database Name
					Type : String
					Desc : Name of your Database
			
				DATABASE_VERS
					Name : Database Version
					Type : String
					Desc : Version of your database

				DATABASE_USERNAME
					Name : Database Username
					Type : String
					Desc : Database Username

				DATABASE_PASSWORD
					Name : Database Password
					Type : String
					Desc : Database Password
	
				DATABASE_SERVER
					Name : Database Server
					Type : String
					Values : IP Address; Default: localhost
					Desc : The IP Address to connect to your database; Default to set as 'localhost' if no specific IP

				DATABASE_PORT
					Name : Database Port Number
					Type : Integer
					Desc : The port number of your database that you are hosting
			"""

			self.DB_SERVER = DATABASE_SERVER
			self.DB_NAME = DATABASE_NAME
			self.DB_UNAME = DATABASE_USERNAME
			self.DB_PASS = DATABASE_PASSWORD
			self.DB_VERS = DATABASE_VERS
			self.DB_PORT = DATABASE_PORT

			self.DB_SOCKET = (
				# Type : Tuple/List
				# Syntax : ([SERVER_IP, SERVER_PORT])
				# Desc : The socket of your database for socket programming
				self.DB_SERVER,
				self.DB_PORT
			)
	
			self.DB_OBJ = {
				"SERVER_IP" : self.DB_SERVER,
				"SERVER_PORT" : self.DB_PORT,
				"NAME" : self.DB_NAME,
				"USERNAME" : self.DB_UNAME,
				"PASSWORD" : self.DB_PASS,
				"VERSION"  : self.DB_VERS,
				"SOCKET"   : self.DB_SOCKET
			}

def debug():
	print("Debugs here")

if __name__ == "__main__":
	debug()
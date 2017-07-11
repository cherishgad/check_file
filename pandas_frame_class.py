import os.path
import pandas as pd

class pandas_frame:
	def __init__(self, file_path):
		self.file_path = file_path
		self.is_frame = False
		self.is_matrix = False
	
	def set_the_file_path(self, file_path):
		self.file_path = file_path
		self.is_frame = False
		self.is_matrix = False

	def csv_to_frame(self):
		try:#check the file is exist
			data = open(self.file_path)
		except IOError:
			self.is_frame = False
			print "Could not open " + self.file_path
			return self.is_frame
		try:#check the pandas is success
			self.frame = pd.read_csv(data, delim_whitespace=True, header = None)
			self.is_frame = True
		except:
			self.is_frame = False
			print 'Fail to make the csv to pandas_frame'
		data.close()
		return self.is_frame
	
	def print_frame(self):
		if self.is_frame:
			print self.frame
		else:
			print 'pandas frame is not exist'
		return

	def frame_to_matrix(self):
		if self.is_frame:
			try:#check the pandas is success
				self.matrix = self.frame.as_matrix(columns=None)
				self.is_matrix = True
			except:
				self.is_matrix = False
				print 'Fail to make the matrix'	
		else:
			print 'matrix need the pandas frame'
		return self.is_matrix
	
	def print_matrix(self):
		if self.is_matrix:
			print self.matrix
		else:
			print 'matrix is not exist'

	
	def extract_matrix_value(self, row, col):
		if self.is_matrix:
			try:
				temp = self.matrix[row][col]
				return temp
			except:
				print 'row or col number is error'
				return -1
		else:
			print 'matrix is not exist'
			return -1

	def extract_matrix_column(self, col):
		if self.is_matrix:
			try:
				temp = self.matrix[:,col]
				return temp
			except:
				print 'col number is error'
				return [-1]
		else:
			print 'matrix is not exist'
			return [-1]


import os.path
import pandas as pd
import pandas_frame_class
class files_read:
	def __init__(self, csv_path):
		self.csv_path = csv_path
		self.pandas_frame = pandas_frame_class.pandas_frame(self.csv_path)
		self.is_frame = self.pandas_frame.csv_to_frame()
		self.is_matrix = self.pandas_frame.frame_to_matrix()
		self.is_files_array = False	
		
	def set_the_file_path(self, csv_path):
		self.csv_path = csv_path
		self.pandas_frame.set_the_file_path(self.csv_path)
		self.is_frame = self.pandas_frame.csv_to_frame()
		self.is_matrix = self.pandas_frame.frame_to_matrix()

	def print_matrix(self):
		if(self.is_matrix):
			self.pandas_frame.print_matrix()
	
	def print_frame(self):
		if(self.is_frame):
			self.pandas_frame.print_frame()
		
	def check_files(self, files_path, matrix_col_num, files_format):
		if not(self.is_matrix):
			print "Fail to check the files: matrix is not exist"
			return -1
		self.files_array = self.pandas_frame.extract_matrix_column(1)
		if (self.files_array[0] == -1):
		 	print "Fail to check the files: matrix does not suitable"
		self.is_files_array = True #success
		count = 0 # count fail case
		try:
			for file_name in self.files_array:
				if not os.path.exists(files_path + str(file_name) + files_format):
					count+=1
				
		except:
			print "wrong file_array"
			self.is_files_array = False # do not use array
			return -1
	
		return count

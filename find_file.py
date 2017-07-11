import os.path
import pandas as pd
import pandas_frame_class
AVA_path = '/home/cherishgad/ava/AVA.txt'
image_path = '/home/cherishgad/AVA/images/'
Style_path = '/home/cherishgad/ava/style.txt'

def check_files(files_path, files_array, files_format):
	count = 0
	try:
		for file_name in files_array:
			if not os.path.exists(files_path + str(file_name) + files_format):
				count+=1
				
	except:
		print "wrong file_array"
		return -1
	
	return count
if __name__=="__main__":
	AVA_frame = pandas_frame_class.pandas_frame(AVA_path)
	AVA_frame.csv_to_frame()
	AVA_frame.print_frame()
	AVA_frame.frame_to_matrix()
	AVA_frame.print_matrix()
	matrix_data = AVA_frame.extract_matrix_column(1)
	print check_files(image_path, matrix_data, ".jpg")


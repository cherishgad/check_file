import os.path
import pandas as pd
import files_read_class
AVA_path = '/home/cherishgad/ava/AVA.txt'
image_path = '/home/cherishgad/AVA/images/'
Style_path = '/home/cherishgad/ava/style.txt'

if __name__=="__main__":
	AVA_images = files_read_class.files_read(AVA_path)
	AVA_images.print_frame()
	AVA_images.print_matrix()
	print AVA_images.check_files(image_path, 1, ".jpg")

import os.path
import os
import pandas as pd
import files_read_class
style_path = '/home/cherishgad/avaTxt/style_image_lists/'
aesthetic_path = '/home/cherishgad/avaTxt/aesthetics_image_lists/'

AVA_path = '/home/cherishgad/avaTxt/AVA.txt'
image_path = '/home/cherishgad/AVA/images/'

def search(dirname):
	file_name_list = []
	filenames = os.listdir(dirname)
	for filename in filenames:
		full_filename = os.path.join(dirname, filename)
		ext = os.path.splitext(full_filename)[-1]
		if ext == ".jpgl":
			file_name_list.append(full_filename)
	return file_name_list
if __name__=="__main__":
	AVA_images = files_read_class.files_read(AVA_path)
	print AVA_path
	AVA_images.print_matrix()
	print AVA_images.check_files(image_path, 1, ".jpg")
	
	aesthetic_list = search(aesthetic_path)
 
	for aesthetic_path in aesthetic_list:
		aesthetic_images = files_read_class.files_read(aesthetic_path)
		print aesthetic_path
		aesthetic_images.print_matrix()
		print aesthetic_images.check_files(image_path, 0,".jpg")
	
	
	style_list = search(style_path)
	
	for style_path in style_list:
		style_images = files_read_class.files_read(style_path)
		print style_path
		style_images.print_matrix()
		print style_images.check_files(image_path, 0,".jpg")





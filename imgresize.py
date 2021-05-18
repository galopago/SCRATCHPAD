from PIL import Image
import os 

# List all jpg and png files in directory and resizes them
# to 1029x772 and saves with their original name with
# MEDUIM appended. Doesn't resize files if have MEDIUM in their names

resized_img_str="MEDIUM"
MEDIUM_SIZE_X=1029
MEDIUM_SIZE_Y=772
ext_list=['jpg','JPG','png','PNG']

filelist=os.listdir()
for file in filelist:
	splitfile=file.split(".")
	if len(splitfile) > 1 :
		extension = splitfile[-1:][0]
		filename = splitfile[0]
		res=any(ele in extension for ele in ext_list)
		# valid image file and NOT resized yet!
		if res == True and filename.find(resized_img_str) == -1:
			print("valid image file and not resized yet:",filename,extension)
			image = Image.open(filename+'.'+extension)
			image.thumbnail((MEDIUM_SIZE_X,MEDIUM_SIZE_Y))
			image.save(filename+'_'+resized_img_str+'.'+extension)

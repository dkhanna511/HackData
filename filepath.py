import cv2
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys
directory = "/media/dheeraj/9A26F0CB26F0AA01/WORK/CEERI/Real Image Denoising Challenge - Track 1: sRGB_onsite_track2/SIDD_Medium_Srgb/Data"
files = os.listdir(directory)
GT_Save="/media/dheeraj/9A26F0CB26F0AA01/WORK/CEERI/Real Image Denoising Challenge - Track 1: sRGB_onsite_track2/SIDD_Medium_Srgb/Ground_Truth"
Noisy_Save="/media/dheeraj/9A26F0CB26F0AA01/WORK/CEERI/Real Image Denoising Challenge - Track 1: sRGB_onsite_track2/SIDD_Medium_Srgb/Noisy"
'''images=os.path.join(directory,files)
print("\n\n\nimages=\n", images)'''
print( " files = \n\n\n\n\n", files)
print("\n\n\n\n")

images=[]
for file in files:
	path=os.path.join(directory, file)
	for img in os.listdir(path):
		images.append(img)
		print("path= " , "\n\n\n\n", img)
		img_array=cv2.imread(os.path.join(path, img))
		#plt.imshow(img_array)
		#plt.show()

		#print("printing ith image: ", "\n\n")
		#print(i[5])
		if img[5]=='G' and img[6]=='T':
			cv2.imwrite(GT_Save + "/" +str(img) , img_array )
			
		elif img[5]=='N' and img[6]=='O':
			cv2.imwrite(Noisy_Save + "/" +str(img) , img_array)		
	
print(images)

'''
for i in images:
	print("printing ith image: ", "\n\n")
	print(i[5])
	if i[5]=='G' and i[6]=='T':
		cv2.imwrite(GT_Save + "/" +str(i) , )
			
	elif i[5]=='N' and i[6]=='O':
		cv2.imwrite(Noisy_Save + "/" +str(i) , i)		
			
'''
'''
for file in files:
	path=os.path.join(directory, files)
    for img in os.listdir(path):
    	img_array=cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE ) #converting the photo to greyscale
    	plt.imshow(img_array)
    	plt.show()
    	    
''' 
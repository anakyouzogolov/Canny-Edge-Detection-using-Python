import cv2 

image_file = 'cat.jpg'
try: 
	# Read image from your dir 
	img = cv2.imread(image_file) 

	# Canny edge detection
    # Canny(image, threshold1, threshold2)
	edges = cv2.Canny(img, 100, 300)

	# Write image back to disk. 
	cv2.imwrite('sult.jpg', edges) 

    # Input Output Errors
except IOError: 
	print ('Error while reading files !!!') 

import imutils
import cv2
import numpy as np
#Open template and get canny
def seek():
	template = cv2.imread('target/lastPicture.jpg')
	template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	template = cv2.Canny(template, 50, 125)
	(height, width) = template.shape[:2]
	#open the main image and convert it to gray scale image
	main_image = cv2.imread('target/lastPicture.png')
	big_gray_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
	img_h, img_w = big_gray_image.shape
	gray_image = big_gray_image[(img_h-400):img_h-100 , 0:img_w]
	cv2.imshow("", gray_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	temp_found = None
	for scale in np.linspace(0.2, 1.0, 20)[::-1]:
	   #resize the image and store the ratio
	   resized_img = imutils.resize(gray_image, width = int(gray_image.shape[1] * scale))
	   ratio = gray_image.shape[1] / float(resized_img.shape[1])
	   if resized_img.shape[0] < height or resized_img.shape[1] < width:
	      break
	   #Convert to edged image for checking
	   e = cv2.Canny(resized_img, 50, 125)
	   match = cv2.matchTemplate(e, template, cv2.TM_CCOEFF_NORMED)
	   (_, val_max, _, loc_max) = cv2.minMaxLoc(match)
	   if temp_found is None or val_max>temp_found[0]:
	      temp_found = (val_max, loc_max, ratio)
	#Get information from temp_found to compute x,y coordinate
	(_, loc_max, r) = temp_found
	(x_start, y_start) = (int(loc_max[0]), int(loc_max[1]))
	(x_end, y_end) = (int((loc_max[0] + width)), int((loc_max[1] + height)))
	#Draw rectangle around the template
	cv2.rectangle(gray_image, (x_start, y_start), (x_end, y_end), (0, 255, 255), 5)
	cv2.imwrite('TemplateFound.png', gray_image)
	cv2.waitKey(0)

if __name__ == "__main__":
    seek();

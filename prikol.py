import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])


image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)




contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)


idx = 0
for c in contours:
	x,y,w,h = cv2.boundingRect(c)
	if w>50 and h>50:
		idx+=1
		new_img=image[y:y+h,x:x+w]
		cv2.imwrite(str(idx) + '.png', new_img)






cv2.imshow("Image", image)


cv2.waitKey(0)

# lastly we write our image to file in JPG format
# new_image.jpg is just the path to the new file
cv2.imwrite("new_image.jpg", image)

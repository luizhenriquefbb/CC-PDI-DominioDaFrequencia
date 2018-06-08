import cv2

def showImage(image, title="image"):
	print("showing "+ title)
	cv2.imshow(title, image)
	cv2.waitKey(0)

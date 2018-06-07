# python libs
import argparse

# Dependencias
import cv2

# minhas libs
import DCT2D
import util
# .....

def main(image_path):
	# Ler a imagem
	image = cv2.imread(image_path)

	print("showing image")
	cv2.imshow("Original", image)
	cv2.waitKey(0)

	
	# aplicar dominio da frequencia
	# ...
	transformada = DCT2D.dct2d(image)


	# selecionar n pontos mais importantes
	# ...


	print("showing transformed image")
	cv2.imshow("transformed", transformada)
	cv2.waitKey(0)
	
	print("the end")

if __name__ == '__main__':
	# build argument parser
	ap = argparse.ArgumentParser()
	# image
	ap.add_argument("-i", "--image", required=False,
				 help="Path to the image to be scanned")
	# n pontos mais importantes
	ap.add_argument('-n', '--number', required=True,
				 help='Number of points to consider')
	
	args = vars(ap.parse_args())
	
	if args["image"] == None:
		image_path = '../images/Lena-original-gray.png'  # imagem padrao
	else:
		image_path = args["image"]
	

	
	main(image_path)

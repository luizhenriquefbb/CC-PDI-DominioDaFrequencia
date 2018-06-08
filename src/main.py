# python libs
import argparse

# Dependencias
import cv2

# minhas libs
import DCT2D
# .....

def main(image_path):

	# dctOpenCV()
	dctNosso()

	

def dctOpenCV():
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

def dctNosso():
	# Ler a imagem
	image = cv2.imread(image_path)

	print("showing image")
	cv2.imshow("Original", image)
	cv2.waitKey(0)

	coluna=len(image)
	linha=len(image[0])
	
	# aplicar dominio da frequencia
	# ...
	colunaTransformada = []
	linhaTransformada = []
	imagemTransformada = [[]]

	# aplica a dct de 1 dimensao para as colunas da imagem 
	for c in range(coluna):
		colunaTransformada[c] = DCT2D.dct1d(image[c])

	# aplica a dct de 1 dimensao para as linhas da imagem 
	for l in range(linha):
		linhaTransformada[l] = DCT2D.dct1d([i[l] for i in image])

	# Multiplica linhaTransformada por colunaTransformada de cada pixel
	for c in range(coluna):
		for l in range(linha):
			imagemTransformada[c][l] = colunaTransformada[c] * linhaTransformada[l]		



	# selecionar n pontos mais importantes
	# ...


	print("showing transformed image")
	cv2.imshow("transformed", imagemTransformada)
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

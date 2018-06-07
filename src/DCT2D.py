import cv2
import numpy as np
import math

import util


def dct2d(original):
	'''
	Discrete cosine transform

	Parametros:
		original: imagem OpenCV
	'''

	# TODO: Identificar se eh RGB ou monocromatica
	# ...
	# Sucao: Nao fazer distincao. Aplicar DCT pra cada uma das cores. no final dar um merge das DCT's

	# TODO: colocando para cinza apenas para testes
	gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)



	
	# ===============From openCV===========================================================
	
	# Performs a forward or inverse Discrete Cosine transform of a 1D or 2D
	# floating-point array.

	# Parameters:

	# 	original(CvArr) - Source array, real 1D or 2D array
	# 	dst(CvArr) - Destination array of the same size and same type as the source
	# 	flags (int) -
	# 		Transformation flags, a combination of the following values
	# 		CV_DXT_FORWARD do a forward 1D or 2D transform.
	# 		CV_DXT_INVERSE do an inverse 1D or 2D transform.
	# 		CV_DXT_ROWS do a forward or inverse transform of every individual row of 
	# 		the input matrix. This flag allows user to transform multiple vectors simultaneously 
	# 		and can be used to decrease the overhead (which is sometimes several times larger 
	# 		than the processing itself), to do 3D and higher-dimensional transforms and so forth
	

	
	imf = np.float32(gray)/255.0  # float conversion/scale
	dst = cv2.dct(imf)           # the dct
	gray = np.uint8(dst)*255.0    # convert back

	
	# ===========end from openCV================================================================
	
	# TODO: Precisamos fazer o nosso
	# Aplicar a dct1d para as linhas
	# ...


	# Aplicar a dct1d para as colunas da imagem resultante
	# ...


	# TODO
	# return dst
	return gray # nao sei se retorna um ou outro

def dct1d(fileira):
	'''
	Aplica DCT-1d para uma fie=leira de pixels
	
	ver formula em extras/dct_1d.png

	Parametros:
		Fileira - numpy array
	'''

	transformada = fileira # variavel que vai ser retornada (array do mesmo tamanho da entrada)
	
	nGrande = len(fileira)  # largura da imagem
	pi = 3.1416
	nPequeno = None  # indice na familia de cossenos
	


	#k == indice no array para recuperar o pixel????
	for k in range(len(fileira)):
		transformada[k] = math.sqrt(2/nGrande)

		freq = (pi*k)/(nGrande)
		fase = (pi*k)/(2*nGrande)


		# c varia dependendo do k
		c = None
		if k == 0 :
			c = math.sqrt(1/2)
		else:
			c = 1


		# Soma
		soma = 0
		for nPequeno in range(nGrande-1):
			soma += fileira[nPequeno] * math.cos(freq*nPequeno + fase)

		transformada[k]+=soma

	return transformada

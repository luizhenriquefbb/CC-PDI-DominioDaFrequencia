import cv2
import numpy as np


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
	
	
	return dst



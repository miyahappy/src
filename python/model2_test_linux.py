import numpy as np
from matplotlib import pyplot as plt
import cv2,os,keras,shutil
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential,load_model
from keras.optimizers import RMSprop,SGD
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#from PIL import Image
path = "./keras/num_or_chr"
os.chdir(path)
#img = cv2.imread('test.tif')
####resize#####
def resize(input_file,a,b):
	image=cv2.imread(input_file)
	res=cv2.resize(image,(a,b),interpolation=cv2.INTER_CUBIC)
	#cv2.imshow('iker',res)
	#cv2.imshow('image',image)
	#cv2.waitKey(0)

#create a black use numpy,size is:512*512
def blank(a,b):
	img2 = np.zeros((a,b), np.uint8)     
	#fill the image with white  
	img2.fill(255)
	#cv2.imwrite(path+'blank.jpg',img2)

###expand borders,255,255,255=white####
def expand(in_data,a,b,c,d):
	out = cv2.copyMakeBorder(in_data,a,b,c,d,cv2.BORDER_CONSTANT,value=[255,255,255])
	return out
	#cv2.imshow('a',a)
	#cv2.waitKey(0)

#a = os.listdir('./test/test')
#for i in a:
#	img = cv2.imread('./test/test/'+i)
#	sp = img.shape
#	h = sp[0]  # height(rows) of image
#	w = sp[1]  # width(colums) of image
#	if h < 300 and w < 300:
#		a_x = int((300-h)/2)
#		a_y = int((300-w)/2)
#		out = expand(img,a_x,a_x,a_y,a_y)
#		out = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY)
#		res=cv2.resize(out,(300,300),interpolation=cv2.INTER_CUBIC)
#		cv2.imwrite('./test_working/test/'+i,res)
	

	
	
#f = np.load('./mnist/mnist.npz')
#print(f)
#x_train, y_train = f['x_train'], f['y_train']
#x_test, y_test = f['x_test'], f['y_test']
#x_test = np.array(x_test)
#print(x_test.shape)
#images = []
#images =np.empty([912,1232])
#a =os.listdir('./tif')
#print(a)
#for i in a:
	#image = cv2.imread('./tif/'+i)
	#image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	#sp = img.shape
	#height = sp[0]  # height(rows) of image
	#width = sp[1]  # width(colums) of image
	#chanael = sp[2]  # the pixels value is made up of three primary colors
	#print ( 'width: %d \nheight: %d \nnumber: %d' % (width, height, chanael))
	#print(image)
	#image = image.flatten()
	#images.append(image)
	#np.concatenate([images,image])
#images = np.array(images)
#print(images)
#print(images.shape)
#print(images.ndim)
#print(images.size)
batch_size=32



def input_img(imgfile): 
	image = cv2.imread(imgfile,0)
	sp = image.shape
	h = sp[0]  # height(rows) of image
	w = sp[1]  # width(colums) of image
	if h >= w :
		a_x = 0
		a_y = int((h-w)/2)
	elif h < w:
		a_x = int((w-h)/2)
		a_y = 0
	out = expand(image,a_x,a_x,a_y,a_y)
	#out = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY)
	res = cv2.resize(out,(300,300),interpolation=cv2.INTER_CUBIC)
	#print imgfile 
	arr = np.asarray(res,dtype="float32")  
	arr = arr.reshape(1, 300, 300, 1)
	return arr


model = load_model('/home/userroot/keras/model2/model2.h5')

#dir_test = './test/num/'
dir_test = './application/output/'
for i in os.listdir(dir_test):
	arr = input_img(dir_test+i)
	a = model.predict_classes(arr, batch_size=1, verbose=0)
	#a = model.predict(arr, batch_size=1, verbose=0)
	#if a == 1:
	#	num += 1
	#	shutil.copyfile(dir_test+i, './application/num/'+i)
	#else:
	#	chr_ += 1
	#	shutil.copyfile(dir_test+i, './application/chr/'+i)
	print(a)
#print("wrong: "+str(num))
#print("right: "+str(chr_))
#print(chr_/(chr_+num))



#print dir(model.predict_classes)
#score = model.evaluate(test_generator,batch_size=batch_size,verbose=1, sample_weight=None)
#print(score)





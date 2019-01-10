import numpy as np
from matplotlib import pyplot as plt
import cv2,os,tensorflow,keras
from PIL import Image
path = "./keras/"
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
	#cv2.imshow('a',a)
	#cv2.waitKey(0)

#f = np.load('./mnist/mnist.npz')
#print(f)
#x_train, y_train = f['x_train'], f['y_train']
#x_test, y_test = f['x_test'], f['y_test']
#x_test = np.array(x_test)
#print(x_test.shape)
images = []
#images =np.empty([912,1232])
a =os.listdir('./tif')
print(a)
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

train_datagen = keras.preprocessing.image.ImageDataGenerator()
        #rescale=1./255,
        #shear_range=0.2,
        #zoom_range=0.2,
        #horizontal_flip=True)
train = train_datagen.flow_from_directory(
        './tif',
        target_size=(20, 20),
        batch_size=32)
print(dir(train))
print(train.__dict__)
model.fit_generator(train, steps_per_epoch=500, epochs=50)

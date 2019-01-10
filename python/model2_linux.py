import numpy as np
from matplotlib import pyplot as plt
import cv2,os,keras
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential,load_model
from keras.optimizers import RMSprop,SGD
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#from PIL import Image
path = "./keras/model2"
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
	
def resize(input_dir,output_dir):
	a = os.listdir(input_dir)
	for i in a:
		img = cv2.imread(input_dir+i)
		sp = img.shape
		h = sp[0]  # height(rows) of image
		w = sp[1]  # width(colums) of image
		if h >= w:
			a_x = 0
			a_y = int((h-w)/2)
		elif h < w:
			a_x = int((w-h)/2)
			a_y = 0
		out = expand(img,a_x,a_x,a_y,a_y)
		out = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY)
		res=cv2.resize(out,(300,300),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(output_dir+i,res)

#chr_num = list(range(1,25))
#print(chr_num)
#for i in chr_num:
#	print(i)
#	os.mkdir('./working/'+str(i))	
for i in range(1,25):
	input_dir = './origin/'+str(i)+'/'
	output_dir = './working/'+str(i)+'/'
	resize(input_dir,output_dir)
	
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
batch_size=64

sgd = SGD(lr=0.01, clipvalue=0.5)

train_datagen = keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
train_generator = train_datagen.flow_from_directory(
        './working/',color_mode='grayscale',
        target_size=(300, 300),
        batch_size=batch_size,class_mode='binary')
test_datagen = keras.preprocessing.image.ImageDataGenerator()
#test_generator = test_datagen.flow_from_directory(
#        './test_working/',color_mode='grayscale',
#		target_size=(300, 300),
#       batch_size=batch_size,class_mode='binary')
#train_generator= train_generator.reshape(5494, 88804).astype('float32') 
#print(dir(train_generator))
#print(train_generator.__dict__)
model = Sequential()
model.add(Conv2D(64,kernel_size=3,activation='relu',input_shape=(300,300,1)))
model.add(Conv2D(128,kernel_size=3,activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Conv2D(64,kernel_size=3,activation='relu'))
model.add(Conv2D(128,kernel_size=3,activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(24, activation='softmax'))
model.summary()
model.compile(loss='sparse_categorical_crossentropy',
              #optimizer=keras.optimizers.Adadelta(),
              optimizer=sgd,
              metrics=['accuracy']) 
model.fit_generator(train_generator, steps_per_epoch=20, epochs=100,
					verbose=1)#,validation_data=test_generator,
					#validation_steps=20)
model.save('model2.h5')





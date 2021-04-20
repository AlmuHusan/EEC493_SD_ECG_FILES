from skimage import img_as_float
from skimage import io, color, morphology
from skimage.transform import rotate
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random
import decimal

supervised=True
pottasiumList=[0]
randPot = [format(1 + (x * .1),'1.1f') for x in range(0, 81)]
print(randPot)
for i in randPot:
    pottasiumList=[0]
    # Generate random pattasium level from 1.0 to 9.0
    # You can increase the amount of images per level by increasing the range
    for j in range(5):
        if supervised:
            pottasiumList.append(i)
        image = img_as_float(color.rgb2gray(io.imread('images/'+i+".png")))

        image=np.fliplr(image)
        image=rotate(image,180)
        image_binary = image < 0.5
        out_skeletonize = morphology.skeletonize(image_binary)
        out_thin = morphology.thin(image_binary)
        arr=out_thin.astype(np.uint8)
        arr=np.matrix.transpose(arr)
        result = np.where(arr == 1)

        slicedX=result[0][::2]
        slicedY=result[1][::2]
        mu, sigma = 0, 3
        # creating a noise
        noise = np.random.normal(mu, sigma, [1,slicedY.size])
        #Remove graph UI
        plt.xticks([])
        plt.yticks([])
        plt.axis('off')
        plt.title('')
        #plot graph +noise

        plt.plot(slicedX,slicedY+noise[0])
        plt.figure()
    #Go through and save all the images
    if supervised:
        for i in plt.get_fignums():
            fig =plt.figure(i)
            potLevel=pottasiumList[i-1]
            print(potLevel)
            plt.savefig("data/"+'{}'.format(potLevel)+"%d.png" % i)
    else:

        for i in plt.get_fignums():
            fig = plt.figure(i)
            plt.savefig('data/figure%d.png' % i)
    plt.figure().clear()
    plt.close('all')


#How the image is process chart
"""
f, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(10, 3))
ax0.imshow(image, cmap='gray')
ax0.set_title('Input')

ax1.imshow(out_skeletonize, cmap='gray')
ax1.set_title('Skeletonize')

ax2.imshow(out_thin, cmap='gray')
ax2.set_title('Thin')

plt.savefig('char_out.png')
plt.show()
"""
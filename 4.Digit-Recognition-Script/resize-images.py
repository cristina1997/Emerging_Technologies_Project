from PIL import Image

# Resize the image from the non-resized folder to a 28x28 pixel image and save it to a new folder
# Number 2
img2 = Image.open("numbers/non-resized/number2.png")    # open the image
img2 = img2.resize((28, 28), Image.ANTIALIAS)           # resize the image to 28x28 pixels
img2.save("numbers/resized/number2.png")                # save the image to a new folder 

# Number 3
img3 = Image.open("numbers/non-resized/number3.png")    # open the image 
img3 = img3.resize((28, 28), Image.ANTIALIAS)           # resize the image to 28x28 pixels
img3.save("numbers/resized/number3.png")                # save the image to a new folder 

# Number 6
img6 = Image.open("numbers/non-resized/number6.png")    # open the image 
img6 = img6.resize((28, 28), Image.ANTIALIAS)           # resize the image to 28x28 pixels
img6.save("numbers/resized/number6.png")                # save the image to a new folder 
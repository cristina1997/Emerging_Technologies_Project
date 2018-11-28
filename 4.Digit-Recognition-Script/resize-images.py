from PIL import Image

# Resize the image from the non-resized folder to a 28x28 pixel image and save it to a new folder
# Number 1
img1 = Image.open("numbers/non-resized/number1.png") 
img1 = img1.resize((28, 28), Image.ANTIALIAS)
img1.save("numbers/resized/number1.png") 

# Number 2
img2 = Image.open("numbers/non-resized/number2.png") 
img2 = img2.resize((28, 28), Image.ANTIALIAS)
img2.save("numbers/resized/number2.png") 

# Number 3
img3 = Image.open("numbers/non-resized/number3.png") 
img3 = img3.resize((28, 28), Image.ANTIALIAS)
img3.save("numbers/resized/number3.png") 

# Number 6
img6 = Image.open("numbers/non-resized/number6.png") 
img6 = img6.resize((28, 28), Image.ANTIALIAS)
img6.save("numbers/resized/number6.png") 
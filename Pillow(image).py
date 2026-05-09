from PIL import Image 
image=Image.open('/Users/ravendrapatel/Dog image .jpeg')
image.show()
cropped = image.crop((100,100,400,400))
cropped.show()

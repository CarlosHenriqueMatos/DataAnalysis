'''fonts : https://www.youtube.com/watch?v=5QR-dG68eNE&t=258s

Obs: was made some modifications like functions to dont use comments
'''
from PIL import Image, ImageColor

def ImportImage(way, name):
    imported_image = Image.open(way+name)
    return imported_image

def SaveAndPrintImage(image,path,name_image):
    image.show()
    image.save(path+name_image)
    
def CreateNewImage(length, width):
    image_blank = Image.new("RGBA",(length,width))
    return image_blank

def InformationsImage(image):
    image.show()
    print(image.size)
    
def ImageRotate(image):
    image_rotate = image.rotate(-60, expand=True, fillcolor = ImageColor.getcolor('red','RGB'))#fillcolor = (0,0,255))#(red,green,blue))
    print(ImageColor.getcolor('red', 'RGB'))
    image_rotate.show()

def FocousPart(image, left_x, top_y, right_x, bottom_y):
    image_crop = image.crop((left_x,top_y,right_x,bottom_y))
    InformationsImage(image_crop)
    
def FlipHorizontalAndVertical(image):
    InformationsImage(image.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
    InformationsImage(image.transpose(Image.Transpose.FLIP_TOP_BOTTOM))
    
def ResizeImage(image, length, width):
    InformationsImage(image.resize((length, width)))
    
def main():
    path = "/home/carlos/Documents/SwapDS/dataset/"
    name_image = "Rafd090_01_Caucasian_female_angry_left.jpg"
    
    image = ImportImage(path,name_image)
    
    #image_crop = FocousPart(image, 55, 40, 500, 400)
    ResizeImage(image, 10000,10000)
    
    
    
if __name__ == "__main__":
    main()
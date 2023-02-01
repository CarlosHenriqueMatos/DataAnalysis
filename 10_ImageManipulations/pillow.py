'''fonts : https://www.youtube.com/watch?v=5QR-dG68eNE&t=258s

Obs: was made some modifications like functions to dont use comments
'''
from PIL import Image, ImageColor

def ImportImage(way, name):
    imported_image = Image.open(way+name)
    return imported_image

def SaveAndPrintImage(image,path,name_image):
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
    return InformationsImage(image.resize((length, width)))
    
def DoubleResolution(scale_factor, image):
    return image.resize((image.size[0] * scale_factor, image.size[1] * scale_factor))
    
    
def main():
    path = "/home/carlos/Documents/SwapDS/dataset/"
    name_image = "Rafd090_01_Caucasian_female_angry_left.jpg"
    
    image = ImportImage(path,name_image)
    
    InformationsImage(image)
    
    image_double_resolution = DoubleResolution(2, image)
    SaveAndPrintImage(image_double_resolution, path, "fifithresolution.jpg")
    InformationsImage(image_double_resolution)
    
    
    
if __name__ == "__main__":
    main()
'''fonts : https://www.youtube.com/watch?v=5QR-dG68eNE&t=258s

Obs: was made some modifications like functions to dont use comments
'''
from PIL import Image, ImageColor, ImageEnhance, ImageFilter
import cv2
import numpy
from matplotlib import cm

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
    
def EnhanceImage(image, value):
    
    color_enhancer = ImageEnhance.Color(image)
    color_image = color_enhancer.enhance(value)
    
    contrast_enhancer = ImageEnhance.Contrast(image)
    contrast_image = contrast_enhancer.enhance(value)
    
    brightness_enhancer = ImageEnhance.Brightness(image)
    brightness_image = brightness_enhancer.enhance(value)
    
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    sharpness_image = sharpness_enhancer.enhance(value)

    
    #InformationsImage(color_image)
    #InformationsImage(contrast_image)
    #InformationsImage(brightness_image)
    #InformationsImage(sharpness_image)

    
def FImageFilter(image):
    
    image_blur = image.filter(ImageFilter.BLUR)
    image_contour = image.filter(ImageFilter.CONTOUR)
    image_detail = image.filter(ImageFilter.DETAIL)
    image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
    image_edge_more = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image_find_edges = image.filter(ImageFilter.FIND_EDGES)
    image_emboss = image.filter(ImageFilter.EMBOSS)
    image_sharp = image.filter(ImageFilter.SHARPEN)
    image_smooth = image.filter(ImageFilter.SMOOTH())
    image_smooth_more = image.filter(ImageFilter.SMOOTH_MORE)
    
    
    image_contour_edges = image_edge.filter(ImageFilter.CONTOUR)
    image_edges_emboss_countour = image_contour_edges.filter(ImageFilter.FIND_EDGES)
    image_edges_emboss_countourBW = image_edges_emboss_countour.convert('LA')
    #image_edges_emboss_countourBW.show()
    return image_edges_emboss_countourBW
'''    
    image_blur.show()
    image_contour.show()
    image_detail.show()
    image_edge.show()
    image_edge_more.show()
    image_find_edges.show()
    image_emboss.show()
    image_sharp.show()
    image_smooth.show()
    image_smooth_more.show()
'''

def ImageFilter2(image):
    image_filtered_min = image.filter(ImageFilter.MinFilter(size = 5))
    image_filtered_median = image.filter(ImageFilter.MedianFilter(size = 5))
    image_filtered_max = image.filter(ImageFilter.MaxFilter(size = 5))
    image_filtered_min.show()
    image_filtered_median.show()
    image_filtered_max.show()
    
def ImageFilter3(image):
    image_boxblur = image.filter(ImageFilter.BoxBlur())
    
def BlackOrWhite(image):
    print(image.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(2):
                if image[i][j][k] > 170:
                    image[i][j][k] = 255
                else:
                    image[i][j][k] = 0
    return image

def ContourBlackAndWhite(image):
    image_grayscale = FImageFilter(image)
    image_grayscale = numpy.array(image_grayscale)
    image = BlackOrWhite(image_grayscale)
    PIL_image = Image.fromarray(numpy.uint8(image)).convert('L')
    PIL_image = Image.fromarray(image.astype('uint8'))
    
    return PIL_image

def BoxGaussianUsharpFilters(image):
    image_boxblur = image.filter(ImageFilter.BoxBlur(radius = 4))
    image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius = 4))
    image_unsharp = image.filter(ImageFilter.UnsharpMask(radius = 4))
    image_boxblur.show()
    image_gaussblur.show()
    image_unsharp.show()
    
def main():
    
    path = "/home/carlos/Documents/SwapDS/dataset/"
    name_image = "Rafd090_01_Caucasian_female_angry_left.jpg"

    image = ImportImage(path,name_image)
    print(image.mode)
    BoxGaussianUsharpFilters(image)
    
if __name__ == "__main__":
    main()
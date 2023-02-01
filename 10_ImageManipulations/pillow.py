'''fonts : https://www.youtube.com/watch?v=5QR-dG68eNE&t=258s

Obs: was made some modifications like functions to dont use comments
'''
from PIL import Image

def import_image(way, name):
    imported_image = Image.open(way+name)
    return imported_image

def save_and_print_image(image,path,name_image):
    image.show()
    image.save(path+name_image)
    
def create_new_image(length, width):
    image_blank = Image.new("RGBA",(length,width))
    return image_blank

def informations_image(image):
    print(image.size)
    print(image.filename)
    print(image.format)
    print(image.format_description)
    
def main():
    path = "/home/carlos/Documents/SwapDS/dataset/"
    name_image = "Rafd090_01_Caucasian_female_angry_left.jpg"
    
    image = import_image(path,name_image)
        
    image_blank = create_new_image(1000,600)
    
if __name__ == "__main__":
    main()
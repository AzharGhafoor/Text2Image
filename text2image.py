#to install package
# pip install pillow


#function that does the magic
# -----------------------------
#import packages
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

#function body
def image_create(data,name):
    def draw_multiple_line_text(image, text, font, text_color, text_start_height):
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        y_text = text_start_height
        lines = textwrap.wrap(text, width=40)
        for line in lines:
            line_width, line_height = font.getsize(line)
            draw.text(((image_width - line_width) / 2, y_text), 
                      line, font=font, fill=text_color)
            y_text += line_height

    def main():
        #image_width
        image = Image.new('RGB', (800, 600), color = (0, 0, 0))
        fontsize = 40  # starting font size
        font = ImageFont.truetype("arial.ttf", fontsize)
        text1 = data

        text_color = (200, 200, 200)
        text_start_height = 0
        draw_multiple_line_text(image, text1, font, text_color, text_start_height)
        image.save(name+'.png')

    if __name__ == "__main__":
        main()


#python script to read all files from a folder and then extract the content of each file
# and pass it to function to create its image and then store it with its original name
# --------------------------------------------------------------------------------------

type = ['vulnerable','non-vulnerable'] # these are my two folders containing files where data is the main directory
for tpe in type:
    path = "data/"+tpe+"/"
    for (root, dirs, file) in os.walk(path):
        for f in file:
            print(f) # here f is the file name
            file1 = open(path+f,"r+") 
            try:
                x= str(file1.readlines()) # here x contains all content of the file f
                image_create(x,f) # passing values to function
            except:
                pass

"""
File: img_ascii.py
------------------

Converts the image to ASCII characters.
"""
from simpleimage import SimpleImage

FILENAME = 'brahm.jpg'               # Image name which we wanna convert to ASCII
IMG_CHARS = '▓▒░ '                  # ASCII charachters you wanna show the image in
BREAKPOINTS = (30, 100, 200)

# The program takes in an image and converts it into ASCII art. 
# We're going to do this by replacing each pixel in the image with an ASCII character.

def convert2ascii(px):
    avg = (px.red + px.blue + px.green) // 3
    if avg < BREAKPOINTS[0]:
        return IMG_CHARS[0]
    elif avg < BREAKPOINTS[1]:
        return IMG_CHARS[1]
    elif avg < BREAKPOINTS[2]:
        return IMG_CHARS[2]
    else:
        return IMG_CHARS[3]

def convert_img_to_ascii(img_file):
    """
    Converts an image to ASCII characters stored in IMG_CHARS based on the
    brightness breakpoints in BREAKPOINTS and prints out the resulting ascii.
    """
    # First let's import the image file
    img = SimpleImage(img_file)
    # Let's resize the image file so it fits in the terminal window
    resize_img_for_ascii(img)
    # Next we loop over each image to compute the average pixel value
    # and convert it to ASCII string !!!
    for y in range(img.height):
        # We used a temporary variable here which will represent our output for each row
        row=""
        for x in range(img.width):
            # Get the pixel-RGB value of x-row and y-column
            pixel=img.get_pixel(x,y)
            # Now convert this RGB-pixel to a string-value
            row+=convert2ascii(pixel)
        print(row)
        # The string 'row' resets after each column-y

def main():
    convert_img_to_ascii(FILENAME)


def resize_img_for_ascii(img):
    """
    PROVIDED FUNCTION: Resize an image to account for the fact that the ASCII
    characters are taller than they are wide, so that the resulting ASCII looks
    proportionally correct.

    Arguments
    ---------
    img (simpleimage.SimpleImage) -- The image to resize.
    """
    # Stretch the width of the image by a factor of two
    width = img.width * 2.3
    height = img.height

    # Scale so the width is 150px
    scale_factor = 70 / width
    width = round(scale_factor * width)
    height = round(scale_factor * height)

    # Resize the underlying PIL image.
    img.pil_image = img.pil_image.resize((width, height))
    img.px = img.pil_image.load()
    size = img.pil_image.size
    img._width = size[0]
    img._height = size[1]


if __name__ == '__main__':
    main()
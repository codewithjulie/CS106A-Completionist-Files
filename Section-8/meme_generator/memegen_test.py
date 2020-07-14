# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator
from simpleimage import SimpleImage

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('pooh.png')

    # add text to the top and bottom of the meme
    meme_gen.add_text('CS50', 590, 65)
    meme_gen.add_text('CiP 106B', 550, 420)

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()

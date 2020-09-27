With the power to manipulate images the same way you would with software such as Microsoft Paint or Adobe Photoshop, Python can automatically edit hundreds or thousands of images with ease. You can install Pillow by running pip install --user -U pillow==6.0.0. 

In Pillow, RGBA values are represented by a tuple of four integer values. For example, the color red is represented by (255, 0, 0, 255). This color has the maximum amount of red, no green or blue, and the maximum alpha value, meaning it is fully opaque.

Pillow offers the ImageColor.getcolor() function so you don’t have to memorize RGBA values for the colors you want to use. This function takes a color name string as its first argument, and the string 'RGBA' as its second argument, and it returns an RGBA tuple.

    ➊ >>> from PIL import ImageColor
    ➋ >>> ImageColor.getcolor('red', 'RGBA')
    (255, 0, 0, 255)
    ➌ >>> ImageColor.getcolor('RED', 'RGBA')
    (255, 0, 0, 255)

Many of Pillow’s functions and methods take a box tuple argument. This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. The four integers are, in order, as follows:

* Left The x-coordinate of the leftmost edge of the box.
* Top The y-coordinate of the top edge of the box.
* Right The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer.
* Bottom The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.

![pillow_tupple](/automate_boring_stuff\images\pilow_tupple.png)

## Manipulating Images with Pillow

Once you have the image file zophie.png in your current working directory, you’ll be ready to load the image of Zophie into Python, like so:

    >>> from PIL import Image
    >>> catIm = Image.open('zophie.png')

If the image file isn’t in the current working directory, change the working directory to the folder that contains the image file by calling the os.chdir() function.

    >>> import os
    >>> os.chdir('C:\\folder_with_image_file')

Any changes you make to the Image object can be saved to an image file (also of any format) with the save() method. All the rotations, resizing, cropping, drawing, and other image manipulations will be done through method calls on this Image object.

    >>> catIm.filename
    'zophie.png'
    >>> catIm.format
    'PNG'
    >>> catIm.format_description
    'Portable network graphics'
    >>> catIm.size
    ➊ (816, 1088)
    ➎ >>> catIm.save('zophie.jpg')

Calling the save() method and passing it 'zophie.jpg' saves a new image with the filename zophie.jpg to your hard drive ➎

    >>> from PIL import Image
    ➊ >>> im = Image.new('RGBA', (100, 200), 'purple')
    >>> im.save('purpleImage.png')
    ➋ >>> im2 = Image.new('RGBA', (20, 20))
    >>> im2.save('transparentImage.png')

Here we create an Image object for an image that’s 100 pixels wide and 200 pixels tall, with a purple background ➊. This image is then saved to the file purpleImage.png. We call Image.new() again to create another Image object, this time passing (20, 20) for the dimensions and nothing for the background color ➋. Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified, so the second image has a transparent background;

## Copying and Pasting Images onto Other Images

    >>> from PIL import Image
    >>> catIm = Image.open('zophie.png')
    >>> catCopyIm = catIm.copy()

The catIm and catCopyIm variables contain two separate Image objects, which both have the same image on them. Now that you have an Image object stored in catCopyIm, you can modify catCopyIm as you like and save it to a new filename, leaving zophie.png untouched. For example, let’s try modifying catCopyIm with the paste() method.

The paste() method is called on an Image object and pastes another image on top of it. Let’s continue the shell example by pasting a smaller image onto catCopyIm.

    >>> faceIm = catIm.crop((335, 345, 565, 560))
    >>> faceIm.size
    (230, 215)
    >>> catCopyIm.paste(faceIm, (0, 0))
    >>> catCopyIm.paste(faceIm, (400, 500))
    >>> catCopyIm.save('pasted.png')

First we pass crop() a box tuple for the rectangular area in zophie.png that contains Zophie’s face. This creates an Image object representing a 230×215 crop, which we store in faceIm. Now we can paste faceIm onto catCopyIm. The paste() method takes two arguments: a “source” Image object and a tuple of the x- and y-coordinates where you want to paste the top-left corner of the source Image object onto the main Image object.

## Resizing an Image

The resize() method is called on an Image object and returns a new Image object of the specified width and height. It accepts a two-integer tuple argument, representing the new width and height of the returned image. Enter the following into the interactive shell:

    >>> from PIL import Image
    >>> catIm = Image.open('zophie.png')
    ➊ >>> width, height = catIm.size
    ➋ >>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
    >>> quartersizedIm.save('quartersized.png')

## Rotating and Flipping Images

    >>> from PIL import Image
    >>> catIm = Image.open('zophie.png')
    >>> catIm.rotate(90).save('rotated90.png')
    >>> catIm.rotate(180).save('rotated180.png')
    >>> catIm.rotate(270).save('rotated270.png')

The rotate() method has an optional expand keyword argument that can be set to True to enlarge the dimensions of the image to fit the entire rotated new image. For example, enter the following into the interactive shell:

    >>> catIm.rotate(6).save('rotated6.png')
    >>> catIm.rotate(6, expand=True).save('rotated6_expanded.png')

You can also get a “mirror flip” of an image with the transpose() method. You must pass either Image.FLIP_LEFT_RIGHT or Image.FLIP_TOP_BOTTOM to the transpose() method. Enter the following into the interactive shell:

    >>> catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    >>> catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

## Changing Individual Pixels

    >>> from PIL import Image
    ➊ >>> im = Image.new('RGBA', (100, 100))
    ➋ >>> im.getpixel((0, 0))
    (0, 0, 0, 0)
    ➌ >>> for x in range(100):
            for y in range(50):
                ➍ im.putpixel((x, y), (210, 210, 210))

        
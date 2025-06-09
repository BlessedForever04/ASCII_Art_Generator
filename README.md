# ASCII_Art_Generator
<h2>What is ASCII_ART_Generator?</h2>
ASCII_ART_Generator is a program that generates ASCII Arts from given images.

<h2>You might wonder, how it works?</h2>
Well, first you have to understand how images works, images are stored in comupters in 3 layered 2d grid/array, each layer representing RGB (Red, Green, Blue) color intensity
https://github.com/user-attachments/assets/429f0081-0ea8-42f2-9d63-81c094ddbab5
This is how images are stored in computer.

As images are stored in grid, their index represent pixels in image
https://github.com/user-attachments/assets/723d9233-70ed-4cb7-a2ca-6313dc08fec7

<h2>Technical information</h2>
Now you know how images are stored in computers, and this is what I used for creating ASCII Art.
Here images are of 2 types, colored which contain 3 layers i.e RGB and another is Grayscale i.e Black and white image
Grayscale image's index hold the curresponding brightness intensity of that pixel in UINT8 format ranging from 0 to 255, 0 being the lowest brightness and 255 being highest brightness.
As brightness and complete picture is available in indices (image[100][100]) and their brightness value ranging from 0 to 255, using numpy we can configure these parameteres leading to image manipulation, in my code I have also reduced the brightness of image with 50 for better contrasted result, these can be adjusted accordingly

```
image = cv.imread(input_path, cv.IMREAD_GRAYSCALE)
image = image.astype(np.int16) - 50
image = np.clip(image, 0, 255)
image = image.astype(np.uint8)
```
Here image is in UINT8 format, for manipulating values and to avoid overflow or underflow within range 0 and 255, we first convert it to INT16 increasing the range for manipulation and then clipping it for the desired range.
For creating ASCII Art, we can simply replace pixels with Ascii characters (Higher brightness intensity can be represented with dense and bigger AScii characters such as "@", "#", "$" etc and lower can be represented as ".", "'", "," etc
To represent the gradient of brightness within image, we would need more character
List of characters: "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. "
Now these characters are assigned to respective brightness intensity and then is printed on image and then saved

<h2>How program works</h2>
Reading image using OpenCV

```
image = cv.imread(input_path, cv.IMREAD_GRAYSCALE)
```
then adjusting brightness according to the tase

```
image = image.astype(np.int16) - 50
image = np.clip(image, 0, 255)
image = image.astype(np.uint8)
```
Creating complete black image same as the size of provided image

```
(height, width) = image.shape
new_image = np.zeros((height, width), dtype = np.uint8)
```

Main priting of characters on new image

```
for y in range(0, height, char_h): #skipped by char_h as height of a character
        for x in range(0, width, char_w): #skipped by char_w as width of a character
            brightness = image[y, x] #brightness intensity of image at (x, y)(y - height index, x - width index)
            character = brightness2ascii(brightness) #brightness to ASCII character conversion
            #cv.putText function to write text (ASCII Characters) on image
            cv.putText(new_image, #Image to write on
                       character, #str to write
                       (x, y + char_h - 2), #Coordinate/position
                       font, #Font
                       font_scale, #Font scale
                       (255,255,255), #White color of character
                       thickness, #thickness of character
                       lineType=cv.LINE_AA) #parameter the determines how edges are rendered (LINE_AA = Auto Aliasing)
```
brightness2ascii() function

```
def brightness2ascii(brightness):
    character_index = int((brightness/255) * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[character_index]
```
It calculates the index of ascii character and returns the character

<h2>Sources:</h2>
OpenCV documentation - Python
https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
Numpy Documentation
https://numpy.org/doc/

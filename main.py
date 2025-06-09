import numpy as np #Numeric python for performing mathematical operations
import cv2 as cv #OpenCV which stands for open source computer vision

#Constand character string according to their brightness (Density and size)
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1] #[::-1] for string's reverse order, starting from end and going towards the start

#function to allocate curresponding ASCII character to pixel's brightness 
def brightness2ascii(brightness):
    character_index = int((brightness/255) * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[character_index]

#function to generate ASCII Art
def generate(input_path, output_path = "ASCII-Art.png"): #input_path is name of the image being read, output_path is the name of image being generated.
    image = cv.imread(input_path, cv.IMREAD_GRAYSCALE) #cv.IMREAD_GRAYSCALE format used for reading only the brightness of pixels and not RGB layers of image.
        
    #simple image name/path validation
    if image is None:
        print("Wrong image name, recheck!")
        return

    #this here is just a brightness adjustments done for better quality in generated image (optional)
    #here image is of UINT8 type (8 bits) which ranges from 0 to 255 and to avoid overflow and underflow I converted it to INT16 and then back again to UINT8
    image = image.astype(np.int16) - 50 #50 is general observed brightness correction according to me (can be adjusted according to the image's brightness)
    #clip function for clipping/cropping/segmenting array from 0 to 255 (UINT8 range)
    image = np.clip(image, 0, 255)
    image = image.astype(np.uint8)

    #shape function provides dimension of image (Height and weight)
    (height, width) = image.shape

    #black background by using np.zeros (Allocates all 0s, i.e zero brightness)
    new_image = np.zeros((height, width), dtype = np.uint8)

    #some character's parameters
    #kept smaller so multiple characters can be fitted to avoid overlap
    font = cv.FONT_HERSHEY_SIMPLEX
    font_scale = 0.3 
    thickness = 1

    #cv.getTextSize returns tuple ((Width, Height), Baseline) of character (Width, height and baseline of character with provided font and other data) 
    (char_w, char_h), baseling = cv.getTextSize("A", font, font_scale, thickness)

    #Assigning and writing ASCII character on the black background previously created (new_image)
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
    
    #Saving generated image (new_image) as output_path
    cv.imwrite(output_path, new_image)
    print(f"Successfuly saved \"{output_path}\"")

#just welcome message and Instruction
print("""\nWelcome to image to ASCHII art generator!\n
Instruction: Keep your image in the current directory and enter the image's name (Without extension).
It is required for image to be of higher quality, higher the resolution of image, higher the resolution of generated image!""")

#Asking for image's name
input_path = input("Enter the image's name (with extension (.png .jpeg .jpg)): ")

#Generate funcion called with argument input_path
generate(input_path)
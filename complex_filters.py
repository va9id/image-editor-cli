from Cimpl import get_height, get_width, copy, get_color, set_color, create_color, create_image
from simple_filters import grayscale

def red_channel(img):
    """(Cimpl.Image) -> Cimpl.Image
    
    Returns a new image with the color of the image passed as the argument 
    changed to red
    
    >>>red_flter(file)
    
    Author: Jaxson Brown
    """

    h = get_height(img)
    w = get_width(img)

    new_img = copy(img)
    
    for y in range(0,h):
        for x in range(0,w):
            color = get_color(img, x,y)
            new_color = color[0]
            set_color(new_img, x, y, create_color(new_color,0,0))

    return new_img

def green_channel(img):
    height = get_height(img)
    width = get_width(img)
    filtered_img = copy(img)
    for y in range(0,height):
        for x in range(0,width):
            img_color = get_color(img, x,y)
            filter_color = img_color[1]
            set_color(filtered_img, x, y, create_color(0, filter_color,0))
    return filtered_img

def blue_channel(image): 
    blue_image = copy(image) 
    for pixel in image:
        x, y, (r, g, b) = pixel 
        new_colour = create_color( 0, 0, b) 
        set_color (blue_image, x, y, new_colour)
    return blue_image

def combine(red_img,green_img,blue_img):
    height = get_height(red_img)
    width = get_width(red_img)
    new_img = create_image(width, height)
    for y in range(0, height):
        for x in range(0, width):
            red_color = get_color(red_img, x, y)
            green_color = get_color(green_img, x, y)
            blue_color = get_color(blue_img, x, y)
            set_color(new_img, x, y, create_color(red_color[0], green_color[1],
                                           blue_color[2]))
                    
    return new_img

# Function definition for the two_tone filter
def two_tone(image, colour1, colour2): 
    colours = ["black", "white", "red" , "lime", "blue",
              "yellow", "cyan" ,"magenta", "gray"]
    rgb_values = [ (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), 
                (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), 
                (128, 128, 128)] 
    
    two_tone_image = copy(image) 
    
    for i in range(len(colours)): 
        if colour1 == colours[i]: 
            tone1 = rgb_values[i] 
            new_c1 = create_color(tone1[0], tone1[1], tone1[2])
        if colour2 == colours[i]:
            tone2 = rgb_values[i] 
            new_c2 = create_color(tone2[0], tone2[1], tone2[2]) 
            
    for pixel in two_tone_image:
        x, y, (r, g, b) = pixel 
        brightness = (r+g+b) // 3
        if 0 <= brightness <= 127: 
            set_color (two_tone_image, x, y, new_c1)   
        elif 128 <= brightness <= 255: 
            set_color(two_tone_image, x, y, new_c2) 
    return two_tone_image

def three_tone(image, colour1, colour2, colour3): 
    colours = ["black", "white", "red" , "lime", "blue",
              "yellow", "cyan" ,"magenta", "gray"]
    
    rgb_values = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), 
                    (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), 
                    (128, 128, 128)] 
    
    three_tone_image = copy(image) 
    
    for i in range(len(colours)): 
        if colour1 == colours[i]: 
            tone1 = rgb_values[i] 
            new_c1 = create_color(tone1[0], tone1[1], tone1[2])
        if colour2 == colours[i]:
            tone2 = rgb_values[i] 
            new_c2 = create_color(tone2[0], tone2[1], tone2[2]) 
        if colour3 == colours[i]:
            tone3 = rgb_values[i] 
            new_c3 = create_color(tone3[0], tone3[1], tone3[2])             
        
    for pixel in three_tone_image:
        x, y, (r, g, b) = pixel 
        brightness = (r+g+b) // 3
        if 0 <= brightness <= 84: 
            set_color (three_tone_image, x, y, new_c1)   
        elif 85 <= brightness <= 170: 
            set_color(three_tone_image, x, y, new_c2) 
        elif 171 <= brightness <= 255: 
            set_color(three_tone_image, x, y, new_c3)         
                       
    return three_tone_image

def extreme_contrast(img):
    new_img = copy(img)
    
    height = get_height(img)
    width = get_width(img)
    
    for y in range(0, height):
        for x in range(0, width):
            color = get_color(img, x , y)
            if 0 <= color[0] <= 127:
                red_color = 0
            elif 128 <= color[0] <= 255:
                red_color = 255
            if 0 <= color[1] <= 127:
                green_color = 0
            elif 128 <= color[1] <= 255:
                green_color = 255
            if 0 <= color[2] <= 127:
                blue_color = 0
            if 128 <= color[2] <= 255:
                blue_color = 255
            
            set_color(new_img , x, y, create_color(red_color, green_color, blue_color))
            
    return new_img
    
def sepia(img):
    new_img = copy(img)
    gray_img = grayscale(new_img)
    
    height = get_height(gray_img)
    width = get_width(gray_img)
    
    for y in range(0, height):
        for x in range(0, width):
            color = get_color(gray_img, x, y)
            
            if color[0] < 63:
                blue_color = color[2] * 0.9
                red_color = color[0] * 1.1
            
            elif 63 <= color[0] <=191:
                blue_color = color[2] * 0.85
                red_color = color[0] * 1.15
            
            elif color[0] > 191:
                blue_color = color[2] * 0.93
                red_color = color[0] * 1.08               
                
            set_color(new_img, x, y, create_color(red_color, color[1], blue_color))
            
    return new_img

def _adjust_component(component_value: int) -> int:
    if 0<=component_value<=63:
        value = 31
    elif 64<=component_value<=127:
        value = 95
    elif 128<=component_value<=191: 
        value = 159
    elif 192<=component_value<=255:
        value = 223
    return value

# Function definition for posterize filter
def posterize(FILENAME):
    new_image=copy(FILENAME)
    for pixel in FILENAME:
        x, y, (r, g, b) = pixel 
        r1=_adjust_component(r)
        g1=_adjust_component(g)
        b1=_adjust_component(b) 
        set_color(new_image,x,y,create_color(r1,g1,b1))
    return new_image

def detect_edges(img, threshold):
    new_img = copy(img)
    height = get_height(img)
    width = get_width(img)    
    for x in range(0, width):
        set_color(new_img, x, height-1, create_color(255,255,255))
    for y in range(0, height-1):
        for x in range(0, width):
            color1 = get_color(img, x, y)
            color2 = get_color(img, x, y+1)
            brightness1 = (color1[0] + color1[1] + color1[2]) / 3
            brightness2 = (color2[0] + color2[1] + color2[2]) / 3
            difference = abs(brightness1 - brightness2)
            if difference > threshold:
                set_color(new_img, x, y, create_color(0, 0, 0))
            else:
                set_color(new_img, x, y, create_color(255, 255, 255))
    return new_img

def detect_edges_better(img, threshold):
    new_img = copy(img)
    height = get_height(img)
    width = get_width(img)
    set_color(new_img, width-1, height-1, create_color(255, 255, 255))
    for y in range(0, height-1):
        for x in range(0, width):
            color1 = get_color(img, x, y)
            color2 = get_color(img, x, y+1)
            brightness1 = (color1[0] + color1[1] + color1[2]) / 3
            brightness2 = (color2[0] + color2[1] + color2[2]) / 3
            difference1 = abs(brightness1 - brightness2)
            if difference1 > threshold:
                set_color(new_img, x, y, create_color(0, 0, 0))
            else:
                set_color(new_img, x, y, create_color(255, 255, 255))
    for y in range(0, height):
        for x in range(0, width-1):
            color3 = get_color(img, x, y)
            color4 = get_color(img, x+1, y)
            brightness3 = (color3[0] + color3[1] + color3[2]) / 3
            brightness4 = (color4[0] + color4[1] + color4[2]) / 3
            difference2 = abs(brightness3 - brightness4)
            if difference2 > threshold:
                set_color(new_img, x, y, create_color(0, 0, 0))
            else:
                set_color(new_img, x, y, create_color(255, 255, 255))
    return new_img

def flip_vertical(image):
    vertical_image = copy(image)
    for x in range(get_width(image)):
        for y in range(get_height(image)):
            new_colour = get_color(image, x, y)
            set_color(vertical_image, get_width(image)-x-1, y, new_colour)
    return vertical_image

def flip_horizontal(image): 
    horizontal_image = copy(image)

    for y in range(get_height(image)):
        for x in range(get_width(image)):
            new_colour = get_color(image, x, y)
            set_color(horizontal_image, x, get_height(image)-1-y, new_colour)    
            
    return horizontal_image
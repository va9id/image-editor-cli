from image_functionality import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color

def invert(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        inverted = create_color(255 - r, 255 - g, 255 - b)
        set_color(new_image, x, y, inverted)
    return new_image

def grayscale_from_red(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        gray = create_color(r, r, r)
        set_color(new_image, x, y, gray)       
    return new_image
        
def grayscale_from_green(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        gray = create_color(g, g, g)    
        set_color(new_image, x, y, gray)       
    return new_image

def grayscale_from_blue(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        gray = create_color(b, b, b)      
        set_color(new_image, x, y, gray)        
    return new_image

def grayscale(image: Image) -> Image:
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image
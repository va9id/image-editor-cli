from image_functionality import load_image, save_as, show
from complex_filters import * 


def get_input() -> str:
    """Returns the command the user inputs
    
    >>>get_input()
    """
    cmd = input(menu()).upper()
    while cmd not in all_commands:
        print("No such command\n") 
        cmd = input(menu()).upper()
    else:
        return cmd

def load(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns an image that the user chooses """
    image = load_image(input("Enter the name of an image file: "))
    show(image)   
    if image == None: 
        print("\nNo image loaded") 
    return image 
    
def save(image) -> None:
    """(Cimpl.Image) -> None
    Saves the image the user has already loaded and/or modified"""
    if image == None:
        print("No image to save") 
    else:
        save_as(image)
        print("Your image was saved")

def two(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the two tone filter applied to it.
    
    >>>two(image) 
    """ 
    if image == None: 
        print("No image loaded\n") 
    else: 
        image = two_tone(image, 'yellow', 'cyan') 
        show(image)         
    return image 

def three(image):  
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the three tone filter applied to it.
    
    >>>three(image) 
    """     
    if image == None: 
        print("No image loaded\n")
    else: 
        image = three_tone(image, 'yellow', 'magenta', 'cyan') 
        show(image)        
    return image 

def xtreme(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the extreme contrast filter 
    applied to it.
    
    >>>xtreme(image) 
    """     
    if image == None: 
        print("No image loaded\n")    
    else: 
        image = extreme_contrast(image) 
        show(image) 
    return image 

def tint(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the sepia tinting filter applied to it.
    
    >>>tint(image) 
    """     
    if image == None: 
        print("No image loaded\n")     
    else: 
        image = sepia(image) 
        show(image) 
    return image 


def post(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the posterize filter applied to it.
    
    >>>post(image) 
    """     
    if image == None: 
        print("\nNo image loaded")     
    else: 
        image = posterize(image) 
        show(image) 
    return image


def edge(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the edge detection filter applied
    to it.
    
    >>>edge(image) 
    """     
    if image == None: 
        print("No image loaded\n")
    else:
        threshold_val = int(input("Choose a threshold value: "))
        image = detect_edges(image, threshold_val ) 
        show(image) 
    return image 

def improve(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the imporved edge detection
    filter applied to it.
    
    >>>improve(image) 
    """     
    if image == None: 
        print("No image loaded\n") 
    else: 
        threshold_val = int(input("Choose a threshold value: "))
        image = detect_edges_better(image, threshold_val ) 
        show(image) 
    return image 

def vert(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the flip vertical filter 
    applied to it. 
    
    >>>vert(image) 
    """     
    if image == None: 
        print("No image loaded\n") 
    else:   
        image = flip_vertical(image)
        show(image) 
    return image 

def horz(image): 
    """(Cimpl.Image) -> Cimpl.Image
    Returns the image the user chose with the flip horizontal 
    filter applied to it.
    
    >>>horz(image) 
    """     
    if image == None: 
        print("No image loaded\n")  
    else: 
        image = flip_horizontal(image)
        show(image) 
    return image   

def menu() -> str: 
    """Returns the display menu
    
    >>> menu()
    """ 
    menu_text = "L)oad image S)ave-as\n2)-tone\
    3)-tone   X)treme contrast   T)int sepia   P)osterize\nE)dge detect\
    I)mproved edge detect   V)ertical flip   H)orizontal flip\nQ)uit\n\n: "    
    return menu_text


# Dictionary of all possible valid commands 
all_commands = { "L":load, "S": save, "2":two, "3":three, "X":xtreme, "T":tint,
             "P":post, "E":edge, "I":improve, "V":vert, "H":horz, "Q":None} 

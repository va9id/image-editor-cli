from ui import*

if __name__ == "__main__": 
    #Mainscript 
    image = None 
    run_program = True 
    stop_program = False

    print("Below are the following commands. Please choose one and begin!")

    while run_program:
        cmd = get_input()
        if cmd != 'Q':
            image = all_commands[cmd](image)
        elif cmd == "Q": 
            print("Quitting program")
            run_program = stop_program 
        
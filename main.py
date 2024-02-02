from heandlers import *


commands = {
    
    'hello': help_handler,
    'add' : add_handler,
    'change': change_handler,
    'phone' : phone_handler,
    'show all': show_all_handler,
    'good': bye_handler,
    'close': bye_handler,
    'exit': bye_handler,
    'search': search_handler,
}


def get_handler(command):
    try:
        return commands[command]
    except KeyError as er:
        return er

def main():
    load()
    while True:
        get_command = input(">>").lower()
        sep_com = get_command.split(' ')
        if get_command.startswith(tuple(commands)):
            if get_command.startswith("show all"):
                handler = get_handler("show all")
            else:
                handler = get_handler(sep_com[0])
            if sep_com[0] in ['add', 'change', 'phone']:
                print(handler(get_command))
            elif sep_com[0] == 'hello':
                print(handler())
            elif sep_com[0] == 'search':
                print(handler(get_command))
            elif sep_com[0] == 'show' and sep_com[1] == 'all':
                print(handler())    
            elif sep_com[0] in ['good', 'close', 'exit']:
                print(handler())
                save()
                break
            else:
                print("Give me correct command")
        else:
            print("Give me correct command")
        




if __name__ == '__main__':

    main()

    #print(contact_list)

from classes import *
import pickle

contact_list = AddressBook()

def input_error(func):
    
    error_v = "Give me correct number"
    error_i = "Give me name and phone"
    error_k = "Give me name"
    
    def inner(*args):

        try:
            return func(*args)
        except ValueError:
            return error_v
        except IndexError:
            return error_i
        except KeyError:
            return error_k
    return inner


def help_handler():
    hello = "How can I help you?"
    return hello


@input_error
def add_handler(command):
    raw_command = command.removeprefix('add ')
    user_data = raw_command.split(' ')
    contact = Record(user_data[0])
    contact.add_phone(user_data[1])
    contact_list.add_record(contact)
    message = "Contact has been added"
    return message



@input_error
def change_handler(command):
    raw_command = command.removeprefix('change ')
    user_data = raw_command.split(' ')
    contact_back = contact_list.find(user_data[0])
    old_phone = contact_back.phones[0]
    contact_back.edit_phone(str(old_phone), user_data[1])
    message = "Contact has been changed"
    return message



@input_error
def phone_handler(command):
    raw_command = command.removeprefix('phone ')
    user_data = raw_command.split(' ')
    contact_back = contact_list.find(user_data[0])
    return contact_back


@input_error
def search_handler(command):
    raw_command = command.removeprefix('search ')
    user_data = raw_command.split(' ')
    match_list = contact_list.search(user_data[0])
    return match_list


def show_all_handler():
    return contact_list


def bye_handler():
    bye = "Good bye!"
    return bye

def load():
    global contact_list
    with open('contact_list.bin', "rb") as fh:
        contact_list = pickle.load(fh)

def save():
    with open('contact_list.bin', 'wb') as file:
        pickle.dump(contact_list, file)
    

if __name__ == '__main__':

    help_handler()
    add_handler()
    change_handler()
    phone_handler()
    show_all_handler()
    bye_handler()
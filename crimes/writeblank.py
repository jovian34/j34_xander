
    
def open_file(filename):
    with open(filename, mode='wt', encoding='utf-8') as python_file:
        print('You are done!')

def get_file_name():
    f = input('Enter the name of your new python file: ')
    return f + '.py'

filepath = get_file_name()
open_file(filepath)

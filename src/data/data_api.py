from constants import DATA_PATH
import os

## This is the data file for Data queries

'''
Index:

create_file
create_dir

'''


##### C R U D  O P E R A T I O N S  ###################################################################################

# --- C r e a t e  F i l e ----------------------------------------------
def create_file(filename, path=''):
    '''
        create a file .txt about an theme

        Input:
                filename    :   the name of the theme
                str

                path        :   the path (subject) of the theme
                str
    '''

    with open(path + filename, "w") as file:
        pass 


# --- C r e a t e  D i r e c t o r y  ---------------------------------
def create_dir(dirname):
    '''
        create a directory (a subject)

        Input:
                dirname     :   the name of the directory
                str
    '''

    os.makedirs(DATA_PATH + dirname, exist_ok=True) 


# --- U p d a t e ---
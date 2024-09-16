from constants import DATA_PATH
from entities.question import Question, QuestionList
import os

## This is the data file for Data queries

'''
### Index ###

-- Subject/Argument operations --
create_file(argument, path='')
create_dir(subject)
read_by_subject(subject)
read_by_argument(argument, subject)


-- Questions Operations--

-- Utils --
parse(content, subject, argument):
get_argument_list(subject):

'''

### S U B J E C T / A R G U M E N T  O P E R A T I O N S  #############################################################

# --- C r e a t e  F i l e ------------------------------------------------------------------------------------------
def create_file(argument, path=''):
    '''
        create a file .txt (argument)

        Input:
                filename    :   the name of the argument
                str

                path        :   the path (subject) of the argument
                str
    '''

    with open(path + argument, "w") as file:
        pass 


# --- C r e a t e  D i r e c t o r y  --------------------------------------------------------------------------------
def create_dir(subject):
    '''
        create a directory (a subject)

        Input:
                dirname     :   the name of the directory
                str
    '''

    os.makedirs(DATA_PATH + subject, exist_ok=True) 


# --- R e a d  S u b j e c t --------------------------------------------------------------------------------
def read_by_subject(subject):
    '''
        read all the questions in a subject

        Input:
                subject         :   the subject of the questions
                str

        Output:
                <QuestionList>  :   the list of all the questions    
    '''

    argument_list = get_argument_list(subject)

    all_questions = QuestionList()
    for argument in argument_list:
        arg_questions = read_by_argument(argument, subject)
        all_questions.extend(arg_questions)

    return all_questions


# --- R e a d  A r g u m e n t  --------------------------------------------------------------------------------------
def read_by_argument(argument, subject):
    '''
        read all the question of an argument

        Input:
                argument            :   the argument of the questions
                str

                subject             :   the subject of the questions
                str
        
        Output:
                <QuestionList>      :   the list of all the questions
    '''

    path = subject + '/' + argument + '.txt'

    with open(path, 'r') as file:
        content = file.read()
    
    return parse(content, subject, argument)



### Q U E S T I O N S  O P E R A T I O N S ##############################################################################

# --- S a v e  A r g u m e n t ---
def save_argument(argument, subject):
    pass

# --- Read Questions ---

# --- Update Question ---

# --- Delete Question ---


#### U T I L S ##########################################################################################################

def parse(content, subject, argument):
    '''
        it composes the question object read from the file

        Input:
                content         :   the entire content of the file
                str

                subject         :   the subject of the questions
                str

                argument        :   the argument of the questions
                str
        
        Output:
                question_list   :   the list of all the questions
                QuestionList
    '''

    questions = content.split('***')
    question_list = QuestionList()

    for question in questions:
        
        question_attributes = question.split('**:')
        new_question = Question(
            question_attributes[0],
            subject,
            argument,
            question_attributes[1],
            question_attributes[2],
            question_attributes[3]
        )

        question_list.append(new_question)

    return question_list

def get_argument_list(subject):
    '''
        returns all the arguments in a subject

        Input:
                subject     :   name of the subject
                str
        
        Output:
                list<str>   :   the list of all the argumnent in a subject
    '''

    file_list = os.listdir(subject)
    args_list = []

    for file in file_list:
        file = file.split('.')
        args_list.append[file[0]]

    return args_list

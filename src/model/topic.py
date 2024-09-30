from model.question import Question, QuestionList
import os


class Topic():

    def __init__(self, name, subject):
        
        self.name = name
        self.subject = subject
        self.path = self.subject + '/' + self.name + '.txt'

        if os.path.exists(self.path) and os.path.isfile(self.path):
            self.all_questions = self.get_all_questions()
        else:
            raise ValueError('the passsed resource does not exist.')


    # --- R e a d  A l l  Q u e s t i o n s ---------------------------------------------------------------------------
    def get_all_questions(self):
        '''
            read all the question of an topic

            Input:
                    topic            :   the topic of the questions
                    str

                    subject             :   the subject of the questions
                    str
            
            Output:
                    <QuestionList>      :   the list of all the questions
        '''


        with open(self.path, 'r') as file:
            content = file.read()
        
        return self.parse(content)
    

    # --- A d d  Q u e s t i o n -------------------------------------------------------------------------------------
    def add_question(self, text, ans):

        self.reset_questions_order()
        last_question = self.all_questions[-1]
        new_id = last_question.id + 1

        new_question = Question(
            new_id,
            self.subject,
            self.name,
            text,
            ans,
            False
        )

        self.all_questions.append(new_question)


    # --- S h u f f l e -----------------------------------------------------------------------------------------------        
    def shuffle_all(self):
        self.all_questions.shuffle()
        return self.all_questions


    # --- P a r s e --------------------------------------------------------------------------------------------------
    def parse(self, content):
        '''
            it composes the question object read from the file

            Input:
                    content         :   the entire content of the file
                    str

                    subject         :   the subject of the questions
                    str

                    topic           :   the topic of the questions
                    str
            
            Output:
                    question_list   :   the list of all the questions
                    QuestionList
        '''

        questions = content.split('***')
        question_list = QuestionList()

        for question in questions:
            
            question_attributes = question.split('**:')

            deleted = question_attributes[3]
            if deleted == False:
                id = question_attributes[0]
                text = question_attributes[1]
                ans = question_attributes[2]
                new_question = Question(
                    id,
                    self.subject,
                    self.name,
                    text,
                    ans,
                    deleted
                )

                question_list.append(new_question)

        return question_list
    
    # --- R e s e t  Q u e s t i o n s  O r d e r --------------------------------------------------------------------
    def reset_questions_order(self):
        '''
            reset the questions order
        '''
        self.all_questions = self.get_all_questions()


    ### C L A S S  M E T H O D S ######################################################################################

    def create_topic(topic_name, path=''):
        '''
            create a file .txt (topic)

            Input:
                    filename    :   the name of the topic
                    str

                    path        :   the path (subject) of the topic
                    str
        '''

        if not(path.endswith('/')):
            path = path + '/'
            
        with open(path + topic_name, "w") as file:
            pass 

    
    def update_topic(subject_name, old_name, new_name):

        if not(subject_name.endswith('/')):
            path = subject_name + '/'

        old_topic_name = path + old_name
        new_topic_name = path + new_name

        os.rename(old_topic_name, new_topic_name)

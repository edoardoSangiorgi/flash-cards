from topic import Topic
from question import QuestionList
from constants import DATA_PATH
import os

class Subject():

    def __init__(self, name):
        
        self.name = name
        if os.path.exists(self.name):
            self.topics_list = self.get_all_topics()
            self.all_topics = self.read_all_topics()
        else:
            raise ValueError('the passed resource does not exists.')
        

    # --- R e a d  T o p i c s ------------------------------------------------------------------------------------------
    def read_all_topics(self):
        '''
            return all the topic instances contained in an argument

            Output:
                    all_topics      :   all topics
                    list<Topic>
        '''

        all_topics = []
        for topic_name in self.topics_list:
            new_topic = Topic(topic_name, self.name)
            all_topics.append(new_topic)

        return all_topics


    # --- G e t  T o p i c s  L i s t -------------------------------------------------------------------------------------
    def get_all_topics(self):
        '''
            returns all the arguments in a subject

            Input:
                    subject     :   name of the subject
                    str
            
            Output:
                    list<str>   :   the list of all the argumnent in a subject
        '''

        file_list = os.listdir(self.name)
        topics_list = []

        for file in file_list:
            file = file.split('.')
            topics_list.append[file[0]]

        return topics_list
    

    # --- G e t  A l l  Q u e s t i o n s -------------------------------------------------------------------------------
    def get_all_questions(self):

        all_questions = QuestionList()
        for topic in self.all_topics:
            all_questions.extend(topic.all_questions)

        return all_questions
    

    # --- S h u f f l e  A l l  Q u e s t i o n s  -----------------------------------------------------------------------
    def shuffle_all(self):

        all_questions = self.get_all_questions()
        
        return all_questions.shuffle()
    




    ### C L A S S  M E T H O D S  #########################################################################################

    # --- C r e a t e -----------------------------------------------------------------------------------------------------
    def create_subject(name):
        '''
            create a directory (a subject)

            Input:
                    dirname     :   the name of the directory
                    str
        '''

        os.makedirs(DATA_PATH + name, exist_ok=True) 


    # --- D e l e t e -----------------------------------------------------------------------------------------------------
    def delete_subject(name):
        '''
            sets the subject as deleted
        '''
        os.rename(name, name + '-deleted')
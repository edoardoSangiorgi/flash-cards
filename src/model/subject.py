from model.topic import Topic
from model.question import QuestionList
from model.constants import DATA_PATH
import os

class Subject():

    def __init__(self, name):
        
        self.name = name
        self.name_path = DATA_PATH + name
        if os.path.exists(self.name_path):
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
                    list<str>   :   the list of all the topic names in a subject
        '''

        file_list = os.listdir(self.name_path)
        topics_list = []

        for file in file_list:
            file = file.split('.')
            topics_list.append(file[0])

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
        all_questions.shuffle()

        return all_questions
    




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


    # --- U p d a t e ---------------------------------------------------------------------------------------------------
    def update_subject(old_name, new_name):
        '''
            update the subject name directory
        '''
        os.rename(old_name, new_name)


    # --- R e a d -------------------------------------------------------------------------------------------------
    def get_all():
        '''
            read all the subject

            Output:
                    subject_list    :   the list which contains the name of all the subject
                    list
        '''

        dirs = [dir for dir in os.listdir(DATA_PATH) if os.path.isdir(os.path.join(DATA_PATH, dir))]
        return Subject.get_available_subject(dirs)
        
    
    # --- Utils ---------------------------------------------------------------------------------------------------
    def get_available_subject(subject_list):
        '''
            returs all the available subjects and delete from the list
            the ones which are deleted

            Input:
                    subject_list    :   the list of the subject
                    list[str]

            Ouput:
                    new_list        :   the list of the available subjects
                    list[str]
        '''
        available_subject = []
        for subject in subject_list:
            if not(Subject.is_deleted(subject)):
                available_subject.append(subject)

        return available_subject


    def is_deleted(subject):
        '''
            check if the subject is deleted

            Input:
                    subject     :       the name of the subject
                    str
        '''
        if subject.endswith('-deleted'): return True
        else: return False
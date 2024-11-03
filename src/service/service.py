from model.subject import Subject
from model.topic import Topic
import model.utils as utils



# --- S u b j e c t  F l a s h c a r d --------------------------------------------------------------------------
def subject_flashcard(subject_name):
    '''
        return all the subject questions shuffled

        Input:
                subject_name    :   the name of the subject

        Output:
                QuestionList    :   the shuffled list of all the questions
    '''

    subject = Subject(subject_name)
    return subject.shuffle_all()


# --- T o p i c  F l a s h c a r d ------------------------------------------------------------------------------ 
def topic_flashcard(subject_name, topic_name):
    '''
        return all the subject questions shuffled

        Input:
                subject_name    :   the name of the subject

        Output:
                QuestionList    :   the shuffled list of all the questions
    '''
    
    topic = Topic(topic_name, subject_name)
    return topic.shuffle_all()


### C R U D  S U B J E C T #######################################################################################

def add_subject(subject_name):
    Subject.create_subject(subject_name)
    return get_all_subject()


def remove_subject(subject_name):
    Subject.update_subject(subject_name, subject_name + '-deleted')
    return get_all_subject()


def update_subject(old_name, new_name):
    Subject.update_subject(old_name, new_name)
    return get_all_subject()


def get_all_subject():
    return Subject.get_all()


### C R U D  T O P I C ###########################################################################################

def add_topic(subject_name, topic_name):
    Topic.create_topic(subject_name, topic_name)


def remove_topic(subject_name, topic_name):
    Topic.update_topic(subject_name, topic_name, topic_name + '-deleted')


def update_topic(subject_name, old_topic_name, new_topic_name):
    Topic.update_topic(subject_name, old_topic_name, new_topic_name)



### C R U D  Q U E S T I O N S ###################################################################################

def add_question(subject_name, topic_name, text, ans):
    
    topic = Topic(topic_name, subject_name)
    topic.add_question(text, ans)


def remove_question(subject_name, topic_name, text, ans):
    pass


def update_questions(subject_name, topic_name, text, ans):
    pass


### F L A S H C A R D S ######################################################################################

def flashcard(subject_name, topic_name=None):
    
    if topic_name is not None:
        deck = Topic(topic_name, subject_name)
    else:
        deck = Subject(subject_name)

    return deck.shuffle_all()

    
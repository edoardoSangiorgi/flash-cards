from model.subject import Subject
from model.topic import Topic



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


def remove_subject(subject_name):
    
    Subject.delete_subject(subject_name)


def update_subject(old_name, new_name):
    
    Subject.update_subject(old_name, new_name)



### C R U D  T O P I C ###########################################################################################

def add_topic(subject_name, topic_name):
    
    Topic.create_topic(topic_name, subject_name)


def remove_topic(subject_name, topic_name):
    pass


def update_topic(subject_name, topic_name):
    pass



### C R U D  Q U E S T I O N S ###################################################################################

def add_question(subject_name, topic_name, text, ans):
    pass


def remove_question(subject_name, topic_name, text, ans):
    pass


def update_questions(subject_name, topic_name, text, ans):
    pass
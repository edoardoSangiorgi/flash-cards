import random


### Q U E S T I O N  C L A S S ########################################################################################
class Question:
    '''
        It represents the question in the application.

        Each question has:
        - just a subject
        - just an argument

        Specfically:
        - each subject has one or more arguments
        - each argument has one or more questions
    '''

    def __init__(
        self,
        id,
        subject='',
        argument='',
        text='',
        ans='',
        deleted=False,
    ):
        self.id = id
        self.subject = subject
        self.argument = argument
        self.text = text
        self.ans = ans
        self.deleted = deleted


    def __repr__(self):
        '''
            returns a string representation of the object Question

            Output:
                    <string>    :   key,value-like
                                    ex:
                                    Question(id=1, subject=Math, argument=Functions, deleted=False)
        '''
        return f"Question(id={self.id}, subject='{self.subject}', argument='{self.argument}', deleted={self.deleted})"




##### Q U E S T I O N  L I S T  C L A S S ###############################################################################
class QuestionList(list):

    def __init__(self):
        super().__init__()
        


    # --- C r e a t e -----------------------------------------------------------------------------------------------------

    def append(self, new_question):
        '''
            add a question in the question list

            Input:
                    new_question    :   question to add
                    Question
        '''

        if isinstance(new_question, Question):
            super().append(new_question)

        else:
            raise TypeError("The instance passed is not a Question instance")
        
    
    def extend(self, new_question_list):
        '''
            extend the self list with all the elements of the passed list

            Input:
                    new_question_list   :   the list to ad to the self
                    QuestionList
        '''

        if isinstance(new_question_list, QuestionList):
            super().extend(new_question_list)

        else:
            raise TypeError('The data passed are not  QuestionList instances')



    # --- R e a d ----------------------------------------------------------------------------------------------------------
    
    def get_by_id(self, id):
        '''
            return a question by id

            Input:
                    id          :   id of the question
                    int

            Output:
                    question    :   found question
                    Question

                    or

                    None        :   question not found
        '''

        for question in self:
            if question.id == id:
                return question
    
        return None


    def get_by_subject(self, subject):
        '''
            returns all the question of a subject

            Input:
                    subject         :   the subject of the question
                    str

            Output:
                    list<Question>  :   the list of the question that belong to a subject
                                        the argument of the single questions could be different
        '''

        return [question for question in self if question.subject == subject]
    

    def get_by_argument(self, argument):
        '''
            returns all the question of an argument

            Input:
                    argument         :   the argument of the question
                    str

            Output:
                    <QuestionList>  :   the list of the question that belong to an argument
                                        the subject of the questions will be the same
        '''

        return [question for question in self if question.argument == argument]



    # --- U p d a t e -------------------------------------------------------------------------------------------------

    def update_question(self, id, **kwargs):
        '''
            update the question with the specified id

            Input:
                    id  :   the id of the question to update
                    int           
        '''

        question = self.get_by_id(id)
        if question:
            for key, value in kwargs.items():
                if hasattr(question, key):
                    setattr(question, key, value)
        else:
            print(f"No question found with ID: {id}")



    # --- D e l e t e ------------------------------------------------------------------------------------------------

    def delete_by_id(self, id):
        '''
            remove the question by the id (set deleted as True)

            Input:
                    id  :   id of the question
                    int
        '''

        question = self.get_by_id(id)
        if question:
            question.deleted = True
        else:
            print(f"No question found with ID: {id}")

    
    # --- S h u f f l e -------------------------------------------------------------------------------------------
    def shuffle(self):
        '''
            shuffle the original list
        '''
        random.shuffle(self)
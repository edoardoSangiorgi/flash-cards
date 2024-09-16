
### Q U E S T I O N  C L A S S  ########################################################################################
class Question():

    def __init__(
        self,
        id,
        subject = '',
        argument = '',
        text = '',
        ans = '',
        deleted = True,
    ):

      self.id = id
      self.subject = subject
      self.argument = argument
      self.text = text
      self.ans = ans
      self.deleted = deleted


##### Q U E S T I O N  L I S T  C L A S S  ###############################################################################
class QuestionList(list):
   
    # --- A d d ---

    # --- D e l e t e ---

    # --- U p d a t e ---

    pass
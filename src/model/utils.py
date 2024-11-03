import os

DATA_NAME = '/src/model/data-resources'
DATA_PATH = os.getcwd() + DATA_NAME + '/'


def path_builder(args, terminator='/'):

    remove_none(args)
    if is_all_strings(args):
        return "/".join(args) + terminator
    
    raise ValueError("Tutti gli elementi di args devono essere stringhe")

def is_all_strings(args):
    '''
        check if all the element in the 'args' is string-type
        args can be a single string or a list/tuple of strings
    '''
    if isinstance(args, (list, tuple)):
        return all(isinstance(arg, str) for arg in args)
    return isinstance(args, str)


def remove_none(args):
    return [arg for arg in args if arg is not None]
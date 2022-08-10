import os

def mkdir(path):
    '''Create a directory if it does not exist'''
    if not os.path.isdir(path):
        parent, _ = os.path.split(path)
        mkdir(parent)
        os.mkdir(path)

def add_version(savepath, replace=False):
    '''Appends a version number to the end of a path if that path already exists with the given name and if replace is False'''
    savefile, saveext = os.path.splitext(savepath)
    if replace or not os.path.exists(savepath):
        return savepath
    else:
        version = 1
        new_savepath = '{} ({}){}'.format(savefile, version, saveext)
        while os.path.exists(new_savepath):
            version += 1
            new_savepath = '{} ({}){}'.format(savefile, version, saveext)
        return new_savepath

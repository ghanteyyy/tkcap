class TkCapException(Exception):
    '''
    tkcap raise this exception if pyautogui module was not found installed
    or master parameter in CAP class is not an instance of tkinter.Tk,
    or tkinter.TopLevel or tkinter.tix.Tk or tkinter.tix.Toplevel or if
    pyautogui module is found not installed.
    '''

    pass


class ExtensionError(TkCapException):
    '''
    This exception is raised by tkcap when the extension provided by user
    is invalid.
        VALID_EXTENSION = ['tif', 'tiff', 'jpg', 'png', 'jpeg', 'jpe',
                           'jfif', 'bmp', 'dib', 'gif']
    '''

    pass


class PathNotFoundError(TkCapException):
    '''
    This exception is raised when the user provides invalid path.
    '''

    pass


class ImageNameExistsError(TkCapException):
    '''
    This exception is raised when the user provides the name of image
    that already exists in the same directory.
    '''

    pass

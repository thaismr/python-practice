""" Single Line Module Doc """


class MyClass:
    """My doc

    Just like any other doc
    """

    def __init__(self, text):
        """Initializes class data

        :param text: text for this class
        :type text: str
        """

        self.text = text
        self.show_text(text)

    @staticmethod
    def show_text(text):
        """ Just print some text """
        if not isinstance(text, str):
            raise TypeError('text must be a string')
        if len(text) > 100:
            raise ValueError('text must have at most 100 characters')
        print(text)


# I need z to be an int when I use it somewhere else
z: int = 10


# Takes a float and returns a float
def something(num: float) -> float:
    return num + .4

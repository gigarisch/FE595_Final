from textblob import TextBlob
from variables import PoS_dict
from textblob import Word
from textblob.wordnet import VERB

def get_polarity(input_text):
    return str(TextBlob(input_text).polarity)


def get_subjectivity(input_text):
    return str(TextBlob(input_text).subjectivity)



def get_PoS(input_text):
    return "<br>".join([str((x[0],"{}: {}".format(x[1],PoS_dict.get(x[1]))))
                        for x in TextBlob(input_text).pos_tags])


def get_NP(input_text):
    return "<br>".join(TextBlob(input_text).noun_phrases)


def get_spellcheck(input_text):
    return str(TextBlob(input_text).correct())




def get_detect_language(input_text):
    return str(TextBlob(input_text).detect_language())


def get_translate(input_text):
    return str(TextBlob(input_text).translate(to='fr'))

def get_definition(input_text):
    return str(Word(input_text).definitions)

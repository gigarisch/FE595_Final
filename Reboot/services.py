from textblob import TextBlob
from variables import PoS_dict

def tester(input_text):
    return str(TextBlob(input_text).polarity)


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
    return suggest(TextBlob(input_text).string)


def get_detect_language(input_text):
    return str(TextBlob(input_text).detect_language)


def get_translate(input_text):
    return str(TextBlob(input_text).translate(to='fr'))

def service8():
    return "This is a placeholder for service 8: user documentation C"

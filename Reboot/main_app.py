from flask import Flask, request
from services import get_polarity, get_subjectivity, get_PoS, get_NP, get_spellcheck, get_detect_language, get_translate, service8


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def home():
    errors = ""
    if request.method == "POST":
        Sentence = None
        Word1 = None
        Word2 = None
        try:
            Sentence = str(request.form["Sentence"])
        except:
            errors += "<p>{!r} is invalid.</p>\n".format(request.form["Sentence"])
        try:
            Word1 = str(request.form["Word1"])
        except:
            errors += "<p>{!r} is invalid.</p>\n".format(request.form["Word1"])
        try:
            Word2 = str(request.form["Word2"])
        except:
            errors += "<p>{!r} is invalid.</p>\n".format(request.form["Word2"])
        if Sentence is not None or (Word1 is not None and Word2 is not None):
            polarity2_result = get_polarity(Sentence)
            subjectivity_result = get_subjectivity(Sentence)
            PoS_Result = get_PoS(Sentence)
            NP_Result = get_NP(Sentence)
            spellcheck_result = get_spellcheck(Sentence)
            language_result = get_detect_language(Sentence)
            translated_result = get_translate(Sentence)
            service8_result = service8()

            return '''
                        <html>
                            <body>
                                <p>The Polarity Score is: {polarity2_result}</p>
                                <p>The Subjectivity Score is: {subjectivity_result}</p>
                                <p>The PoS Value is: {PoS_Result}</p>
                                <p>The Noun Phrases are: {NP_Result}</p>
                                <p>The Spellcheck results are: {spellcheck_result}</p>
                                <p>The Language used is: {language_result}</p>
                                <p>The In French that is: {translated_result}</p>
                                <p>The Documentation is: {service8_result}</p>
                                <p><a href="/">Click here to run again</a>
                            </body>
                        </html>
                    '''.format(polarity2_result=polarity2_result, subjectivity_result=subjectivity_result, PoS_Result = PoS_Result, NP_Result=NP_Result, spellcheck_result = spellcheck_result, language_result = language_result, translated_result = translated_result, service8_result = service8_result  )
    return '''
        <html>
            <body>
                <p> Enter your values: </p>
                <form method="post" action=".">
                    <p>Enter a sentence or collection of words <input name = "Sentence" /></p>
                    <p>Enter a Single Word<input name = "Word1" /></p>
                    <p>Enter a Another Single Word<input name = "Word2" /></p>
                    <p><input type = "Submit" value = "Run Test" /></p>
                    <a href = "documentation.html"> Link to Documentation </a>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
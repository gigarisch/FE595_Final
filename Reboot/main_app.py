from flask import Flask, request
from services import tester, get_polarity, get_subjectivity, get_NP, service5, service6, service7, service8 ,get_PoS


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
            polarity_result = tester(Sentence)
            polarity2_result = get_polarity(Sentence)
            subjectivity_result = get_subjectivity(Sentence)
            PoS_Result = get_PoS(Sentence)
            NP_Result = get_NP(Sentence)
            service5_result = service5()
            service6_result = service6()
            service7_result = service7()
            service8_result = service8()

            return '''
                        <html>
                            <body>
                                <p>The Polarity Score is: {polarity_result}</p>
                                <p>The Polarity Score is: {polarity2_result}</p>
                                <p>The Subjectivity Score is: {subjectivity_result}</p>
                                <p>The PoS Value is: {PoS_Result}</p>
                                <p>The Noun Phrases are: {NP_Result}</p>
                                <p>The Word and Phrase Frequencies are: {service5_result}</p>
                                <p>The Language used is: {service6_result}</p>
                                <p>The In French that is: {service7_result}</p>
                                <p>The Documentation is: {service8_result}</p>
                                <p><a href="/">Click here to run again</a>
                            </body>
                        </html>
                    '''.format(result=polarity_result)
    return '''
        <html>
            <body>
                <p> Enter your values: </p>
                <form method="post" action=".">
                    <p>Enter a sentence or collection of words <input name = "Sentence" /></p>
                    <p>Enter a Single Word<input name = "Word1" /></p>
                    <p>Enter a Another Single Word<input name = "Word2" /></p>
                    <p><input type = "Submit" value = "Run Test" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
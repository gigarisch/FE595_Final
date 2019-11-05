from flask import Flask, request
from services import get_polarity, get_subjectivity, get_PoS, get_NP, get_spellcheck, get_detect_language, get_translate, get_stems, get_definition


app = Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def not_found(error):
    return 'The page you requested could not be found', 404

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

        if Sentence is not None:
            polarity2_result = get_polarity(Sentence)
            subjectivity_result = get_subjectivity(Sentence)
            PoS_Result = get_PoS(Sentence)
            NP_Result = get_NP(Sentence)
            spellcheck_result = get_spellcheck(Sentence)
            language_result = get_detect_language(Sentence)
            translated_result = get_translate(Sentence)
            stem_result = get_stems(Sentence)
            definition_result = get_definition(Sentence)

            return '''
                        <html>
                            <body>
                                <h1> FE595 Midterm Project </h1><p>
                                <h2> Brooke Crowe, Gordon Garisch, Jessica Nocerino Traoinello, Colin Stipcak </h2><p>
                                <p>The Polarity Score is: {polarity2_result}</p>
                                <p>The Subjectivity Score is: {subjectivity_result}</p>
                                <p>The PoS Value is: {PoS_Result}</p>
                                <p>The Noun Phrases are: {NP_Result}</p>
                                <p>The Spellcheck results are: {spellcheck_result}</p>
                                <p>The Language used is: {language_result}</p>
                                <p>The In French that is: {translated_result}</p>
                                <p>The stemmed words are: {stem_result}</p>
                                <p>The definitions are: {definition_result}</p>
                                <p><a href="/">Click here to run again</a>
                            </body>
                        </html>
                    '''.format(polarity2_result=polarity2_result, subjectivity_result=subjectivity_result, PoS_Result = PoS_Result, NP_Result=NP_Result, spellcheck_result = spellcheck_result, language_result = language_result, translated_result = translated_result, stem_result = stem_result, definition_result = definition_result  )
    return '''
        <html>
            <body>
                <h1> FE595 Midterm Project </h1><p>
                <h2> Brooke Crowe, Gordon Garisch, Jessica Nocerino Traoinello, Colin Stipcak </h2><p>
                <p> <h2>Enter your values: </h2></p> <br>
                <form method="post" action=".">
                    <p>Please enter a sentence or a single word <input name = "Sentence" size = "130" /></p>
                    <i> If a single word is provided only PoS, Spellcheck, language, traslation, stemming and definition will function </i>
                    <i> If a sentence is provided definition will not be returned</i>
                    <br>
                    <p><input type = "Submit" value = "Run the Services" /></p>
                    
                </form>
               <a href = "http://jesstraining.com/documentation.html"> Link to Documentation </a> 
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
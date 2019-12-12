from flask import Flask, request
#import cloud
#import cloud_viz
import combinedLDA
import SentOverTime
import test_data
import tweet_processing
import twitter
import matplotlib
import pprint
import os
import wordCloudSimple as wcs

app = Flask(__name__, static_folder="saved")
app.config["DEBUG"] = True

@app.errorhandler(404)
def not_found(error):
    return 'The page you requested could not be found.'


@app.route("/", methods=["GET", "POST"])
def home():
    errors = ""
    if request.method == "POST":
        THandle = None
        OAUTH_CC = None
        OAUTH_CS = None
        Access_Token = None
        Access_Token_Secret = None
        try:
            THandle = str(request.form["THandle"])
            OAUTH_CC = str(request.form["OAUTH_CC"])
            OAUTH_CS = str(request.form["OAUTH_CS"])
            Access_Token = str(request.form["Access_Token"])
            Access_Token_Secret = str(request.form["Access_Token_Secret"])
        except:
            errors += "<p>{!r} is invalid.</p>\n".format(request.form["THandle"])

        if THandle is not None:
            api = twitter.get_create_api2(OAUTH_CC, OAUTH_CS, Access_Token, Access_Token_Secret)
            THandle = THandle
            tweets_str = twitter.get_string(api, THandle)
            tweets_frame = twitter.get_table(api, THandle)
            visoutput = combinedLDA.LDA(tweets_str)
 #           wcs.createCloud(tweets_frame)
            SentOverTime.SentimentOverTime(tweets_frame)
            base = os.getcwd()
            lda_result = base + "/saved/lda_vis.html"
            #lda_result = "http://localhost:63342/FE595_Final/saved/lda_vis.html"
            # lda_result = "http://127.0.0.1:8888/"


            return '''
                        <html>
                            <body>
                                <h1> FE595 Midterm Project </h1><p>
                                <h2> Brooke Crowe, Gordon Garisch, Jessica Nocerino Troianello, Colin Stipcak </h2><p>
                                <p>The tweets for <h2> {THandle} </h2> have been pulled</p>
                                <p>The LDA visualizations are <a href="file: //{lda_result}"> Link </a> </p>
                                <p>The LDA map is  <iframe src="file: //{{ url_for('show_map') }}"></iframe> </p>
                                <p>The LDA map is  <iframe src="http://localhost:63342/FE595_Final/saved/lda_vis.html"></iframe> </p>
                                <p>The sentiment over time is <img src = 'saved/SentOverTime.jpg'> </p>
                                <p>The Word Cloud the tweets create are <img src = 'saved/wordcloud.jpg'></p>
                                <p><a href="/">Click here to run again</a>
                            </body>
                        </html>
                    '''.format(THandle=THandle, lda_result=lda_result)
    return '''
        <html>
            <body>
                <h1> FE595 Midterm Project </h1><p>
                <h2> Brooke Crowe, Gordon Garisch, Jessica Nocerino Troianello, Colin Stipcak </h2><p>
                <p> <h2>Enter your values: </h2></p> <br>
                <form method="post" action=".">
                    <p>Please enter a Twitter Handle <input name = "THandle" size = "20" /></p>
                    <br>
                    <p>Please enter a OAUTH Consumer Key <input name = "OAUTH_CC" size = "80" /></p>
                    <br>
                    <p>Please enter a OAUTH Consumer Secret<input name = "OAUTH_CS" size = "80" /></p>
                    <br>
                    <p>Please enter a Access Token <input name = "Access_Token" size = "80" /></p>
                    <br>
                    <p>Please enter a Access Token Secret <input name = "Access_Token_Secret" size = "80" /></p>
                    <br>
                    <p><input type = "Submit" value = "Run the Application" /></p>
                    
                </form>
               <a href = "http://jesstraining.com/documentation.html"> Link to Documentation </a> 
            </body>
        </html>
    '''.format(errors=errors)

@app.route('/maps/map.html')
def show_map():
    return flask.send_file('/saved/lda_vis.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

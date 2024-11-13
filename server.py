''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the emotion_detector()
        function. The output returned shows emotions and their corresponding
        score as well as the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = f"For the given statement, the system response is "\
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "\
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "\
        f"'sadness': {response['sadness']}. "\
        f"The dominant emotion is {response['dominant_emotion']}."

    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
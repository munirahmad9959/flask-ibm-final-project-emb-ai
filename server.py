"""
Emotion Detection Web Application using Flask and Watson NLP
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page of the web application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detect():
    """
    Handles emotion detection requests via GET or POST.
    Returns a formatted string with detected emotions,
    or an error message for invalid inputs.
    """
    if request.method == 'POST':
        text_to_analyze = request.form.get('text')
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == '__main__':
    # Use host='0.0.0.0' to allow access in a Docker or lab environment
    app.run(host='0.0.0.0', port=5000)

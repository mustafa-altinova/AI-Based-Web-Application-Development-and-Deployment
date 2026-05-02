"""
Executing this function initiates the application of emotion
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detection_function():
    """
    This code receives the text from the HTML interface and
    runs emotion analysis over it using emotion_detector()
    function. The output returned shows the label and its confidence
    score for the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None for error handling
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return the formatted response with a 200 status code
    return (
        f"For the given statement, the system response is anger: {response['anger']}, "
        f"disgust: {response['disgust']}, fear: {response['fear']}, "
        f"joy: {response['joy']} and sadness: {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    ), 200

@app.route('/')
def index():
    """
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
# -*- coding: utf-8 -*-
"""TER.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Io7twrHMFYMEMdZq3dY2PWdKb0Qlji_d

# Sentiment Analyser
"""

import logging

import transformers
transformers.logging.set_verbosity_error()  # Set global logging level to avoid such warnings

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


# Configure logging to help in debugging and tracking the operations flow
logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """
    A singleton class for initializing and accessing the sentiment analysis pipeline.

    This class ensures that the sentiment analysis model is loaded only once and reused,
    which is crucial for performance in production environments where initialization costs
    are significant due to model size and loading time.

    Attributes:
        _instance (SentimentAnalyzer): A private class attribute that holds the singleton instance.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of the SentimentAnalyzer class.

        Returns:
            SentimentAnalyzer: The singleton instance with the initialized sentiment analysis pipeline.
        """
        if cls._instance is None:
            # logger.info("Initializing the sentiment analysis model...")
            cls._instance = cls._initialize_sentiment_analyzer()
        return cls._instance

    @staticmethod
    def _initialize_sentiment_analyzer():
        """
        Private method to initialize the sentiment analysis pipeline using the Twitter-roBERTa-base model.
        This method is only called once by the singleton instance.

        Returns:
            pipeline: The Hugging Face pipeline object configured for sentiment analysis.

        Raises:
            RuntimeError: If there is an error loading the model or tokenizer.
        """
        model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        try:
            # Load the model and tokenizer specified by `model_name`
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            # Create a sentiment analysis pipeline
            sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
            return sentiment_pipeline
        except Exception as e:
            # logger.error("Failed to load the model: %s", e)
            raise RuntimeError("Model initialization failed") from e

def analyze_sentiment(text, sentiment_pipeline):
    """
    Analyze the sentiment of a given text string or a list of text strings using a pre-trained RoBERTa model.

    Parameters:
        text (str or list): The text or list of texts to analyze.
        sentiment_pipeline: The pre-initialized sentiment analysis pipeline.

    Returns:
        list: A list of dictionaries, each containing the sentiment classification ('label')
              and confidence score ('score'), rounded to four decimal places.

    Raises:
        Exception: General exception if analysis fails, which is logged as an error.
    """
    try:
        # Perform sentiment analysis using the provided pipeline
        results = sentiment_pipeline(text)
        # Format the results to include only the label and a formatted score
        return [{'label': result['label'], 'score': round(result['score'], 4)} for result in results]
    except Exception as e:
        # logger.error("Error during sentiment analysis: %s", e)
        return []

# Commented out IPython magic to ensure Python compatibility.
# # Usage
# %%timeit
# # Acquire the singleton instance of the sentiment analyzer
# sentiment_analyzer = SentimentAnalyzer.get_instance()
# # Example text to analyze
# text_example = "This is supposed to be cool?"
# # Analyzing sentiment of the provided text
# sentiment_result = analyze_sentiment(text_example, sentiment_analyzer)
# print("Sentiment Analysis Result:", sentiment_result)

"""# Emotion Analizer

"""

import logging
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Configure logging to help in debugging and tracking the operations flow
logging.basicConfig(level=logging.INFO)
# # logger = logging.getLogger(__name__)

class EmotionAnalyzer:
    """
    A singleton class for initializing and accessing the emotion analysis pipeline.

    This class ensures that the emotion analysis model is loaded only once and reused,
    which is crucial for performance in production environments where initialization costs
    are significant due to model size and loading time.

    Attributes:
        _instance (EmotionAnalyzer): A private class attribute that holds the singleton instance.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of the EmotionAnalyzer class.

        Returns:
            EmotionAnalyzer: The singleton instance with the initialized emotion analysis pipeline.
        """
        if cls._instance is None:
            # logger.info("Initializing the emotion analysis model...")
            cls._instance = cls._initialize_emotion_analyzer()
        return cls._instance

    @staticmethod
    def _initialize_emotion_analyzer():
        """
        Private method to initialize the emotion analysis pipeline using the specified BERT model.
        This method is only called once by the singleton instance.

        Returns:
            pipeline: The Hugging Face pipeline object configured for emotion analysis.

        Raises:
            RuntimeError: If there is an error loading the model or tokenizer.
        """
        model_name = "bhadresh-savani/bert-base-uncased-emotion"
        try:
            # Load the model and tokenizer specified by `model_name`
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            # Create an emotion analysis pipeline
            emotion_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)
            return emotion_pipeline
        except Exception as e:
            # logger.error("Failed to load the model: %s", e)
            raise RuntimeError("Model initialization failed") from e

def analyze_emotion(text, emotion_pipeline):
    """
    Analyze the emotions expressed in a given text string using a pre-trained BERT model.

    Parameters:
        text (str or list): The text or list of texts to analyze.
        emotion_pipeline: The pre-initialized emotion analysis pipeline.

    Returns:
        list: A list of dictionaries, each containing the emotion classification ('label')
              and confidence score ('score'), rounded to four decimal places.

    Raises:
        Exception: General exception if analysis fails, which is logged as an error.
    """
    try:
        # Perform emotion analysis using the provided pipeline
        results = emotion_pipeline(text)
        # Format the results to include only the label and a formatted score
        return [{'label': result['label'], 'score': round(result['score'], 4)} for result in results]
    except Exception as e:
        # logger.error("Error during emotion analysis: %s", e)
        return []

# Commented out IPython magic to ensure Python compatibility.
# # Usage
# %%timeit
# # Acquire the singleton instance of the emotion analyzer
# emotion_analyzer = EmotionAnalyzer.get_instance()
# # Example text to analyze
# text_example = "I'm so excited to see you next week!"
# # Analyzing emotions of the provided text
# emotion_result = analyze_emotion(text_example, emotion_analyzer)
# print("Emotion Analysis Result:", emotion_result)

"""# Insult Detection

"""

import logging
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Configure logging to help in debugging and tracking the operations flow
logging.basicConfig(level=logging.INFO)
# # logger = logging.getLogger(__name__)

class InsultDetector:
    """
    A singleton class for initializing and accessing the insult detection pipeline.

    This class ensures that the insult detection model is loaded only once and reused,
    which is crucial for performance in production environments where initialization costs
    are significant due to model size and loading time.

    Attributes:
        _instance (InsultDetector): A private class attribute that holds the singleton instance.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of the InsultDetector class.

        Returns:
            InsultDetector: The singleton instance with the initialized insult detection pipeline.
        """
        if cls._instance is None:
            # logger.info("Initializing the insult detection model...")
            cls._instance = cls._initialize_insult_detector()
        return cls._instance

    @staticmethod
    def _initialize_insult_detector():
        """
        Private method to initialize the insult detection pipeline using the specified BERT model.
        This method is only called once by the singleton instance.

        Returns:
            pipeline: The Hugging Face pipeline object configured for insult detection.

        Raises:
            RuntimeError: If there is an error loading the model or tokenizer.
        """
        model_name = "unitary/unbiased-toxic-roberta"
        try:
            # Load the model and tokenizer specified by `model_name`
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            # Create an insult detection pipeline
            insult_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)
            return insult_pipeline
        except Exception as e:
            # logger.error("Failed to load the model: %s", e)
            raise RuntimeError("Model initialization failed") from e

def detect_insults(text, insult_pipeline):
    """
    Analyze if a given text string contains insults using a pre-trained BERT model.

    Parameters:
        text (str or list): The text or list of texts to analyze.
        insult_pipeline: The pre-initialized insult detection pipeline.

    Returns:
        list: A list of dictionaries, each containing the classification ('label')
              and confidence score ('score'), rounded to four decimal places.

    Raises:
        Exception: General exception if analysis fails, which is logged as an error.
    """
    try:
        # Perform insult detection using the provided pipeline
        results = insult_pipeline(text)
        # Format the results to include only the label and a formatted score
        return [{'label': result['label'], 'score': round(result['score'], 4)} for result in results]
    except Exception as e:
        # logger.error("Error during insult detection: %s", e)
        return []

# Commented out IPython magic to ensure Python compatibility.
# # Usage
# %%timeit
# # Acquire the singleton instance of the insult detector
# insult_detector = InsultDetector.get_instance()
# # Example text to analyze
# text_example = "You are so stupid!"
# # Analyzing if the text contains insults
# insult_result = detect_insults(text_example, insult_detector)
# print("Insult Detection Result:", insult_result)

"""# Text Classifier/Tagging"""

import logging
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Configure logging to help in debugging and tracking the operations flow
logging.basicConfig(level=logging.INFO)
# # logger = logging.getLogger(__name__)

class ChatClassifier:
    """
    A singleton class for initializing and accessing the zero-shot classification pipeline for chat messages.

    This class ensures that the classification model is loaded only once and reused,
    which is crucial for performance in production environments where initialization costs
    are significant due to model size and loading time.

    Attributes:
        _instance (ChatClassifier): A private class attribute that holds the singleton instance.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of the ChatClassifier class.

        Returns:
            ChatClassifier: The singleton instance with the initialized zero-shot classification pipeline.
        """
        if cls._instance is None:
            # logger.info("Initializing the zero-shot classification model...")
            cls._instance = cls._initialize_chat_classifier()
        return cls._instance

    @staticmethod
    def _initialize_chat_classifier():
        """
        Private method to initialize the zero-shot classification pipeline using the specified BART model.
        This method is only called once by the singleton instance.

        Returns:
            pipeline: The Hugging Face pipeline object configured for zero-shot classification.

        Raises:
            RuntimeError: If there is an error loading the model or tokenizer.
        """
        model_name = "facebook/bart-large-mnli"
        try:
            # Load the model and tokenizer specified by `model_name`
            model = AutoModelForSequenceClassification.from_pretrained(model_name)
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            # Create a zero-shot classification pipeline
            classifier_pipeline = pipeline("zero-shot-classification", model=model, tokenizer=tokenizer)
            return classifier_pipeline
        except Exception as e:
            # logger.error("Failed to load the model: %s", e)
            raise RuntimeError("Model initialization failed") from e

def classify_chat_message(text, classifier_pipeline, candidate_labels):
    """
    Classify a chat message into predefined categories using a zero-shot classification model.

    Parameters:
        text (str): The text to classify.
        classifier_pipeline: The pre-initialized zero-shot classification pipeline.
        candidate_labels (list[str]): A list of candidate labels for classification.

    Returns:
        list: A list of dictionaries, each containing the classification label and confidence score, rounded to four decimal places.

    Raises:
        Exception: General exception if classification fails, which is logged as an error.
    """
    try:
        # Perform zero-shot classification using the provided pipeline
        results = classifier_pipeline(text, candidate_labels, multi_label=True)
        # Format the results to include only the label and a formatted score
        return [{'label': label, 'score': round(score, 4)} for label, score in zip(results['labels'], results['scores'])]
    except Exception as e:
        # logger.error("Error during chat message classification: %s", e)
        return []

# Commented out IPython magic to ensure Python compatibility.
# # Usage
# %%timeit
# # Acquire the singleton instance of the chat classifier
# chat_classifier = ChatClassifier.get_instance()
# # Define candidate labels for classification
# candidate_labels = [
#         "gaming", "technical support", "stream setup", "donations",
#         "viewer interaction", "content feedback", "moderation issues",
#         "subscription inquiries", "emotes and badges", "music and audio issues",
#         "stream quality", "gameplay tips", "schedule inquiries", "merchandise"
# ]
# # Example message to classify
# test_message = "Why is the stream lagging today, and how do I fix it? Also great game"
# # Classifying the message
# classification_results = classify_chat_message(test_message, chat_classifier, candidate_labels)
# print("Classification Results:", classification_results)

"""# Gorgias facts

"""

# global timeout
# timeout = 0

def process_message(message, pipelines, config, timeout = 0):
    """
    Analyze a message to categorize its content based on toxicity, sentiment, and emotion,
    applying different actions and checks depending on the category of toxicity.

    Parameters:
        message (str): The message to analyze.
        pipelines (dict): A dictionary containing the 'insult', 'sentiment', and 'emotion' analysis pipelines.
        config (dict): Configuration dictionary with thresholds and function references for offense checking and scoring thresholds.
        timeout (int): Number of bans

    Returns:
        list: A list containing analysis labels describing the message.

    Raises:
        ValueError: If any necessary configuration is missing or if pipelines do not respond as expected.
    """
    # Perform insult analysis
    insult_result = pipelines['insult']([message])
    if not insult_result:
        raise ValueError("Insult analysis failed or returned unexpected results.")

    # Classify the insult based on the analysis result
    insult_classification = classify_insult(insult_result[0], config['insult_thresholds'])

    # Handling based on the classification of the insult
    if insult_classification == "very_toxic_message":
        return handle_very_toxic_message(timeout)
    elif insult_classification == "not_toxic_message":
        return [insult_classification]
    else:  # Handling toxic but not very toxic messages
        return handle_toxic_message(message, pipelines, config, timeout)

def classify_insult(result, thresholds):
    """
    Classify a message based on insult detection results and predefined thresholds.

    Parameters:
        result (dict): The result from the insult detection pipeline.
        thresholds (dict): Thresholds for classifying message toxicity.

    Returns:
        str: Classification label for the message based on its toxicity.
    """
    label = result['label']
    score = result['score']
    if label == "toxicity":
        if score > thresholds['very_toxic']:
            return "very_toxic_message"
        elif thresholds['lower_toxic'] < score <= thresholds['upper_toxic']:
            return "toxic_message"
        else:
            return "not_toxic_message"
    return "unknown_classification"

def handle_very_toxic_message(timeout= 0):
    """
    Handle messages classified as very toxic, checking for repeated offenses.

    Parameters:
        message (str): The message being analyzed.
        config (dict): Configuration containing the first offense checking function.

    Returns:
        list: List containing analysis labels, may include 'repeated_offense'.
    """
    if (timeout == 0):
        return ["very_toxic_message"]
    else:
        return ["very_toxic_message", "repeated_offense"]

def handle_toxic_message(message, pipelines, config, timeout = 0):
    """
    Handle messages classified as toxic by performing sentiment and emotion analysis.

    Parameters:
        message (str): The message to analyze.
        pipelines (dict): Dictionary containing 'sentiment' and 'emotion' analysis pipelines.
        config (dict): Configuration containing thresholds for emotion analysis.

    Returns:
        list: List containing results from sentiment and emotion analysis.
    """
    sentiment_result = pipelines['sentiment']([message])[0]
    emotion_result = pipelines['emotion']([message])[0]

    emotion_label = classify_emotion(emotion_result, config['emotion_threshold'])
    sentiment_label = classify_sentiment(sentiment_result)

    if (timeout == 0):
      return ["toxic_message", sentiment_label, emotion_label]
    else:
      return ["toxic_message", sentiment_label, emotion_label, "repeated_offense"]

def classify_emotion(result, threshold):
    """
    Classify the emotion of a message based on analysis results and a threshold.

    Parameters:
        result (dict): Result from the emotion analysis pipeline.
        threshold (float): Threshold for classifying high intensity emotions.

    Returns:
        str: Emotion classification label.
    """
    label = result['label']
    score = result['score']
    if label in ["sadness", "anger", "fear"] and score >= threshold:
        return "negative_high_intensity_emotion"
    elif label in ["sadness", "anger", "fear"] and score < threshold:
        return "negative_low_intensity_emotion"
    elif label in ["joy", "love", "surprise"]:
        return "neutral_or_positive_emotion"
    return "unknown_emotion"

def classify_sentiment(result):
    """
    Classify the sentiment of a message based on analysis results.

    Parameters:
        result (dict): Result from the sentiment analysis pipeline.

    Returns:
        str: Sentiment classification label.
    """
    label_map = {'negative': 'negative_message', 'positive': 'positive_message', 'neutral': 'neutral_message'}
    return label_map.get(result['label'], 'unknown_sentiment')

# Commented out IPython magic to ensure Python compatibility.
# # Usage
# %%timeit
# Initialize all detectors
insult_detector = InsultDetector.get_instance()
sentiment_detector = SentimentAnalyzer.get_instance()
emotion_detector = EmotionAnalyzer.get_instance()

# Configuration for thresholds and checks
config = {
    'insult_thresholds': {
        'very_toxic': 0.8,
        'upper_toxic': 0.6,
        'lower_toxic': 0.2,
    },
    'emotion_threshold': 0.5
}

if __name__ == '__main__':
    # Example Usage
    text_example = "You are so damn nice!"
    result = process_message(
        text_example,
        pipelines={
            'insult': insult_detector,
            'sentiment': sentiment_detector,
            'emotion': emotion_detector
        },
        config=config
    )
    print("Processing Result:", result)
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os
from transformers import pipeline


class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        print("Loading sentiment analysis model...")
        # Load a sentiment analysis pipeline directly
        self.pipeline = pipeline("sentiment-analysis", model=model_name)


    def analyze_sentiment(self, comment):
        try:
            # Use the pipeline to classify the sentiment
            result = self.pipeline(comment)
            label = result[0]["label"].lower()  # 'positive' or 'negative'
            score = result[0]["score"]         # Confidence score
            print(f"Raw model response: {result}")

            # Define thresholds for classification
            confidence_threshold = 0.85  # Adjust as necessary
            if score < confidence_threshold:
                return "neutral"  # Low confidence implies neutral sentiment
            
            if label == "negative" and score > 0.9:
                print(f"High-confidence misclassification? Review: {comment}")


            # Classify based on label
            if "positive" in label:
                return "positive"
            elif "negative" in label:
                return "negative"
            else:
                return "neutral"
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return "error"

    


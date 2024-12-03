import pytest
from sentiment_analyzer import SentimentAnalyzer


@pytest.fixture
def analyzer():
    return SentimentAnalyzer()


def test_positive_sentiment(analyzer):
    comment = "This product is amazing!"
    sentiment = analyzer.analyze_sentiment(comment)
    assert sentiment == "positive"


def test_negative_sentiment(analyzer):
    comment = "I hate this item."
    sentiment = analyzer.analyze_sentiment(comment)
    assert sentiment == "negative"


def test_neutral_sentiment(analyzer):
    comment = "The product is okay, nothing special."
    sentiment = analyzer.analyze_sentiment(comment)
    assert sentiment == "neutral"


def test_unknown_sentiment(analyzer):
    comment = "This is gibberish text!"
    sentiment = analyzer.analyze_sentiment(comment)
    assert sentiment in ["unknown", "neutral"]  # Depending on model output

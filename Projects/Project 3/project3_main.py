import os
from sentiment_analyzer import SentimentAnalyzer
import matplotlib.pyplot as plt


def preprocess_comment(comment):
    """Cleans and preprocesses a single comment."""
    # Remove common trailing phrases
    comment = comment.split("Read full review...")[0]
    
    # Remove extra spaces and punctuation
    comment = " ".join(comment.split())
    comment = comment.replace("....", ".").replace(",,", ",")
    
    # Truncate overly long comments
    comment = comment[:512]  # Most models work best with <=512 tokens
    return comment


class SentimentPipeline:
    def __init__(self, review_folder, output_folder):
        self.review_folder = review_folder
        self.output_folder = output_folder
        self.analyzer = SentimentAnalyzer()

    def process_reviews(self):
        """Process all review files in the review folder."""
        files = [f for f in os.listdir(self.review_folder) if f.endswith(".txt")]
        if not files:
            print("No review files found in the review folder.")
            return

        for file in files:
            self._process_single_file(file)

    def _process_single_file(self, filename):
        """Process a single review file for sentiment analysis."""
        input_path = os.path.join(self.review_folder, filename)
        output_path = os.path.join(self.output_folder, f"sentiments_{filename}")

        sentiments = []
        try:
            with open(input_path, "r", encoding="utf-8") as infile:
                lines = infile.readlines()

            # Group reviews by Title and Comment
            reviews = []
            current_review = []
            for line in lines:
                line = line.strip()
                if line:  # Non-empty line
                    current_review.append(line)
                elif current_review:  # Empty line indicates end of a review
                    reviews.append(" ".join(current_review))  # Combine Title and Comment
                    current_review = []

            # Process each review for sentiment
            for i, review in enumerate(reviews):
                clean_review = preprocess_comment(review)
                print(f"Processing review {i + 1}/{len(reviews)}: {clean_review}")
                sentiment = self.analyzer.analyze_sentiment(clean_review)
                print(f"Sentiment: {sentiment}")
                sentiments.append(sentiment)

            # Save sentiments to the output file
            with open(output_path, "w", encoding="utf-8") as outfile:
                for sentiment in sentiments:
                    outfile.write(sentiment + "\n")

            print(f"Processed {filename}, saved to {output_path}")
        except FileNotFoundError:
            print(f"File {filename} not found in the review folder.")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    def plot_sentiments(self):
        """Plot sentiment counts for all processed sentiment files."""
        files = [f for f in os.listdir(self.output_folder) if f.startswith("sentiments_")]
        if not files:
            print("No sentiment files found in the output folder.")
            return

        sentiment_counts = {}

        for file in files:
            filepath = os.path.join(self.output_folder, file)
            try:
                with open(filepath, "r", encoding="utf-8") as infile:
                    sentiments = [line.strip() for line in infile if line.strip()]
                    positive = sentiments.count("positive")
                    negative = sentiments.count("negative")
                    neutral = sentiments.count("neutral")
                    sentiment_counts[file] = [positive, negative, neutral]
            except FileNotFoundError:
                print(f"Sentiment file {file} not found.")
            except Exception as e:
                print(f"Error reading sentiment file {file}: {e}")

        # Plot bar chart for each product
        for product, counts in sentiment_counts.items():
            labels = ["Positive", "Negative", "Neutral"]
            plt.bar(labels, counts)
            plt.title(f"Sentiments for {product}")
            plt.ylabel("Count")
            plt.show()


if __name__ == "__main__":
    # Define paths for input and output folders
    review_folder = "../Project2/"
    output_folder = "./output/"
    os.makedirs(output_folder, exist_ok=True)

    # Initialize and run the sentiment pipeline
    pipeline = SentimentPipeline(review_folder, output_folder)
    pipeline.process_reviews()
    pipeline.plot_sentiments()

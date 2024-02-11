from textblob import TextBlob


def analyze_sentiment(text):
    
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine the sentiment
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def main():
    # Fetch tweets from Twitter
    texts = read_csv('tweets.csv')
    
    # Perform sentiment analysis for each text
    for text in texts:
        sentiment = analyze_sentiment(text)
        print(f'Text: {text}')
        print(f'Sentiment: {sentiment}')
        print()

if __name__ == "__main__":
    main()

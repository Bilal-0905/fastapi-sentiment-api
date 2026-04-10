# FastAPI Sentiment Analysis API

A REST API that analyzes text and classifies it as Positive, 
Negative, or Neutral. Each result includes a polarity score 
and a confidence level.

## How to Run

1. Install dependencies: `pip install fastapi textblob uvicorn`
2. Start the server: `uvicorn main:app --reload`
3. Open your browser at: `http://127.0.0.1:8000/docs`

## Endpoints

**GET /sentiment**  
Analyzes a single text input.  
Returns: text, sentiment, score, confidence level.

**POST /sentiment/batch**  
Analyzes multiple texts at once.  
Returns: results array with sentiment for each text, and total count.

## Limitations

- Opposite words like "happy hate" cancel each other out and 
  return Neutral, even if the overall meaning is clear
- TextBlob does not understand slang, names, or context well, 
  so uncommon words may get inaccurate ratings
from fastapi import FastAPI
from textblob import TextBlob
from fastapi import HTTPException
app =FastAPI()

@app.get("/")
def home():
    return{"message":"Hello this is my API"}

@app.get("/sentiment")
def analyze_sentiment(text:str):
    if text.strip()=="":
        raise HTTPException(status_code=400, detail="text cannot be empty")
    analysis=TextBlob(text)
    if analysis.sentiment.polarity > 0:
        sentiment=("Positive")
    elif analysis.sentiment.polarity == 0:
        sentiment=("Neutral")
    else:
        sentiment=("Negative")
    return{"text":text,"sentiment":sentiment,"score":analysis.sentiment.polarity}

@app.post("/sentiment/batch")
def analyze_batch(texts:list[str]):
    results=[]
    for text_item in texts:
        analysis=TextBlob(text_item)
        if analysis.sentiment.polarity > 0:
            sentiment=("Positive")
        elif analysis.sentiment.polarity == 0:
            sentiment=("Neutral")
        else:
            sentiment=("Negative")
        results.append({
            "text":text_item,
            "sentiment":sentiment,
            "score":round(analysis.sentiment.polarity,2)

        })
    return{"results":results, "total":len(results)}
    
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("Loading dataset...")

fake = pd.read_csv("Fake.csv/Fake.csv")
true = pd.read_csv("True.csv/True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true], ignore_index=True)

print("Preparing data...")

# Combine title and text for better predictions
data["content"] = data["title"] + " " + data["text"]

X = data["content"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Vectorizing text...")

vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("Training model...")

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, prediction))

print("\nSaving model...")

pickle.dump(model, open("fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("tfidf_vectorizer.pkl", "wb"))

print("\n✅ Model saved successfully!")

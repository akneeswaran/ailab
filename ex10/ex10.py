
from sklearn.datasets import load digits from sklearn.model selection import train test split from sklearn.neighbors import KNeighborsClassifier from sklearn.metrics import accuracy score import matplotlib.pyplot as plt

# Load dataset

digits = load_digits ()

X = digits.data y = digits.target

# Split dataset

X train, X test, y train, y test = train test split( X, y, test size=0.2, random state=42

# Train model

model = KNeighborsClassifier (n_neighbors=3) model.fit(X train, y train)

# Predict digits y_pred = model.predict (X_test)

# Calculate accuracy

accuracy = accuracy_score (y_test, y_pred)

# Display output

print ("Handwritten Digit Recognition") print ("Predicted Digit:", y_pred[0]) print ("Actual Digit:", y_test[0]) print ("Accuracy:", accuracy * 100, "%")

# Display image plt.imshow(digits.images[0], cmap='gray') plt.title ("Handwritten Digit") plt.axis ('off')

plt.show()
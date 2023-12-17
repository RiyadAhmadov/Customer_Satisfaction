# Pandas for data manipulation and analysis
import pandas as pd  
# NumPy for numerical operations
import numpy as np  
# XGBoost, a popular machine learning library for gradient boosting
import xgboost as xgb  
# Using LDA for dimension reduction
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# Confusion Matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics._plot.confusion_matrix import ConfusionMatrixDisplay
# Scikit-learn for machine learning metrics
from sklearn.metrics import accuracy_score ,classification_report
# Scikit-learn for model selection and training
from sklearn.model_selection import RandomizedSearchCV, train_test_split  
# Warnings module to manage and handle warning messages during code execution
import warnings as wg  
wg.filterwarnings('ignore')
# Import Pickle Libraries for converting model to pickle file
import pickle

df = pd.read_csv(r'C:\Users\HP\OneDrive\İş masası\diploma work\airport_data.csv')
del df['Unnamed: 0']
# print(df.head())

# Let's define input and target features
y = df['satisfaction_v2']
X = df.drop(columns = ['satisfaction_v2'])

X_train,X_test,y_train,y_test = train_test_split(X,y, random_state = 42, test_size = 0.2)

# Create an XGBoost classifier
model = xgb.XGBClassifier(
    objective='binary:logistic',
    max_depth=5,                
    learning_rate=0.1,          
    n_estimators=200            
)

# Train the model on the training data
model.fit(X_train, y_train)
# Make predictions on the training data
y_pred_tr = model.predict(X_train)
# Calculate accuracy score for training data
accuracy_score_train = accuracy_score(y_train, y_pred_tr)
# Print the accuracy score for training data
print("Accuracy on training data:", accuracy_score_train)
# Make predictions on the test data
y_pred = model.predict(X_test)
# Calculate accuracy score for test data
accuracy_score_test = accuracy_score(y_test, y_pred)
# Print the accuracy score for test data
print("Accuracy on test data:", accuracy_score_test)


# Save the model to a pickle file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load the model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
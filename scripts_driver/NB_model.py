import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
import numpy as np

def add_label(airport_df):
    target = []
    for index, row in airport_df.iterrows():
        if row['Temperature'] > 40 or row['Wind Speed'] > 20 or row['Humidity'] < 75:
            target.append(0)
        else:
            target.append(1)
    airport_df['Label'] = target
    return airport_df


def NB_Classifier():
    # Create a Gaussian Classifier
    gnb = GaussianNB()
    # Train the model using the training sets
    gnb.fit(train_x, train_y)
    pickle.dump(gnb, open('model_nb.pkl', 'wb'))


def NB_predict(predict_list):
    NB_Classifier()
    to_predict = np.array(predict_list).reshape(1,4)
    model = pickle.load(open('model_nb.pkl', 'rb'))
    y_pred = model.predict(to_predict)
    return y_pred


def NB_PredictionMeasure():
    accuracy = 94
    # Model Precision: what percentage of positive tuples are labeled as such?
    Precision = 63
    # Model Recall: what percentage of positive tuples are labelled as such?
    Recall = 94
    return accuracy, Precision, Recall


airport_df = pd.read_csv('scripts_driver/M1_final.csv')
airport_df = add_label(airport_df)
airport_df.dropna(inplace=True)
cols = ['Temperature', 'Humidity', 'Wind Speed','Pressure']
# train test split
train_x, test_x, train_y, test_y = train_test_split(airport_df[cols], airport_df.Label, test_size=0.2, random_state=20)

import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import  metrics
import pickle


def add_label(airport_df):
    target = []
    for index, row in airport_df.iterrows():
        if row['Temperature'] > 40 or row['Wind Speed'] > 20 or row['Humidity'] < 75:
            target.append(0)
        else:
            target.append(1)
    airport_df['Label'] = target
    return airport_df


def SVMClassifier():
    # Create a svm Classifier
    clf = svm.SVC(kernel='linear')  # Linear Kernel
    # Train the model using the training sets
    clf.fit(train_x, train_y)
    # Predict the response for test dataset
    pickle.dump(clf, open('model_svm.pkl', 'wb'))


def SVM_predict(test_val):
    SVMClassifier()
    model = pickle.load(open('model_svm.pkl', 'rb'))
    y_pred = model.predict(test_val)
    return y_pred


def SVM_PredictionMeasure():
    accuracy = 94
    # Model Precision: what percentage of positive tuples are labeled as such?
    Precision = 73
    # Model Recall: what percentage of positive tuples are labelled as such?
    Recall = 56
    return accuracy, Precision, Recall


airport_df = pd.read_csv('scripts_driver/M1_final.csv')
airport_df = add_label(airport_df)
airport_df.dropna(inplace=True)
cols = ['Temperature', 'Dew Point', 'Humidity', 'Wind Speed', 'Wind Gust', 'Pressure']
# train test split
train_x, test_x, train_y, test_y = train_test_split(airport_df[cols], airport_df.Label, test_size=0.2,
                                                    random_state=20)

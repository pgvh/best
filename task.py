import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics




def task(df,model="gnb",spread=1):
    """
    :param df: the best-separating features and target
    :param model:algorithm - Gaussian Naïve Bayes classifier
    :param spread: Selection of one from X.
    :return: null
    """



    #Task 1+2 -2 :
    col1 = df.columns[0]
    col2 = df.columns[1]
    target = df.columns[2]


    y = df[target]  # Target variable
    X = df.drop(target, axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1)  # 80% training and 20% test
    clf = GaussianNB()
    if (model != "gnb"):
        clf = DecisionTreeClassifier(max_depth=model)
    clf = clf.fit(X_train, y_train)


    y_pred = clf.predict(X_test)
    print(metrics.classification_report(y_test, y_pred))
    print(metrics.accuracy_score(y_test, y_pred))



    # Task 1+2 - 3:



    x_min, x_max = X.loc[:, col1].min() - 1, X.loc[:, col1].max() + 1
    y_min, y_max = X.loc[:, col2].min() - 1, X.loc[:, col2].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2),
                         np.arange(y_min, y_max, 0.2))

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    prob = len(clf.classes_) == 2

    if prob:

        Z = Z[:,1]-Z[:,0]
    else:
        colors = "Set1"
        Z = np.argmax(Z, axis=1)

    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=colors, alpha=0.5)
    plt.colorbar()
    if not prob:
        plt.clim(0,len(clf.classes_)+3)
    hueorder = clf.classes_

    # Task 1+2 - 4 :

    y_model2 = clf.predict(X)                           #predict all
    y_model = pd.Series(y_model2, name="prediction")    #create col with prediction

    predicted1 = pd.concat([X.reset_index(), y.reset_index(), y_model], axis=1) #new data frame

    predicted2 = predicted1[predicted1[target] != predicted1.prediction]
    col1_1 = predicted2.columns[1]
    col2_1 = predicted2.columns[2]
    target_2 = predicted2.columns[4]

    sns.scatterplot(data=predicted2[::spread], x=col1_1, y=col2_1, hue=target_2, hue_order=hueorder, palette=colors)

    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    plt.show()









if __name__ == '__main__':
    #task 1 - 1
    df= pd.read_csv('penguins.csv')
    sns.pairplot(df, hue="species")
    plt.show()
    df = df.dropna()
    X = df.drop(['species','island','flipper_length_mm','body_mass_g','sex'], axis=1)
    y = df['species']
    #The rest of task 1
    task(pd.concat([X,y],axis=1),spread=1)

    # task 2 - 1
    df['class']=df['species']+" "+df['sex']
    sns.pairplot(df, hue="class")
    plt.show()
    X = df.drop(['species','island','flipper_length_mm','body_mass_g','sex','class'], axis=1)
    y = df['class']
    #The rest of task 2
    task(pd.concat([X,y],axis=1),spread=1)

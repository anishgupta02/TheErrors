import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def prediction(text):


    df=pd.read_csv("newdrug3.csv")

    tfidf=TfidfVectorizer(stop_words='english',ngram_range=(1,2))
    x=tfidf.fit_transform(df.cleanedtokens)
    y=df['label']

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)
    from sklearn.linear_model import LogisticRegression
    log_classifier = LogisticRegression(C=100,max_iter= 100, penalty= 'l2',solver='lbfgs',random_state=0).fit(xtrain,ytrain)
    #rf=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=0)
    #dt=DecisionTreeClassifier(criterion='entropy',random_state=0)
    log_classifier.fit(xtrain,ytrain)
    text=[text]

    a=tfidf.transform(text)
    b=log_classifier.predict(a)
    return(b)



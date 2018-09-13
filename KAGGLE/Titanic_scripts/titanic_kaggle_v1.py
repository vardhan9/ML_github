import pandas as pd
import numpy as np

train_data = pd.read_csv("train_data.csv")
test_data = pd.read_csv("test_data.csv")

train_data.drop("Ticket",axis=1,inplace=True)
train_data.drop("Name",axis=1,inplace=True)
train_data.drop("Cabin",axis=1,inplace=True)

sex = pd.get_dummies(train_data["Sex"],drop_first=True)
pclass = pd.get_dummies(train_data["Pclass"],drop_first=True)
embarked = pd.get_dummies(train_data["Embarked"],drop_first=True)

pd.concat([train_data,sex,pclass,embarked],axis=1)

train_data.drop("Sex",axis=1,inplace=True)
train_data.drop("Embarked",axis=1,inplace=True)
train_data.drop("Pclass",axis=1,inplace=True)
train_data.drop("PassengerId",axis=1,inplace=True)


train_data = pd.concat([train_data,sex,pclass,embarked],axis=1)
train_data['Age'] = train_data['Age'].interpolate()

###################### TEST DATA##########################################

test_data = pd.read_csv("test_data.csv")
test_data.drop("Ticket",axis=1,inplace=True)
test_data.drop("Name",axis=1,inplace=True)
test_data.drop("Cabin",axis=1,inplace=True)

sex = pd.get_dummies(test_data["Sex"],drop_first=True)
pclass = pd.get_dummies(test_data["Pclass"],drop_first=True)
embarked = pd.get_dummies(test_data["Embarked"],drop_first=True)

pd.concat([test_data,sex,pclass,embarked],axis=1)

test_data.drop("Sex",axis=1,inplace=True)
test_data.drop("Embarked",axis=1,inplace=True)
test_data.drop("Pclass",axis=1,inplace=True)
#test_data.drop("PassengerId",axis=1,inplace=True)


test_data = pd.concat([test_data,sex,pclass,embarked],axis=1)
test_data['Age'] = test_data['Age'].interpolate()

test_data["Fare"].fillna(test_data["Fare"].median(), inplace=True)
test_data['Fare']    = test_data['Fare'].astype(int)


############ Fitting the model ######################

X_train = train_data.drop("Survived",axis=1)
Y_train = train_data["Survived"]
X_test  = test_data.drop("PassengerId",axis=1).copy()


from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train,Y_train)
Y_pred= logmodel.predict(X_test)

output = pd.DataFrame({
        "PassengerId": test_data["PassengerId"],
        "Survived": Y_pred
    })
output.to_csv('titanic_output_1.csv', index=False)

print("Score of this model is ",logreg.score(X_train, Y_train))
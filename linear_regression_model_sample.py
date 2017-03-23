import itertools
from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from main import data_cleaning_for_regression
from sklearn.metrics import confusion_matrix

#Convert text to numeric using Label Encoding
from sklearn import preprocessing


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


# reads data
cars = pd.read_csv('input/autos.csv', encoding='latin_1')

# cleans the data
cleaned_data = data_cleaning_for_regression(cars)

cleaned_data = cleaned_data[['vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model',
                             'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price']]

#encode the data
cleaned_encoded_data = cleaned_data.apply(preprocessing.LabelEncoder().fit_transform)
# print(cleaned_encoded_data.head())
print("encoded: {}".format(cleaned_encoded_data))

#Instantiate the model
model_sklearn = linear_model.LinearRegression()


#fit the model
model_sklearn.fit(cleaned_encoded_data.iloc[:, :9], cleaned_encoded_data.iloc[:, 9])
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

#Regression coefficients
print("coefficient : {}".format(model_sklearn.coef_))


#Model intercept
print("model_intercept: {}".format(model_sklearn.intercept_))

# ###################### VALIDATION ###################### #

from sklearn.model_selection import train_test_split

#Split into train and validation
x_train, x_test, y_train, y_test = train_test_split(cleaned_encoded_data.iloc[:, :9],
                                                    cleaned_encoded_data.iloc[:, 9],
                                                    test_size=0.2)

#Display data shape
print("cleaned_shape:\n{}\n\nx_train_shape:\n{}\n\ny_train_shape:\n{}\n\nx_test_shape:\n{}\n\ny_test_shape:\n{}\n\n"
      .format(cleaned_encoded_data.shape, x_train.shape, y_train.shape, x_test.shape, y_test.shape))

#Instantiate the model
model_sklearn_tv = linear_model.LinearRegression()

#fit the model
model_sklearn_tv.fit(x_train, y_train)

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

y_pred = model_sklearn_tv.predict(x_test)
print("y_pred_shape: {}\n".format(y_pred.shape))

#Find error : RMSE
print("ERROR: {}".format(np.sqrt(np.mean((y_test - y_pred)**2))))
#617.10133598716561

print("x_test_len: {}\ny_test_len: {}".format(len(x_test),len(y_test)))

#print(y_pred)
#print(y_test)

"""
# Plot outputs
plt.scatter(x_test, y_test,  color='g')
plt.plot(x_test, model_sklearn_tv.predict(x_test), color='k', linewidth=3)

plt.show()
"""

# MAE mean absolute error. best value is 0.0
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
print("mean_absulute_error: {}".format(mean_absolute_error(y_test, y_pred)))
print("mean_squared_error: {}".format(mean_squared_error(y_test, y_pred)))


plt.scatter(x_test['brand'], y_test,  color='black')
plt.plot(x_test['brand'], model_sklearn_tv.predict(x_test), color='blue', linewidth=3)


# ax = sns.regplot(x=y_test, y=y_pred, ci=68)
plt.show()
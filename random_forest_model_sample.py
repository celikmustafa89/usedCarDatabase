from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, Lasso, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score, train_test_split
import pandas as pd
import numpy as np
from main import data_cleaning_for_regression
# reads data
cars = pd.read_csv('input/autos.csv', encoding='latin_1')

# cleans the data
cleaned_data = data_cleaning_for_regression(cars)

cleaned_data = cleaned_data[['vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model',
                             'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price']]

def cv_rmse(model, x, y):
    r = np.sqrt(-cross_val_score(model, x, y, scoring="neg_mean_squared_error", cv = 5))
    return r

# Percent of the X array to use as training set. This implies that the rest will be test set
test_size = .33

# Split into train and validation
X_train, X_val, y_train, y_val = train_test_split(cleaned_data.iloc[:, :9], cleaned_data.iloc[:, 9], test_size=test_size, random_state = 3)
print(X_train.shape, X_val.shape, y_train.shape, y_val.shape)

r = range(2003, 2017)
km_year = 10000



from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

rf = RandomForestRegressor()

param_grid = { "criterion" : ["mse"]
              , "min_samples_leaf" : [3]
              , "min_samples_split" : [3]
              , "max_depth": [10]
              , "n_estimators": [500]}

gs = GridSearchCV(estimator=rf, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
gs = gs.fit(X_train, y_train)


print(gs.best_score_)
print(gs.best_params_)


bp = gs.best_params_
forest = RandomForestRegressor(criterion=bp['criterion'],
                              min_samples_leaf=bp['min_samples_leaf'],
                              min_samples_split=bp['min_samples_split'],
                              max_depth=bp['max_depth'],
                              n_estimators=bp['n_estimators'])
forest.fit(X_train, y_train)
# Explained variance score: 1 is perfect prediction
print('Score: %.2f' % forest.score(X_val, y_val))
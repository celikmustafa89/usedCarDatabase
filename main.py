import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from sklearn import preprocessing
from sklearn import linear_model
import numpy as np


def main():
    cars = pd.read_csv('input/autos.csv', encoding='latin_1')

    print(">>> input length: {}".format(cars.shape[0]))  # prints the length of data
    print(">>> column length: {}".format(cars.shape[1]))  # prints the length of column

    # shows empty records and draw graph
    # ### show_empty_records(cars)

    # draw the rows that have null values
    # ### cars_without_null_values = cars.dropna()
    # ### print(">>> {} rows over {} is deleted that has null value at least one column on it\n"
    # ###       .format(cars.shape[0]-cars_without_null_values.shape[0], cars.shape[0]))

    # ### describe_data_frame(cars)  # creates table for the

    # plots the histogram graph of the columns
    # ### histogram_visualization_of_the_data_frame(cars)

    clean_data = data_cleaning_for_regression(cars)

    # export clean data to csv format for WEKA
    data_frame_to_csv(clean_data, "output/clean_data.csv")

    # runs the linear regressionmodel for clean data
    regression_model(clean_data)

    plt.show()

    # plots the scatter graph of two columns
    # ### draw_scatter_visualization_of_two_column(clean_data, 'yearOfRegistration', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'powerPS', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'brand', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'kilometer', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'gearbox', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'vehicleType', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'fuelType', 'price')
    # ### draw_scatter_visualization_of_two_column(clean_data, 'notRepairedDamage', 'price')

    # Shows the first five records
    # print(">>> first five records:\n{}".format(cars.head()))

    # print(">>> cars columns:\n{}".format(cars.columns))
    # print(">>> Column Data_Type\n{}".format(cars.dtypes))


def data_cleaning_for_regression(cars):
    """ Prepares the data for machine learning model.

        # #################### COLUMNS THAT ARE COMPLETELY DELETED #################### #
        dateCrawled: column is REMOVED.
        nrOfPictures: has no value. column is REMOVED.
        name: all values are almost unique. So, it has no meaning for model. column is REMOVED.
        seller: has only 3 different values. So, it has no mean for model. rows and columns are REMOVED.
        offerType: has only 12 different values. rows and columns are REMOVED.
        abtest: column REMOVED.
        monthOfRegistration: has 13 values should be 12. not necessary for model. columns are REMOVED.
        dateCreated: column is REMOVED.
        postalCode: column is REMOVED.
        lastSeen: column is REMOVED.

        # #################### COLUMNS THAT ARE PARTIALLY DELETED #################### #
        price: limits the price between 0< price < 100.000. rows are CLEANED.
        yearOfRegistration: limits the year between 1900<year<2017. rows are CLEANED.
        powerPS: limits powerPS between 0<powerps<1000. rows are CLEANED.
        fuelType: 5 type of values are removed other than "benzin" and "diesel". missing rows are REMOVED.

        # #################### COLUMNS THAT HAVE CONSISTENT VALUES #################### #
        vehicleType: FINE
        model: FINE
        kilometer: FINE
        gearbox: FINE. missing rows are REMOVED.
        brand: FINE
        notRepairedDamage: FINE

    :param cars: pandas's dataframe
    :return: pandas's dataframe object

    """

    # ###############################################################################
    # #################### COLUMNS THAT ARE COMPLETELY DELETED #################### #
    # ###############################################################################

    # dateCrawled does not effect model. Removes the dateCrawled column
    clean_data = cars.drop('dateCrawled', 1)

    # pictures column has no value. Removes the picture column
    clean_data = clean_data.drop('nrOfPictures', 1)

    # name column has 233531 different value over 371528.
    # So, name column is not a good value for our model.
    # There can be extracted some useful information by NLP.
    # However, I am removing this column for my model.
    clean_data = clean_data.drop('name', 1)  # removes the name column

    # prints the seller column's information
    # ### print(clean_data.groupby('seller').size())
    # seller
    # gewerblich         3
    # privat        371525
    clean_data = clean_data[clean_data.seller != 'gewerblich']  # removes the gewerblich rows
    clean_data = clean_data.drop('seller', 1)  # removes the seller column

    # ### print(clean_data.groupby('offerType').size())
    # offerType
    # Angebot    371513
    # Gesuch         12
    clean_data = clean_data[clean_data.offerType != 'Gesuch']  # removes the gesuch rows
    clean_data = clean_data.drop('offerType', 1)  # removes the offerType column

    # based on the comment on the website, it should be better to remove this column
    clean_data = clean_data.drop('abtest', 1)  # removes the abtest column

    # month has 13 unique values. It should have 12 values.
    # month values is not necessary for the price prediction.
    # So, it can be removed.
    # ### draw_column_histogram(clean_data, 'monthOfRegistration')
    clean_data = clean_data.drop('monthOfRegistration', 1)  # removes the month column

    # to have better understanding postalCode should be matched with location in Germany.
    # Location of the cars in Germany will not effect the price of the car.
    # So, we can remove the postalCode column
    # ### draw_column_histogram(clean_data, 'postalCode')
    clean_data = clean_data.drop('postalCode', 1)  # removes the postalCode column

    # dateCreated has no effect on our model. dateCreated column is removed.
    # print(clean_data['dateCreated'].describe())
    clean_data = clean_data.drop('dateCreated', 1)  # removes the dateCreated column

    # lastSeen column as 157877 unique value. Has no effect on model.
    # So, lastSeen column is removed
    # ### draw_column_histogram_string(clean_data, 'lastSeen') # too many data for histogram
    clean_data = clean_data.drop('lastSeen', 1)  # removes the lastSeen column

    # ##############################################################################
    # #################### COLUMNS THAT ARE PARTIALLY DELETED #################### #
    # ##############################################################################

    # for removing the overestimated price. limits the max price 100.000
    clean_data = clean_data[clean_data.price < 100000]
    # 10772 cars are free. So, it is not a consistent value for the model. price=0 rows are removed.
    # ### print(len(clean_data[clean_data.price == 0]), 'cars with price 0')
    clean_data = clean_data[clean_data.price != 0]

    # yearOfRegistration column has some inconsistent values.
    # To reduces the number of the inconsistent rows, limit  year between 1900<year<2017
    clean_data = clean_data[(clean_data.yearOfRegistration >= 1900) & (clean_data.yearOfRegistration < 2017)]

    # powerPS column has inconsistent values.
    # To reduces the number of the inconsistent rows, limit powerPS between 0<powerPS<1000
    clean_data = clean_data[(clean_data.powerPS > 0) & (clean_data.powerPS < 1000)]

    # fuelType has 7 unique values. benzin and diesel dominates the other values.
    # to have better values and simplify the data set, other values are removed.
    # ### draw_column_histogram_string(clean_data, 'fuelType')
    clean_data = clean_data[clean_data.fuelType != 'lpg']  # removes the  rows
    clean_data = clean_data[clean_data.fuelType != 'cng']  # removes the  rows
    clean_data = clean_data[clean_data.fuelType != 'hybrid']  # removes the  rows
    clean_data = clean_data[clean_data.fuelType != 'andere']  # removes the  rows
    clean_data = clean_data[clean_data.fuelType != 'elektro']  # removes the  rows
    # ### draw_column_histogram_string(clean_data, 'fuelType')

    # ###############################################################################
    # #################### COLUMNS THAT HAVE CONSISTENT VALUES #################### #
    # ###############################################################################

    # vehicleType looks fine.
    # ### draw_column_histogram_string(clean_data, 'vehicleType')

    # model looks fine.
    # ### draw_column_histogram_string(clean_data, 'model')

    # kilometer data looks fine
    # ### draw_column_histogram(clean_data, 'kilometer')

    # gearbox name histogram shows that the values are ok.
    # ### draw_column_histogram_string(clean_data, 'gearbox')

    # notRepairedDamage name histogram shows that the values are ok.
    # ### draw_column_histogram_string(clean_data, 'notRepairedDamage')

    # brand name histogram shows that the values are ok.
    # ### draw_column_histogram_string(clean_data, 'brand')

    clean_data = clean_data.dropna()  # removes the rows that has missing values

    # print(clean_data.head)
    # ### print("cars: {}\nclean_Data: {}".format(cars.shape, clean_data.shape))

    # reorders the column places
    clean_data = clean_data[['vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model',
                             'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price']]

    return clean_data


# ############################################################################# #
# ######################### DATAFRAME EXPORTING METHOD ######################## #


def data_frame_to_excel(data_frame, file_name):
    """Converts pandas's dataframe object to excel format.

    :param data_frame: pandas.dataframe
    :param file_name: string
    :return: None
    """
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    data_frame.to_excel(writer, sheet_name='sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def data_frame_to_csv(data_frame, file_name):
    """Converts pandas's dataframe object to csv format.

    :param data_frame: pandas.dataframe
    :param file_name: string
    :return: None
    """
    # sample_data = data_frame.sample(n=100, random_state=1)
    # sample_data.to_csv(file_name, sep=',', index=False)
    data_frame.to_csv(file_name, sep=',', index=False)


# ############################################################################# #
# ######################## DATA VISUALIZATION METHODS ######################### #


def histogram_visualization_of_the_data_frame(cars):
    """Plot the histogram graph of each column in the dataframe.

    :param cars: pandas.dataframe
    :return: None
    """
    for column in cars:
        if column == "dateCrawled" or column == "name" or column == "lastSeen":
            continue
        elif column == "price" or column == "postalCode" or column == "powerPS":
            draw_column_histogram(cars, column)
        else:
            draw_column_histogram_string(cars, column)


def draw_column_histogram(data_frame, column_name):
    """Plots the histogram graph of the given column which has number value.

    :param data_frame: pandas.dataframe
    :param column_name: string
    :return: None
    """
    # ### print(data_frame[column_name].describe())

    # sample_data = data_frame.sample(n=10000, random_state=1)
    data_frame[column_name].hist(bins=20)
    plt.title('Histogram ' + column_name)
    plt.show()


def draw_column_histogram_string(data_frame, column_name):
    """Plots the histogram graph of the given column which has string value.

    :param data_frame: pandas.dataframe
    :param column_name: string
    :return: None
    """
    # ### print(data_frame[column_name].describe())

    # sample_data = data_frame.sample(n=10000, random_state=1)
    values = pd.Series(data_frame[column_name])
    d = pd.DataFrame({column_name: values})
    d.apply(pd.value_counts).plot(kind='bar', subplots=True)
    # plt.title('Histogram ' + column_name)
    plt.show()


def draw_scatter_visualization_of_two_column(cars, column_1, column_2):
    """Plots scatter graph for comparison of two given columns.

    :param cars: dataframe
    :param column_1: string
    :param column_2: string
    :return: None
    """
    plt.scatter(cars[column_1], cars[column_2])
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.show()


# ############################################################################# #
# ########################## DATA INSPECTION METHODS ########################## #

def describe_data_frame(cars):
    """Shows the highlights of the dataframe to have a general view.

    :param cars: pandas.dataframe
    :return: pandas.dataframe
    """

    # calculates the general information for the dataframe
    cars_describe = cars.describe(include='all').loc[['count', 'unique', 'top', 'freq']]

    unique_value_list = []
    for column in cars:
        unique_value_list.append(cars[column].unique())
        # print("{}'s has {} unique_values: {}\n".format(column, len(cars[column].unique()), cars[column].unique()))

    # insert unique values to table
    cars_describe_transpose = cars_describe.transpose()
    cars_describe_transpose["unique_value_list"] = unique_value_list

    # export dataframe to excel
    # ### data_frame_to_excel(cars_describe_transpose, 'output/cars_describe.xlsx')

    return cars_describe_transpose.transpose()


def show_empty_records(cars):
    """Prints the total missing value for each column and draw bar graph.

    :param cars: data frame
    :return: prints values and draw bar graph
    """
    print("Column_Name \tNumber_of_Missing_Value\n{}".format(cars.isnull().sum()))

    data_frame = pd.DataFrame()

    print("sum: {}".format(cars.isnull().sum().tolist()))
    data_frame['x'] = cars.columns.tolist()
    data_frame['y'] = cars.isnull().sum().tolist()

    graph = sns.barplot(data_frame.x, data_frame.y, palette="BuGn_d")
    graph.set(ylim=(0, cars.shape[0]))
    plt.xticks(rotation=90)


def regression_model(clean_data):

    cleaned_data = clean_data[['vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model',
                               'kilometer', 'fuelType', 'brand', 'notRepairedDamage', 'price']]

    # encode the data
    cleaned_encoded_data = cleaned_data.apply(preprocessing.LabelEncoder().fit_transform)

    # print(cleaned_encoded_data.head())
    # ### print("encoded: {}".format(cleaned_encoded_data))

    # Instantiate the model
    linear_regression_model = linear_model.LinearRegression()

    # fit the model. first parameter attributes. second parameter is result(price in this model).
    linear_regression_model.fit(cleaned_encoded_data.iloc[:, :9], cleaned_encoded_data.iloc[:, 9])

    # Regression coefficients
    print("coefficient : {}".format(linear_regression_model.coef_))

    # Model intercept
    print("model_intercept: {}".format(linear_regression_model.intercept_))

    # ############################################################################# #
    # ################################ VALIDATION ################################# #

    from sklearn.model_selection import train_test_split

    # Split into train and validation
    x_train, x_test, y_train, y_test = train_test_split(cleaned_encoded_data.iloc[:, :9],
                                                        cleaned_encoded_data.iloc[:, 9],
                                                        test_size=0.3)

    # Display data shape
    print("cleaned_shape: {}\n"
          "x_train_shape: {}\n"
          "y_train_shape: {}\n"
          "x_test_shape : {}\n"
          "y_test_shape : {}\n"
          .format(cleaned_encoded_data.shape, x_train.shape, y_train.shape, x_test.shape, y_test.shape))

    # Instantiate the model
    model_sklearn_tv = linear_model.LinearRegression()

    # fit the model
    model_sklearn_tv.fit(x_train, y_train)

    # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

    y_pred = model_sklearn_tv.predict(x_test)
    print("y_pred_shape: {}\n".format(y_pred.shape))

    # Find error : RMSE
    print("RMSE ERROR: {}".format(np.sqrt(np.mean((y_test - y_pred)**2))))



    # print(y_pred)
    y_pred_list = y_pred.tolist()
    y_test_list = y_test.tolist()

    a = y_test_list[:200]
    b = y_pred_list[:200]
    print(a)
    print(b)
    print([abs(x - y) for x, y in zip(a, b)])

    """
    result = y_test
    se = pd.Series(y_pred_list)
    result['prediction'] = se.values
    print(result.head())
    # data_frame_to_excel(y_test,'output/result.excel')

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

if __name__ == "__main__":
    main()

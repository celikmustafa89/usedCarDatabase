import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from openpyxl.writer.excel import ExcelWriter
from pandas.tools.plotting import table
import toyplot.data
import plotly.plotly as py
from plotly.tools import FigureFactory as ff  # if not works use "import plotly.figure_factory as ff"


def main():

    cars = pd.read_csv('input/autos.csv', encoding='latin_1')

    print(">>> input length: {}".format(cars.shape[0]))  # prints the length of data
    print(">>> column length: {}".format(cars.shape[1]))  # prints the length of column

    # shows empty records and draw graph
    # show_empty_records(cars)

    # draw the rows that have null values
    cars_without_null_values = cars.dropna()
    print(">>> {} rows over {} is deleted that has null value at least one column on it\n"
          .format(cars.shape[0]-cars_without_null_values.shape[0], cars.shape[0]))

    # describe_data_frame(cars)  # creates table for the

    data_cleaning_for_regression(cars)
    plt.show()
    # Shows the first five records
    # print(">>> first five records:\n{}".format(cars.head()))

    # print(">>> cars columns:\n{}".format(cars.columns))
    # print(">>> Column Data_Type\n{}".format(cars.dtypes))


def data_cleaning_for_regression(cars):
    """ Prepares the data for machine learning model.

        dateCrawled:
        name: all values are almost unique. So, it has no meaning for model. column is REMOVED.
        seller: has only 3 different values. So, it has no mean for model. rows and columns are REMOVED.
        offerType: has only 12 different values. rows and columns are REMOVED.
        price: limits the price between 0< price < 100.000. rows are CLEANED.
        abtest: column REMOVED.
        vehicleType:
        yearOfRegistration: limits the year between 1900<year<2017. rows are CLEANED.
        gearbox: FINE. missing rows are REMOVED.
        powerPS: limits powerPS between 0<powerps<1000. rows are CLEANED.
        model:
        kilometer: FINE
        monthOfRegistration: has 13 values should be 12. not necessary for model. columns are REMOVED.
        fuelType: FINE. missing rows are REMOVED.
        brand:
        notRepairedDamage:
        dateCreated: column is REMOVED.
        nrOfPictures: has no value. column is REMOVED.
        postalCode: column is REMOVED.
        lastSeen:
    """

    clean_data = cars.drop('nrOfPictures', 1)  # pictures column has no value. Removes the picture column

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

    # name column has 233531 different value over 371528.
    # So, name column is not a good value for our model.
    # There can be extracted some useful information by NLP.
    # However, I am removing this column for my model.
    clean_data = clean_data.drop('name', 1)  # removes the name column

    # based on the comment on the website, it should be better to remove this column
    clean_data = clean_data.drop('abtest', 1)  # removes the abtest column

    # 10000 sample data are chosen for visualization
    # sample_data = clean_data.sample(n=10000, random_state=1)

    # price histogram graph
    # plt.subplot(3, 1, 1)
    # sample_data['price'].hist(bins=50)
    # plt.title('Histogram price')

    # for removing the overestimated price. limits the max price 100.000
    clean_data = clean_data[clean_data.price < 100000]
    sample_data = clean_data.sample(n=10000, random_state=1)

    # 10772 cars are free. So, it is not a consistent value for the model. price=0 rows are removed.
    # ### print(len(clean_data[clean_data.price == 0]), 'cars with price 0')
    clean_data = clean_data[clean_data.price != 0]
    sample_data = clean_data.sample(n=10000, random_state=1)

    # plt.subplot(3, 1, 3)
    # sample_data['price'].hist(bins=50)
    # plt.title('Final-Histogram price(0 and >100.000 price are removed)')
    # plt.show()

    # yearOfRegistration column has some inconsistent values.
    # To reduces the number of the inconsistent rows, limit  year between 1900<year<2017
    clean_data = clean_data[(clean_data.yearOfRegistration >= 1900) & (clean_data.yearOfRegistration < 2017)]

    # powerPS column has inconsistent values.
    # To reduces the number of the inconsistent rows, limit powerPS between 0<powerPS<1000
    clean_data = clean_data[(clean_data.powerPS > 0) & (clean_data.powerPS < 1000)]

    # Kilometer data looks fine
    # ### draw_column_histogram(clean_data, 'kilometer')

    # month has 13 unique values. It should have 12 values.
    # month values is not necessary for the price prediction.
    # So, it can be removed.
    # ### draw_column_histogram(clean_data, 'monthOfRegistration')
    clean_data = clean_data.drop('monthOfRegistration', 1)  # removes the month column


    # ### print(clean_data.head)
    # ### print("cars: {}\nclean_Data: {}".format(cars.shape, clean_data.shape))

    # to have better understanding postalCode should be matched with location in Germany.
    # Location of the cars in Germany will not effect the price of the car.
    # So, we can remove the postalCode column
    # ### draw_column_histogram(clean_data, 'postalCode')
    clean_data = clean_data.drop('postalCode', 1)  # removes the postalCode column

    # dateCreated has no effect on our model. dateCreated column is removed.
    # print(clean_data['dateCreated'].describe())
    clean_data = clean_data.drop('dateCreated', 1)  # removes the dateCreated column

    draw_column_histogram_string(clean_data, 'brand')


def regression_model():
    pass


def describe_data_frame(cars):
    """Shows the highlights of the dataframe to have a general view.

    :param cars:
    :return:
    """

    # calculates the general information for the dataframe
    cars_describe = cars.describe(include='all').loc[['count', 'unique', 'top', 'freq']]
    # print(cars_describe)

    unique_value_list = []
    for column in cars:
        unique_value_list.append(cars[column].unique())
        # print("{}'s has {} unique_values: {}\n".format(column, len(cars[column].unique()), cars[column].unique()))

    #print(unique_value_list)
    # insert unique values to table
    cars_describe_transpose = cars_describe.transpose()
    cars_describe_transpose["unique_value_list"] = unique_value_list

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('output/cars_describe.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    cars_describe_transpose.to_excel(writer, sheet_name='cars_describe')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def show_empty_records(cars):
    """Prints the total missing value for each column.

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


def draw_column_histogram(data_frame, column_name):

    print(data_frame[column_name].describe())

    # sample_data = data_frame.sample(n=10000, random_state=1)
    data_frame[column_name].hist(bins=20)
    plt.title('Histogram ' + column_name)
    plt.show()


def draw_column_histogram_string(data_frame, column_name):

    print(data_frame[column_name].describe())

    # sample_data = data_frame.sample(n=10000, random_state=1)
    data_frame.apply(pd.value_counts)
    #plt.title('Histogram ' + column_name)
    plt.show()


if __name__ == "__main__":
    main()


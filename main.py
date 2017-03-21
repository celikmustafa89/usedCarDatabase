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

    describe_data_frame(cars)

    plt.show()
    # Shows the first five records
    # print(">>> first five records:\n{}".format(cars.head()))

    # print(">>> cars columns:\n{}".format(cars.columns))
    # print(">>> Column Data_Type\n{}".format(cars.dtypes))


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


if __name__ == "__main__":
    main()
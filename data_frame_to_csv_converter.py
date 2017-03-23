"""
DATAFRAME OBJECT TO CSV FORMAT CONVERTER CODE SAMPLE
"""
import pandas as pd
import main

cars = pd.read_csv('input/autos.csv', encoding='latin_1')
cars_without_null_values = cars.dropna()

clean_data = cars_without_null_values[
                        ['seller',
                         'offerType','abtest',
                         'postalCode',
                         'monthOfRegistration',
                         'vehicleType', 'fuelType',
                         'yearOfRegistration', 'gearbox',
                         'powerPS', 'model',
                         'kilometer',
                         'brand', 'notRepairedDamage',
                         'price']]
main.data_frame_to_csv(clean_data, "output/whole_data.csv")
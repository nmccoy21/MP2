import csv

# globals
# strings for the columns names in the csv file and for the file name
style = 'style'
year_formed = 'formed'
year_split = 'split'
band_name = 'band_name'
origin_country = 'origin'
file_end_date = 2017
metal_file_name = 'metal_bands_2017_MP2.csv'

def read_data(file_name):
    # open and read the file
    # we're setting the encoding here to utf-8 to avoid
    # decoding errors on Windows machines
    with open(file_name, 'r', encoding="utf-8-sig") as csvfile:
        # read the data using a DictReader
        # use a list comprehension to create a new nested list from the data
        # each element will be a Dictionary (or Ordered Dictionary, depending on your version of Python)
        # representing a row from the csv file

    # return the list for use in other functions
    # note: we are returning ALL of the data from the csv file here
    # we will filter and clean this data in other functions
                          

def get_bands_formed_in_year(year):
    # Get the data from the csv using the read_data() function
    band_data = read_data(metal_file_name)
    # Look through the data and make a nested list of bands who formed that year and their country of origin 
    # For every row in the data, find the year the band formed.
    # If it matches the year used in the argument, add a new element to the list of bands formed that year.
    # Each element of the nested list will consist of a tuple, in the form of (band_name, country)

    # return band_list

# return a nested list of tuples or lists containing info for bands with a given keyword in their style
def get_bands_with_style(style_keyword):
    # get the data using your read_data() function
    band_data = read_data(metal_file_name)
    # iterate through the nested list, looking at the data in the band's 'style' column
    # if a band's listed style includes the keyword, add the band name and style to to a new nested list (band_name, style)
    # we don't want this to be case sensitive!

    # return band_list

# read our csv file and return a nested list of countries and the number of bands that have formed in the country
def get_bands_per_country():
    # get the data using your read_data() function
    band_data = read_data(metal_file_name)
    # Look at the 'origin' column of each row, and count up the number of bands who claim that country as an origin
    # Some bands are too metal for an origin country. Set those to 'Unaffiliated'
    # Store this data in a nested list, where each element is in the form of (country, num_bands)   

    # sort the list, in descending order, by the number of bands in the country
    # ex: [('USA', 1139), ('Sweden', 736), ('Germany', 254), ('Unaffiliated', 8)]

    # return bands_per_country

def get_longest_lived_bands(num_bands):
    # return the data from the file with read_data()
    band_data = read_data(metal_file_name)

    # Look at each row of the data, looking at the 'formed' and the 'split' data, and calculating how long each band
    # has been active. Store the results in a nested list, where each element is a tuple in the form (band, num_years_active)
        # If we don't have a 'formed' date, we can't make any assumptions about the band longevity,
        # so we'll need to ignore that band
        
        # If we don't have an end date, we'll assume the band was still intact as of the date of this data (2017) 

        # if the band split the same year it formed, we'll say they lasted a year
    
    # Sort the list in descending order
    # Return a portion of the newly sorted nested list, containing the number of bands passed to the num_bands argument
    
    # return longest_lived_bands

def print_table(nested_list, col_1_name, col_2_name):
    pass # remove when you start this
    # Print the elements of a nested list in two collumns
    # The names of the collumns should be printed at the top of the table
    # Use formatting to ensure the collumns are alligned (Lesson #13)

    # no return

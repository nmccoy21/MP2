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
    #### open and read the file
    #### we're setting the encoding here to utf-8 to avoid
    #### decoding errors on Windows machines
    with open(file_name, 'r', encoding="utf-8-sig") as csvfile:
        host_reader = csv.DictReader(csvfile)
        metal_list = [row for row in host_reader]
        
        #### read the data using a DictReader
        #### use a list comprehension to create a new nested list from the data
        #### each element will be a Dictionary (or Ordered Dictionary, depending on your version of Python)
        #### representing a row from the csv file
        
        return metal_list
    
    #### return the list for use in other functions
    #### note: we are returning ALL of the data from the csv file here
    #### we will filter and clean this data in other functions
                          
def get_bands_formed_in_year(year):
    band_list = []
    band_dict = {}
    #### Get the data from the csv using the read_data() function
    band_data = read_data(metal_file_name)
    for item in band_data:
        if item['formed'] != '-':
            if int(item['formed']) == year:
                band_list.append((item['band_name'],item['origin']))
        
        
    
    ####Look through the data and make a nested list of bands who formed that year and their country of origin 
    #### For every row in the data, find the year the band formed.
    #### If it matches the year used in the argument, add a new element to the list of bands formed that year.
    #### Each element of the nested list will consist of a tuple, in the form of (band_name, country)

    #### return band_list
    return sorted(band_list)

# return a nested list of tuples or lists containing info for bands with a given keyword in their style
def get_bands_with_style(style_keyword):
    #### get the data using your read_data() function
    band_list = []
    band_data = read_data(metal_file_name)
    #### iterate through the nested list, looking at the data in the band's 'style' column
    for item in band_data:
        if style_keyword.lower() in item['style'].lower():
    #### if a band's listed style includes the keyword, add the band name and style to to a new nested list (band_name, style)
            band_list.append((item['band_name'],item['style']))
    #### we don't want this to be case sensitive!
    #### return band_list
    return band_list

# read our csv file and return a nested list of countries and the number of bands that have formed in the country
def get_bands_per_country():
    #### get the data using your read_data() function
    band_data = read_data(metal_file_name)
    band_dict = {}
    count = 0
    #### Look at the 'origin' column of each row, and count up the number of bands who claim that country as an origin
    for item in band_data:
        if ',' in item['origin']:
            for b in item['origin'].split(','):
                b = b.strip()
                band_dict[b] = band_dict.get(b,0) + 1
        else:
            
            
            if item['origin'] != '-':
                if item['origin'] in band_dict:
                    band_dict[item['origin']] += 1
                else:
                    band_dict[item['origin']] = 1
            else:
                band_dict['Unaffiliated'] += 1
    #### Some bands are too metal for an origin country. Set those to 'Unaffiliated'
    #### Store this data in a nested list, where each element is in the form of (country, num_bands)
    
    
    bands_per_country = sorted([(j,k) for k,j in (band_dict.items())], reverse = True)
    bands_per_country_in_order = [(j,k) for k, j in bands_per_country]
    
            
    #### sort the list, in descending order, by the number of bands in the country
    #### ex: [('USA', 1139), ('Sweden', 736), ('Germany', 254), ('Unaffiliated', 8)]

    ####return bands_per_country
    return bands_per_country_in_order

def get_longest_lived_bands(num_bands):
    #### return the data from the file with read_data()
    band_data = read_data(metal_file_name)
    longest_lived_bands = []
    #### Look at each row of the data, looking at the 'formed' and the 'split' data, and calculating how long each band
    #### has been active. Store the results in a nested list, where each element is a tuple in the form (band, num_years_active)
    for item in band_data:
        if item['formed'] != '-':
        #### If we don't have a 'formed' date, we can't make any assumptions about the band longevity,
        #### so we'll need to ignore that band
            
        #### If we don't have an end date, we'll assume the band was still intact as of the date of this data (2017) 
            if item['split'] == '-':
                item['split'] = 2017
            num_years_active = int(item['split']) - int(item['formed'])
        #### if the band split the same year it formed, we'll say they lasted a year
            if num_years_active == 0:
                num_years_active = 1
                
            longest_lived_bands.append((num_years_active, item['band_name']))
    longest_lived_bands.sort()
    longest_lived_bands = [(name,years) for years,name in reversed(longest_lived_bands)]
    
    #### Sort the list in descending order
    #### Return a portion of the newly sorted nested list, containing the number of bands passed to the num_bands argument
    
    return longest_lived_bands[:num_bands]

def print_table(nested_list, col_1_name, col_2_name, width = 10):
    template = "{:<{}} {:<{}}"
    #### print headers
    print(template.format(col_1_name,width,col_2_name,width))

    #### print dashed line
    print("-"*width*2)

    #### print data
    for row in nested_list:
        print(template.format(row[0],width,row[1],width))
        
    print()
        
    #### Print the elements of a nested list in two collumns
    #### The names of the collumns should be printed at the top of the table
    #### Use formatting to ensure the collumns are alligned (Lesson #13)

    # no return

if __name__ == '__main__':
##    print_table(get_bands_formed_in_year(1969),"Band name", "Country of origin", 20)
##    print_table(get_longest_lived_bands(10), 'Band name', 'Years Active', 25)
##    print_table(get_bands_with_style('progressive thrash'), 'Band name', 'Style(s)', 25)
    print_table(get_bands_per_country(), 'Place(s) of origin','Bands hailing from place', 25)

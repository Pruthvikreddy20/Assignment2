#TO OUTPUT THE COUNTRIES AS COLUMNS AND YEARS AS ROWS
#import pandas library for reading the csv file
import pandas as pd
import matplotlib.pyplot as plt
def process_ff_data(filename):
    # Load the data into a DataFrame
    df = pd.read_csv(filename, skiprows=4)
    
    # Extract the data for the years 2010-2019
    yearsDF = df.loc[:, 'Country Name':'2019']
    yearsDF.columns = [col if not col.isdigit() else str(col) for col in yearsDF.columns]
    
    # Transpose the DataFrame to get a country-centric view
    countriesDF = yearsDF.transpose()
    
    # Replace empty values with 0
    countriesDF = countriesDF.fillna(0)
    
    # Set the column names for the countries DataFrame
    countriesDF.columns = countriesDF.iloc[0]
    countriesDF = countriesDF.iloc[1:]
    countriesDF.index.name = 'Year'
    
    # Set the column names for the years DataFrame
    yearsDF = yearsDF.rename(columns={'Country Name': 'Year'})
    yearsDF = yearsDF.set_index('Year')
    
    return yearsDF, countriesDF



#calling the function we created above
yearsDF, countriesDF = process_ff_data('API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv')

# MAKING THE COUNTRIES TO BE COLUMNS
countriesDF

#to output the years as the columns
yearsDF

#employ .decribe() to explore the statistical properties(years)
yearsDF.describe()

#employ .decribe() to explore the statistical properties(countries)
countriesDF.describe()

#to get overall information about the countries

countriesDF.info()

#general information about the years in the dataset
yearsDF.info()

#correlation 
yearsDF.corr()

#A COMBINED BAR GRAPH FOR FOSSIL FUEL CONSUMPTION AMONG G7 COUNTRIES(2004 - 2014)

# Load the CSV file into a DataFrame
df = pd.read_csv("API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv", skiprows=4)

# Define the G7 countries
g7_countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

# Filter the DataFrame to only include the G7 countries
df_filtered = df[df["Country Name"].isin(g7_countries)]

# Create a new DataFrame with only the relevant columns
df_plot = df_filtered[["Country Name", "2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]]

# Set the index of the DataFrame to be the country names
df_plot.set_index("Country Name", inplace=True)

# Convert the data to numeric values
df_plot = df_plot.apply(pd.to_numeric, errors='coerce')

# Create a bar chart with the G7 countries and years
ax = df_plot.plot(kind="bar", figsize=(12,6), width=0.8)
ax.set_xticklabels(g7_countries)

# Set the title and axis labels
plt.title("Fossil Fuel Energy Consumption (% of Total) in G7 Countries")
plt.xlabel("Country")
plt.ylabel("% of Total Energy Consumption")

# Show the plot
plt.show()



# Load the CSV file into a DataFrame
df = pd.read_csv("API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv", skiprows=4)

# Define the G7 countries
g7_countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

# Filter the DataFrame to only include the G7 countries
df_filtered = df[df["Country Name"].isin(g7_countries)]

# Create a new DataFrame with only the relevant columns
df_plot = df_filtered[["Country Name", "2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]]

# Set the index of the DataFrame to be the country names
df_plot.set_index("Country Name", inplace=True)

# Convert the data to numeric values
df_plot = df_plot.apply(pd.to_numeric, errors='coerce')

# Create a bar chart with the G7 countries and years
plt.figure(figsize=(10, 6))
for country in g7_countries:
    x = df_plot.loc[country, "2004":"2014"].values
    y = range(11)
    plt.scatter(x, y, label=country)
plt.yticks(range(11), df_plot.columns)
plt.title("Fossil Fuel Energy Consumption (% of Total) in G7 Countries")
plt.xlabel("% of Total Energy Consumption")
plt.ylabel("Year")
plt.legend()
plt.show()

#A LINE GRAPH FOR FOSSIL FUEL CONSUMPTION AMONG G7 COUNTRIES(2004 - 2014)


# Load the CSV file into a DataFrame
df = pd.read_csv("API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv", skiprows=4)

# Define the countries of interest
countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

# Filter the DataFrame to only include the countries of interest
df_filtered = df[df["Country Name"].isin(countries)]

# Create a new DataFrame with only the relevant columns
df_plot = df_filtered[["Country Name", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]]

# Set the index of the DataFrame to be the country names
df_plot.set_index("Country Name", inplace=True)

# Convert the data to numeric values
df_plot = df_plot.apply(pd.to_numeric, errors='coerce')

# Create a line graph with the countries of interest and years
plt.figure(figsize=(10, 6))
for country in countries:
    plt.plot(df_plot.loc[country], label=country)

# Set the title and axis labels
plt.title("Fossil Fuel Energy Consumption (% of Total) in Selected Countries")
plt.xlabel("Year")
plt.ylabel("% of Total Energy Consumption")
plt.legend()

# Show the plot
plt.show()

#A BAR GRAPH FOR FOSSIL FUEL CONSUMPTION AMONG G7 COUNTRIES(2004 - 2014)

# Load the CSV file into a DataFrame
df = pd.read_csv("API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv", skiprows=4)

# Define the countries of interest
countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

# Filter the DataFrame to only include the countries of interest and the year 2014
df_filtered = df.loc[df["Country Name"].isin(countries), ["Country Name", "2014"]]

# Convert the data to numeric values
df_filtered["2014"] = pd.to_numeric(df_filtered["2014"], errors='coerce')

# Sort the data in descending order of 2014 values
df_filtered = df_filtered.sort_values(by="2014", ascending=False)

# Create a bar chart with the countries and their 2014 values
plt.figure(figsize=(10, 6))
plt.bar(df_filtered["Country Name"], df_filtered["2014"])

# Set the title and axis labels
plt.title("Fossil Fuel Energy Consumption (% of Total) in 2014")
plt.xlabel("Country")
plt.ylabel("% of Total Energy Consumption")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()


#A BAR GRAPH FOR URBAN POPULATION GROWTH AMONG G7 COUNTRIES(2004 - 2014)


# Load the CSV file into a DataFrame
df = pd.read_csv("API_SP.URB.GROW_DS2_en_csv_v2_5226876.csv", skiprows=4)

# Define the countries of interest
countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

# Filter the DataFrame to only include the countries of interest and the year 2014
df_filtered = df.loc[df["Country Name"].isin(countries), ["Country Name", "2014"]]

# Convert the data to numeric values
df_filtered["2014"] = pd.to_numeric(df_filtered["2014"], errors='coerce')

# Sort the data in descending order of 2014 values
df_filtered = df_filtered.sort_values(by="2014", ascending=False)

# Create a bar chart with the countries and their 2014 values
plt.figure(figsize=(10, 6))
plt.bar(df_filtered["Country Name"], df_filtered["2014"])

# Set the title and axis labels
plt.title("Urban population growth (annual %) in 2014")
plt.xlabel("Country")
plt.ylabel("% of Urban population growth")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()


#A STACKED BAR CHART FOR FOSSIL FUEL CONSUMPTION AMONG G7 COUNTRIES(2004 - 2014)


# read the csv file
data = pd.read_csv("API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv", skiprows=4)

# select the columns we need
columns = ['Country Name'] + [str(year) for year in range(2004, 2015)]
df = data[columns]

# choose ten countries to display
countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]
df = df[df['Country Name'].isin(countries)]

# set the index to Country Name
df = df.set_index('Country Name')

# create the stacked bar graph
ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))

# set the x label and y label
ax.set_xlabel('Country')
ax.set_ylabel('Fossil fuel energy consumption (% of total)')

# set the title
ax.set_title('Fossil fuel energy consumption (% of total) for ten countries from 2004 to 2014')

# show the graph
plt.show()


#A PIE CHART FOR FOSSIL FUEL CONSUMPTION AMONG G7 COUNTRIES(2014)


# Load the data from the CSV file
df = pd.read_csv("API_EG.USE.COMM.FO.ZS_DS2_en_csv_v2_5342139.csv", skiprows=4)

# Filter the data for the selected countries and year
selected_countries = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]
selected_year = "2014"
filtered_data = df.loc[df["Country Name"].isin(selected_countries), ["Country Name", selected_year]]

# Set the country names as the index
filtered_data = filtered_data.set_index("Country Name")

# Create the pie chart using matplotlib
plt.pie(filtered_data[selected_year], labels=filtered_data.index, autopct='%1.1f%%')
plt.title(f"Fossil Fuel Energy Consumption (%) by Country in {selected_year}")
plt.show()


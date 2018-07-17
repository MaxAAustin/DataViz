# Firstname Lastname
# Date
# Computer Science 205 Section YY
# Regression Participation Project

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Reads the CSV data in from the relative path to the wine.csv file and sets the index column to the id. 
df = pd.read_csv("Data_Files/wine.csv", index_col='id')


# Prints the first and last five rows of the data head and tail to the console by calling head() and tail() from Pandas and setting 5 as the parameter.
#print(df.head(5))
#print(df.tail(5))

# Prints the name of the columns 
#print(df.columns)

# Creates a scatterplot from the dataframe read in, above. 
# Sets x values to the members from the 'price' column; y values are elements from the 'points' column of the wine.csv
#df.plot.scatter(x='price', y='points')

# Sets a title for the scatter plot
#plt.title('Wine Scores By Price')

# Uses Matplotlib to show the scatterplot made from the dataframe. 
#plt.show()

x = df['price']
y = df['points']

def regression():
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    
    results = [slope, intercept, r_value, p_value, std_err]
    #print(results)
    return results

def display_stats(results):
    index = 0
    labels = ["Slope: ","Intercept: ","R Value: ","P Value: ","Standard Error: "]
    for row in results:
        print()
        print(labels[index], row)
        index += 1

def plot_regression(x, y, results):
    #df.plot.scatter(x='price', y='points')
    line_y = results[1] + results[0]*x

    plt.plot(x, y, 'o', label='Wines')
    plt.plot(x, line_y, 'r', label='Fitted Line')
    plt.legend()
    plt.title('Wine Scores By Price')
    plt.show()

def main():
    res = regression()
    display_stats(res)
    plot_regression(x, y, res)

if __name__ == "__main__":
    main()


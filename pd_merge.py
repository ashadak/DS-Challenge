# Import Pandas library
import pandas as pd


infile = 'text1.txt'

def merge(file) :

  # read in the input text file into a pandas dataframe 
  df = pd.read_csv(file)

  # Since we read the content of the file into a datafram, we won't have to remove the empty space between the two csv-like files, Pandas will just ignore the space when making the dataframe
  # The columns for the second csv-like file will appear as a row in the dataframe. We will delete this row by finding the row that has 'id' (a column name) as a value for the 'id' column and remove it from the dataframe
  df = df[df['id'] != 'id']

  # Now we'll sort the rows in the dataframe by id
  df = df.sort_values(by='id')
  
  # Finally we convert our dataframe back into a text file (although we're using the pandas 'to_csv' function) and return it
  outfile = df.to_csv('outfile.txt', index=False)

  return outfile


merge(infile)
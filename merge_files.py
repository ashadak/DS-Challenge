infile = 'text1.txt'

def merge_files(infile):

    outfile = "outfile.txt"

    with open(infile, 'r', encoding='utf-8') as infile, open(outfile, 'w') as outfile:

        lines = [line for line in infile] # Add all the lines from the input file into a list

        new_line = lines.index("\n") # get the index of the empty space between the two 'csv-like' files

        col_names = new_line + 1 # The line followed by the empty space is the columns for the second 'csv-like' file, we will also get the index of that line

        del lines[new_line: col_names+1] # remove empty space and column names for the second 'csv-like' file from the list

        lines[1:] = sorted(lines[1:]) # We want the rows to be ordered by id, so we will sort our list starting from index=1 to ensure the column names (from the first 'csv-like' file) retain their place as the first row

        # Now since the rows have been sorted, it is possible that two rows get inserted on the same line if the last row from the initial infile has been moved
        #(since it will not have "\n" at the end). To address this, we will look for the element in the list that does not contain the "\n" substring and add "\n" at the end of it
        for index in range(len(lines)) :
            if "\n" not in lines[index] :
                lines[index] = lines[index] + "\n"

        # Now we will write the lines from our list into the outfile and return it
        for element in lines:
            outfile.write(element)

        return outfile


merge_files(infile)
   


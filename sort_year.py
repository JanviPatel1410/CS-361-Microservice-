import numpy as np
import csv
import time


infile_path = 'add input file path'
outfile_path = 'add output file path'

while True:

    time.sleep(1)
    if open(infile_path, 'r').read() != '#':

        with open(infile_path, 'r') as infile:
            year = infile.readline().strip()

            if year.isdigit():
                year = int(year) - 1
                file = infile.readline().strip()
            infile.close()
            open(infile_path, 'w').close()
            open(infile_path, 'w').write('#')
            infile.close()

        with open('./infile.csv', newline='') as csvfile:

            csv_input = csv.reader(csvfile, delimiter=',', quotechar='"')
            count = 0

            for index in csv_input:
                arrayLine = np.array(index)
                if count == 0:
                    sort_years = np.array(arrayLine)
                    count = 1
                else:
                    sort_years = np.vstack([sort_years, arrayLine])
        csvfile.close()

        while True:

            row_changed = False

            for index in range(2, len(sort_years)):
                firstSort = sort_years[index - 1][year]
                secondSort = sort_years[index][year]

                if secondSort > firstSort:
                    sort_years[[index - 1, index]] = sort_years[[index, index - 1]]
                    row_changed = True

            if not row_changed:
                break
        open(outfile_path, 'w').close()

        with open(outfile_path, 'w') as output:

            for index in sort_years:

                for inputs in range(sort_years.shape[1]):
                    if inputs != 1:
                        output.write(str(index[inputs]))

                    else:
                        output.write('"')
                        output.write(str(index[inputs]))
                        output.write('"')
                    output.write(',')
                output.write('\n')

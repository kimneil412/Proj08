#####################################################
# Computer Project #8
# Neil Kim
# Algorithms
# Import CSV file
# Import Pylab file
# Make functions for different types of definitions
# Asks to input text
# Prompt for inputs
# Using the text spits out information
# Calculations of Data
#####################################################
import csv
import pylab
from operator import itemgetter

#This function repeatedly prompts the user for a filename until the file is opened
#successfully. An error message should be shown if the file cannot be opened.
def open_file():
    file = input("Enter filename: ")
    x = True
    while x:
        try:
            fp = open(file, encoding = 'utf-8')
            x = False
        except FileNotFoundError:
            print("File not found!")
            file = input("Enter filename: ")
            x = True
    return fp

#This function read a file pointer and returns 3 dictionaries: Parameters, Returns, and The function displays nothing
def read_file(fp):
    file = csv.reader(fp)
    next(file, None)
    D1 = {}
    D2 = {}
    D3 = {}
    x = 1000000
    for line in file:
        p = line[1].strip()
        p = p.lower()
        n = line[0].strip()
        n = n.lower()
        try:
            year = int(line[(3 - 1)])
            e = float(line[(7 - 1)]) * x
            o = float(line[(9 - 1)]) * x
            na = float(line[(6 - 1)]) * x
            j = float(line[(8 - 1)]) * x
        except:
            continue
        pub = line[(5-1)].strip()
        pub = pub.lower()
        genre = line[(4 - 1)].strip()
        genre = genre.lower()
        glb = na + e + j + o
        t3 = (pub, n, year, na, e, j, o, glb)
        if pub in D3.keys():
            D3[pub].append(t3)
        else:
            D3[pub] = [t3]
        t2 = (genre, year, na, e, j, o, glb)
        if genre in D2.keys():
            D2[genre].append(t2)
        else:
            D2[genre] = [t2]
        t1 = (n, p, year, genre, pub, glb)
        if n in D1.keys():
            D1[n].append(t1)
        else:
            D1[n] = [t1]
    for i in sorted(D1):
        D1[i] = sorted(D1[i], key=itemgetter(5), reverse=True)
    for i in sorted(D2):
        D2[i] = sorted(D2[i], key=itemgetter(6), reverse=True)
    for i in sorted(D3):
        D3[i] = sorted(D3[i], key=itemgetter(7), reverse=True)
    D3_name = {}
    L3 = []
    for i in D3:
        L3.append(i)
    L3.sort()
    L3.sort()
    L3.sort()
    for z in L3:
        D3_name[z] = D3[z]
    D2_name = {}
    L2 = []
    for i in D2:
        L2.append(i)
    L2.sort()
    L2.sort()
    L2.sort()
    for z in L2:
        D2_name[z] = D2[z]
    D1_name = {}
    L1 = []
    for i in D1:
        L1.append(i)
    L1.sort()
    L1.sort()
    L1.sort()
    for i in L1:
        D1_name[i] = D1[i]
    return D1_name, D2_name, D3_name

#This function iterates through the dictionary D1 and return a subset of the data as
#indicated in Parameters, Returns, and the function displaying nothing
def get_data_by_column(D1, indicator, c_value):
    i = []
    if indicator == 'platform':
        for x, y in D1.items():
            for values in y:
                if values[1] == c_value:
                    i.append(values)
        i = sorted(i, key=itemgetter(5), reverse=True)
        i = sorted(i, key=itemgetter(2))
    else:
        for x, y in D1.items():
            for values in y:
                if values[2] == c_value:
                    i.append(values)
        i = sorted(i, key=itemgetter(5), reverse=True)
        i = sorted(i, key=itemgetter(1))
    return i
    pass

#This function iterates through the dictionary D3 (which contains the publisher data with
#publisher as the D3 key). It will return a list of all tuples where the publisher key equals
#the publisher parameter
def get_publisher_data(D3, publisher):
    i = []
    for key, value in D3.items():
        for values in value:
            if values[0] == publisher:
                i.append(values)
    i = sorted(i, key=itemgetter(1))
    i = sorted(i, key=itemgetter(7), reverse=True)
    i = sorted(i, key=itemgetter(1))
    i = sorted(i, key=itemgetter(7), reverse=True)
    return i
    pass


#This function prints a table of all the global game sales stored in L1 by either all
#platforms in a single year or all years for a single platform. This function does not return
#anything.
def display_global_sales_data(L, indicator):
    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    if indicator == 'year':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format(header1[0], header1[1], header1[2], header1[3], header1[4]))
        total = 0
        for tups in L:
            total += tups[5]
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(tups[0][:25], tups[1], tups[3], tups[4][:25], tups[5]))
        print("\n{:90s}{:<12,.02f}".format('Total Sales', total))
    if indicator == 'platform':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format(header2[0], header2[1], header2[2], header2[3], header2[4]))
        total = 0
        for tups in L:
            total += tups[5]
            print("{:30s}{:<10}{:20s}{:30s}{:<12,.02f}".format(tups[0][:25], tups[2], tups[3], tups[4][:25], tups[5]))
        print("\n{:90s}{:<12,.02f}".format('Total Sales', total))
    pass

#This function iterates through the dictionary D2 (which contains the list of regional sales
#by genre) and return a list of the total regional sales per genre whose value at the year
#column is equal to 'year'
def get_genre_data(D2, year):
    L = []
    for key, value in D2.items():
        for values in value:
            if values[1] == year:
                L.append(values)
    genreL = {}
    for genres in L:
        if genres[0] in genreL:
            genreL[genres[0]] += 1
        else:
            genreL[genres[0]] = 1

    finalL = []
    for key, value in genreL.items():
        na, e = 0, 0
        j, o = 0, 0
        glb = 0
        genre = key
        c = value
        for tuples in L:
            if key == tuples[0]:
                a = tuples[2]
                na += a
                ngr = tuples[3]
                e += ngr
                toggaf = tuples[4]
                j += toggaf
                reggin = tuples[5]
                o += reggin
                glb += tuples[6]
        t = (genre, c, na, e, j, o, glb)
        finalL.append(t)
    finalL = sorted(finalL, key=itemgetter(0))
    finalL = sorted(finalL, key=itemgetter(6), reverse=True)

    return finalL

    pass

#This function prints a table of all the total regional sales for each genre stored in
#genre_list. This function does not return anything
def display_genre_data(genre_list):
    header = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(header[0], header[1], header[2], header[3], header[4], header[5]))
    t_glb = 0
    for i in genre_list:
        gn = i[1]
        n = i[2]
        e = i[3]
        j = i[4]
        o = i[5]
        glb = i[6]
        t_glb += glb
        print("{:15s}{:15s,.02f}{:15s,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(gn, n, e, j, o, glb))
    print("\n{:75s}{:<15,.02f".format("Total Sales", t_glb))
    return

#This function prints a table of all the total regional sales for each genre stored in
#pub_list. This function does not return anything.
def display_publisher_data(pub_list):
    t_glb = 0
    pub = pub_list[0][0]
    header = ['Title', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(header[0], header[1], header[2], header[3], header[4], header[5]))
    for i in pub_list:
        x = i[1].slice(25)
        n = i[3]
        e = i[4]
        j = i[5]
        o = i[6]
        glb = i[7]
        t_glb += glb
        print("{:30s}{:15s,.02f}{:15s,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(x, n, e, j, o, glb))
    print("\n{:90s}{:<15,.02f".format("Total Sales", t_glb))
    return

#This function receives a list L of tuples with global sales that was generated by the
#get_data_by_column function
def get_totals(L, indicator):
    xy = {}
    x = []
    y = []
    for i in L:
        if indicator == "year":
            if i[1] in xy.keys():
                xy[i[1]] +=i[5]
            else:
                xy[i[1]] = i[5]
        elif indicator == "platform":
            if i[2] in xy.keys():
                xy[i[2]] += i[5]
            else:
                xy[i[2]] = i[5]
    for key, val in xy.items():
        x.append(key)
        y.append(val)
    return x, y

#This function receives a list of global sales per genre for a particular year (that is, the list
#L comes from a call to get_genre_data for a particular year, the call being done in
#option 3 of main).
def prepare_pie(genres_list):
    x1 = []
    x2 = []
    x3 = []
    for i in genres_list:
        tup = (i[0], i[(7-1)])
        x1.append(tup)
    x1.sort()
    x1.sort()
    x1.sort()
    x1.sort(key = itemgetter(1), reverse = True)
    x1.sort()
    x1.sort(key=itemgetter(1), reverse=True)
    for y in x1:
        x3.append(y[1])
        x2.append(y[0])
    return x2, x3

#This function creates bar plots when the user wants to process the global sales
#data by year or platform.
def plot_global_sales(x, y, indicator, value):
    '''
        This function plots the global sales per year or platform.

        parameters:
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)

        Returns: None
    '''
    if indicator == 'year':
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")

    pylab.ylabel("Total copies sold (millions)")

    pylab.bar(x, y)
    pylab.show()

#This function creates a pie plot when the user
#wants to process the global sales data by genre in a particular year.
def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.

        parameters:
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order
            year: the year of the genre data (int)

        Returns: None
    '''

    pylab.pie(values, labels=genre, autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()

#This function is the starting point of the program. The program starts by opening the file
#with the video game sales and reading the data into three dictionaries.
def main():
    # Menu options for the program
    MENU = '''Menu options

    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit

    Enter choice: '''
    fp = open_file()
    D1, D2, D3 = read_file(fp)
    choice = input(MENU)

    while choice != '5':

        # Option 1: Display all platforms for a single year
        if choice == '1':

            try:
                year = int(input("Enter year: "))
                data_column = get_data_by_column(D1, 'year', year)
                if data_column == []:
                    print("The selected year was not found in the data.")
                else:
                    print("\n{:^80s}".format("Video Game Sales in {}".format(year)))
                    display_global_sales_data(data_column, 'year')
                    plot = input("Do you want to plot (y/n)?")
                    if plot == "y":
                        x, y = get_totals(data_column, 'Year')
                        plot_global_sales(x, y, 'Year', year )

            # if the list of platforms for a single year is empty, show an error message
                pass

            except ValueError:
                print("Invalid year.")

        elif choice == '2':
            try:
                p = str(input("Enter platform: "))
                d = get_data_by_column(D1, "platform", p)
                if d == []:
                    print("The selected platform was not found in the data.")
                else:
                    print(d)
                    plot = input("Do you want to plot (y/n)? ")
                    if plot == "y":
                        x, y = get_totals(d, "Platform")
                        plot_global_sales(x, y, d, "Platform")

            except ValueError:
                print("Invalid Platform.")
        elif choice == "3":
            try:
                year = int(input("Enter year: "))
                g = get_genre_data(D2, year)
                display_genre_data(g)
                plot = input("Do you want to plot (y/n)? ")
                if plot == "y":
                    x, y = prepare_pie(g)
                    plot_genre_pie(x, y, year)
            except ValueError:
                print("Invalid year.")
        elif choice == "4":
            keyword = input('Enter keyword for publisher: ')
            p = str(input("Enter keyword for publisher: "))
            m = []
            for i in D3.values():
                for t in i:
                    if t[0] == p:
                        match.append(t)


            # Option 4: Display publisher data

            # Enter keyword for the publisher name

            # search all publisher with the keyword
            match = []

            # print the number of matches found with the keywords
            if len(match) > 1:
                print("There are {} publisher(s) with the requested keyword!".format(len(match)))
                for i, t in enumerate(match):
                    print("{:<4d}{}".format(i, t[0]))

                # PROMPT USER FOR INDEX
                index = input("Select the index for the publisher to use: ")
                print(match[index])
            else:
                print('No publisher name containing "{}" was found!'.format(keyword))
                index = 0

        else:
            print("Invalid option. Please Try Again!")
        choice = input(MENU)

    print("\nThanks for using the program!")
    print("I'll leave you with this: \"All your base are belong to us!\"")


if __name__ == "__main__":
    main()
## Automation on Drug Interactions Profiling


**Overview:**

Our goal in developing this code and surrounding architecture has several levels. There are three python files that execute this functionality: compile.py, parser.py, and query.py. The user need only call compile.py, which will automatically call parser.py, and then the user can call query.py which will prompt them to input their search. The data that compile.py runs on is taken from the FAERS website in the form of an .xml file. The output is in the form a .csv file that any user can open with a program like Microsoft Excel. On a fundamental level, we developed a program that has lasting use for healthcare professionals to take the information provided by the FDA, extract the relevant data, and query based on the reactions, drugs, or substances based on each individual patients' needs.

**Requirement:**

The program can be run on different computer operating systems such as Linux, Microsoft, and Mac with basic requirement fulfilled. Different server services can be accessed through 
* [Amazon Web Services](https://aws.amazon.com/) 
* [Microsoft Azure](https://portal.azure.com/) 
* [Chameleon Cloud](https://www.chameleoncloud.org)

Basic requirement:
  * Python3
  * Python libraries: pandas, numpy


**Installing Requirements**

The latest python3 version can be found [here](https://www.python.org/downloads/ "Python Downloads")

For installation and setting up python can be found [here](https://realpython.com/installing-python/ "Installing and Python setup")

For pandas and numpy installation, it can be found [here](https://pandas.pydata.org/pandas-docs/stable/install.html)


**Running Program**

In this directory, there are two programs that served different function.

  * compile.py is for parsing the xml file into smaller csv file that only contains 3 headings (Drug, Substance, Reaction)
  * query.py is for querying specific information from the csv file

Steps to achieve desired result:

  * Downloads and extract the zip file from the [FDA website](https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html)
  * Locate the xml file(s) that is inside the zip file after extracting
  * Copy the xml file(s) and place them into the same directory as the three python file (compile.py, parser.py, and query.py)
  * Run the compile.py using python3
  ```
  $ python3 compile.py
  ```
  * Once the program is finished, there will two files created in that directory: 1) scanned_file.txt which records all the xml file that has been processed, and 2) compiled_data.csv which stores information pertaining the substance, drugs, and reactions
  * The next step will be running query.py using Python 3
  ```
  $ python3 query.py
  ```
  by running this program, the user will be prompted to specified the field that they are interested in. For example, if you are interested in looking for reactions based on *drugs*. you will put it *drug* on the prompt.
  ```
  Are you looking for a "drug", "substance", or "reaction", please enter without quotes: drug
  ```

  The next prompt will instruct the user to specify on which field they are looking for specifically.

  For example, if you are looking for *Humira:*

  ```
  Please put the Drug, format as a list for multiple Drug, e.g. [x,y,z]: [Humira]
  ```

  However, if you are looking for multiple drugs, like *Humira* and *Repatha:*

  ```
  Please put the Drug, format as a list for multiple Drug, e.g. [x,y,z]: [Humira, Repatha]
  ```

  Once the program queries the information, it will tell the user that the file for the query has been created.
  The file will contain the queried information based on the parameters that the user inputted.

**Notes**

The query.py program is meant to produce another csv file which is smaller compared to the original raw xml file. As such, the program will run analysis on the data in less time.

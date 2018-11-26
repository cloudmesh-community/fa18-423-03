## Big Data on Health Care - Drug Adverse Effect on Patient


**Overview:**

The project ultimate goal is to improve the health care system that we currently have by further looking into drugs that patients used. Patients are prescribed with multiple drugs for the purpose of curing their illness. On the hope of doing so, some patients may recover fully, and some may not be so lucky.  Taking different drugs at the same time might cause them to interact with one another and thus resulting in unforeseeable adverse effect on the patients themselves. As such, patients may become more ill or sometimes can lead to death. The currently available information is being stored in a big file data which only partial of the information is useful to run query on. Therefore, the purpose of this project is to assist in terms of streamlining the currently available information into more digestible data that can be used by users to do further research on the drugs and the patient reactions.


**Requirement:**

The program can be run on different computer operating systems such as Linux, Microsoft, and Mac with basic requirement fulfilled. Different server services can be accessed through [Amazon Web Services](https://github.com/cloudmesh-community/fa18-423-02/blob/master/project-code/aws-setup.md) [Microsoft Azure](http)

Basic requirement:
  * Python3
  * Python libraries: pandas, numpy


**Installing Requirements**

The latest python3 version can be found [here](https://www.python.org/downloads/ "Python Downloads")

For installation and setting up python can be found [here](https://realpython.com/installing-python/ "Installing and Python setup")

For pandas and numpy installation, it can be found [here](https://pandas.pydata.org/pandas-docs/stable/install.html)


**Running Program**

In this directory, there are two programs that served different function.

  * project.py is for parsing the xml file into smaller csv file that only contains 3 headings
  * query.py is for querying specific information from the csv file

Steps to achieve desired result:

  * Downloads and extract the zip file from the [FDA website](https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html)
  * Locate the xml file(s) that is inside the zip file after extracting
  * Copy the xml file(s) and place them into the same directory as the three python file (project.py, parser.py, and query.py)
  * Run the project.py using python3
  ```
  $ python3 project.py
  ```
  * Once the program is finished, there will two files created in that directory: 1) scanned_file.txt which records all the xml file that has been processed, and 2) compiled_data.csv which stores information pertaining the substance, drugs, and reactions
  * The next step will be running query.py using python 3
  ```
  $ python3 query.py
  ```
  by running this program, the user will be prompted to specified the field that they are interested in. For example, if you are interested in looking for reactions based on *drugs*. you will put it *drug* on the prompt.
  ```
  Type in query either you are looking for drug, substance, or reaction: drug
  ```

  The next prompt will prompt the user to specify on which things that they are looking for specifically.

  For example, if you are looking for *Calcium* and the reactions on that drug.

  ```
  Please put the Drug, format as a list for multiple Drug, e.g. [x,y,z]: Calcium
  ```

  For example, if you are looking for *Calcium* and *Aspirin*.

  ```
  Please put the Drug, format as a list for multiple Drug, e.g. [x,y,z]: [Calcium, Aspirin.]
  ```

  Once the program processed the information, it will tell the user that the file for the query has been created.
  The file will contains specific information based on the query that the user input in.

**Notes**

The query.py program is meant to produce another csv file which is lighter as compare to the original raw xml file. As such, the machine that will further run analysis on the data will take less time.

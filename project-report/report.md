# Automation on Drug Interactions Profiling :hand: fa18-423-06, fa18-423-03, fa18-423-02, fa18-423-05

| Chandler Mick
| chmick@iu.edu
| Indiana University
| hid: fa18-423-06
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-code/README.md)

## Introduction

For our project, we created a Python program that took raw data from the United
States Food and Drug Administration's Adverse Event Reporting System (FAERS) and
filtered out important components for a user to query the information simply.

## Dataset

The dataset is an Extensible Markup Language (XML) file from the FAERS on the
FDA's website. FAERS is a collection of reports from doctors, nurses, and
patients who have reported to the FDA side-effects of using certain commercial
drugs [CITE FAERS website]. This data is used by the FDA to formulate warnings
and regulations against drugs to warn consumers of the potential side effects
that come about from using pharmaceutical drugs.

The publicly available XML file is a 112 MB file with over 16 million rows of
data. Therefore, the file cannot be easily evaluated and assessed without
creating some sort of program to trim out the unnecessary data and store the
valuable data for running the query. The data that we analyzed with our program
covers the months of July 2018 to September 2018. However, a user would most
likely want to analyze data from previous quarters, which is possible with our
program.

The XML file contains 67 tags for each "adverse event report." An adverse event
report is a negative side effect to a drug from anything including migraines to
something as serious as death. Every tag includes information about the patient,
the side effect, the drug, treatment duration, etc. For this project, we decided
the most important tags that would want to be accessed would be the
reactionmeddrapt, medicinalproduct, and activesubstancename. These relate to the
reactions from the drug, the name of the drug, and the substances in the drug,
respectively.

## Implementation

![ProgramDesign](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-report/project_design.PNG)

### parser.py
Our parser.py file takes an XML file containing the initial FAERS raw data from
the website and converts it to a dataframe format to be stored in a CSV file.
This initial parse separates the three tags that we are looking to store for
our program (reactionmeddrapt, medicinalproduct, and #activesubstancename). The
parser.py program flows into the project.py program #where the dataframe format
allows the data to be easily manipulated.

### project.py
Our project.py file takes an XML file containing the initial FAERS raw data from
the website and converts the selected data to a CSV file. Using the parsing.py
function, the function takes our dataframe data and outputs the three tags that
we used in our project. This program takes the original, large dataset and forms
a smaller, compact dataset with the data that we deemed important.

### query.py
Our query.py file takes the compiled CSV file and allows a user to return
certain data based on inputted values. These inputted values can be certain
drugs, substances within the drugs, or the reactions of the drugs. This user
queried data can be used by the user to evaluate the specific results that they
are looking for. This CSV file can be transferred to a spreadsheet for simple 
data analysis.

## Conclusion

## Bibliography

## Work Breakdown


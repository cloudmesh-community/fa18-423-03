# Automation on Drug Interactions Profiling :hand: fa18-423-06, fa18-423-03, fa18-423-02, fa18-423-05

| Chandler Mick
| chmick@iu.edu
| Indiana University
| hid: fa18-423-06
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-code/README.md)  
| Kelvin Liuwie
| kliuwie@gmail.com
| Indiana University
| hid: fa18-423-02
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-code/README.md)  
| Yixing Hu
| yixihu@gmail.com
| Indiana University
| hid: fa18-423-05
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-code/README.md)  
| Omkar Tamhankar
| otamhank@iu.edu
| Indiana University
| hid: fa18-423-03
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-report/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-423-03/blob/master/project-code/README.md)

**:mortar_board: Learning Objectives**

* Creating a program that can parse and query large data sets
* Exploring various "free" cloud servers to run our program
* Evaluating which cloud server provides the optimal working efficiency

## Introduction

For our project, we created a Python program that took raw data from the United
States Food and Drug Administration's Adverse Event Reporting System (FAERS) and
filtered out important components for a user to query the information simply.
The main issue that we noticed was that the important information that Food and
Drug Administration (FDA) was collecting was in large datasets that incredibly
difficult to breakdown analyze for the average users of the information. Users
of this information could be regulators, doctors, or even concerned consumers.
Therefore, we believe that our program simplifies the analysis of these big data
sets that are provided by the FDA and makes them fit for spreadsheets, such as
Excel, for more in-depth review of the drug data.

One of the most important issues in the pharmaceutical industry today is
determining the quality of a drug on the market [CITE from pharmtech].Currently
a pharmaceutical company needs only prove in human clinical trials that a drug
is safe when taken in isolation. However, humans are not basic research subjects
and are often taking a number of medications. As the state of the healthcare
system continues to fall victim to political cycles, it is always important to
make sure that information on the safety and effects of drugs on the market need
to be readily and easily available for review. We hope that our project
represents an example of what could be implemented in the marketplace to present
the information to those who need to be aware of the effects of the drugs that
they are interacting with.

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
our program (reactionmeddrapt, medicinalproduct, and activesubstancename). The
parser.py program flows into the project.py program where the dataframe format
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




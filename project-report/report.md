# Automation on Drug Interactions Profiling

## Abstract

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

## Work Breakdown (New Page)




Problem: The FDA has a public database, FDA's Adverse Event Reporting System
(FAERS), that holds information regarding adverse events to drugs. A common
issue in the healthcare system is determining whether a drug is safe or not.
Currently a pharmaceutical company needs only prove in human clinical trials
that a drug is safe when taken in isolation. However, humans are not basic
research subjects and are often taking a number of medications. Therefore, we
will be using the FDA’s database to cross-reference cases in which a patient who
is taking two drugs has the same adverse event as a patient who is on the same
two drugs. In this way we can start to chip away at the issue regarding safety
of drug interactions.

Data Sources: The raw data that we will be using will taken from the FAERS
Quarterly Data Extract Files which are available online
(https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html). The data
contains information of the demographics and administrative information, drug
information from the case reports, reaction information, patient outcome, and
some relation information on the source of the reports. Data provided are
available in two formats ASCII and XML. Raw data will be filtered by extracting
relevant columns of information relevant to the research methodology. The data
are originally extracted from AERS database and disclose to be not cumulative.
Hence, there might be overlapped or repeated entries inside database and/or
across different files as they are sectioned into different quarters of the
year.

Data Cleaning: For the preliminary examination, the data will be filtered based
on the available entries on the data, i.e. assessing missing values in entries
and group them based on entries. The main reason is that the program developed
will be used in a way that users will be querying information pertaining to the
drugs and the program will displayed relevant information regarding to the
query. Hence, missing value in entries will hinder the aggregation process; the
program may display empty information or there might be complication during
retrieval.

Model: Model proposed for this program will include decision tree, cluster
analysis, and/or association analysis. The model will be trained with all
currently available data and will also be dynamic in a way that it will adapt
with new information fed into the cloud. Decision tree will assist user to
produce output that will predict the likelihood outcome/symptoms a patient might
have based on inputs given, i.e. different drugs taken at particular time.
Cluster analysis will be used for specific group of users in medical field, i.e.
doctors or scientists, to categorize certain symptoms based on drugs with the
hope that they will be able to use information produce to find other replacement
drugs that do not give adverse effect to the patient. For initial
experimentation, the team will be attempting to cluster information based on
symptoms and grouped them based on chemicals component of the drugs. Association
analysis will also serve the same purpose as clustering analysis, but to the
extent of exploring the likelihood of a symptom/outcome by taking chemicals as
inputs. Another data involvement: Drug ingredients data might be needed to have
better understanding on how certain drugs react with each other based on
chemical reactions.

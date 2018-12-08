import pandas as pd, numpy as np
import xml.etree.ElementTree as ET

#parsing function takes an xml file and convert it to dataframe format to be stored to csv
def parsing (file_name):
    tree = ET.parse (file_name)
    
    
    report = tree.findall('safetyreport')
    
    reaction_drug = []
    for item in report:
        patient= item.findall('patient')
    
        for info in patient:
            reaction = info.findall('reaction/reactionmeddrapt')
            reaction = list(set([item.text for item in reaction]))
    
            drug = info.findall('drug/medicinalproduct')
            drug = set([item.text for item in drug])
            drug = list(drug)
            
            substance = info.findall('drug/activesubstance/activesubstancename')
            substance = list(set([item.text for item in substance]))
            
            reaction_drug.append([reaction,drug,substance])
            
    rd_df = pd.DataFrame(reaction_drug)
    rd_df.columns = ['reaction','drug','substance']
    return rd_df
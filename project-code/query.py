import pandas as pd, numpy as np

data = pd.read_csv('compiled_data.csv')

def list_checking (me, you):
    for item in me:
        if item not in you:
            return False
    return True

def drug_look(drug_list):
    temp =[]
    drug_list = [drug.upper() for drug in drug_list]
    for i in range(len(data['drug'])):
        check = [item.upper() for item in eval(data['drug'][i])]
        if list_checking(drug_list,check):
            temp.append(data.loc[i])
    df = pd.DataFrame(temp)
    file_name = "_".join(drug_list)
    df.to_csv(file_name+".csv",index =False)
    print('File has been processed. The file name is', file_name+'.csv')
            
def reaction (reaction_list):
    temp = []
    reaction_list = [reaction.upper() for reaction in reaction_list]
    for i in range(len(data['reaction'])):
        check = [item.upper() for item in eval(data['reaction'][i])]
        if list_checking(reaction_list,check):
            temp.append(data.loc[i])
    df = pd.DataFrame(temp)
    file_name = "_".join(reaction_list)
    df.to_csv(file_name+".csv",index =False)
    print('File has been processed. The file name is', file_name+'.csv')
            
def substance (substance_list):
    temp = []
    substance_list = [subs.upper() for subs in substance_list]
    for i in range(len(data['substance'])):
        check = [item.upper() for item in eval(data['substance'][i])]
        if list_checking(substance_list, check):
            print(data.loc[i])
    df = pd.DataFrame(temp)
    file_name = "_".join(substance_list)
    df.to_csv(file_name+".csv",index =False)
    print('File has been processed. The file name is', file_name+'.csv')
            
def list_construct (user_input):
    formated = user_input.split(',')
    new_string = '["'+ formated.pop(0).replace('[','').replace('"','').replace("'",'')+ '"'
    for i in range(len(formated)-1):
        new_string += ',"'+ formated[i].replace('"','').replace("'",'') +'"'
    new_string += ',"' + formated[len(formated)-1].replace(']','').replace('"','').replace("'",'') + '"]'
    return eval(new_string)

def query (user_input):
    if user_input.upper() == 'REACTION':
        user_input = input('Please put the reactions, format as a list for multiple reaction, e.g. [x,y,z]: ')
        if list_checking(['[',']'], list(user_input)):
            user_input = list_construct(user_input)
            print('processing')
            reaction(user_input)
            print('processed')
        else:
            print('processing')
            reaction([user_input])
            print('processed')

    elif user_input.upper() == 'DRUG':
        user_input = input('Please put the Drug, format as a list for multiple Drug, e.g. [x,y,z]: ')
        if list_checking(['[',']'], list(user_input)):
            user_input = list_construct(user_input)
            print('processing')
            drug_look(user_input)
            print('processed')
        else:
            print('processing')
            drug_look([user_input])
            print('processed')

    else:
        user_input = input('Please put the substance, format as a list for multiple substance, e.g. [x,y,z]: ')
        if list_checking(['[',']'] , list(user_input)):
            user_input = list_construct(user_input)
            print('processing')
            substance(user_input)
            print('processed')
        else:
            print('processing')
            substance(user_input)
            
def main():
    while True:
        user_input = input('Type in query either you are looking for drug, substance, or reaction: ')
        if user_input.upper() == 'STOP':
            break
        elif user_input.upper() in ['REACTION','SUBSTANCE','DRUG']:
            query(user_input)
        else: 
            print('Invalid input')
            
main()
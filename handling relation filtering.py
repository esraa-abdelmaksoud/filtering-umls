#Abbreviations available in Critical UMLS Information file in Thesis folder
import pandas as pd

"""Getting English LONIC concepts from UMLS.
Apply to the 19 million rows in 18 files.
"""
for c in range (1,18):
    concept_list=[]
    # Reading file
    df=pd.read_excel(r'D:\Practical\UMLS\files\umls split{}.xlsx'.format(c), encoding='utf8',index=False,\
    header=None, names = ['CUI','LAT','TS','LUI','STT','SUI','ISPREF','AUI','SAUI','SCUI','SDUI','SAB',\
    'TTY','CODE','STR','SRL','SUPPRESS','CVF'])
    
    file_line_count = df.shape[0]
    print('Loading dataframe done')

    #Getting concepts of current file
    for i in range(file_line_count):

        cui= df.loc[i,'CUI']
        if df.loc[i,'SAB'] == 'LNC' and df.loc[i,'LAT']=='ENG':
            concept_list.append(cui)

    #Deleting duplicates in concept_list
    concept_list = list(dict.fromkeys(concept_list))
    print('Concepts ready')


    #Getting concepts that exist in concept_list only
    f_df=df[df['CUI'].isin(concept_list)]

    #Getting English concepts only
    final_df=f_df[f_df['LAT']=='ENG']

    #Saving dataframe
    final_df.to_excel(r'D:\Practical\UMLS\files\filtered umls{}.xlsx'.format(c),header=True,index=False,encoding='utf8')



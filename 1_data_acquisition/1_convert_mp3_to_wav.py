'''
This code is convert from mp3 to wav.
Fro the calls that we have are located in df_shortcalls.csv
initially the csv
'''

import glob
import pydub
import csv
import pandas as pd
from tqdm import tqdm ## great tool to keep track of loop process
import re


df_shortcalls = pd.read_csv("metadata.csv.cvs")
redo = [] ## Keep track of the missing files

dic = {'id': [], 'fromame_rate':[] , 'length':[]}

for a in tqdm(range(1,len(df_shortcalls))):
    '''To make sure that I have downloaded all the files from S3 I will first
        try to read the file name from the mp3 folder and if the file is not there record that file name in a list (redo) 
        for future reference n 
    '''
    file = glob.glob("./mp3/"+str(df_shortcalls.gradable_id[a])+".mp3")
    
    if file == []:
        redo.append(str(df_shortcalls.gradable_id[a]))
        pass
    else: 
        file_neme = re.search(r"[0-9]+.mp3", file[0]).group()[:-4] ## get the file id which contains only number 

        sound = pydub.AudioSegment.from_mp3(file[0]) ## read the mp3 file
        sound.export("./wav/"+file_neme, format="wav") ## save the file as .wav
        dic['id'].append(int(file_neme) ## add the file id to dic
        dic['frame_rate'].append(sound.frame_rate) ## add the file frame_rate to dic
        dic['length'].append(len(sound)) ## add the file length to dic

    
df = pd.DataFrame.from_dict(dic)
df.to_csv("./wav/metadata.csv") ## saving the meta files 

df = pd.DataFrame({'missing_data':redo})
df.to_csv("missing_data.csv") ## saving the list of the missing files
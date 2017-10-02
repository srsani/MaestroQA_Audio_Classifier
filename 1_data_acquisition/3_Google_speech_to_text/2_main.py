'''
Depending how many files needs to be processed, this scrip runs 1_transcribe.py for as mamy audio files that are avalile. 
Save the txt file to a local drive.  
'''

import subprocess
import glob
import pandas as pd
import time
from tqdm import tqdm ## great tool to keep track of loop process

files = glob.glob('/home/srs/Desktop/Untitled Folder/wav/*.wav')

info = pd.read_csv('/home/srs/Desktop/Untitled Folder/wav/metadata_missing_data.csv')
info2 = pd.read_csv('/home/srs/Desktop/Untitled Folder/wav/metadata.csv')


for batch in tqdm(range (2000,5690,10)):
    time.sleep(150) 
    
    for file in tqdm((files[batch-10:batch])):

        try:
            metadata = info2[info2.id == int(file[38:-4])]
            #rate = str(metadata.frame_rate.iloc[0])
            size = str(metadata.lenght.iloc[0])
            output = str(metadata.id.iloc[0])
        except:
            metadata = info[info.id == int(file[38:-4])]
            #rate = str(metadata.frame_rate.iloc[0])
            size = str(metadata.lenght.iloc[0])
            output = str(metadata.id.iloc[0])

        #print (file[38:-4],size,rate )
        subprocess.Popen(['python transcribe.py --rate=22050 gs://maestroqa/'+ file[38:-4]+'.wav --size='+size+' --output='+output], shell=True)
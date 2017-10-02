'''
In this code, I am reading two json files into pandas dataframes. 
One of the constrain the link to audio recording on S3 server and in the other json file I have the score for each call. 
So I made df4 that contains all only the scored audio files with the S3 url. 

'''
import pandas as pd
from tqdm import tqdm ## great tool to see the process of your for loop
import requests
import multiprocessing ## great tool to keep track of loop process
from itertools import product


## reading metadata to dataframs.
df = pd.read_json('/Users/srs/Dropbox/GitHub/MaestroQA_Audio_Classifier/Data/voice_comments.json')
df2 = pd.read_json('/Users/srs/Dropbox/GitHub/MaestroQA_Audio_Classifier/Data/voice_gradables.json')
## Seperating the files that have both the S3 and are scored. 
df3 = df[["gradable_id","recording_url"] ]
df4 = df3.dropna()

def download(name, url):

	    response = requests.get(url, stream=True)
	    print (name,url)
	    with open('/Users/srs/Dropbox/GitHub/MaestroQA_Audio_Classifier/Data/mp3/'+str(name)+".mp3", "wb") as handle:
	        for data in tqdm(response.iter_content()):
	            handle.write(data)
    
'''
Downgliding files from S3 is a slow process so I recommend using a PCI SSD or at list and SSD,
 and also all the processing power you have available on your computer. In my case I used 20 cores. 
 '''
if __name__ == '__main__':
	with multiprocessing.Pool(processes=20) as pool:
		results = pool.starmap(download, product(df4['gradable_id'], df4['recording_url']))
  

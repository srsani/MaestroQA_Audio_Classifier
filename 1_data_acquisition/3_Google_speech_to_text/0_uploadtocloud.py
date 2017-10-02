'''
First we need to have all the audio in Google storage. 
This code shows how to send all of the wav files to a bucket. 
'''

from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import json
import glob 
import re
from tqdm import tqdm ## great tool to keep track of loop process


def upload(file):
    bucket = client.get_bucket('bucket name') ## add bucket name
    file_neme = re.search(r'[0-9]+.wav', file).group()
    blob = bucket.blob(file_neme) ## name of the file 
    blob.upload_from_filename(file)
    
if __name__ == '__main__':
    with open('./googleAPI/your credential name.json') as credentials_dict:    
        credentials_dict = json.load(credentials_dict)
    
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict)
    client = storage.Client(credentials=credentials, project='project name') ## add project name
    ## Reading the files in this path to list  
    files = glob.glob("./wav/*.wav")
    ## Upload the files to Google Cloud Buket

    for file in tqdm(files)):
        upload(file)
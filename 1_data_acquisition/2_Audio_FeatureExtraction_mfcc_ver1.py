'''
In this script "python_speech_features" is used to extract mfcc, d_mfcc, fbank_feat, mfcc_pca1 for future
classification and data extraction. All the files are saved as numpy arrays, 

 - 13 mfcc has been extracted from each recording and save them as np array.
 - The audio frame rate that we saved during conversion of mp3 to wav is used in mffcc_feat. 
 - window of 10ms is used for ftt.  

Since this process can be a very slow, I have used pool to utilize 18 processor. 

'''

from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
from python_speech_features import base
import scipy.io.wavfile as wav
from multiprocessing import Pool
import numpy as np
import pandas as pd
from sklearn.decomposition import IncrementalPCA
import numpy as np
import glob
from tqdm import tqdm ## great tool to keep track of loop process
import re

def audio_process(file):
    
    metadata = df_shortcalls[df_shortcalls.gradable_id == int(file[6:-4]) ]
    (rate,sig) = wav.read(file)
    mfcc_feat = mfcc(sig, 
                        samplerate = rate,
                        winlen = 0.1,
                        nfilt=13,
                        numcep=4, 
                        nfft=4096)

    d_mfcc_feat = delta(mfcc_feat, 5)
    fbank_feat = logfbank(sig,rate,nfft = 4096)
    
    X = mfcc_feat
    ipca = IncrementalPCA(n_components=1)
    ipca.fit(X)
    output = ipca.transform(X)
    
    file_neme = re.search(r"[0-9]+.wav", file).group()[:-4] ## get the file id which contains only number and drop the wav
        
    ## Save mfcc
    np.save("./mfcc/"+file_neme+'_'+str(metadata.category.iloc[0])+"_.npy", mfcc_feat)
    ## Save d_mfcc_feat
    np.save("./d_mfcc/"+file_neme+'_'+str(metadata.category.iloc[0])+"_.npy", d_mfcc_feat)
    ## Save fbank_feat
    np.save("./fbank_feat/"+file_neme+'_'+str(metadata.category.iloc[0])+"_.npy", fbank_feat)
    ## Save mfcc_pca
    np.save("./mfcc_pca1/"+file_neme+'_'+str(metadata.category.iloc[0])+"_.npy", output)
    print(fbank_feat.shape[0])
 
if __name__ == '__main__':
    
    files = glob.glob("./wav/*.wav")
    df_shortcalls = pd.read_csv("/home/srs/Desktop/Untitled Folder/df_shortcalls.cvs")


    pool = Pool(18) # on 18 processors
    ## by uising tqdm we can see the progress of our script
    for _ in tqdm.tqdm(pool.map(audio_process, files) , total=len(files)):
        pass
        
    pool.close()
    pool.join()
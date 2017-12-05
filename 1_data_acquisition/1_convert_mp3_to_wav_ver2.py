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
from multiprocessing import Pool

% mkdir ./Data/wav

data = glob.glob("./Data/mp3/*.mp3")
def mp3wav(file):
    
    sound = pydub.AudioSegment.from_mp3(file)
    sound = sound.set_channels(1)
    file_neme_wav = re.search(r"[a-z]+_[0-9]+.mp3", file).group()[:-4]    
    sound.export("./Data/wav/"+"filename_"+file_neme_wav+"_len_"+str(len(sound))+"_rate_"+str(sound.frame_rate)+".wav", format="wav")

if __name__ == '__main__':
    with Pool(processes=28) as pool:
        for i in tqdm((pool.imap_unordered(mp3wav, data))):
            pass
    
    pbar.close()
    pool.close()
    pool.join()
    
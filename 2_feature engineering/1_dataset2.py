'''
Data set2:

Making a dataset with 180 mfcc from each audio file. 
Initially each file was divided to 9 bin and then from each bin, max, min, mean, median and variation was calculated and used as future. 

'''
import pandas as pd
import glob
import numpy as np
from tqdm import tqdm ## great tool to keep track of loop process

##################################################################

def bin_1(array,width):
    bb = round(array.size /width)
    result = (array[:(array.size // bb) * bb].reshape(-1, bb)).transpose()
    return(result)


def element1(array,model):
    if model == 1:
        return (np.min(array))
    if model == 2:
        return (np.max(array))
    if model == 3:
        return (np.mean(array))
    if model == 4:
        return (np.var(array))
    if model == 5:
        return (np.median(array))

def columnname(nbin,nmfcc,nfunc):
    l = []
    l.append('gradable_id')
    for a in range(1,nbin):
        for b in range(1,nmfcc):
            for c in range(1,nfunc):
                l.append('mfcc_'+str(c)+'_m'+str(b)+'_bin'+str(a))
    return(l)

##################################################################
# reading in metadata and also dataset1 to add to add to dataset2	
df_shortcalls = pd.read_csv("/home/srs/Desktop/Untitled Folder/df_shortcalls.cvs")
files = glob.glob("./mfcc/*.npy")
df = pd.read_csv('dataset1_ver3.csv')
##################################################################

dataset2 = pd.DataFrame()
for file in tqdm(files):
    metadata = df_shortcalls[df_shortcalls.gradable_id == int(file[7:-7])]
    gradable_id = metadata.gradable_id.iloc[0]
    
    mfcclist = []
    df2 = pd.DataFrame()


    mfcclist.append(gradable_id)
    
    mfcc = np.load(file)  
    df2 = pd.DataFrame()
    
    metadata2 = df[df.gradable_id == int(file[7:-7])]
    mfcc_len = metadata2.length_mfcc.iloc[0]
    
    for b in range(4):
        df2 = pd.DataFrame()
        mfcc_1 = bin_1(mfcc[:,b],10)

        for a in range(0,9):
            mfcclist.append(element1(mfcc_1[:,a],1))
            mfcclist.append(element1(mfcc_1[:,a],2))
            mfcclist.append(element1(mfcc_1[:,a],3))
            mfcclist.append(element1(mfcc_1[:,a],4))
            mfcclist.append(element1(mfcc_1[:,a],5))

        df2 = pd.DataFrame(mfcclist).transpose()
     
    dataset2 = dataset2.append(df2)

dataset2.columns = columnname(10,6,5)
dataset2.to_csv('dataset2.csv')   
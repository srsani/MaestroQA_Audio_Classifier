'''
To make a first dataset which contains max,min,mean,variance,median, of mfcc 1 to 4
plus: qa_score,gradable_id,category, length_audio and tags from the metadata. 

This file generates dataset1.csv
'''

from multiprocessing import Pool
import numpy as np
import pandas as pd
import glob

def detaset1(file):
    
    mfcc_feat = np.load(file)
    metadata = df_shortcalls[df_shortcalls.gradable_id == int(file[7:-7]) ]


    dic['gradable_id'].append(metadata.gradable_id.iloc[0])
    dic['category'].append(metadata.category.iloc[0])
    dic['qa_score'].append(metadata.qa_score.iloc[0])
    dic['length_audio'].append(metadata.length.iloc[0])
    dic['tags'].append(metadata.tags.iloc[0])


    dic['length_mfcc'].append(mfcc_feat.shape[0])

    dic['mfcc_feat_mean_1'].append((np.mean(mfcc_feat[:,0])))
    dic['mfcc_feat_mean_2'].append((np.mean(mfcc_feat[:,1])))
    dic['mfcc_feat_mean_3'].append((np.mean(mfcc_feat[:,2])))
    dic['mfcc_feat_mean_4'].append((np.mean(mfcc_feat[:,3])))


    dic['mfcc_feat_median_1'].append((np.median(mfcc_feat[:,0])))
    dic['mfcc_feat_median_2'].append((np.median(mfcc_feat[:,1])))
    dic['mfcc_feat_median_3'].append((np.median(mfcc_feat[:,2])))
    dic['mfcc_feat_median_4'].append((np.median(mfcc_feat[:,3])))

    dic['mfcc_feat_max_1'].append((np.max(mfcc_feat[:,0])))
    dic['mfcc_feat_max_2'].append((np.max(mfcc_feat[:,1])))
    dic['mfcc_feat_max_3'].append((np.max(mfcc_feat[:,2])))
    dic['mfcc_feat_max_4'].append((np.max(mfcc_feat[:,3])))

    dic['mfcc_feat_min_1'].append((np.min(mfcc_feat[:,0])))
    dic['mfcc_feat_min_2'].append((np.min(mfcc_feat[:,1])))
    dic['mfcc_feat_min_3'].append((np.min(mfcc_feat[:,2])))
    dic['mfcc_feat_min_4'].append((np.min(mfcc_feat[:,3])))

    dic['mfcc_feat_var_1'].append((np.var(mfcc_feat[:,0])))
    dic['mfcc_feat_var_2'].append((np.var(mfcc_feat[:,1])))
    dic['mfcc_feat_var_3'].append((np.var(mfcc_feat[:,2])))
    dic['mfcc_feat_var_4'].append((np.var(mfcc_feat[:,3])))

###############################################################

if __name__ == '__main__':
    
    dic = {'gradable_id': [], 
       'length_audio':[],
       'length_mfcc':[],
       'category':[],
       'qa_score':[],
       'tags':[],
       
       'mfcc_feat_mean_1':[] ,
       'mfcc_feat_mean_2':[] ,
       'mfcc_feat_mean_3':[] ,
       'mfcc_feat_mean_4':[] ,
       
       'mfcc_feat_median_1':[],
       'mfcc_feat_median_2':[] ,
       'mfcc_feat_median_3':[] ,
       'mfcc_feat_median_4':[] ,
       
       'mfcc_feat_max_1':[] ,
       'mfcc_feat_max_2':[] ,
       'mfcc_feat_max_3':[] ,
       'mfcc_feat_max_4':[] ,
       
       'mfcc_feat_var_1':[] ,
       'mfcc_feat_var_2':[] ,
       'mfcc_feat_var_3':[] ,
       'mfcc_feat_var_4':[] ,
       
       'mfcc_feat_min_1':[] ,
       'mfcc_feat_min_2':[] ,
       'mfcc_feat_min_3':[] ,
       'mfcc_feat_min_4':[]}
    
    for file in files:
        detaset1(file)
    df = pd.DataFrame.from_dict(dic)
    df.to_csv('dataset1.csv')
   
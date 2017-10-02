# Making an Audio Classifier to streamline call Center Management:

During the past year, the price of storage media – and consequently, hard drives - has decreased significantly which has resulted in access to an unprecedented amount of information, that which has never been seen before. As that fact relates to this project, my goal was to streamline the communication strategies for customer service-facing businesses by creating an audio classifier designed to pinpoint instances of problematic communication (“bad” customer service) without requiring the actual listening of individual voice recordings from phone conversations.   

During this project, I worked as a consultant for MaestroQA, a startup company whose goal is to help customer service teams improve the quality of their communications. MaestroQA offers a unique platform to its clients that helps keep track of audio recordings from customer-service based phone conversations. Customer service managers then listen to their support staff’s calls to identify the quality of these communications. Currently, random calls are selected and observed to undergo this quality control process. This is an inefficient approach of finding areas to improve upon, since on average only 10 % of all interactions receive a ‘bad’ quality rating. Additionally, due to the large corpus of recorded calls, only about 1% of all calls can be monitored, leaving 99.9% of the recorded calls unusable for the sake of this project. To streamline this process, and help lead to greater efficiencies, I have developed a model that can predict the ‘bad’ quality calls by an accuracy of 68%. By implementing this model, the efficiency of call screening will improve by nearly one full order of magnitude. Now, not only will MaestroQA be able to help their clients improve upon day to day customer service interactions, they will also be able to help these companies save on internal Human Resource department’s time management by drastically lowering the amount of time spent listening to ‘good’ quality calls.   

Data Description:

-	Recordings of call in mp3 format.
-	Metadata of calls containing the tags that were selected before talking to a customer service representative.
-	The scores of the graded calls. These are the labels which state whether or not a call was ‘good’ or ‘bad’ quality.
<p>

This repository is organized as follows:
-	Visualization:
    - In this section I have looked at the metadata and explained how I went through an under sampling process to get a balanced dataset.

-	Data acquisition:
    - Download the audio files from S3
    - Convert mp3 to wav
    - Extract mfcc, fbank_feat, delta fbank_feat and mfcc_pca1
    - Speech to text with Google API
-	Feature engineering:
    - Dataset1: based on 20 mfcc
    - Dataset2: based on 180 mfcc
    - Sentimental analysis of text data from Google API
-	Modeling:
    - Testing Random Forest Classifier, Gradient Boosting Classifier, Logistic Regression, and K-Nearest Neighbors on the two datasets made in the previous section

For more detailed information regarding how to work with Google Speech to Text API, please visit my post [here](https://medium.com/@RedjaiSani/speech-to-text-using-google-api-f9ad4dff08fe). I have also wrote a blog about my project which can be viewed [here](http://www.redjaisani.com/streamlining-call-center-management.html).  

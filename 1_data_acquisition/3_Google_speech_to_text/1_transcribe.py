'''
This script works extract the text from an audio file and save it to local hard drive as a .txt file.  
'''

def _poll(operation, upper_bounds):
    '''
    Here we are making field Asynchronous so that we can process files that their length exceed 1 minute.
    '''
    n = 0
    while not operation.complete:
        sleep_secs = random.triangular(
            1, 1 + upper_bounds,
            1 + (0.99**n) * upper_bounds)
        n += 1

        logging.debug('Sleeping for %s', sleep_secs)
        time.sleep(sleep_secs)

        operation.poll()
        logging.debug(operation)

    return operation


def transcribe(bucket, path, metadata):
    client = speech.Client()
    l = []

    sample = client.sample(source_uri='gs://{}/{}'.format(bucket, path),
                           encoding=speech.Encoding.LINEAR16,
                           sample_rate_hertz=metadata['rate'])
    operation = sample.long_running_recognize( language_code='en-US', max_alternatives=1)
    file_size_megs = metadata['size'] * 2**-20
    operation = _poll(operation, file_size_megs)


    best_transcriptions = [r.alternatives[0] for r in operation.results if r.alternatives]
    return best_transcriptions, metadata


def main(uris, rate, size,output ):

    for uri in uris:
        logging.info('Transcribing {}'.format(uri))
        bucket, path = uri[5:].split('/', 1)
        transcriptions, metadata = transcribe(bucket, path, {'size': size,'rate': rate,})
        for t in transcriptions:
            out_text = ('({}): {}\n'.format(t.confidence, t.transcript))
            l.append(out_text)
        with open("text"+str(output)+'.txt', "w") as output:
            output.write(str(l))



if __name__ == '__main__':
    from google.cloud import speech
    import argparse
    import logging
    import random
    import time

    l = []
    parser = argparse.ArgumentParser(
        description=__doc__)
    parser.add_argument('gcs_uris',  nargs='+')
    parser.add_argument('--rate', type=int, required=True)
    parser.add_argument('--size', type=int, required=True)
    parser.add_argument('--output', type=str, required=True)
   
    args = parser.parse_args()

    main(args.gcs_uris, args.rate, args.size, args.output)
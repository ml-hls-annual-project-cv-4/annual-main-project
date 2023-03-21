import requests
import os
import random
import numpy as np
import time
from multiprocessing import Pool

def gen_requests_number(lam):
    '''
    Function generates random number from poisson distribution. 
    This number is supposed to be used for define parallel requests quantity
    '''
    return round(np.random.poisson(lam))

def sleep_random_time(lam):
    '''
    Function makes system sleep for random time from poisson distribution
    '''
    time_to_sleep = max(0., np.random.poisson(lam))
    time.sleep(time_to_sleep)
    pass

def choose_random_image():
    random_img_number = random.randint(0,len(os.listdir('datasets/images/train/')))
    return os.listdir('datasets/images/train/')[random_img_number]

def make_reuqest(img_name, predict_service_host = 'http://predict_service:8000'):
    '''
    Function sends POST request to predict_service. 
    Images stored in datasets/images/train/ directory thus it should mounted to docker
    '''
    file = {'selectedFile': open(f'datasets/images/train/{img_name}', 'rb')}
                
    response=requests.request(
        'POST', 
        url=f'{predict_service_host}/uploadfile/',
        files=file)
    
    return response.status_code

def make_parallel_requests(requests_number, sleep_time):
    '''
    Function sends random number of parallel requests then sleeps random seconds
    '''
    requests_number = gen_requests_number(requests_number)
    images = [choose_random_image() for i in range(requests_number)]

    with Pool(requests_number) as pool:
            pool.map(make_reuqest, images)
            
    sleep_random_time(sleep_time)
    pass

while True:
    make_parallel_requests(150, 5)
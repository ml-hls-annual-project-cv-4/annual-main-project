import requests
import os
import random
import numpy as np
import time
from multiprocessing import Pool

class ReqImitation:

    def __init__(self, requests_number, sleep_time, 
                 images_folder='dataset/images/', 
                 predict_service_host = 'https://predict_service:3000'):
        self.requests_number = requests_number
        self.sleep_time = sleep_time
        self.images_folder = images_folder
        self.predict_service_host = predict_service_host
    
    def gen_requests_number(self):
        '''
        Function generates random number from poisson distribution. 
        This number is supposed to be used for define parallel requests quantity
        '''
        return round(np.random.poisson(self.requests_number))

    def sleep_random_time(self):
        '''
        Function makes system sleep for random time from poisson distribution
        '''
        time_to_sleep = max(0., np.random.poisson(self.sleep_time))
        time.sleep(time_to_sleep)
        pass

    def choose_random_image(self):
        random_img_number = random.randint(0, len(os.listdir(self.images_folder)) - 1)
        return os.listdir(self.images_folder)[random_img_number]

    def make_reuqest(self, img_name):
        '''
        Function sends POST request to predict_service. 
        Images stored in dataset/images/ directory thus it should mounted to docker
        '''
        file = {'selected_file': open(f'dataset/images/{img_name}', 'rb')}
                    
        response=requests.request(
            'POST', 
            url=f'{self.predict_service_host}/uploadfile/',
            files=file,
            verify=False)
        
        return response.status_code

    def make_parallel_requests(self):
        '''
        Function sends random number of parallel requests then sleeps random seconds
        '''
        requests_number = np.max([1, self.gen_requests_number()])
        images = [self.choose_random_image() for i in range(requests_number)]

        with Pool(requests_number) as pool:
                pool.map(self.make_reuqest, images)
                
        self.sleep_random_time()
        
    
    pass


if __name__ == '__main__':
            
    reqs = ReqImitation(requests_number=5, sleep_time=5,
                        images_folder='dataset/images/', 
                        predict_service_host = 'https://predict_service:3000')

    while True:
        reqs.make_parallel_requests()

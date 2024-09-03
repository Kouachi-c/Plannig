import pandas as pd
from datetime import datetime
import pygame
import time
from datetime import timedelta


DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

MORNINGS_WAKING_TIME = '05:30'
NIGHT_SLEEPING_TIME = '00:30'
SPORT_TIME = '05:50'
PRAY_TIME = '05:40'
DEPARTURE_TO_SCHOOl_TIME = '07:15'
DEPARTURE_TO_WORK_TIME = '19:10'

musicLoader = pygame.mixer.music

while True :
    time_ = datetime.now()
    my_time = time_.strftime("%I:%M %p")
    print(my_time)
    # # Print the current date and time
    # if my_time == test:
    #     print("OOOOOKKKKK")
    #     break
    # #print("Current date and time:", now)
from dataclasses import dataclass
import datetime
import os 

time = datetime.datetime.today()
date = time.strftime('%d-%m-%Y')
os.mkdir(date)
from datetime import datetime
import pandas as pd

class Bike():
    """A standard Bike Ride Class"""
    def __init__(self):
        """Initialize the Bike object"""
        self.bike_ride_date = ''
        self.bike_num = 0
        self.distance_mi = 0
        self.max_elevation_ft = 0
        self.elevation_gain_ft = 0
        self.elapsed_time_minutes = 0
        self.total_calories = 0
        self.avg_heart_rate_bpm = 0
        self.temperature_f = 0
        self.destination = ''
        self.comments = ''
        self.file_path = "/home/ec2-user/environment/bike/data/bike.csv"
        
        #list of valid bikes
        self.bikes = ['Surly Midnight Special', 'Trek 400', 'Trek Verve', 'Trek 930']
        
        #Load in the data file
        self.load_file(self.file_path)
        
    def load_file(self,file_path):
        """Load in the data file into a dataframe"""
        try:
    
            # read the input file into a dataframe
            df = pd.read_csv(file_path, index_col='bike_ride_number')
    
        except FileNotFoundError:
            print("File " + file_path + " not found. Please check spelling. Names are case sensitive.\n")
    
        else:
            print(df)
            
    def list_bikes(self):
        i=1 #counter
        print('')
        print('Select from the following:')
        for bike in self.bikes:
           print('\t'+str(i)+'. '+bike)
           i += 1
            
#Main Program
myride = Bike().list_bikes()
#myride.list_bikes()
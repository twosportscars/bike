from datetime import datetime
import pandas as pd

class Bike():
    """A standard Bike Ride Class"""
    def __init__(self, bike_ride_date, bike_num, distance_mi, max_elevation_ft, elevation_gain_ft, elapsed_time_minutes, total_calories, avg_heart_rate_bpm, temperature_f, destination, comments='' ):
        """Initialize the Bike object"""
        self.bike_ride_date = bike_ride_date
        self.bike_num = bike_num
        self.distance_mi = distance_mi
        self.max_elevation_ft = max_elevation_ft
        self.elevation_gain_ft = elevation_gain_ft
        self.elapsed_time_minutes = elapsed_time_minutes
        self.total_calories = total_calories
        self.avg_heart_rate_bpm = avg_heart_rate_bpm
        self.temperature_f = temperature_f
        self.destination = destination
        self.comments = comments
        self.file_path = "/home/ec2-user/environment/bike/data/bike.csv"
        
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
            
#Main Program
myride = Bike('4/20/2021',1,10.3,500,600,70,490,121,71,'Preston')
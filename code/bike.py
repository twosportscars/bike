import pandas as pd

class Bike():
    """A standard Bike Ride Class"""
    def __init__(self):
        """Initialize the Bike object"""
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
            self.df = pd.read_csv(file_path, index_col='bike_ride_number')
    
        except FileNotFoundError:
            print("File " + file_path + " not found. Please check spelling. Names are case sensitive.\n")
    
        else:
            print(self.df)
            # print(self.df.info())
            self.num_rows = self.df.shape[0]
            
    def list_bikes(self):
        """Lists out the available bikes and their position in the list."""
        i=1 #counter
        print('')
        print('Select from the following:')
        for bike in self.bikes:
           print('\t'+str(i)+'. '+bike)
           i += 1
           
    def calc_avg_speed(self,miles,minutes):
        """calculate the average speed"""
        return (miles / minutes * 60)
           
    def append_ride(self):
        """appends a new ride to the file"""
        self.num_rows += 1
        print('\nThis is ride #: '+ str(self.num_rows)+'\n')
        self.bike_ride_date = input('Enter the date of the ride, format mm/dd/yyyy: ' )
        self.list_bikes()
        self.bike_num = int(input('Enter the number of the bike you rode: '))
        self.bike_model = self.bikes[self.bike_num-1]
        self.distance_mi = float(input('Enter the number of miles you rode: '))
        self.max_elevation_ft = int(input('Enter the max elevation in feet: '))
        self.elevation_gain_ft = int(input('Enter the elevation gain in feet: '))
        self.elapsed_time_minutes = int(input('Enter the elapsed time in minutes: '))
        self.total_calories = int(input('Enter the total calories burned: '))
        self.avg_heart_rate_bpm = int(input('Enter the average heart rate (bpm): '))
        self.temperature_f = int(input('Enter the temperature in F: '))
        self.destination = input('Enter the destination: ')
        self.comments = input('Enter any comments or hit ENTER to continue: ')
        
        # Calculate the average speed
        self.avg_speed_mph = self.calc_avg_speed(self.distance_mi, self.elapsed_time_minutes)
        # print(self.avg_speed_mph)
        
        # Print out the result and give them an opportunity to abort if data is not good
        print('\nHere are your inputs:\n')
        print('Date of the ride: ' + self.bike_ride_date)
        print('Bike Model ridden: ' + self.bike_model)
        print('Miles ridden: ' + str(self.distance_mi))
        print('Max Elevation in Feet: ' + str(self.max_elevation_ft))
        print('Elevation gain in Feet: ' + str(self.elevation_gain_ft))
        print('Elapsed time in minutes: ' + str(self.elapsed_time_minutes))
        print('Calculated average speed: ' + str(self.avg_speed_mph))
        print('Total calories burned: ' + str(self.total_calories))
        print('Average heart rate (bpm): ' + str(self.avg_heart_rate_bpm))
        print('Average temperature (F): ' + str(self.temperature_f))
        print('Destination: ' + self.destination)
        print('Comments: ' + self.comments)
        print()
        response = input('Are these correct (y/n): ')
        if response == 'y':
            print('\nGetting ready to append file, here is the new dataset: \n')
            self.df.loc[str(self.num_rows)] = [self.bike_ride_date, self.bike_model, self.distance_mi, self.max_elevation_ft, self.elevation_gain_ft, self.elapsed_time_minutes,self.avg_speed_mph,
            self.total_calories, self.avg_heart_rate_bpm, self.temperature_f, self.destination, self.comments]
            print(self.df)
            
            
            #write the data frame back out
            self.df.to_csv(self.file_path,index=True)
            print('\nProgram Ended, re-run to add another ride.')
            
        else:
            print('\nAborting -- re-run to start over for this ride.')
         
 

#Main Program
Bike().append_ride()

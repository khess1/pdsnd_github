##Import packages 
import time
import pandas as pd
import numpy as np

##User input setup:
#Create dictionary of city names along with .csv files that contain data for each of the cities
cities = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Create list of month names
months = ['all','january','february','march','april','may','june'] 

#Create list of day names
days = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

#Create list of answer choices
answers = ['no']

##Create function that filters the data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day to filter by, or "all" to apply no day filter
    """
	
    print("\nHello! Let\'s explore some US bikeshare data!\n")
	
    #Get user input for city - either 'new york city', 'washington', or 'chicago'  
    while True: 
        city = input("\nWhich city would you like to see data for? Please enter either 'new york city', 'washington', or 'chicago'.\n").lower() #INPUT MUST BE IN LOWERCASE LETTERS
        if city in cities:
            break
        else:
            print("\nInvalid input. Please enter a valid city - either new york city, washington, or chicago.")

    #Get user input for month - either 'january', 'february', 'march', 'april', 'may', 'june', or 'all' if they do not wish to filter by a specific month 
    while True:
        month = input("\nWould you like to see data for a particular month? If so, please enter either 'january', 'february', 'march', 'april', 'may', or 'june'. If you do not wish to see data for a particular month, please enter 'all'.\n").lower() #INPUT MUST BE IN LOWERCASE LETTERS          
        if month in months:
            break
        else:
            print("\nInvalid input. If you would like to see data for a particular month, please enter a valid month - either 'january', 'february', 'march', 'april', 'may', or 'june'. If you do not wish to see data for a particular month, please enter 'all'.\n")
            
    #Get user input for day - either 'sunday', 'monday, 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', or 'all' if they do not wish to filter by a specific day   
    while True:
        day = input("\nWould you like to see data for a particular day? If so, please enter either 'sunday', 'monday', 'tuesday', 'wednesday, 'thursday', 'friday', 'saturday', or 'sunday'. If you do not wish to see data for a particular day, please enter 'all'.\n").lower() #INPUT MUST BE IN LOWERCASE LETTERS
        if day in days:
            break
        else:
            print("\nInvalid input. If you would like to see data for a particular day, please enter a valid day - either 'sunday', 'monday', 'tuesday', 'wednesday, 'thursday', 'friday', 'saturday', or 'sunday'. If you do not wish to see data for a particular day, please enter 'all'.\n")

    print('-'*40)
    return city, month, day

##Create function that loads the filtered data
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day (if applicable).

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day to filter by, or "all" to apply no day filter
    
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day (if applicable)
    """

    #Reads city data into a dataframe
    df = pd.read_csv(cities[city])
	
    #Convert 'Start Time' and 'End Time' columns into datetime format 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Create new column called 'month' 
    df['month'] = df['Start Time'].dt.month 
    
    #Create new column called 'day' 
    df['day'] = df['Start Time'].dt.weekday_name

    #Create new column called 'hour' 
    df['hour'] = df['Start Time'].dt.hour
    
    #Create filter by month (if applicable)
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Create filter by day (if applicable)
    if day != 'all':
        
        #Filter by day to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

##Create function that displays travel time statistics
def time_stats(df):
    """Displays statistics on travel times."""
    
    #Get user input for seeing data on the most popular travel times: 
        #If 'yes' and the data is not filtered by either month or day, the loop will print data on the most popular month, day, and hour to travel. 
        #If 'yes' and the data is filtered by month but not by day, the loop will print data on the most popular day and hour to travel. 
        #If 'yes' and the data is not filtered by month but is filtered by day, the loop will print data on the most popular month and hour to travel. 
        #If 'yes' and the data is filtered by both month and day, the loop will print data on the most popular hour to travel. 
        #If 'no', the loop will break and move on to the next question.
    while True:
        answer = input("\nWould you like to see data on the most popular travel times? Please enter either 'yes' or 'no'.\n")
        if answer in answers:
            break
  
        else:
            print("\nCalculating Statistics on Travel Times...")
            start_time = time.time()
        
        #Display the most popular month (if applicable)
        if len(df['month'].unique()) > 1: 
            most_popular_month = df['month'].mode()[0]
    
            if most_popular_month == 1:
                print("\nThe most popular month to travel is: January")
            elif most_popular_month == 2:
                print("\nThe most popular month to travel is: February")
            elif most_popular_month == 3:
                print("\nThe most popular month to travel is: March")
            elif most_popular_month == 4:
                print("\nThe most popular month to travel is: April")
            elif most_popular_month == 5:
                print("\nThe most popular month to travel is: May")
            elif most_popular_month == 6:
                print("\nThe most popular month to travel is: June")
        
        #Display the most popular day
        if len(df['day'].unique()) > 1: 
            most_popular_day = df['day'].mode()[0]

            if most_popular_day== 'Sunday':
                print("\nThe most popular day to travel is: Sunday")
            elif most_popular_day == 'Monday':
                print("\nThe most popular day to travel is: Monday")
            elif most_popular_day == 'Tuesday':
                print("\nThe most popular day to travel is: Tuesday")
            elif most_popular_day == 'Wednesday':
                print("\nThe most popular day to travel is: Wednesday")
            elif most_popular_day == 'Thursday':
                print("\nThe most popular day to travel is: Thursday")
            elif most_popular_day == 'Friday':
                print("\nThe most popular day to travel is: Friday")
            elif most_popular_day == 'Saturday':
                print("\nThe most popular day to travel is: Saturday")
            elif most_popular_day == 'Sunday':
                print("\nThe most popular day to travel is: Sunday")

        #Display the most popular hour       
        most_popular_hour = df['hour'].mode()[0]
    
        if most_popular_hour == 0:
            print("\nThe most popular hour to travel is: 12 AM")
        elif most_popular_hour == 1:
            print("\nThe most popular hour to travel is: 1 AM")
        elif most_popular_hour == 2:
            print("\nThe most popular hour to travel is: 2 AM")
        elif most_popular_hour == 3:
            print("\nThe most popular hour to travel is: 3 AM")
        elif most_popular_hour == 4:
            print("\nThe most popular hour to travel is: 4 AM")
        elif most_popular_hour == 5:
            print("\nThe most popular hour to travel is: 5 AM")
        elif most_popular_hour == 6:
            print("\nThe most popular hour to travel is: 6 AM")
        elif most_popular_hour == 7:
            print("\nThe most popular hour to travel is: 7 AM")
        elif most_popular_hour == 8:
            print("\nThe most popular hour to travel is: 8 AM")
        elif most_popular_hour == 9:
            print("\nThe most popular hour to travel is: 9 AM")
        elif most_popular_hour == 10:
            print("\nThe most popular hour to travel is: 10 AM")
        elif most_popular_hour == 11:
            print("\nThe most popular hour to travel is: 11 AM")
        elif most_popular_hour == 12:
            print("\nThe most popular hour to travel is: 12 PM")
        elif most_popular_hour == 13:
             print("\nThe most popular hour to travel is: 1 PM")
        elif most_popular_hour == 14:
             print("\nThe most popular hour to travel is: 2 PM")
        elif most_popular_hour == 15:
             print("\nThe most popular hour to travel is: 3 PM")
        elif most_popular_hour == 16:
             print("\nThe most popular hour to travel is: 4 PM")
        elif most_popular_hour == 17:
             print("\nThe most popular hour to travel is: 5 PM")
        elif most_popular_hour == 18:
             print("\nThe most popular hour to travel is: 6 PM")
        elif most_popular_hour == 19:
             print("\nThe most popular hour to travel is: 7 PM")
        elif most_popular_hour == 20:
             print("\nThe most popular hour to travel is: 8 PM")
        elif most_popular_hour == 21:
             print("\nThe most popular hour to travel is: 9 PM")
        elif most_popular_hour == 22:
             print("\nThe most popular hour to travel is: 10 PM")
        elif most_popular_hour == 23:
             print("\nThe most popular hour to travel is: 11 PM")

        print("\nThis took %s seconds.\n" % (time.time() - start_time))
        print('-'*40)
        
        break

##Create function that displays station statistics
def station_stats(df):
    """Displays statistics on stations."""
    
    #Get user input for seeing data on the most popular stations: 
        #If 'yes', the loop will print data on the most popular start station, end station, and combination of start and end stations.
        #If 'no', the loop will break and move on to the next question.
    while True:
        answer = input("\nWould you like to see data on the most popular stations? Please enter either 'yes' or 'no'.\n").lower()
        
        if answer in answers:   
            break   
            
        else:
            print("\nCalculating Statistics on Stations...")
            start_time = time.time()

            #Display the most popular start station
            print("\nThe most popular start station is:\n", df['Start Station'].mode()[0])
            
            #Display the most popular end station
            print("\nThe most popular end station is:\n", df['End Station'].mode()[0])
            
            #Display the most popular combination of start and end stations
            df['combination'] =  df['Start Station'] + ',' + " " + df['End Station']
            print("\nThe most popular combination of start and end stations is:\n", df['combination'].mode()[0])
            
            print("\nThis took %s seconds.\n" % (time.time() - start_time))
            print('-'*40)
            
            break

##Create function that displays trip duration statistics            
def trip_duration_stats(df):
    """Displays statistics on trip duration."""
    
     #Get user input for seeing data on average and total travel times: 
        #If 'yes', the loop will print data on both average and total travel times. 
            #If either the average, total, or both are less than 60 minutes, the loop will display the data in minutes. 
            #If either the average, total, or both are more than 60 minutes, the loop will display the data in hours.
        #If 'no', the loop will break and move on to the next question.
    while True:
        answer = input("\nWould you like to see data on average and total travel times? Please enter either 'yes' or 'no'.\n").lower()
        
        if answer in answers:
            break   
            
        else:
    
            print("\nCalculating Statistics on Trip Duration...")
            start_time = time.time()
            
            #Display average travel time
            average_travel_time_minutes = int(df['Trip Duration'].mean() / 60) #Divide by 60 to get answer in minutes
            average_travel_time_hours = int(average_travel_time_minutes / 60) #Divide by 60 to get answer in hours
            
            if average_travel_time_minutes < 60:
                print("\nThe average travel time is:", average_travel_time_minutes, "minutes")
            else:
                print("\nThe average travel time is:", average_travel_time_hours, "hours")
    
            #Display total travel time
            total_travel_time_minutes = int(df['Trip Duration'].sum() / 60) #Divide by 60 to get answer in minutes
            total_travel_time_hours = int(total_travel_time_minutes / 60) #Divide by 60 to get answer in hours
            
            if total_travel_time_minutes < 60:
                print("\nThe total travel time is:", total_travel_time_minutes, "minutes")
            else:
                print("\nThe total travel time is:", total_travel_time_hours, "hours")
    
            print("\nThis took %s seconds.\n" % (time.time() - start_time))
            print('-'*40)
            
            break

##Create function that displays user statistics
def user_stats(df):
    """Displays statistics on users."""
    
    #Get user input for seeing data on users: 
        #If 'yes', the loop will print data on user types, gender (if available), and birth years (if available). 
        #If 'no', the loop will break and move on to the next question.
    while True:
        answer = input("\nWould you like to see data on users? Please enter either 'yes' or 'no'.\n").lower()
        
        if answer in answers:
            break   
            
        else:
    
            start_time = time.time()
            print("\nCalculating Statistics on Users...")

            #Display user type counts
            print("\nUser Type:")
            print(df['User Type'].value_counts()) 
  
            #Display gender counts (if available)
            if 'Gender' in df:  
                print("\nGender:")
                print(df['Gender'].value_counts()) 
                
            else:
                print("\nStatistics on gender is not available for this city.\n")
       
            #Display earliest, most recent, and most popular birth year (if available)
            if 'Birth Year' in df:
                print("\nBirth Years:")
                earliest_birth_year = int(df['Birth Year'].min())
                print("The earliest birth year on record is:", earliest_birth_year)
                most_recent_birth_year = int(df['Birth Year'].max())
                print("The most recent birth year on record is:", most_recent_birth_year)
                most_common_birth_year = int(df['Birth Year'].mode()[0])
                print("The most common birth year on record is:", most_common_birth_year)
	
            else:
                print("\nStatistics on birth years is not available for this city.\n")

            print("\nThis took %s seconds.\n" % (time.time() - start_time))
            print('-'*40)
            
            break

##Create function that displays raw data                         
def raw_data(df):
    """Displays raw data."""
    
    #Get user input for seeing the raw data: 
        #If 'yes', the loop will print the first five rows of the raw data.
        #If 'no', the loop will break and move on to the next question.
    while True:
        answer = input("\nWould you like to see the raw data? Please enter either 'yes' or 'no'.\n").lower()
        if answer in answers:
            break
  
        else:
            print("\nGetting the raw data...")
            start_time = time.time()
            
            #Display first five rows of the raw data 
            count = 0
            while (answer not in answers):
                print(df.iloc[count:count+5])
                #Display another five rows of the raw data 
                count += 5
                 #Get user input for seeing more raw data: 
                     #If 'yes', the loop will print the next five rows of the raw data (this process will continue until the user specifies "no")
                     #If 'no', the loop will break and move on to the next question.
                answer = input("\nWould you like to continue seeing more raw data? Please enter either 'yes' or 'no'.\n").lower()
                
            print("\nThis took %s seconds.\n" % (time.time() - start_time))
            print('-'*40)
            
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        #Get user input for seeing data on another city: 
            #If 'yes', the process will restart and the user will be asked to input the name of another city.
            #If 'no', the loop will break.
        another_city = input("\nWould you like data for another city? Please enter either 'yes' or 'no'.\n")
        if another_city.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

                
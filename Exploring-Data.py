import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('\n please select the city you want to know information about it,is it Chicago, Washington, New York city,all.\n').lower()
        if city not in ('all','chicago','washington','new york city'):
            print ('sorry,in valid input,try again.')
            continue
        else:
             break
    while True:
        month=input ('\n please select the month you want\n').lower()
        if month not in ('january','february','march','april','may','june','all'):
            print( 'sorry, invalid input, please try again ')
            continue
        else:
            break
    while True:
        day=input ('\n please select the day you want \n').lower()
        if day not in ('saturday','sunday','monday','tuesday','wednesdy','thursday','all'):
            print('sorry,invalid input, please try again ')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data from csv files.
    
    df=pd.read_csv(CITY_DATA[city.lower()])
    
    # convert Start Time columne into datetime.
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # extract month into new columne                                  
    df['month']=(df['Start Time'].dt.month)
    # extract days into new columne              
    df['day_of_week']=(df['Start Time'].dt.day_name)  

          
     # filter data by month  
    if month != 'all':
       months=['january','february','march','april','may','june']
       month=months.index(month)+1
       df=df[df['month']==month]
       
     # filter data by days  
    if day != 'all':
       df=df[df['day_of_week']==day.title()]
       
                                                                        
     # end of function
    return df


 # Asking user if he want to see some rows of data before filteration


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    the_common_month=df['month'].mode()
    print('the common month is : ',the_common_month)


    # TO DO: display the most common day of week
    the_common_day=df['day_of_week'].mode()
    print('the common day is : ',the_common_day)


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    the_common_hour=df['hour'].mode()
    print('the common hour is : ', the_common_hour)          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()
    print('the most commonly used start station is: ',common_start)               


    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()
    print('the most commonly used end station is: ',common_end)            


    # TO DO: display most frequent combination of start station and end station trip
    combination=(df['Start Station']+df['End Station']).mode()
    print('most frequent combination of start station and end station trip is: ',combination)           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('total travel time is: ',total_time/3600,'hour')               


    # TO DO: display mean travel time
    the_mean=df['Trip Duration'].mean()               
    print('mean travel time is: ',the_mean/60,'min')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('counts of user types are: ', user_type)              


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender=df['Gender'].value_counts()              
        print('counts of gender are: ',gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:

        earliest=(df['Birth Year'].min())
    
        print('the earliest year of birth is : ',earliest)   
       
        most_recent=(df['Birth Year'].max())
    
        print('the recent year of birth is: ', most_recent)    
            
        global common_year
        common_year=(df['Birth Year'].mode())
    
        print('the common year of birth is: ',common_year)   
    else:
         print('Birth Year information cannot be calculated because it does not appear in the dataframe')         

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    
   while True:       
        view_data= input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc=0
        if view_data=="no":
         break
        if view_data== 'yes':
          print(df.iloc[0:5])
        while True:
         view_display = input("Do you wish to continue?:Enter yes or no ").lower()
         if view_display=="yes":
          start_loc += 5
         print(df.iloc[start_loc:start_loc+5])
         if view_display =='no':
          break
        break
            
    


    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

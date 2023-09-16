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
    cities = ['Chicago' , 'New York City', 'wWshington']
    while True:
        city = input("please enter a city from the listed cities: ").lower()
        if city not in CITY_DATA.keys():
            print("Please enter a correct city")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january' , 'february', 'march' , 'april' , 'may' , 'june']
    while True:
        month = input("Please enter a month:").lower()
        if month not in months:
            print("Please re-enter a month fron january to june:")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday' , 'tuesday', 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']
    while True:
        day = input('Please enter a day: ').lower()
        if day not in days:
            print('Please re-enter a day fron the list:')
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
    df = pd.read_csv(CITY_DATA[city]) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        if day != 'all':
            df= df[df['day_of_week'] == day.title()] 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month is: {common_month}")

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day is: {common_day}")

    # TO DO: display the most common start hour
    common_start_hour = df['start_hour'].mode()[0]
    print(f"The most common start hour is: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most common start station is: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most common End station is: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station_trip'] = df['Start Station'] + 'to' + df['End Station']
    common_combination_station= df['combination_station_trip'].mode()[0]
    print(f"The most frequent combination of Start Station and End Station trip is: {common_combination_station}") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df["Trip Duration"].sum()
    print(f"The total travel time is:{total_travel_time} seconds \n The total travel time is:{total_travel_time/60} minutes\n The total travel time is:{total_travel_time/3600} hours") 
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(f"The mean travel time is:{mean_travel_time} seconds \n The mean travel time is:{mean_travel_time/60} minutes\n The mean travel time is:{mean_travel_time/3600} hours")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df["User Type"].value_counts()
    print(f"The counts_of_user_types are: {counts_of_user_types}")

    # TO DO: Display counts of gender

    try:
        gender = df['Gender'].value_counts()
        print(f"The counts of users by gender are :{gender}")
    except:
        print("There is no 'Gender' column in this city.")
    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\nThe most common year of birth: {common_year}")                                
    
    except:
           print("There are no birth year details in this city.")    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df) :
    start_point = 0
    view_data = input ('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    while True :
        if view_data == "no" :
            break 
        print (df[start_point:start_point+5])
        view_data = input("Do you wish to continue?: ").lower()     
        start_point +=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

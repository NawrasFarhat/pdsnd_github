import time
import pandas as pd
import numpy as np
#hello i am nawras
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in cities:
            break
        else:
            print("Invalid input. Please enter either Chicago, New York City, or Washington.")
    
    while True:
        month = input("Which month? January, February, March, April, May, June or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month from January to June or 'all'.")
    
    while True:
        day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day of the week or 'all'.")
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    Months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = df['month'].mode()[0]
    print('Most Common Month:', Months[common_month - 1])
    
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', common_day)
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)
    
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
    
    df['Start-End Combo'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Start-End Combo'].mode()[0]
    print('Most Frequent Combination of Start and End Station:', common_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_duration = df['Trip Duration'].sum()
    print('Total Travel Time:', total_duration)
    
    mean_duration = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_duration)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('Counts of User Types:\n', df['User Type'].value_counts())
    
    if 'Gender' in df.columns:
        print('\nCounts of Gender:\n', df['Gender'].value_counts())
    else:
        print("No gender data available for this city.")
    
    if 'Birth Year' in df.columns:
        print('\nEarliest Year of Birth:', int(df['Birth Year'].min()))
        print('Most Recent Year of Birth:', int(df['Birth Year'].max()))
        print('Most Common Year of Birth:', int(df['Birth Year'].mode()[0]))
    else:
        print("No birth year data available for this city.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    while True:
        view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no: ').lower()
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5

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

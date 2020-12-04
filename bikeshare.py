#bikeshare python project :)
# Arwa Alfalij :)

# the links that help for solving project:
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html
#https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column
#https://stackoverflow.com/questions/1016814/what-to-do-with-unexpected-indent-in-python
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
    city = input("\n  please input either chicago, new york city, washington to analyze data? \n").lower()
    while city.lower() not in CITY_DATA:
        city = input("please try again, and input either chicago, new york city, washington to analyze data \n").lower()
        
           


    # TO DO: get user input for month (all, january, february, ... , june)
    # how: i should to be sure the user will write a  month  not any things else ,and the month from the list :(all, january, february, ... , june) so I will use while loop her also
    month_list = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month=input("\n  please inter the month from the list:(january, february,march,april,may, june) or all  to analyze data? \n").lower()
    while month not in month_list:
     month = input("please try again and inter the month from the list:(january, february,march,april,may, june) or all \n").lower()
      
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # how: i want  to be sure the user will write a  month not invalid input for example  cat  (all, monday, tuesday, ... sunday) so I will use while loop her also
    day_listm=['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

    day=input("please enter day  to analyze?\n").lower()
    while day not in day_listm:
         day=input("please try to enter correct day  to analyze ?\n").lower()
     


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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   #  month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month 
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
         
        
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    commonMonth = df['month'].mode()[0]
    print("The most common month is: ",commonMonth)


    # TO DO: display the most common day of week
    commonDay = df['day_of_week'].mode()[0]
    print("The most common day of week is: ",commonDay)

    # TO DO: display the most common start hour
    commonHour = df['hour'].mode()[0]

    print('Most common Start Hour:', commonHour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # AS IN commonDay,commonHour,commonMonth i can use mode to find most common number in a data set,that used in practice of project but  i want  try to use value_counts()[:1].sort_values(ascending=False) to diversification  the uses of functions 
    commonStartStation = df['Start Station'].value_counts()[:1].sort_values(ascending=False)
    print("The most commonly used start station: " , commonStartStation.to_string())


    # TO DO: display most commonly used end station
    # AS in above I can  find common by mode() and value_counts()[:1].sort_values(ascending=False) now i want try to use  value_counts().idxmax() which will work same, to diversification  the uses of functions  
    commonEndStation = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station : " , commonEndStation)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + ' - ' + df['End Station']
    commonCombination = df['frequent_combination'].mode()[0]
    print(" most frequent combination of start station and end station trip : ", commonCombination)  
    
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

  # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print("The total travel time  is: " ,total_trip)

    # TO DO: display mean travel time
    average_trip  = df['Trip Duration'].mean()
    print("The mean travel time  is: " ,average_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userCount = df['User Type'].value_counts()
    print("The mean travel time  is: " ,userCount)
    


    # TO DO: Display counts of gender
    # Testing if the column name exists in the columns in the data frame,since "Washington" does not have all the columns
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        genderCount = df['Gender']
        print("counts of gender:",genderCount.value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print('Earliest birth is: \n',earliest)   
        recent= df['Birth Year'].max()
        print('Most recent birth is: \n',recent)
        most = df['Birth Year'].mode()[0]
        print('Most common birth is:\n',most )
    # print:   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_5_raw_data(df):
     """Display 5 raws data if user request.
     Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
     """
     raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n').lower()
     if raw_data !='yes':
        return
         
     print(df.head())
     after=0
     while True:
          raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n').lower()
          if raw_data != 'yes':
             break
                
          after = after + 5
          print(df.iloc[after:after+5])
          continue
      
     


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_5_raw_data(df)
        
            
        
        
       
                
            
               

        again = input('\nWould you like to restart? Enter yes or no.\n')
        if again.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

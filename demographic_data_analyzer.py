import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male = df[df['sex'] == 'Male']
    average_age_men = male['age'].mean().round(decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = len(df[df['education'] == 'Bachelors'])
    total_people = len(df)
    percentage_bachelors = round((bachelors/total_people)*100, 1) 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    lower_education = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])  
    higher_education_count = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')])
    lower_education_count = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')])  
    
    # percentage with salary >50K
    higher_education_rich = round((higher_education_count/higher_education)*100, 1)
    lower_education_rich = round((lower_education_count/lower_education)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_min_work_hours = df[df['hours-per-week'] == df['hours-per-week'].min()]
    num_min_workers = df_min_work_hours[df_min_work_hours['salary'] == '>50K'].shape[0]
    rich_percentage = num_min_workers/df_min_work_hours.shape[0] * 100

    # What country has the highest percentage of people that earn >50K?
    above_50K_by_country = df[df['salary'] == '>50K'].groupby(['native-country']).size()
    total_by_country = df.groupby(['native-country']).size()
    percentage_by_country = (above_50K_by_country/total_by_country)*100
    highest_earning_country = percentage_by_country.idxmax()
    highest_earning_country_percentage = round(percentage_by_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India
    IN_above_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    groupby_occupation = IN_above_50k.groupby('occupation').size()
    top_IN_occupation = groupby_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


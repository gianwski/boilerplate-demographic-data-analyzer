import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df["race"].value_counts())

    # What is the average age of men?
    average_age_men = df.groupby("sex")["age"].mean().loc["Male"]
    average_age_men = round(average_age_men, 1)
  
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df["education"].value_counts(normalize=True) * 100).loc["Bachelors"]
    percentage_bachelors = round(percentage_bachelors, 1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
   
    df_higher_education = df[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")]
    df_higher_education_rich = df_higher_education[df_higher_education["salary"] == ">50K"]
    higher_education_rich = df_higher_education_rich.shape[0] / df_higher_education.shape[0] * 100
    higher_education_rich = round(higher_education_rich, 1)
       
    # What percentage of people without advanced education make more than 50K?
    
    df_lower_education = df[(df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")]
    df_lower_education_rich = df_lower_education[df_lower_education["salary"] == ">50K"]
    lower_education_rich = df_lower_education_rich.shape[0] / df_lower_education.shape[0] * 100
    lower_education_rich = round(lower_education_rich, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df["education"].value_counts(normalize=True) * 100).loc[["Bachelors", "Masters", "Doctorate"]].sum()
    lower_education = 100 - higher_education
    
    # percentage with salary >50K
    higher_education_rich = higher_education_rich
    lower_education_rich = lower_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df_num_min_workers = df[df["hours-per-week"] == min_work_hours]
    N_num_min_workers = df_num_min_workers.shape[0]
    N_num_min_workers_rich = df_num_min_workers[df_num_min_workers["salary"] == ">50K"].shape[0]
    rich_percentage = N_num_min_workers_rich / N_num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    df_rich = df[df["salary"] == ">50K"]
    country_counts = df["native-country"].value_counts()
    rich_country_counts = df_rich["native-country"].value_counts()
    rich_country_percentage = (rich_country_counts / country_counts) * 100
    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = rich_country_percentage.max()
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_India_rich = df_rich[df_rich["native-country"] == "India"]
    top_IN_occupation = df_India_rich["occupation"].value_counts().idxmax()

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

import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degrees
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df['education'].isin(advanced_education)
    lower_edu = ~higher_edu

    higher_edu_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    # 5. Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich percentage among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest percentage of >50K earners
    country_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    country_percent = (country_earning / country_total * 100).dropna()
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    # 8. Top occupation in India for >50K earners
    india_earnings = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_earnings['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:
", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_edu_rich)
        print("Percentage without higher education that earn >50K:", lower_edu_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

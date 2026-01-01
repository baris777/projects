import pandas as pd
from pathlib import Path

data_path = Path("data/cleaned/escs_trend_cleaned.csv")
df = pd.read_csv(data_path)

def main():
    while True:
        print("PISA Data Explorer")
        print("-" * 20)
        print("\nMenu\n" \
        "1) Country Codes\n" \
        "2) One Country Over Time\n" \
        "3) Compare Multiple Countries\n" \
        "0) Exit\n")
        a = input("Choice: ")
        if a == "1":
            get_cnt_codes()
        elif a == "2":
            cnt_code = input("Please enter the country code: ")
            print()
            cnt_over_time(df, cnt_code)
            print()
        elif a == "3":
            cnt_first = input("Please enter the first country: ")
            cnt_second = input("Please enter the second country: ")
            cnt_year = input("Please enter the year (2015, 2018 or 2022): ")
            print()
            comp_cnt(cnt_first, cnt_second, cnt_year)
            print()
        elif a == "0":
            break
        else:
            print("Please enter a valid input!\n")
            continue

def sum_data(df):
    avg = df.groupby(["Year", "Country"], as_index=False)[
        ["Overall Social Status", "Parents' Occupation", 
         "Home Possessions", "Parents' Education"]].mean()
    return avg

def get_cnt_codes():
    avg = sum_data(df)
    countries = avg["Country"].drop_duplicates().to_list()
    print("\nCountry Codes: \n")
    for i in range(0, len(countries), 20):
        print(", ".join(countries[i:i+20]))
    print()

def cnt_over_time(df, country_code):
    avg = sum_data(df)
    code = country_code.strip().upper()
    out = (avg[avg["Country"].astype(str).str.upper() == code]
           .sort_values("Year")
           .reset_index(drop=True))
    
    print(out[[
        "Year", "Country", "Overall Social Status", 
        "Parents' Occupation", "Home Possessions", "Parents' Education"]])

def comp_cnt(first_country, second_country, country_year):
    avg = sum_data(df)
    c1 = first_country.strip().upper()
    c2 = second_country.strip().upper()
    year = int(country_year)
    if year not in avg["Year"].unique():
        print("Year not found!")
        return
    if c1 not in avg["Country"].str.upper().unique() or c2 not in avg["Country"].str.upper().unique():
        print("Country not found")
        return
    out = avg[
           (avg["Year"] == int(country_year)) &
           (avg["Country"].str.upper().isin([c1,c2]))
           ]
    print(out)

if __name__ == "__main__":
    main()
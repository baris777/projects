import pandas as pd

# I wrote this function to clean and standardize PISA 
# trend data so that it would be ready for analysis.

def clean_data():
    df = pd.read_csv(r"C:/Users/Asus/Desktop/portfolio/pisa_trend_analysis/data/raw/escs_trend.csv")

    # The raw file contains many columns, but for this analysis I only kept:
    # the PISA cycle, country code, OECD indicator, and the trend data
    cols = ["cycle","cnt","oecd","escs_trend","hisei_trend","homepos_trend","paredint_trend"]
    df = df[cols].copy()

    # Some numeric columns may contain invalid values. Thus, I explicitly 
    # converted them to numeric and forced invalid entries to NaN.
    numeric_cols = ["escs_trend","hisei_trend","homepos_trend","paredint_trend"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    # I converted cycle and oecd to numeric first, then store them as Int64.
    # This allows missing values without breaking the data type.
    df["cycle"] = pd.to_numeric(df["cycle"], errors="coerce").astype("Int64")
    df["oecd"]  = pd.to_numeric(df["oecd"],  errors="coerce").astype("Int64")

    # I dropped rows with missing essential fields and 
    # removed extreme ESCS trend values to avoid distortion.
    df = df.dropna(subset=["cycle", "cnt", "escs_trend"])
    df = df[df["escs_trend"].between(-5, 5)]

    # I translated codes into clear language.
    cycle_map = {5: 2015, 6: 2018, 7: 2022}
    oecd_map  = {0: "OECD", 1: "Non-OECD"}

    # I printed out any values that failed to map correctly.
    df["cycle"] = df["cycle"].replace(cycle_map).astype("Int64")
    df["oecd"] = df["oecd"].map(oecd_map).astype("string")
    print("Unmapped cycles:", sorted(df.loc[~df["cycle"].isin([2015, 2018, 2022]), "cycle"].dropna().unique()))
    print("Unmapped oecd:", df.loc[df["oecd"].isna(), "oecd"].head())

    # I renamed columns for analysis.
    names = {
        "cycle": "Year",
        "cnt": "Country",
        "oecd": "OECD status",
        "escs_trend": "Overall Social Status",
        "hisei_trend": "Parents' Occupation",
        "homepos_trend": "Home Possessions",
        "paredint_trend": "Parents' Education",
    }
    df = df.rename(columns=names)
    df.to_csv(r"C:/Users/Asus/Desktop/portfolio/pisa_trend_analysis/data/cleaned/escs_trend_cleaned.csv", index=False)
    return df

clean_data()
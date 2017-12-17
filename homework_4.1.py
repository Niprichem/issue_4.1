import os
import pandas as pd


def top_count_names(path, years, top_count):
    cols =['Name', 'Gender', 'Count']
    data_list = [pd.read_csv(os.path.join(path, 'yob{}.txt'.format(year)), names=cols)
        for year in years]
    pd_data = pd.concat(data_list).groupby('Name').sum()
    top_pd_data = pd_data.sort_values(by='Count', ascending=False).head(top_count)
    return top_pd_data


def gender_count_dynamics(path, years):
    cols =['Name', 'Gender', 'Count']
    data = {year: pd.read_csv(os.path.join(path, 'yob{}.txt'.format(year)), names=cols)
        for year in years}
    pd_data = pd.concat(data, names=['Year'])
    pd_data_gender = pd_data.groupby(['Year', 'Gender']).sum()
    return pd_data_gender


def main():
    path = 'names'

    all_years = ((1880,), (1900, 1950, 2000))
    top_count = 3
    for years in all_years:
        print(top_count_names(path, years, top_count))

    years = (1900, 1950, 2000)
    print(gender_count_dynamics(path, years))


if __name__ == '__main__':
    main()

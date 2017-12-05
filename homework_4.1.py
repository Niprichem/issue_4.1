import os
import pandas as pd


def count_top3(path, years):
    cols =['name', 'gender', 'count']
    data_list = [pd.read_csv(os.path.join(path, 'yob{}.txt'.format(year)), names=cols)
        for year in years]
    data = data_list[0]
    for d in data_list[1:]:
        data.merge(d, on='name')
    return data.sort_values(by='count', ascending=False)[:3]


def main():
    path = 'names'
    all_years = ((1880,), (1900, 1950, 2000))
    for years in all_years:
        print(count_top3(path, years))


if __name__ == '__main__':
    main()

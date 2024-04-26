import csv
import pandas as pd
import datetime

df = pd.read_csv('sample.csv', skipinitialspace = True)

def show_table(only_available=False):
    if only_available:
        print(df.loc[df['Status']=='Available'].to_string(index=False))
    else:
        print(df.to_string(index=False))


def change_status(kitta_no , availability = True):
    if availability:
        df.loc[df['Kitta no']==kitta_no, 'Status'] = "Available"
    else:
        df.loc[df['Kitta no']==kitta_no, 'Status'] = "Not Available"
    df.to_csv('sample.csv')

def generate_bill(c_name, data_frame  , duration):
    output = f"Name of customer: {c_name}\n\n"
    total_amount = data_frame['Price'].sum()
    date_of_rent = datetime.datetime.now()
    for label , value in df.items():
        output += f"{label} : {value}"
    
    print(output)


    

    



def main():
    show_table()
    print()
    # x = input("1. Show Available Land Only\n2. Buy Land\n\n\t >>> ")
    generate_bill('da', df, 'dAAS')
    # breakpoint()
    





# change_status(42)
main()
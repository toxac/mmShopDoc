import os
import csv

headers = ['sno', 'name', 'address', 'locality', 'city', 'state', 'pincode', 'type', 'phone1', 'phone2', 'mobile' ]


def reshape(row):
    dealer = {}
    dealer["name"] = row[1].capitalize()
    dealer["address"] = row[2].capitalize() + ", "+row[3].capitalize() + ", "+row[4].capitalize() + ", "+row[5].capitalize() + " - " + row[6].capitalize()
    dealer["city"] = row[4].capitalize()
    dealer["state"] = row[5].capitalize()
    dealer["type"] = row[7].capitalize()
    dealer["phone"] = str(row[8]) +", "+ str(row[9])
    dealer["mobile"] = row[10]
    return dealer

def getUserInput():
    filename = input("enter filename: ")
    return filename

def cleanup_data(filename):
    # types: Dealer, Exclusive, Display
    processed_data = {"dealer": [], "exclusive":[], "display":[], "others":[]}
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
            # if count is above 1
            formatted_data = reshape(row)
            if formatted_data["type"] == "Dealer":
                processed_data["dealer"].append(formatted_data)
            elif formatted_data["type"] == "Exclusive" :
                processed_data["exclusive"].append(formatted_data)
            elif formatted_data["type"] == "Display" :
                processed_data["display"].append(formatted_data)
            else:
                processed_data["others"].append(formatted_data)
            line_count += 1
        print(f'Processed {line_count} lines')
    return processed_data

def data_status(cleaned_data):
    print(f'Total Dealers: {len(cleaned_data["dealer"])}')
    print(f'Total Exclusive: {len(cleaned_data["exclusive"])}')
    print(f'Total Display: {len(cleaned_data["display"])}')
    print(f'Total Others: {len(cleaned_data["others"])}')

def main():
    filename = getUserInput()
    formatted_data = cleanup_data(filename)
    data_status(formatted_data)
    print(sorted(formatted_data['exclusive'], key = lambda x: x['city']))



if __name__ == "__main__":
    main()
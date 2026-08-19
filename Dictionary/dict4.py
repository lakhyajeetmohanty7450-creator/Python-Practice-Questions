# Create a dictionary mapping five countries to their capital cities. Iterate
# through this dictionary using the items() method and print each pair in
# the format: Country → Capital.

countries = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
    "Germany": "Berlin",
    "Australia": "Canberra"
}

for keys ,value in countries.items():
    print(f"{keys} ------ > {value}")
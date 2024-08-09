# Define the class to handle province transformations


class ProvinceMapping:
    def __init__(self, mapping):
        self.mapping = mapping

    def province_map(self, province_name):
        return self.mapping.get(province_name, province_name)

province_mapping = {
    "Nova Scotia": "NS",
    "New Brunswick": "NB",
    "British Columbia": "BC",
    "Alberta": "AB",
    "Saskatchewan": "SK",
    "Manitoba": "MB",
    "Ontario": "ON",
    "Quebec": "QC",
    "Prince Edward Island": "PEI",
    "Newfoundland and Labrador": "NL",
    "Canada": "CA",
    "Nunavut": "NU",
    "North-West Territories": "NWT",
    "Yukon": "YT"
}


''' EXAMPLE

# Import the ProvinceMapping class and the province mapping dictionary
from ProvinceMapping import ProvinceMapping, province_mapping

# Create an instance of the ProvinceMapping class
transformer = ProvinceMapping(province_mapping)

# Transform the 'Geography' column in the businesses_df dataframe
businesses['Geography'] = businesses['Geography'].apply(transformer.province_map)

'''
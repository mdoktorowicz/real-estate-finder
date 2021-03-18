from zillow_finder import zillow_finder
from sheet_filler import sheet_filler


zillow = zillow_finder()
zillow_data = zillow.get_zillow_data()

sheet = sheet_filler()
sheet.fill_sheet(zillow_data)
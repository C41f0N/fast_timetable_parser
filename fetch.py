import gdown
import pandas as pd
def download_timetable():
    google_sheets_url = 'https://docs.google.com/spreadsheets/d/1H3zQ80ptZTc1cI60mt9oWkAa2_JBKqebGflFATf3nvI/'

    # Get the file ID from the Google Sheets URL
    file_id = google_sheets_url.split('/')[-2]
    print(file_id)

    # Construct the download link
    download_link = f'https://drive.google.com/uc?id={file_id}'

    # Define the output file name
    output_file = 'timetable.xlsx'

    # Download the file using gdown
    gdown.download(download_link, output_file, quiet=False)

import gdown
import pandas as pd


def download_timetable() -> bool:
    google_sheets_url = "https://docs.google.com/spreadsheets/d/1H3zQ80ptZTc1cI60mt9oWkAa2_JBKqebGflFATf3nvI/"

    # Get the file ID from the Google Sheets URL
    file_id = google_sheets_url.split("/")[-2]
    # print(file_id)

    # Construct the download link
    download_link = f"https://drive.google.com/uc?id={file_id}"

    # Define the output file name
    output_file = "timetable.xlsx"

    # Download the file using gdown
    try:
        gdown.download(download_link, output_file, quiet=True)
        return True
    except Exception as e:
        print(
            f"[-] Could not download the file: {e} :(.\n[-] Try using an excel file instead."
        )
        return False

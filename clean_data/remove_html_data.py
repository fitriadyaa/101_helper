import pandas as pd
from bs4 import BeautifulSoup

# Load the dataset
file_path = 'yourdata.csv'
data = pd.read_csv(file_path)

# column
html_column = 'content'

# Function to remove HTML tags
def clean_html(html_content):
    if pd.isna(html_content):
        return html_content
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

# Apply the function to the specified column
data[html_column] = data[html_column].apply(clean_html)

# Save the cleaned data to a new CSV file
data.to_csv('cleaned_data.csv', index=False)

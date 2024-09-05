import os
import pandas as pd
from datetime import datetime
import re

class PSDFileAnalyzer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.total_psd_files = 0
        self.keyword_counts = {
            'female': 0,
            'male': 0,
            'guy': 0,
            'fridge magnet female': 0,
            'fridge magnet male': 0
        }
        self.patterns = {
            'fridge magnet female': r'fridge\s*magnet\s*female',
            'fridge magnet male': r'fridge\s*magnet\s*male',
            'female': r'.*female.*',
            'male': r'.*male*',
            'guy': r'.*guy*'
        }

    def analyze_folder(self):
        # Iterate through all files in the directory
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith('.psd'):
                self.total_psd_files += 1
                # print(filename.lower() ,re.search(self.patterns['female'], filename.lower()))
                self._count_keywords(filename)

    def _count_keywords(self, filename):
        # Define regex patterns for each keyword
        patterns = {
            'fridge magnet female': r'fridge\s*magnet\s*female',
            'fridge magnet male': r'fridge\s*magnet\s*male',
            'female': r'.*female.*',
            'male': r'.*male*',
            'guy': r'.*guy*'
        }
        # Normalize filename to lower case for case-insensitive matching
        filename_lower = filename.lower()

        # Check each pattern and increment counts accordingly
        for keyword, pattern in patterns.items():
            if re.search(pattern, filename_lower):
                self.keyword_counts[keyword] += 1
                break
                # print(f"Matched {keyword} in file: {filename}")  # Debugging line

    def save_to_excel(self, output_path):
        # Create a pandas DataFrame for the data
        data = {
            'keyword': ['date', 'female', 'male', 'guy', 'fridge magnet female', 'fridge magnet male', 'total'],
            'count': [datetime.today().strftime('%d/%m/%Y'), 
                      self.keyword_counts['female'], 
                      self.keyword_counts['male'], 
                      self.keyword_counts['guy'], 
                      self.keyword_counts['fridge magnet female'], 
                      self.keyword_counts['fridge magnet male'], 
                      self.total_psd_files]
        }
        df = pd.DataFrame(data)

        # Check if the file already exists
        if os.path.exists(output_path):
            # Load the existing data
            existing_df = pd.read_excel(output_path, header=None)
            # Append the new data as a new column
            combined_df = pd.concat([existing_df, df.iloc[:, 1]], axis=1)
        else:
            # If the file doesn't exist, create a new DataFrame
            combined_df = df
        combined_df.to_excel(output_path, index=False, header=False)

        # Write to Excel with column headers and data row
        # df.to_excel(output_path, index=False, header=False)




if __name__ == "__main__":
    folder_path = "C:\\PythonPrograms\\Task Project\\gulbonda\\Work sample test"
    output_path = "C:\\PythonPrograms\\Task Project\\gulbonda\\Work sample test\\psd_file_counts.xlsx"

    analyzer = PSDFileAnalyzer(folder_path)
    analyzer.analyze_folder()
    analyzer.save_to_excel(output_path)


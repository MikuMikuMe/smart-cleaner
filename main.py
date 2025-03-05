Creating a complete Python program for a project like "Smart-Cleaner" involves several steps, including data analysis, data cleaning, error detection, and handling. Below, I'll provide a basic example of a Python program that can serve as a starting point for such a tool. This example will focus on analyzing and cleaning a dataset with missing values, duplicates, and inconsistent data formats.

We'll use common libraries such as `pandas` for data manipulation and `numpy` for numerical operations. The program will include comments and basic error handling for robustness.

```python
import pandas as pd
import numpy as np

class SmartCleaner:
    def __init__(self, file_path):
        """
        Initialize SmartCleaner with a file path to the dataset.
        """
        self.file_path = file_path
        try:
            self.data = pd.read_csv(file_path)
            print("Data successfully loaded.")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            self.data = None
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            self.data = None
        except pd.errors.ParserError:
            print("Error: Could not parse the file.")
            self.data = None

    def summarize_data(self):
        """
        Provide a summary of the dataset.
        """
        if self.data is not None:
            print("Dataset Summary:")
            print("===================================")
            print(self.data.info())
            print("Descriptive Statistics:")
            print(self.data.describe())
        else:
            print("No data to summarize.")

    def identify_missing_values(self):
        """
        Identify and summarize missing values in the dataset.
        """
        if self.data is not None:
            missing_values = self.data.isnull().sum()
            print("Missing Values Summary:")
            print("===================================")
            print(missing_values[missing_values > 0])
        else:
            print("No data to analyze for missing values.")

    def handle_missing_values(self):
        """
        Handle missing values by filling them with mean of the column for numerical data, 
        and mode for categorical data.
        """
        if self.data is not None:
            for column in self.data.columns:
                if self.data[column].dtype in [np.float64, np.int64]:
                    mean_value = self.data[column].mean()
                    self.data[column].fillna(mean_value, inplace=True)
                else:
                    mode_value = self.data[column].mode()[0]
                    self.data[column].fillna(mode_value, inplace=True)
            print("Missing values handled by mean/mode imputation.")
        else:
            print("No data to handle missing values.")

    def remove_duplicates(self):
        """
        Remove duplicate rows from the dataset.
        """
        if self.data is not None:
            initial_rows = self.data.shape[0]
            self.data.drop_duplicates(inplace=True)
            final_rows = self.data.shape[0]
            print(f"Duplicates removed: {initial_rows - final_rows}")
        else:
            print("No data from which to remove duplicates.")

    def fix_inconsistent_formats(self):
        """
        Detect and fix inconsistent data formats. 
        This example focuses on date formats and capitalization for strings.
        """
        if self.data is not None:
            for column in self.data.columns:
                if pd.api.types.is_datetime64_any_dtype(self.data[column]):
                    self.data[column] = pd.to_datetime(self.data[column], errors='coerce')
                elif pd.api.types.is_string_dtype(self.data[column]):
                    self.data[column] = self.data[column].str.title()

            print("Inconsistent formats fixed where applicable.")
        else:
            print("No data to fix formats.")

    def save_clean_data(self, output_path):
        """
        Save the cleaned data to a new file.
        """
        if self.data is not None:
            try:
                self.data.to_csv(output_path, index=False)
                print(f"Cleaned data saved to {output_path}")
            except Exception as e:
                print(f"Error when saving data: {str(e)}")
        else:
            print("No data to save.")

if __name__ == "__main__":
    cleaner = SmartCleaner("path_to_dirty_dataset.csv")
    cleaner.summarize_data()
    cleaner.identify_missing_values()
    cleaner.handle_missing_values()
    cleaner.remove_duplicates()
    cleaner.fix_inconsistent_formats()
    cleaner.save_clean_data("path_to_clean_dataset.csv")
```

### Key Features:
1. **Loading Data with Error Handling**: The program loads a dataset and handles file-related errors.
2. **Data Summarization**: Basic summarization to understand the dataset.
3. **Missing Value Handling**: The program detects and fills missing values using mean or mode.
4. **Removing Duplicates**: Identifies and removes duplicate rows.
5. **Fixing Inconsistent Formats**: Example fix for date formats and string capitalization.
6. **Saving Cleaned Data**: Cleansed data are saved, with error handling on saving.

This is a simple framework, and you might need to add more specific functionalities based on your requirements, such as handling more complex data cleaning tasks, data validation processes, or logging features for debugging complex datasets.
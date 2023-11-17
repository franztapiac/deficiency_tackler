from git import Repo
import os
from pathlib import Path
import sys
current_file_str_path = os.path.abspath(__file__)
repo_root_str_path = Repo(current_file_str_path, search_parent_directories=True).git.rev_parse("--show-toplevel")
sys.path.append(repo_root_str_path)
import csv
import json
import io
import numpy as np
import pandas as pd
from time import time
import re

def read_and_write_json(input_file, output_file, num_lines=5):
    # Read data from the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Take the first 'num_lines' lines
    subset_data = data[:num_lines]

    # Write the subset data to the output JSON file
    with open(output_file, 'w') as f:
        json.dump(subset_data, f, indent=2)  # 'indent' for pretty formatting



def read_database(db_path):
    db = pd.read_csv(filepath_or_buffer=db_path)
    return db


def read_with_pandas(def_nutrient, db_path):
    result_df = pd.DataFrame()

    chunk_size = 100000  # there are 1,048,576 rows in total
    iteration = 0
    for chunk in pd.read_csv(db_path, chunksize=chunk_size):
        print(f'Chunk iteration {iteration} starting...')
        tic = time()
        matches = chunk[chunk.apply(lambda row: row.astype(str).str.contains(def_nutrient).any(), axis=1)]

        if not matches.empty:
            result_df = pd.concat([result_df, matches])
        toc = time() - tic
        print(f'Chunk iteration {iteration} completed. It took {toc:.0f} seconds.')
        iteration += 1
    return result_df


def read_with_re(def_nutrient, db_path):
    tic = time()
    search_pattern = re.compile(def_nutrient)

    def has_search_string(row):
        return bool(search_pattern.search(' '.join(row.astype(str))))

    print('Reading the csv...')
    df = pd.read_csv(db_path)

    print('Applying the search pattern...')
    result_df = df[df.apply(has_search_string, axis=1)]
    toc = time() - tic
    print(f'Re searching took {toc:.0f} seconds.')
    return result_df


def chunk_foodb_content():
    data_list = []

    # Open the file and read it line by line
    print('Reading the file line by line')
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            print(data)
            data_list.append(data)

    print('Converting to a pandas DF')
    df = pd.DataFrame(data_list)
    print(df.head())

    # Set the maximum size for each chunk
    max_rows_per_chunk = 500000

    # Calculate the number of chunks needed
    num_chunks = (len(df) // max_rows_per_chunk) + 1

    # Specify the base name for the Excel files
    base_excel_file_name = 'output_file_chunk'

    # Export each chunk of the DataFrame to a separate Excel file
    for chunk_num in range(num_chunks):
        start_row = chunk_num * max_rows_per_chunk
        end_row = (chunk_num + 1) * max_rows_per_chunk
        df_chunk = df.iloc[start_row:end_row]

        # Generate the Excel file name for the chunk
        excel_file_path = f'{base_excel_file_name}_{chunk_num + 1}.xlsx'

        # Export the chunk to Excel
        df_chunk.to_excel(excel_file_path, index=False)

def tackle_deficiency(def_nutrient: str, age: int, db_path: Path, test_method: str):
    """
    Run the whole deficiency tackler program. Given the deficiency, find the foods that one can have the nutrient
    or compound that one needs to tackle this deficiency. Sort the foods by concentration of the nutrient.
    :param def_nutrient: The nutrient that the user is deficient in.
    :type def_nutrient: str.
    :param db_path: The path to the food content database.
    :type db_path: Path.
    """
    tic = time()
    whole_db = pd.read_csv(db_path)
    nan_indices = whole_db[whole_db['source_id'].isna()].index
    # for i, nan_index in enumerate(nan_indices):
    #     print(f'Working on index {i} of {len(nan_indices)}.')
    #     row_text = whole_db.iloc[nan_index][0]
    #     row_divided = next(csv.reader(io.StringIO(row_text), quotechar='"', delimiter=','))
    #     converted_list = [float(x) if x.replace('.', '', 1).isdigit() else (np.nan if x == '' else x) for x in row_divided]  # convert list to right dtypes
    #     df_parsed = pd.DataFrame(converted_list).T
    #     whole_db.iloc[nan_index] = df_parsed.iloc[0]  # return df into original
    toc = time() - tic
    print(f'Duration for updating all database: {toc:.0f} seconds.')
    print('f')

    # From all hits
        # separate into different compounds / nutrients by their source_id or orig_source_id
        # For each (orig_)source_id
            # list out the food they are found in together with the content

    # Read db of required nutrients by age group
    # Parse req db for nutrient amount required for age

    # Calculate % of required that is within the food

    # Sort by % requirement
    # Display: picture, % of requiremnt, enumerate in descending amount order,

    pass


if __name__ == '__main__':
    repo_path = Path(repo_root_str_path)
    file_path = repo_path / 'data/Content.json'





    print('Exporting pandas DF')
    csv_file_path = repo_path / 'output_file.csv'
    df.to_csv(csv_file_path, index=False)

    whole_db = pd.read_csv(csv_file_path)

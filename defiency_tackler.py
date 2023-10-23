from pathlib import Path
import pandas as pd
from time import time
import re


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


def tackle_deficiency(def_nutrient: str, age: int, db_path: Path, test_method: str):
    """
    Run the whole deficiency tackler program. Given the deficiency, find the foods that one can have the nutrient
    or compound that one needs to tackle this deficiency. Sort the foods by concentration of the nutrient.
    :param def_nutrient: The nutrient that the user is deficient in.
    :type def_nutrient: str.
    :param db_path: The path to the food content database.
    :type db_path: Path.
    """

    whole_db = read_database(db_path)

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
    database_path = Path(r"C:\Users\franz\Documents\work\projects\deficiency_tackler\data\foodb_2020_04_07_csv\foodb_2020_04_07_csv\Content_unknown_removed.csv")
    deficient_nutrient = 'luteolin'
    age_in_years = 27
    test_mode = 're'
    tackle_deficiency(def_nutrient=deficient_nutrient, age=age_in_years, db_path=database_path,
                      test_method=test_mode)




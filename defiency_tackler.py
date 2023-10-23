from pathlib import Path
from pandas import read_csv


def read_database(db_path):
    db = read_csv(filepath_or_buffer=db_path)
    return db


def tackle_deficiency(def_nutrient: str, age: int, db_path: Path):
    """
    Run the whole deficiency tackler program. Given the deficiency, find the foods that one can have the nutrient
    or compound that one needs to tackle this deficiency. Sort the foods by concentration of the nutrient.
    :param def_nutrient: The nutrient that the user is deficient in.
    :type def_nutrient: str.
    :param db_path: The path to the food content database.
    :type db_path: Path.
    """

    # Search database for all foods with def_nutrient (get the list that the Excel search gives you)

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
    database_path = Path(r"C:\Users\franz\Documents\work\projects\deficiency_tackler\data\foodb_2020_04_07_csv\foodb_2020_04_07_csv\Content.csv")
    deficient_nutrient = 'luteolin'
    age_in_years = 27
    tackle_deficiency(def_nutrient=deficient_nutrient, age=age_in_years, db_path=database_path)




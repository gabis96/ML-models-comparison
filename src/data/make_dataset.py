import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import pandas as pd
import os

from utils import rename_columns, filter_features, validate_country_names, clean_2020_2021


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    df_2015 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2015.csv'))
    df_2016 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2016.csv'))
    df_2017 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2017.csv'))
    df_2018 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2018.csv'))
    df_2019 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2019.csv'))
    df_2020 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2020.csv'))
    df_2021 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2021.csv'))
    df_2022 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2022.csv'))
    logger.info('Successfully read files')
    logger.info('making final data set from raw data')

    # ORGANIZE DATA
    # Prepare datasets
    clean_2020_2021(df_2020, df_2021)
    
    # Rename columns
    rename_columns(df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022)

    # Add year to all datasets
    df_2015['Year']= 2015
    df_2016['Year']= 2016
    df_2017['Year']= 2017
    df_2018['Year']= 2018
    df_2019['Year']= 2019
    df_2020['Year']= 2020
    df_2021['Year']= 2021
    df_2022['Year']= 2022

    # EXTRACT FEATURES by filtering relevant columns
    filter_features(df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022)

    # Merge df concating rows, keeping all columns and having nan where the column does not exist
    df = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022], ignore_index = True, sort = False)
    df = df[['Year', 'Country', 'Dystopia Residual', 'Happiness Rank', 'Freedom', 'Generosity', 'Healthy life expectancy', 'Perceptions of corruption', 'GDP per capita', 'Social support']] # sort ds
                            
    # CLEAN DATA
    # Validate Country names
    validate_country_names(df)

    # Validate data types
    num_cols = df.drop(['Country'], axis=1).columns
    df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce') # transform to numeric

    # Save processed data
    df.to_csv(os.path.join(output_filepath, 'WorldHappinees2015_2022'), index=False)


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main('../data/raw', '../data/processed')

import os
import pandas as pd

from ..features.impute_missing_data import impute_with_knn, impute_poc

class WorldHappinessDS:
    def __init__(self, input_filepath, logger):
        self.logger = logger
        self.df_2015 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2015.csv'))
        self.df_2016 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2016.csv'))
        self.df_2017 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2017.csv'))
        self.df_2018 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2018.csv'))
        self.df_2019 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2019.csv'))
        self.df_2020 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2020.csv'))
        self.df_2021 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2021.csv'))
        self.df_2022 = pd.read_csv(os.path.join(input_filepath, 'HappinessScore2022.csv'))

        self.df = pd.DataFrame()
        self.logger.info('Successfully read files')

    def build_dataset(self):
        '''Build one dataset of World Happiness from 2015 to 2022'''
        # CLEAN & ORGANIZE DATA
        self._clean_2020_2021()        # Prepare datasets
        self._rename_columns()         # Rename columns
        self._add_year_column()        # Add year to all datasets
        
        # EXTRACT FEATURES 
        self._filter_features()        # Filter relevant columns
        df = self._create_df()         # Concat databases            
        
        # CLEAN & VALIDATE DATA
        self._validate_country_names(df)
        self._validate_types(df)

        self.df = df.copy()
        return self.df

    def impute_missing_data(self):
        '''Impute missing data in dataset'''
        impute_poc(self.df)
        impute_with_knn(self.df)

    def save(self, output_filepath):
        '''Save the dataset created'''
        # self.output_filepath = output_filepath
        self.df.to_csv(os.path.join(output_filepath, 'WorldHappinees2015_2022'), index=False)

    def _rename_columns(self):
        """Renames datasets column names to unify to one convention"""
        self.df_2015 = self.df_2015.rename(columns= {'Economy (GDP per Capita)': 'GDP per capita', 'Health (Life Expectancy)': 'Healthy life expectancy', 'Trust (Government Corruption)': 'Perceptions of corruption'})
        self.df_2016 = self.df_2016.rename(columns= {'Economy (GDP per Capita)': 'GDP per capita', 'Health (Life Expectancy)': 'Healthy life expectancy', 'Trust (Government Corruption)': 'Perceptions of corruption'})
        self.df_2017 = self.df_2017.rename(columns= {'Dystopia.Residual': 'Dystopia Residual', 'Economy..GDP.per.Capita.': 'GDP per capita', 'Health..Life.Expectancy.': 'Healthy life expectancy', 'Trust..Government.Corruption.': 'Perceptions of corruption', 'Happiness.Rank': 'Happiness Rank', 'Happiness.Score': 'Happiness Score'})
        self.df_2018 = self.df_2018.rename(columns= {'Country or region': 'Country', 'Freedom to make life choices': 'Freedom', 'Overall rank': 'Happiness Rank', 'Score': 'Happiness Score'})
        self.df_2019 = self.df_2019.rename(columns= {'Country or region': 'Country', 'Freedom to make life choices': 'Freedom', 'Overall rank': 'Happiness Rank', 'Score': 'Happiness Score'})
        self.df_2020 = self.df_2020.rename(columns= {'Country name': 'Country', 'Dystopia + residual': 'Dystopia Residual', 'Explained by: Log GDP per capita': 'GDP per capita', 'Explained by: Freedom to make life choices':'Freedom',  'Explained by: Generosity': 'Generosity', 'Explained by: Healthy life expectancy': 'Healthy life expectancy', 'Explained by: Perceptions of corruption': 'Perceptions of corruption', 'Explained by: Social support': 'Social support', 'Ladder score': 'Happiness Score'})
        self.df_2021 = self.df_2021.rename(columns= {'Country name': 'Country', 'Dystopia + residual': 'Dystopia Residual', 'Explained by: Log GDP per capita': 'GDP per capita', 'Explained by: Freedom to make life choices':'Freedom', 'Explained by: Generosity': 'Generosity', 'Explained by: Healthy life expectancy': 'Healthy life expectancy', 'Explained by: Perceptions of corruption': 'Perceptions of corruption', 'Explained by: Social support': 'Social support', 'Ladder score': 'Happiness Score'})
        self.df_2022 = self.df_2022.rename(columns= {'Dystopia (1.83) + residual': 'Dystopia Residual', 'Explained by: GDP per capita': 'GDP per capita', 'Explained by: Freedom to make life choices':'Freedom', 'Explained by: Generosity': 'Generosity', 'Explained by: Healthy life expectancy': 'Healthy life expectancy', 'Explained by: Perceptions of corruption': 'Perceptions of corruption', 'Explained by: Social support': 'Social support', 'RANK': 'Happiness Rank', 'Happiness score':'Happiness Score'})
        
        self.logger.info('Successfully renamed columns')

    def _clean_2020_2021(self):
        """Prepare datasets for renaming columns and wrangling data"""
        # Add rank to 2020 & 2021.The records are already sorted by happiness
        self.df_2020['Happiness Rank'] = self.df_2020.index + 1
        self.df_2021['Happiness Rank'] = self.df_2021.index + 1

        # Avoid future repeated columns when renaming
        unnecesary_columns = ['Generosity', 'Perceptions of corruption', 'Social support', 'Healthy life expectancy']
        self.df_2020 = self.df_2020.drop(unnecesary_columns, axis=1)
        self.df_2021 = self.df_2021.drop(unnecesary_columns, axis=1)

    def _add_year_column(self):
        """Add years field to each dataset"""
        self.df_2015['Year']= 2015
        self.df_2016['Year']= 2016
        self.df_2017['Year']= 2017
        self.df_2018['Year']= 2018
        self.df_2019['Year']= 2019
        self.df_2020['Year']= 2020
        self.df_2021['Year']= 2021
        self.df_2022['Year']= 2022

    def _filter_features(self):
        """Filters datasets for relevant features"""
        # Common columns accross datasets: Country - Dystopia Residual* - GPD per Capita - Freedom - Generosity - Healthy life expectancy - Perceptions of corruption - Social support* - Happiness Rank - Year
        common_features = list(set(self.df_2015.columns) & set(self.df_2016.columns) & set(self.df_2017.columns) & set(self.df_2018.columns) & set(self.df_2019.columns) & set(self.df_2020.columns) & set(self.df_2021.columns) & set(self.df_2022.columns))

        self.df_2015 = self.df_2015[common_features + ['Dystopia Residual']]
        self.df_2016 = self.df_2016[common_features + ['Dystopia Residual']]
        self.df_2017 = self.df_2017[common_features + ['Dystopia Residual']]
        self.df_2018 = self.df_2018[common_features + ['Social support']]
        self.df_2019 = self.df_2019[common_features + ['Social support']]
        self.df_2020 = self.df_2020[common_features + ['Social support', 'Dystopia Residual']]
        self.df_2021 = self.df_2021[common_features + ['Social support', 'Dystopia Residual']]
        self.df_2022 = self.df_2022[common_features + ['Social support', 'Dystopia Residual']]
        
        self.logger.info('Successfully filtered features')

    def _create_df(self):
        '''Unify all datasets in one'''
        df = pd.concat([self.df_2015, self.df_2016, self.df_2017, self.df_2018, self.df_2019, self.df_2020, self.df_2021, self.df_2022], ignore_index = True, sort = False)
        df = df[['Year', 'Country', 'Dystopia Residual', 'Happiness Rank', 'Freedom', 'Generosity', 'Healthy life expectancy', 'Perceptions of corruption', 'GDP per capita', 'Social support']] # sort ds

        self.logger.info('Successfully created df')
        return df

    def _validate_country_names(self, df):
        """Unify and fix errors in country names"""

        df['Country'] = df['Country'].str.replace('*', '')                          # remove * from countries' names
        df = df.drop(df[df.Country == 'xx'].index)                                  # remove non existing countries
        df.loc[1182, 'Country'] = 'Congo (Kinshasa)'                                # update Congo region
        df.loc[347, 'Country'] = 'Taiwan'                                           # unify Taiwan
        df.loc[df.Country == 'Swaziland', 'Country'] = 'Eswatini, Kingdom of'       # update to current name of the country
        df.loc[df.Country == 'Northern Cyprus', 'Country'] = 'North Cyprus'         # unify North Cyprus
        df.loc[[385, 859, 1011, 1164], 'Country'] = 'Hong Kong'                     # unify Hong Kong
        
    def _validate_types(self, df):
        num_cols = df.drop(['Country'], axis=1).columns
        df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce') # transform to numeric

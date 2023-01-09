def rename_columns(df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022):
    """Renames datasets column names to unify to one convention"""
    df_2015 = df_2015.rename(columns= {'Economy (GDP per Capita)': 'GDP per capita', 'Health (Life Expectancy)': 'Healthy life expectancy', 'Trust (Government Corruption)': 'Perceptions of corruption'})
    df_2016 = df_2016.rename(columns= {'Economy (GDP per Capita)': 'GDP per capita', 'Health (Life Expectancy)': 'Healthy life expectancy', 'Trust (Government Corruption)': 'Perceptions of corruption'})
    df_2017 = df_2017.rename(columns= {'Dystopia.Residual': 'Dystopia Residual', 'Economy..GDP.per.Capita.': 'GDP per capita', 'Health..Life.Expectancy.': 'Healthy life expectancy', 'Trust..Government.Corruption.': 'Perceptions of corruption', 'Happiness.Rank': 'Happiness Rank', 'Happiness.Score': 'Happiness Score'})
    df_2018 = df_2018.rename(columns= {'Country or region': 'Country', 'Freedom to make life choices': 'Freedom', 'Overall rank': 'Happiness Rank', 'Score': 'Happiness Score'})
    df_2019 = df_2019.rename(columns= {'Country or region': 'Country', 'Freedom to make life choices': 'Freedom', 'Overall rank': 'Happiness Rank', 'Score': 'Happiness Score'})
    df_2020 = df_2020.rename(columns= {'Country name': 'Country', 'Dystopia + residual': 'Dystopia Residual', 'Explained by: Log GDP per capita': 'GDP per capita', 'Explained by: Freedom to make life choices':'Freedom',  'Explained by: Generosity': 'Generosity', 'Explained by: Healthy life expectancy': 'Healthy life expectancy', 'Explained by: Perceptions of corruption': 'Perceptions of corruption', 'Explained by: Social support': 'Social support', 'Ladder score': 'Happiness Score'})
    df_2021 = df_2021.rename(columns= {'Country name': 'Country', 'Dystopia + residual': 'Dystopia Residual', 'Explained by: Log GDP per capita': 'GDP per capita', 'Explained by: Freedom to make life choices':'Freedom', 'Explained by: Generosity': 'Generosity', 'Explained by: Healthy life expectancy': 'Healthy life expectancy', 'Explained by: Perceptions of corruption': 'Perceptions of corruption', 'Explained by: Social support': 'Social support', 'Ladder score': 'Happiness Score'})
    df_2022 = df_2022.rename(columns= {'Dystopia (1.83) + residual': 'Dystopia Residual', 'Explained by: GDP per capita': 'GDP per capita', 'Explained by: Freedom to make life choices':'Freedom', 'Explained by: Generosity': 'Generosity', 'Explained by: Healthy life expectancy': 'Healthy life expectancy', 'Explained by: Perceptions of corruption': 'Perceptions of corruption', 'Explained by: Social support': 'Social support', 'RANK': 'Happiness Rank', 'Happiness score':'Happiness Score'})

def filter_features(df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022):
    """Filters datasets for relevant features"""
    # Common columns accross datasets: Country - Dystopia Residual* - GPD per Capita - Freedom - Generosity - Healthy life expectancy - Perceptions of corruption - Social support* - Happiness Rank - Year
    common_features = list(set(df_2015.columns) & set(df_2016.columns) & set(df_2017.columns) & set(df_2018.columns) & set(df_2019.columns) & set(df_2020.columns) & set(df_2021.columns) & set(df_2022.columns))

    df_2015 = df_2015[common_features + ['Dystopia Residual']]
    df_2016 = df_2016[common_features + ['Dystopia Residual']]
    df_2017 = df_2017[common_features + ['Dystopia Residual']]
    df_2018 = df_2018[common_features + ['Social support']]
    df_2019 = df_2019[common_features + ['Social support']]
    df_2020 = df_2020[common_features + ['Social support', 'Dystopia Residual']]
    df_2021 = df_2021[common_features + ['Social support', 'Dystopia Residual']]
    df_2022 = df_2022[common_features + ['Social support', 'Dystopia Residual']]

def validate_country_names(df):
    """Unify and fix errors in country names"""
    df['Country'] = df['Country'].str.replace('*', '')                          # remove * from countries' names
    df = df.drop(df[df.Country == 'xx'].index)                                  # remove non existing countries
    df.loc[1182, 'Country'] = 'Congo (Kinshasa)'                                # update Congo region
    df.loc[347, 'Country'] = 'Taiwan'                                           # unify Taiwan
    df.loc[df.Country == 'Swaziland', 'Country'] = 'Eswatini, Kingdom of'       # update to current name of the country
    df.loc[df.Country == 'Northern Cyprus', 'Country'] = 'North Cyprus'         # unify North Cyprus
    df.loc[[385, 859, 1011, 1164], 'Country'] = 'Hong Kong'                     # unify Hong Kong

def clean_2020_2021(df_2020, df_2021):
    """Prepare datasets for renaming columns and wrangling data"""
    # Add rank to 2020 & 2021.The records are already sorted by happiness
    df_2020['Happiness Rank'] = df_2020.index + 1
    df_2021['Happiness Rank'] = df_2021.index + 1

    # Avoid future repeated columns when renaming
    unnecesary_columns = ['Generosity', 'Perceptions of corruption', 'Social support', 'Healthy life expectancy']
    df_2020 = df_2020.drop(unnecesary_columns, axis=1)
    df_2021 = df_2021.drop(unnecesary_columns, axis=1)

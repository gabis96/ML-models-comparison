Regression Models on World Happiness
==============================

This project curates and unifies all World Happiness datasets, including the last year. Regression is used to tackle missing values imputation and predictive analysis for extrapolating 2023-behaviour. Several regression models are apply, evaluated and compare. It surely extends the current work available online. 

The results of this study will be published on my personal
[blog](https://gabrielarscp.wixsite.com/gabsdatascience/blog).

## Roadmap

- Collect World Happiness datasets from the last years.
- Curate old datasets and homogenize fields to unify all sources in one.
- Check for faulsy values.
- Impute missing values
    - Try out various regression techniques
    - Compare techniques looking at distributions or doing cross validation.
    - Apply the best one.
- Do exploratory data analysis and examine:
    - Correlation between variables (Identify highest correlated variables).
    - Category with higher impact in the Happiness Score.
    - Distribution of Happiness Score.
    - Top/bottom 10 countries in the podium for the last 8 years.
    - Top/bottom 10%til countries in happiness.
    - Overall best performing country in each category by average.
- Do predictive extrapolation using time series on the data and analyze (Future Work):
    - Rank in 2023
    - Which country is on it’s way to becoming the first Utopia? (9.0) 
    - Which country is on it’s way to becoming the first Dystopia? (1.0)
- Compare results evaluating models with appropiate metrics (Future Work). 
- Create infographic.

## Python Stack

**Math & Machine Learning:** sklearn, numpy, scipy

**Data Manipulation:** pandas (for datasets), requests (for scrapping from the web)

**Visualization:** mathplotlib, seaborn (newest interface objects), geopandas

## File Description

To structure my project I have followed the *Cookiecutter* template.

    ├── LICENSE
    <!-- ├── Makefile           <- Makefile with commands like `make data` or `make train` -->
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── maps           <- Geo data.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    <!-- ├── models             <- Trained and serialized models, model predictions, or model summaries -->
    │
    ├── notebooks          <- Jupyter notebooks
    │   ├── 1.data_wrangling.ipynb          
    │   ├── 2.feature_engineering.ipynb     
    │   ├── 3.exploratory_analysis.ipynb     
    │   └── 4.prediction_2023.ipynb
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts generate dataset
    │   │   └── make_dataset.py
    │   │   └── wh_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── requirements.txt   <- The requirements file for reproducing the analysis environment (pip freeze > requirements.txt)

## Datasets
### World Happiness
The World Happiness Report is a landmark survey of the state of global happiness that ranks 156 countries by how happy their citizens perceive themselves to be. 

Unfortunately, my home country Cuba is not in the countries analized. 

Name: World Happiness Report

*Source*: https://www.kaggle.com/datasets/mathurinache/world-happiness-report

*Institution*: Gallup World Survey

*Date*: 2022-03 

#### Factors that explain the Happiness Score
The Happiness Score is explained by the following factors: GDP per capita, Healthy Life Expectancy, Social support, Freedom to make life choices, Generosity, Corruption Perception, Residual error

### Geolocation
Name: Countries geolocation data

Source: https://gadm.org/download_country.html

Date of data collection: 2023-01 

## Results

## Future Work
- EDA: 
    - Examine if population size and Happiness Score are correlated.
    - Identify if there is causal effect between Happiness Score and Wealth/Health.
- Time series Prediction

## Last Update
[2022-01-16] by [Gabriela Rodriguez]

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://gabrielarscp.wixsite.com/gabsdatascience/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielasanta/)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

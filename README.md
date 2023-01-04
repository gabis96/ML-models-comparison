
# Machine Learning Models Comparison in Python

The aim of this repository is to compound comparisons between machine learning algorithms.
This coul provide a general view of what model could be more suited to a given problem or dataset.


The results of this study will be published on my personal
[blog](https://gabrielarscp.wixsite.com/gabsdatascience/blog).
## Roadmap

- Use cookiecutter-data-science template. 
- Define ML problems that will be tackle (Regression, Classification, Clustering, Association).
- Define order to approach the problems (1. Clustering).
- Collect different dataset with the necessary characteristics to analyse with machine learning algorithm type.  
- Define methods to study and then analyze datasets.
- Compare results evaluating with different metrics. 

## Python Stack

**Math & Machine Learning:** sklearn, numpy, scipy

**Data Manipulation:** pandas

**Visualization:** mathplotlib, plotly
## File Description
To structure my project I have followed the *Cookiecutter* template.

- **data**: folder containing all data files.
    - **final**: folder containing final datasets.
        - **paris_social_housing_kmeans.csv**
        - **paris_social_housing_kmeans_centroids.csv**
        - **paris_social_housing_kmeans_map.csv**
        - **paris_social_housing_meanshift.csv**
        - **paris_social_housing_meanshift_centroids.csv**
        - **paris_social_housing_meanshift_map.csv**
    - **processed**:
        - **paris_social_housing.csv**: data after cleaning and filtering important feature.
    - **raw**:
        - **CONTOURS-IRIS_D075.dbf**: database containing data of Paris map. 
        - **CONTOURS-IRIS_D075.shp**: shapefile data of Paris map. 
        - **famillie_2014.csv**: public census data of Paris families.
        - **population_2014.csv**: public census data of Paris population.
        - **revenue_2014.csv**: public census data of Paris revenue.
- **models**: folder containing models definitions.
    - **association**: folder containing association algorithms
    - **classification**: folder containing classification algorithms
    - **clustering**: folder containing clustering algorithms
        - **kmeans**: wrapper class for kmeans model.
        - **meanshift**: wrapper class for meanshift model.
    - **regression**: folder containing regression algorithms
- **notebooks**: folder containing notebooks.
    - **clustering_analysis.ipynb**: notebook for analysing data using clustering algorithms.
- **src**: folder storing all python code. 
    - **clustering.py**: file comprising exampled data for clustering and algorithms comparison. 
    - **visualization.py**: file used for create mapfrom database.
- **requierements.py**: python dependencies.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://gabrielarscp.wixsite.com/gabsdatascience/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielasanta/)


[Go to top](#TOP)
## Summary
## Usage/Examples

```python
from mlcompare import ClusteringComparison

cc = ClusteringComparison()
cc.run_models()     # Runs models on example data
cc.visualize()      # Visualize plots
cc.eval()           # Evaluates metrics on algorithms performance

```


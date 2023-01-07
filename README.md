# Machine Learning Models Comparison in Python

The aim of this repository is to compound comparisons between machine learning algorithms,
helping with a general idea of what model could be more suited to a given problem or dataset.


The results of this study will be published on my personal
[blog](https://gabrielarscp.wixsite.com/gabsdatascience/blog).

## Roadmap

- Use cookiecutter-data-science template. 
- Define ML problems that will be tackle (Regression, Classification, Clustering, Association).
- Tackle one ML approach at a time.
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
    -   
- **models**: folder containing models definitions.
    - **association**: folder containing association algorithms
    - **classification**: folder containing classification algorithms
    - **clustering**: folder containing clustering algorithms
        - **kmeans**: wrapper class for kmeans model.
        - **meanshift**: wrapper class for meanshift model.
    - **regression**: folder containing regression algorithms
- **notebooks**: folder containing notebooks.
    - **clustering_analysis.ipynb**: notebook for analysing data using clustering algorithms.
    - **regression_analysis.ipynb**: notebook for analysing data using clustering algorithms.
- **src**: folder storing all python code. 
    - **clustering.py**: file comprising exampled data for clustering and algorithms comparison. 
    - **visualization.py**: file used to plot results.
- **requierements.py**: python dependencies.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://gabrielarscp.wixsite.com/gabsdatascience/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrielasanta/)

## Usage/Examples

```python
from mlcompare import ClusteringComparison

cc = ClusteringComparison()
cc.run_models()     # Runs models on example data
cc.visualize()      # Visualize plots
cc.eval()           # Evaluates metrics on algorithms performance

```

[Go to top](#TOP)

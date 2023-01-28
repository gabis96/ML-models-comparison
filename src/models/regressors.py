from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline

from .base import RegressorModel

class LinearRegressionModel(RegressorModel):
    '''Sklearn Linear Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        linear_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", LinearRegression())]
        )
        super().__init__(linear_regression)


class RidgeRegressionModel(RegressorModel):
    '''Sklearn Ridge Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        ridge_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", Ridge())]
        )
        super().__init__(ridge_regression)


class LassoRegressionModel(RegressorModel):
    '''Sklearn Linear Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        lasso_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", Lasso())]
        )
        super().__init__(lasso_regression)

class PolynomialRegressionModel(RegressorModel):
    '''Sklearn Linear Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        polynomial_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", LinearRegression())]
        )
        super().__init__(polynomial_regression)

class SGDRegressionModel(RegressorModel):
    '''Sklearn Sctochastic Gradient Descent Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        sgrad_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", SGDRegressor(n_iter_no_change=250, penalty=None, eta0=0.0001, max_iter=100000))]
        )
        super().__init__(sgrad_regression)

class SVRRegressionModel(RegressorModel):
    '''Sklearn SVM Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        svr_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", SVR(kernel='rbf', C=1000000, epsilon=0.001))]
        )
        super().__init__(svr_regression)

class RegressionTreeModel(RegressorModel):
    '''Sklearn Tree Regressor Wrapper class'''
    def __init__(self, preprocessor):
        
        tree_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", DecisionTreeRegressor(max_depth=2))]
        )
        super().__init__(tree_regression)

class RandomForestModel(RegressorModel):
    '''Sklearn Random Forest Wrapper class'''
    def __init__(self, preprocessor):
        
        randforest_regression = Pipeline(
            steps=[("preprocessor", preprocessor), ("regressor", DecisionTreeRegressor(max_depth=2))]
        )
        super().__init__(randforest_regression)
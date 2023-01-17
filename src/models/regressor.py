from sklearn import metrics
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
from seaborn import objects as so


class RegressorModel:
    '''Base class for regresor models'''
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def fit(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def predict(self, X_test):
        return self.pipeline.predict(X_test)

    def evaluate(self, real, predicted, X, y):
        '''
        Calculates scores to evaluate model performance

        Args:
            real: real labels.
            predicted: predicted labels.
            X: real data.
            y: real labels.

        Returns:
            dictionary containing 
        '''
        return {
            'mae': metrics.mean_absolute_error(real, predicted),
            'mse': metrics.mean_squared_error(real, predicted),
            'rmse': np.sqrt(metrics.mean_squared_error(real, predicted)),
            'r2_square': metrics.r2_score(real, predicted),
            'cross_val' : cross_val_score(self.pipeline, X, y, cv=10).mean()
        }

    def graph(self, real, predicted, mode=0):
        '''
        Wrapper function using seaborn to plot the predicted values vs real values

        Args:
            real: real labels.
            predicted: predicted labels.
            mode: 0 for real vs predicted, 1 for real and predicted vs data points.

        Returns:
            seaborn plot
        '''

        if mode == 0:
            return (
                so.Plot(x=real, y=predicted)
                .add(so.Dot())
            )

        # else mode == 1
        X = list(range(0, len(real)))
        df1 = pd.DataFrame(data={
            "X" : X,
            "y" : real,
            "origin" : 'real'
        })
        df2 = pd.DataFrame(data={
            "X" : X,
            "y" : predicted,
            "origin" : 'predicted'
        })

        data = pd.concat([df1, df2]).reset_index(drop=True)

        return (
            so.Plot(data=data, x='X', y='y', color='origin', marker="origin")
            .add(so.Dots())
            .scale(
                color=['#87b7e0', '#cf604a'],
                marker=so.Nominal(["o", "x"]),
            )
        )


    def run(self, X, y, X_train, y_train, X_test, y_test):
        '''
        Runs a defined pipeline: fits the regressor, predicts values, evaluates metrics and visualizes real vs predicted points.

        Args:
            X: real data.
            y: real labels.
            X_train: training data.
            y_train: training labels.
            X_test: test data.
            y_test: test labels.

        Returns:
            predicted values, scores, plot
        '''

        self.fit(X_train, y_train)
        predicted = self.predict(X_test)
        evaluation = self.evaluate(y_test, predicted, X, y)
        plot = self.graph(y_test, predicted)

        return predicted, evaluation, plot



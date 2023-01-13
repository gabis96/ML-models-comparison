import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# newest interface
from seaborn import axes_style, objects as so
from matplotlib.figure import Figure

class WorldHappinessVisualization:
    def __init__(self, df, palette="blend:#87b7e0,#cf604a"):
        self.df = df.copy()
        
        # Personalization
        self.palette = palette
        sns.set_theme(style="dark", palette=palette, color_codes=True)

    def corr_plot(self, figsize=(8,6), palette=None):
        if palette is None:
            palette=self.palette

        corr = self.df.corr() 

        plt.figure(figsize=figsize)
        heatmap = sns.heatmap(corr, vmin=-1, vmax=1, cmap=sns.color_palette(palette=palette, as_cmap=True), annot=True, fmt=".1f")
        heatmap.set_title('Correlations between Features', fontdict={'fontsize':10}, pad=22)
        return heatmap

    def bivariate_happiness_plot(self, figsize=(26, 5), palette=None):
        if palette is None:
            palette=self.palette
            
        relevant_features = ['Freedom', 'Generosity', 'Healthy life expectancy', 'Perceptions of corruption', 'GDP per capita', 'Social support']
        f = Figure(figsize, layout="constrained")
        
        return (
            so.Plot(self.df, y='Happiness Score', color='Happiness Score')
            .add(so.Dots())
            .pair(x=relevant_features)
            .scale(color='dark:#cf604a')
            .on(f)
        )

    def pair_plot(self, palette=None):
        if palette is None:
            palette=self.palette

        return sns.pairplot(self.df, palette=palette)

    def pie_plot(self, figsize=(8,6), palette=None):
        if palette is None:
            palette=self.palette

        nhappy = self.df[self.df['Happiness Score'] > 5].shape[0]
        nunhappy = self.df[self.df['Happiness Score'] < 5].shape[0]

        return plt.pie([nhappy, nunhappy], labels=['Happy', 'Unhappy'], colors=['#87b7e0', '#cf604a'], autopct='%.0f%%')  



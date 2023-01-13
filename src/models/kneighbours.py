from sklearn.neighbors import KNeighborsRegressor

# plotting functions and packages
import matplotlib.pyplot as plt
import numpy as np

class KNeighborsRegressorModel():
    """A K Neighbors Regressor model using scikit-learn's implementation"""
    def __init__(self, test_data, test_labels, train_data, train_labels, start,\
        end):
        # initialize the model and split the data into train and test data to be
        # ready for training and testing
        self.model = KNeighborsRegressor()
        self.test_data = test_data
        self.test_labels = test_labels
        self.train_data = train_data
        self.train_labels = train_labels
        self.start = start
        self.end = end
    
    def train(self):
        """Trains the model using the training data and labels"""
        self.model.fit(self.train_data, self.train_labels[:, -1])
    
    def predict(self):
        """Predicts using test data"""
        self.predictions = self.model.predict(self.test_data)
    
    def r_squared(self):
        """
        Computes the R^2 coefficient to indicate how closely related the testing
        data and test labels are related

        Returns:
            float: The R^2 coefficient
        """
        r_squared = self.model.score(self.test_data, self.test_labels[:, [-1]])
        return r_squared
    
    def graph(self):
        """Graphs the model's predictions vs the actual labels"""
        regions = self.test_labels[:, 2]
        regions_colors = []
        regions_dictionary = {}
        number = 0

        for region in np.unique(regions):
            # assigning each region a different number
            regions_dictionary[region] = number
            number += 1
        
        for region in regions:
            # making sure that each region will get a color
            regions_colors.append(regions_dictionary[region])
        
        # make sure that the subplot and figure can be accessible for hovering
        # and annotations
        self.figure, self.ax = plt.subplots()
        self.plot = plt.scatter(self.predictions, self.test_labels[:, [-1]],\
            label = "A Region",\
            c = regions_colors, cmap = "tab10")
        self.annotate =\
            self.ax.annotate("", xy = (0, 0), xytext = (20, 20),\
                textcoords = "offset points",\
                bbox = dict(boxstyle = "round", fc = "w"),\
                arrowprops = dict(arrowstyle = "->"))
        self.annotate.set_visible(False)

        # show the ideal line, axis labels, title, and legend
        plt.plot([2.8, 7.5], [2.8, 7.5], color = "black", label = "y = x")
        plt.xlabel("Predictions")
        plt.ylabel("Labels")
        plt.title("Happiness Scores – KNeighbors Regressor (" + str(self.start)\
            + " through " + str(self.end) + ")")
        legend1 =\
            self.ax.legend(*self.plot\
                .legend_elements(), loc = "upper left", title = "Region")
        self.ax.add_artist(legend1)
        self.figure.canvas.mpl_connect("motion_notify_event", self.hover)
        plt.show()

import matplotlib.pyplot as plt

class BarGraph:

    @staticmethod
    def single_dataset(labels_and_values, params={}):
        plt.bar(range(len(labels_and_values)), labels_and_values.values(), align='center')
        plt.xticks(range(len(labels_and_values)), labels_and_values.keys(), rotation=params.get("rotation", 45))
        plt.ylabel(params.get("ylabel", ""))
        plt.title(params.get("title", ""))
        plt.show()

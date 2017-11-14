from pylab import plot, xlabel, ylabel, title, show

class LineGraph:

    @staticmethod
    def single_line(x_values, y_values, params={}):
        plot(x_values, y_values)
        xlabel(params.get("xlabel", ""))
        ylabel(params.get("ylabel", ""))
        title(params.get("title", ""))
        show()

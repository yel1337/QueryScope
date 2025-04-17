from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.plot()

    def plot(self):
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
        self.ax.plot(x, y)
        self.draw()


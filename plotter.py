import matplotlib.pyplot as plotter
from datetime import datetime
import os
import numpy as np


def create_chart(dataArr, title, xlabel, ylabel, yscale="linear"):
    for item in dataArr:
        plotter.plot(item["xdata"], item["ydata"],
                     color=item["color"], label=item["label"])

    plotter.title(title)
    plotter.xlabel(xlabel)
    plotter.ylabel(ylabel)
    plotter.yscale(yscale)
    plotter.grid()
    plotter.legend()
    now_time = datetime.now()

    dirname = os.path.dirname(__file__)
    filename = os.path.join(
        dirname, f"report/{title}_{yscale}_chart_{now_time}.png")

    try:
        plotter.savefig(filename)
    except FileExistsError:
        pass
    plotter.close(None)


def create_bar_chart(data, title, xlabel, ylabel):
    courses = list(data.keys())
    values = list(data.values())

    plotter.figure(figsize=(8, 4))

    plotter.bar(courses, values, color='maroon',
                width=10)

    plotter.xlabel(xlabel)
    plotter.ylabel(ylabel)
    plotter.title(title)

    now_time = datetime.now()

    dirname = os.path.dirname(__file__)
    filename = os.path.join(
        dirname, f"report/{title}_bar_chart_{now_time}.png")

    try:
        plotter.savefig(filename)
    except FileExistsError:
        pass
    plotter.close(None)

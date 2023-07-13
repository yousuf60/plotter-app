import numpy as np

from .inputs import inputs
from .outputs import output_data, plt, graph, fig

from .background import background

inp = inputs("data.json")
data_inputs = inp.start()
print(inp.ok_btn)
inp.ok_btn.plt = plt
inp.ok_btn.graph = graph
inp.ok_btn.fig = fig
fig.axes[0].plot(np.asarray(inp.data["xlist"], float), inp.data["ylist"], marker=".")


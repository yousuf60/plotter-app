from simplekivy import SimpleKivy 
from widgets import (
    data_inputs
)

s = SimpleKivy(title="plotter")

THIRD_DICT = {"size_hint":(1, .65), "orientation":"vertical"}


s + [
    data_inputs,
    
    [THIRD_DICT,

    ],
]
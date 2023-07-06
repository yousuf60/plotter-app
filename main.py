from simplekivy import SimpleKivy 
from widgets import (
    data_inputs,
    output_data
)

s = SimpleKivy(title="plotter")




s + [
    data_inputs, #first piece inputs & button

    output_data, #second piece plots
]
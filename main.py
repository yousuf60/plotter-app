from simplekivy import SimpleKivy 
from widgets import (
    data_inputs,
    output_data,
    background,
    
)

from time import sleep

s = SimpleKivy(title="plotter")



front = [{"orientation":"vertical"},data_inputs, output_data]





s + [(
   background,
   front,
        
)]
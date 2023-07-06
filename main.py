from simplekivy import SimpleKivy 
s = SimpleKivy(title="plotter")

FIRST_DICT = {"size_hint":(1, .35), "orientation":"vertical"}
SECOND_DICT = {"size_hint":(1, None), "height":"70dp", "padding":"7dp"}

axis_input = s.TextInput(hint_text="only numsbers")
yis_input = s.TextInput(hint_text="only numsbers")

s + [
    [FIRST_DICT,
        [SECOND_DICT,
            axis_input, s.Label(text="axis")
        ],
        [SECOND_DICT,
            yis_input, s.Label(text="wyis")
        ],
    ],
]
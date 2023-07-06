from simplekivy import SimpleKivy 
s = SimpleKivy()

FIRST_DICT = {"size_hint":(1, .35), "orientation":"vertical"}
SECOND_DICT = {"size_hint":(1, None), "height":"70dp", "padding":"4dp"}

axis_input = s.TextInput(hint_text="only numsbers")
yis_input = s.TextInput(hint_text="only numsbers")
ok_btn = s.Button(text="ok", size_hint=(.4, None), height="50dp", pos_hint={"center_x":.5})

data_inputs = [FIRST_DICT,
        [SECOND_DICT,
            axis_input, s.Label(text="axis")
        ],
        [SECOND_DICT,
            yis_input, s.Label(text="wyis")
        ],
        ok_btn,    
    ]
del s
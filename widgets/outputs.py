from simplekivy import SimpleKivy 
s = SimpleKivy()

FIRST_DICT = {"size_hint":(1, 1)}
lbl = s.lang.Builder.load_string("""
Label:
    text: "ovek"
    

""")

output_data = ([FIRST_DICT,
    lbl
],)
del s, FIRST_DICT
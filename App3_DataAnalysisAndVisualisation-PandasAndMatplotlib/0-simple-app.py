import justpy as jp     # Every justpy app will have a main object that is kwown as a quasar page (aka the webpage)
                            # This webpage may contain different elements (such as html elements). It is called quasar
                            # as justpy uses the quasar framework, written using JS and interpreted through python.
                            # Thus why it is considered "usable" to us. 
                            # DOCS --> {([justpy] Documentation = https://justpy.io/),
                            #           ([quasar framework] Documentation = https://quasar.dev/)}

def app():
    wp = jp.QuasarPage()    # wp == Webpage obj
    h1 = jp.QDiv(           # Contains innate styling from the Quasar lib to make it "look modern and easy to style with" - Ardit
        a=wp,
        text="Analyssis of Course Reviews",
        classes="text-h3 text-center q-pa-lg"
    )
    p1= jp.QDiv(
        a=wp,
        text="these graphs represent course review analysis"
        # , classes="text-body1" # equivlent to something like <p></p>, this is also the default
    )
    
    return wp

jp.justpy(app)


# Coloca el código de tu juego en este archivo.

#DECLARAR LOS PERSONAJES

define osi = Character("Osiris", color = "#DA6FF7")
define led = Character("Ledesma", color = "#20FAF2")
define mk  = Character("Mankito", color = "#5A21ED")

# DEFINIR SPRITES
image chico = "chico.png"
image chico enfadado = "chicoenfadado.png"
image chico sonrie = "chicosonrie.png"
image chico sonrie flip = im.Flip("chicosonrie.png", horizontal= True)

# COMIENZA EL JUEGO

label start:

    # CARGAMOS EL FONDO
    scene atardecer

    #CARGAMOS MUSICA
    play music "music/music.wav" loop fadein 1.0

    #COMIENZA A MOSTRAR TEXTO
    "Habia estado planeando todo durante horas."
    "Practique que decirle a Osiris si me lo encontraba."
    "Hasta le compre una tarjeta en el OXXO de Roblox."
    "Pero en ese momento aparecio el pe@#!!@# de Mankitos."

    show chico at center:
        xzoom 0.75 yzoom 0.75

    mk "Sale un lol?"
    mk "Vamo a fumar uno?"
    mk "No voy a entrar a clae"

    "Este Pe@#$@# siempre molestando"

    led "NO..."

    "Me caga este wey"

    show chico sonrie
    mk "Sale ese LOL o no?"
    mk "Habla pinche wey"

    "Manquitos no era un mal tipo... solo se droga"
    "Y ya por la droga, dice inchuerencias"

    led "Markitos ya vete, hules mal."

    "En eso ya estaba llegando Osiris"

    transform littleright:
        xalign 0.65 yalign 1.0

    #ENTRA CHICA

    show chica at littleright behind chico with dissolve:
        xzoom 0.25 yzoom 0.25 #REDUCIMOS EL TAMANO

    "LLEGO OSIRIS... QUE NERVIOS"

    show chico sonrie with move:
        xzoom -0.75
        xalign 0.30 yalign 1.0

    #SUENA RELOJ
    play sound "sound/tower_clock.ogg"
    queue sound "sound/tower_clock.ogg"
    queue sound "sound/tower_clock.ogg"
    queue sound "sound/tower_clock.ogg"
    queue sound "sound/tower_clock.ogg"

    "Markitos en estado de dorgas, entendio que se tenia que ir"

    hide chico with dissolve

    "Osiris ve como Mankitos se retira"

    show chica at center with move

    stop music fadeout 1.0 #PARA MUSICA

    osi "..."


    #COMIENZO A MOSTRAR TEXTO

    play music "music/sovereign.mp3" fadein 0.5
    "Mientras estaba dando un paseo, vi a Osiris."
    "Se me quedo viendo, mientras jugaba Roblox."

    osi "..."
    "Se veia tan lindo, no sabia que decirle."

    led "Hola"
    "No sabia que mas decirle."

    menu:
        "Recordar.":
            jump escena2

    # ESCENA 2

    label escena2:

    #CARGAMOS EL FONDO CON TRANSICION
        scene atardecer2 with fade

        "Recorde la primera vez que vi a Osiris sudando."
        "Se veia tan lindo mientras se tocaba sus coletas del pelo."


    #SALTAMOS A LA NUECA ESCENA
        menu:
            "Volver a la realidad.":
                jump dialogo

    #ESCENA DONDE HABLAN LOS PERSONAJES

    label dialogo:

        scene atardecer

        show chica at right:
            xzoom 0.25 yzoom 0.25

        "Osiris me vio con extraneza."

        show chica at center

        osi "En que estas pensando... papucho"
        led "Me hulen las bolas"
        osi "tines hambre"
        led "si..."
        osi "pues pica de mi fiambre"

        # MOSTRAMOS DOS OPCIONES

        menu:
            "Picar fiambre":
                jump verdad
            "No Picar fiambre":
                jump mentira

        # ESCENA EN LA QUE PICAMOS EL FIAMBRE
        label verdad:

            "Pica el fiambre Ledesama"
            jump fin

        # ESCENA EN LA QUE NO PICAMOS EL FIAMBRE
        label mentira:

            "NO Picar el fiambre Ledesama"
            jump fin

        label fin:
        # TERMINA EL JUEGO

    return

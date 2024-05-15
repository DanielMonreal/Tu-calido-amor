# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define woman = "Kaori"
define man = "Aki"
define antagonist = "Takeshi"

#Las imagenes se definen asi
image Escuela = "Escuela1.jpg"
image Parque = "Parque1.jpg"
image Estacionamiento = "Estacionamiento1.jpg"
image Casa = "Casa1.png"
image Azotea = "Azotea1.jpg"
image Canchas = "Canchas1.jpg"
image woman = "Woman3.png"
image man = "man.png"

style statHeader:
  is frame
  ypadding 10
  xpadding 10
  xmargin 1
  ymargin 1


screen inv():
  frame:
    xalign 1.0
    style "statHeader"
    text "Day: [Day] | Cash:[Cash] | Cansancio:[Cansancio]"




# El juego comienza aquí.

label start:
    stop music fadeout 0.1
    play sound "audio/Sonido1.ogg"
    play music "audio/Fondo1.ogg"
    $Papas = 0
    $Refresco = 0
    $Chocolate = 0
    $Cash = 0
    $Cansancio = 0
    $Day = 1
    scene black with dissolve
    pause 1
    show text "{size=+30} Daniel Monreal Presents.....{/size}" with dissolve
    $renpy.pause(2,hard='True')
    scene Escuela with dissolve
    show screen inv 
    woman "Que bonito dia es hoy, no crees?."
    woman "Espero que el dia de hoy sea un buen dia."
    show woman at center with dissolve
    pause 1
    woman "Hola Aki como te va!"
    man "Bien Kaori y a ti?, aqui normal paseando por los pasillos"
    woman "Me alegro mucho Aki, oye te gustaria acompañarme a caminar despues de clases (Se sonroja)?"
    pause 1
    hide woman with dissolve 
    show man at center with dissolve
    pause 1
    man "Oh suena interesante, por supuesto no hay ningun problema"
    man "Tambien me gustaria ir a visitar la tienda de ropa y de regalos"
    man "Lo que pasa es que mi madre cumplira pronto años y me gustaria tambien invitar kaori chan?"
    man "Asi que seria maravilloso~"
    hide man with dissolve
    show woman at center with dissolve
    woman "Muy bien adelante Aki suena perfecto"
    man "Kaori antes de que nos vayamos Kaori tengo que decirte algo.."
    show woman at center with dissolve
    woman "Claro que si Aki, dime (un poco curiosa)"
    with hpunch
    man "Desde hace tiempo yo.."
    with hpunch
    woman "Que vas a decirme"
    with hpunch
    woman "Acerca de nuestra relacion"
    man "si algo asi"
    woman "Esta bien"
    "{i}She tums to you.{/i}"
    man "lo que pasa es que me gustas"
    woman "No se que decir..., como te llamas?"

    pause 1
    
    $ P = renpy.input("Enter your name")

    pause 1.0

    woman "Entonces eres %(P)s."
    woman "Que lindo nombre."
    pause 0.5

    P "Gracias"
    P "es un placer"
    pause 
    woman "de nada"
    woman "Te dare esto xd"
    $Cash += 300 
    
    P "Gracias por el cash %(Cash)s "
    P "me ayudo mucho"
    hide Woman with dissolve
    pause 1
    jump Escuelahub

    #This creates a label
    label Escuelahub:
        #this creates a menu
        menu:
            "Parque":
                scene black with dissolve
                "Te diriges al parque."
                pause 1
                scene Parque with dissolve
                pause 0.5
                jump Parquehub

            "Estacionamiento":
                scene black with dissolve
                "Te diriges al estacionamiento"
                pause 1
                scene Estacionamiento with dissolve
                pause 1
                jump Estacionamientohub
            "Casa":
                "Te diriges a la casa"
                scene black with dissolve
                pause 1
                scene Casa with dissolve
                pause 0.5
                jump Casahub 
            "Azotea":
                "Te diriges a la Azotea"
                scene black with dissolve
                pause 1
                scene Azotea with dissolve
                pause 0.5
                jump Azoteahub
            "Canchas":
                "Te diriges a las canchas"
                scene black with dissolve
                pause 1
                scene Canchas with dissolve
                pause 0.5
                jump Canchashub

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

    # Finaliza el juego:

    return

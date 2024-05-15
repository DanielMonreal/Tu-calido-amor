label Azoteahub:
    menu:
        "Tomar dinero de la mesa":
            "Has tomado dinero de la mesa."
            $Cash += 100
            pause 0.5
            jump Azoteahub
        "Salir de la azotea":
            scene black with dissolve
            "Has salido fuera de tu casa"
            pause 1
            scene Casa with dissolve
            pause 0.5
            jump Casahub
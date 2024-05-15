label Casahub:
    menu:
        "Dormir":
            scene black with dissolve
            pause 1
            "Te vas a dormir."
            pause 1
            scene Casa with dissolve
            $Day += 1
            jump Casahub
        "Estudiar":
            scene black with dissolve
            "Vas para la escuela"
            scene Escuela with dissolve
            pause 0.5
            jump Escuelahub
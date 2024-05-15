label Parquehub:
    menu:
        "Dormir":
            scene black with dissolve
            pause 1
            "Te vas a dormir."
            pause 1
            scene Parque with dissolve
            $Day += 1
            jump Parquehub
        "Comer":
            scene black with dissolve
            "Vas para la escuela"
            scene Escuela with dissolve
            pause 0.5
            jump Escuelahub


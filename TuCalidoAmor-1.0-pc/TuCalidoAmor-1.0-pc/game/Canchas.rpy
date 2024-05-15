label Canchashub:
    menu:
        "Refresco - 30$":
            if Cash >= 30:
                $Refresco += 1
                $Cash -= 30
                pause 0.3
                jump Canchashub
            else:
                P "No tengo dinero papu"
                pause 0.5
                jump Canchashub
        "Papas - 25$":
            if Cash >= 25:
                $Papas += 1
                $Cash -= 25
                pause 0.3
                jump Canchashub
            else:
                P "No tengo dinero para esto"
                pause 0.5
                jump Canchashub
        "Chocolate - 15$":
            if Cash >= 15:
                $Papas += 1
                $Cash -= 25
                pause 0.3
                jump Canchashub
            else:
                P "No tengo dinero para esto"
                pause 0.5
                jump Canchashub
        "Salir de la cancha":
            scene black with dissolve
            "Vas para la escuela"
            pause 1
            scene Escuela with dissolve
            pause 0.5
            jump Escuelahub

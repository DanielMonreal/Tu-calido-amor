label Estacionamientohub:
    menu:
        "Caminar para la salida":
            "Tomas tu bicicleta"
            scene Parque with dissolve
            $Cansancio += 10
            pause 0.5
            jump Estacionamientohub
        "Regresar al aula":
            scene black with dissolve
            "Vas para la escuela"
            pause 1
            scene Escuela with dissolve
            pause 0.5
            jump Escuelahub
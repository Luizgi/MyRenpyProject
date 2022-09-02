# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hyuga")
define n = Character("Narrador")
define d = Character("Voz Desconhecida")


# The game starts here.

label start:

    scene street_autumn_day


    n "Este é o primeiro dia de aula de nosso heroí, assim como todos os outros adolescentes, ele gostaria de estar jogando video-game e comendo sorvete"
    n "Mas ele está indo para escola, por obrigação de sua mãe"

    show hyuga sad
    h "Espero que essa escola não seja igual a todas as outras, afinal, já passei por 3 delas"
    h "Espero que os meninos fiquem na mesma sala que eu"
    hide hyuga sad

    d "HYUGAAAAAAAAAAAAAAAAAAAAAAAAAA"


    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hyuga")
define n = Character("Narrador")
define d = Character("Voz Desconhecida")
define m = Character ("Maki")
define s = Character ("Senhorita Morello")

# The game starts here.

label start:


    scene street_autumn_day
    with dissolve

    n "Este é o primeiro dia de aula de nosso heroí, assim como todos os outros adolescentes, ele gostaria de estar jogando video-game e comendo sorvete"
    n "Mas ele está indo para escola, por obrigação de sua mãe"

    show hyuga sad
    h "Espero que essa escola não seja igual a todas as outras, afinal, já passei por 3 delas"
    h "Espero que os meninos fiquem na mesma sala que eu"
    hide hyuga sad

    d "HYUGAAAAAAAAAAAAAAAAAAAAAAAAAA"

    show hyuga happy
    h "Deve ser a Maki"
    h "Finalmente um dos meus amigos, pelo menos esse ano não vou ficar sozinho"
    hide hyuga happy

    show maki happy
    m "Hyuga, senti tanto a sua falta"

    show maki happy at left
    show hyuga happy at right
    h "Eu também Maki, por onde tem passado"
    h "Por que não foi pro colegio estadual no ano passado?"
    hide maki happy
    hide hyuga happy

    show maki annoying at left
    show hyuga surprised at right
    m "S...Sa...Sabe, eu passei um tempinho na California"
    h "Eu não posso acreditar"
    hide maki annoying
    hide hyuga surprised

    show maki normal at left
    show hyuga laugh at right
    h "So whats up my friend"
    h "Tell me everything abouy your travel"
    m "Você sabia que o seu inglês é péssimo"
    h "Tá falando isso por pura inveja"
    hide maki normal
    hide hyuga laugh

    n "Então, Maki e Hyuga conversaram durante toda a sua viagem até a escola"
    n "Hyuga já não estava mais tão triste"
    n "Já havia esquecido a briga que tinha tido com a sua mãe mais cedo"

label cena2:

    scene classroom_scene
    with dissolve

    show srta morello angry
    s "Ei vocês dois, porque demoraram tanto?"
    hide srta morello angry

    show hyuga laugh
    h "Sabe o que é Senhorita Morello, é que o nosso metro atrasou"
    hide hyuga laugh

    show srta morello angry
    s "Caro Hyuga, sente na sua carteira agora ou irei te dar falta imediatamente"
    s "Logo no primeiro dia de aula??"

    menu:
        "Iniciar":
            jump start
        "Cena2":
            jump cena2

    return

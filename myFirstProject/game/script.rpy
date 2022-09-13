# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hyuga")
define n = Character("Narrador")
define d = Character("Voz Desconhecida")
define m = Character ("Maki")
define s = Character ("Senhorita Morello")
define r = Character ("Ramura")
define k = Character ("Diretor Kaio")
define mult = Character ("Os dois")

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
    h "Tell me everything about your travel"
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
    hide srta morello angry

    show ramura angry
    r "Ei, imbecíl, sai da minha frente"
    hide ramura angry

    show hyuga angry
    h "Não estou te atrapalhando, otário"
    hide hyuga angry

    show ramura angry
    r "Você quer partir para briga então seu babaca?"
    hide ramura angry

    n "Então, lhes apresento a mais inovadora da tecníca de jogos: O poder de escolha"
    n "Aqui você poderá decidir o futuro do nosso personagem"
    n "Mas, tome cuidado, toda ação..."
    n "Tem reação"



    menu:
        "Bater em Ramura":
            jump opt1
        "Ficar na sua":
            jump opt2
label opt1:
    show srta morello angry
    s "Ei, vocês dois, vão para a diretoria..."
    s "A....GO....RA"
    hide srta morello angry

    scene sitting_room
    with dissolve

    show director_kaio
    k "Ei vocês"
    k "O que estão fazendo aqui no horário da minha massagem espiritual, com pepino do mar, e folhas de bananeira?"
    hide director_kaio

    show ramura angry at right
    show hyuga angry at left
    r "Esse idiota tentou me bater"
    h "Eu só fiz isso porque você implicou comigo"
    h "Mas eu não iria bater mesmo"
    h "Quer saber, você é muito molenga mesmo"
    r "Tá vendo diretor, esse pedaço de bosta começou a briga, eu não tenho nada a ver com isso"
    r "Eu nem conheço ele na verdade"
    hide ramura angry
    hide hyuga angry

    show director kaio angry
    k "Ei, vocês dois"
    k "Eu não quero saber quem começou, ou quem terminou, vocês tem que saber, que essa é uma escola de respeito"
    k "Quero que vocês dois peçam desculpa um para o outro"

    show ramura surprised at right
    show hyuga surprised at left
    mult "Desculpa"

    return

label opt2:
    show hyuga smirk
    h "Até parece que eu bateria em alguem como você, não merece meu tempo"

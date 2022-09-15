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
define hm = Character ("Na mente de Hyuga")
define t = Character ("Toki")
define mm = Character ("Kenma")

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
    hide director kaio angry

    show ramura angry at right
    show hyuga surprised at left
    mult "Desculpa"
    hide ramura angry
    hide hyuga surprised

    show director_kaio
    k "Agora... Você Ramura, terá uma suspensão de 15 dia"
    hide director_kaio

    show ramura angry
    r "Mas Diretor, eu não fi..."
    hide ramura angry
    show director_kaio
    k "Shiu garoto, não viu que eu estou falando"
    k "E você...Qual é o seu nome mesmo?"
    hide director_kaio
    show hyuga surprised
    h "Hyuga..."
    hide hyuga surprised
    show director_kaio
    k "Isso, isso, Hyuga..."
    k "Obrigado Samuca"
    k "Enfim, voltando ao assunto"
    k "Você terá 25 dias de suspensão, não é a primeira vez que você toma uma ocorrência"
    k "Então, na próxima vez que precisar chamar sua atenção "
    k "Você será EX-"
    k "PUL-"
    k "SO"
    hide director_kaio

    scene galaxy
    show hyuga surprised
    hm "Meu"
    hm "Deus"
    hm "A minha mãe vai me matar"
    hm "O que será que eu vou fazer"
    hm "Na próxima semana vai ter prova"
    hm "Eu vou perder a prova"
    hm "A minha mãe vai me matar"
    hide hyuga surprised
    show hyuga smirk
    hm "Já sei"
    hm "Eu vou fugir de casa"
    hide hyuga smirk
    show hyuga surprised
    hm "Mas e a Maki?!"
    hm "Mas e minha irmã Toki"

    d "Hyuga?"
    d "Hyuga???"
    d "Hyuga????????"

    scene livingroom_night
    show hyuga sad
    h "Oi mamãe"
    hide hyuga sad

    show momma
    mm "Como foi o dia na escola?"
    hide momma
    show hyuga sad
    h "Sabe o que é mãe"
    hide hyuga sad
    show toki
    t "Iiih, tá namorando"
    hide toki
    show hyuga sad
    h "Quem me dera"
    hide hyuga sad
    show toki2
    t "O que aconteceu então?"
    hide toki2
    show momma
    mm "O que aconteceu então?"
    hide momma
    show hyuga sad
    h "Eu fui suspenso por um mês"
    hide hyuga sad
    show momma piss
    mm "Como é que é?"
    mm "VOCÊ CONSEGUIU SER SUSPENSO NA PRIMEIRA SEMANA DE AULA DESSE BIMESTRE???"
    mm "EU NÃO QUERO MAIS SABER DE NADA"
    mm "VOCÊ VAI MUDAR DE ESCOLA, E VAI PARA A MESMA ESCOLA QUE SUA IRMÃ"
    hide momma piss
    show toki
    t "haha"

    scene galaxy
    n "Tá vendo...?"
    n "Eu disse para você, tudo tem consequência! Que tal voltar na ultima decisão?"
menu:
    "Sim":
        jump cena2
    "Não":
        jump End
label End:
    n "Então, esse é o final!"


    return

label opt2:
    show hyuga smirk
    h "Até parece que eu bateria em alguem como você, não merece meu tempo"
    hide hyuga smirk

    scene school_hallway_day
    show maki happy
    m "Eiii Hyugaa"
    hide maki happy
    show hyuga smirk
    h "Ei Maki"
    h "Você viu o Ramura, tentando brigar comigo"
    h "Até parece que eu ia brigar com ele, olha meu porte físico, eu provavelmente seria amassado pro ele"
    h "Eu nunca fiz nenhum esporte, sou fraco, olha meu braço"
    hide hyuga smirk
    show maki normal
    m "Para com isso Hyuga"
    m "Você realmente é bem fraco"
    m "Provavelmente perderia mesmo, perderia até pra mim"
    hide maki normal
    
    scene galaxy
    show hyuga sad
    hm "A muito tempo eu tô querendo contar para Maki"
    hm "Desde o ensino fundamental eu tô segurando meu segredo"
    hm "Já sei, e se eu contasse para ela agora?"
    hide hyuga sad

menu:
    "Contar para Maki":
        jump End2
    "Manter o segredo":
        jump End3

label End2:
    scene school_hallway_day
    show hyuga smirk
    h "Você sabe que..."
    h "Desde o ano passado eu venho esperando para te contar isso"
    h "A verdade é que..."
    hide hyuga smirk 
    show maki normal
    m "Conta logo, você é muito lerdo"
    hide maki normal
    show hyuga smirk
    h "Tá bom, ta bom"
    h "É que..."
    d "Hyugaaaa, vamos para casa"
    hide hyuga smirk

    show momma at right
    mm "Ei, Maki, quanto tempo"
    show maki normal at left
    m "Ei Senhorita Ken"
    m "Quanto tempo"
    mm "Sim, muito tempo mesmo!!Por onde você tava?"
    m "Ahh, eu fui para California"
    mm "Hmm, que chique"
    d "Maki, vamos para casa"
    m "Eu vou para casa agora"
    mm "Ok, Makizinha, até uma próxima"
    mm "Foi um prazer te ver denovo"
    m "Igualmente"
    hide momma
    show hyuga sad at right
    h "Hã, tchau Maki"
    m "Tchau, Hyuga, amanhã você me conta o que tinha para dizer"
    m "Confesso que fiquei um pouco curiosa"
    scene galaxy
    n "Viu?! "
    n "Nem sempre aquilo que você almeja, vai dar certo"
    n "Desde o início isso foi uma grande piada"
    n "Espero que fiquem bravo com isso"

    return
label End3:
    scene school_hallway_day
    d "Makii, vamos para casa"
    show maki normal
    m "Você queria dizer alguma coisa ??"
    hide maki normal
    show hyuga sad
    h "Na realidade não"
    hide hyuga sad
    show maki normal
    m "Ah, ok então"
    m "Até amanhã viu, tchauzinho"
    hide maki normal
    scene galaxy
    n "Acabou"
    n "Sério, era só isso mesmo"
    return
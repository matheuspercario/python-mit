def map_freqs(s):
    """
    s é uma string não-vazia de caracteres
    Retorna um dicionário que mapeia cada caractere em s que
    é um dígito (0-9) ao número de vezes que ele ocorre em s.
    """
    d = {}
    for char in s:
        if char.isdigit():
            if char not in d:
                d[char] = 1
            else:
                d[char] = d[char] + 1
    return d


# Por exemplo:
# print(map_freqs("12"))       # {'1': 1, '2': 1}
# print(map_freqs("a23b22"))   # {'2': 3, '3': 1}
# print(map_freqs("abc"))      # {}

msg = """
6604876475938242194892411578156
5938778408016097535139332871158714
8418583989471965934232094711220186
8483396947751591795330413525601230
9891013991615109032173008691413145
6208709163457923022584197207698456
4280715084237594599246610935233769
6069602714278789007547063812066503
0089131934421761047142851240003485
5909776582369402245551590042294568
2417304281465461187755171760452296
1113306016884779361534926351108731
7643039213765821972966875773893055
5082492694711801320407522758688091
8916348967699300248945174466602234
5007627912560976701720099251853671
0979519426418306753751007408993318
8684126961161162076607541511505520
3519230310450932271754203557448529
1189426223583324560290611264862964
5137580660657354712141892762662375
8257173407970341489267173864014004
6896714543910144851832164482983816
8644759221166972845763778570742709
3057608116050190443294316756256627
2852327566763373906031250239491845
6708869774735400025040216396837359
1915587540803513853344486475304810
7770677711131263791686023732455618
4983478978443019126334088601641953
8433184535749220885590262281237933
2365992719089577403827785142963546
0305357345240598025070030035105623
7625425660648870916620829821532302
8216919729904560071542738526547604
8487089840761657004049438856431953
9852250909255
"""
_msg = """
Hey!

Jenny, Jenny, who can I turn to?
You give me somethin' I can hold on to
I know you think I'm like the others before
Who saw your name and number on the wall

Jenny, I got your number
I need to make you mine
Jenny, don't change your number

867-5309
867-5309
867-5309
867-5309

Jenny, Jenny, you're the girl for me
Oh, you don't know me, but you make me so happy
I tried to call you before, but I lost my nerve
I tried my imagination, but I was disturbed

Jenny, I got your number
I need to make you mine
Jenny, don't change your number

867-5309
867-5309
867-5309
867-5309

I got it, (I got it), I got it
I got your number on the wall
I got it, (I got it), I got it
For a good time, for a good time call

Hey, Jenny, don't change your number
I need to make you mine
Jenny, I call your number

867-5309
867-5309
867-5309
867-5309

Jenny, Jenny, who can I turn to?
867-5309
For the price of a dime I can always turn to you
867-5309

867-5309
867-5309
867-5309
867-5309

(5309) 867-5309
(5309) 867-5309
(5309) 867-5309

---------------------------

Out of the 7,000,000 people in this world, there's only you
Almost 1,000,000 words that I could say, but none of them will do
So many years that I have lived, but it feels like I've just begun
Out of the 7,000,000 people, baby, you're the only 1
I've been too many places. I've seen too many faces
I wrote too many pages; never found a love like you (Love like you)
I don't know how to say it. It's been more than amazing
My whole life, I've been waiting; never found a love like you (Love like you)
Sleep, dream, you, repeat, live, die next to me
Sleep, dream, you, repeat, sleep, dream
Out of the 7,000,000 people in this world, there's only you
Almost 1,000,000 words that I could say, but none of them will do
So many years that I have lived, but it feels like I've just begun
Out of the 7,000,000 people, baby, you're the only 1
You were unexpected, when our lips connected
I was resurrected; never found a love like you (love like you)
Don't care where I'm headed when the world is ending
'Cause you are my heaven; never found a love like you. (Love like you)
Sleep, dream, you, repeat. Live, die next to me
Sleep, dream, you, repeat. Sleep, dream
Out of the 7,000,000 in this world, there's only you
Almost a million words that I could say, but none of them will do
So many years that I have lived, but it feels like I've just begun
Out of the 7,000,000 people, baby, you're the only 1
Surrounded by numbers
(Numbers, numbers, numbers)
You're the only 1
(Numbers, numbers, numbers, numbers)
You're the only 1
You brought me back to life
You did the unthinkable
Yeah, you are my miracle
Out of the 7,000,000 people in this world, there's only you
Almost a million words that I could say, but none of them will do
So many years that I have lived, but it feels like I've just begun
Out of the 7,000,000 people, baby, you're the only 1
Surrounded by numbers
(Numbers, numbers, numbers)
You're the only 1
(Numbers, numbers, numbers, numbers)
You're the only 1
Surrounded by numbers
(Numbers, numbers, numbers)
You're the only 1
(Numbers, numbers, numbers, numbers)
You're the only 1
"""
print(map_freqs(_msg))

from classes import *

#header() should be called on every page
def header():
    print('''
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-
                                             UNNAMED FIEFDOM GAME
-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-'''
    + textColor.WARNING + '\n            Announcement: The Pre-Release has concluded! Congrats Steelwing! || Season 1 begins on 1/3/2021!'
    + textColor.RESET)

#Define Art:
def art_titleScreen():
        print(textColor.WARNING + '''
 _    _                                      _   ______ _       __    _                    _____
| |  | |                                    | | |  ____(_)     / _|  | |                  / ____|
| |  | |_ __  _ __   __ _ _ __ ___   ___  __| | | |__   _  ___| |_ __| | ___  _ __ ___   | |  __  __ _ _ __ ___   ___
| |  | | '_ \| '_ \ / _` | '_ ` _ \ / _ \/ _` | |  __| | |/ _ \  _/ _` |/ _ \| '_ ` _ \  | | |_ |/ _` | '_ ` _ \ / _ `
| |__| | | | | | | | (_| | | | | | |  __/ (_| | | |    | |  __/ || (_| | (_) | | | | | | | |__| | (_| | | | | | |  __/
 \____/|_| |_|_| |_|\__,_|_| |_| |_|\___|\__,_| |_|    |_|\___|_| \__,_|\___/|_| |_| |_|  \_____|\__,_|_| |_| |_|\___|

~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
        ''' + textColor.RESET + '''
                                                  ,--,  ,.-.
                                   ,                   \,       '-,-`,'-.' | ._
                                  /|           \    ,   |\         }  )/  / `-,',
                                  [ ,          |\  /|   | |        /  \|  |/`  ,`
                                  | |       ,.`  `,` `, | |  _,...(   (      .',
                                  \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L|
                                   \  \_\,``,   ` , ,  /  |         )         _,/
                                    \  '  `  ,_ _`_,-,<._.<        /         /
                                     ', `>.,`  `  `   ,., |_      |         /
                                       \/`  `,   `   ,`  | /__,.-`    _,   `|
                                   -,-..\  _  \  `  /  ,  / `._) _,-\`       |
                                    \_,,.) /\    ` /  / ) (-,, ``    ,        |
                                   ,` )  | \_\       '-`  |  `(               |
                                  /  /```(   , --, ,' \   |`<`    ,            |
                                 /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                           ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                          (-, \           ) \ ('_.-._)/ /,`    /
                          | /  `          `/    V   V, /`     /
                       ,--\(        ,     <_/`       ||      /
                      (   ,``-     \/|         \-A.A-`|     /
                     ,>,_ )_,..(    )\          -,,_-`  _--`
                    (_ \|`   _,/_  /  \_            ,--`
                     \( `   <.,../`     `-.._   _,-`    ''' + textColor.WARNING + '''

~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
        ''')

#==================================================
#   Stronghold Art
#==================================================
#  V     .                           v  .
#      ^  |>>{\                     ^    |>>{\
#         |  \}>>  /\_/\_/\_/\_/\        |  \}>>
#        /^\       [=-  -  -  -=]       /^\
#      ,'/^\'.     \............/     ,'/^\'.
#      [ - - ]      \'`'`'`'`'`/      [ - - ]
#  ___ |=,-. |/\/\/\[]- - =-= []/\/\/\|=,-. |
#,'&&&`| |_| ||' '`'||_=_=-_-_|| `' '|| |_|-|   ___
#&&&&&&| =- |/-   = /""|=||=|""\=` =  \| ` =|-''&&&
#&&&&&&|=  /[]= -  ||' \|/\|/  || -  =[]\- =|&&&&&&
#&&&&&&| -|`[] =  `|| [=]  [=] ||  =  []`|-,|&&&&,/
#&&&&&_|` '-[]-  - ||{-} -` {-}|| = `-[]-|` |%_,',
#&&,,' | -|-[]  = .|" `.====.  "|. - _[],,..-', . .
#-- . ,|= |-[] =  ||" =|::::|= "||,-'  ,  .  .   .
#. , .,\__|-[]-  =||" =|::::|= ,+',  .   * .  , . ,
# .    ,  `-------'^--o/'  '\o',  .   . ,   , .   .
#.  ' ,    '  .  -   O/      \O  *            '  *
#==================================================
def art_stronghold(biome, flag):
    F = flagColor(flag)
    C = biomeColor(biome)
    R = textColor.RESET
    W = textColor.RED
    Y = textColor.YELLOW
    G = textColor.GREEN
    M = textColor.MAGENTA
    D = textColor.DIM
    Z = "\\"
    I = "'"
    print('''
                   V     .                           v  .
                      ^  |'''+F+'''>>{\ '''+R+'''                    ^    |'''+F+'''>>{'''+Z+R+'''
                         |  '''+F+'''\}>>'''+R+'''  /\_/\_/\_/\_/\        |  '''+F+'''\}>>'''+R+'''
                      '''+F+'''  /^\ '''+R+'''      [=-  -  -  -=]       /^'''+Z+'''
                      '''+F+''','/^'''+Z+I+'''.'''+R+'''     \............/     '''+F+''','/^'''+Z+I+'''.'''+R+'''
                      [ - - ]      \'`'`'`'`'`/      [ - - ]
                  '''+D+'''___ '''+R+'''|=,-. |/\/\/\[]- - =-= []/\/\/\|=,-. |
                '''+D+''','''+I+'''&&&'''+R+'''`| |_| ||' '`'||_=_=-_-_|| `' '|| |_|-|   '''+D+'''___'''+R+'''
                '''+D+'''&&&&&&'''+R+'''| =- |/-   = /""|=||=|""\=` =  \| ` =|'''+D+'''-''&&&'''+R+'''
                '''+D+'''&&&&&&'''+R+'''|=  /[]= -  ||' \|/\|/  || -  =[]\- =|'''+D+'''&&&&&&'''+R+'''
                '''+D+'''&&&&&&'''+R+'''| -|`[] =  `|| [=]  [=] ||  =  []`|-,|'''+R+'''&&&&'''+D+''',/
                '''+D+'''&&&&&'''+R+'''_|` '-[]-  - ||{-} -` {-}|| = `-[]-|` |'''+D+'''&'''+R+'''_,',
                '''+D+'''&&'''+R+''',,' | -|-[]  = .|" `.====.  "|. - _[],,..-' '''+C+''',  .'''+R+'''
                --'''+C+''' . ,'''+R+'''|= |-[] =  ||" =|::::|= "||,-' '''+C+''' ,  .  .   .'''+R+'''
                '''+C+'''. , .,'''+R+'''\__|-[]-  =||" =|::::|= ,+' '''+C+''',  .   '''+M+'''*'''+C+''' .  , . ,'''+R+'''
                '''+C+''' .    ,'''+R+'''  `-------'^--o/'  '\o '''+C+''',  .   . ,   , .   .'''+R+'''
                '''+C+'''.  ' ,    '  .  -  '''+R+''' O/      \O  '''+M+'''*'''+R+'''     '''+C+'''       '  '''+M+'''*'''+R+'''
        ''')

#==================================================
#   Fief Art 0: OpenCamp
#==================================================
#  ,''-,.,----_                                 _,
#,'         ..|                             ,,-'
#| , --   ..._ \                           /
#`'   ,       \/                          ,'_,,   _
#| )  `..-    |                          ,,:   ,-'
#. :-    _> _,-                         /  \   |
#".-. /'' ,'                           |    |  |
#   {  |''      ,.............,        |   /  /
#   {{ ||    __/ \         ___ \ ...-'' \  ,-',.___
#  _.{ '|---' / / \  ''         \oo  ,.__`.      \.
#`' {  |'    /.'   \    -     )  \ooO    ,'\`-.._ `
#  ,' | '\ ^/ .__.. \.____=___=''.\OOO  | .\    `:-
#  ___            `'^'   ';  '' ' ^    .._ -
# /,' `\.                       __   o..| |'|O
# |||-- '|  \.        /'       [__] o.`--. [O\o  _,
# ```-''|+ ,                   /--\   `[] o..O  / `
#  `'   '  '``-....--`-------.-.........,-----'' \.
#==================================================
def art_fief0(biome):
    C = biomeColor(biome)
    R = textColor.RESET
    W = textColor.RED
    Y = textColor.YELLOW
    G = textColor.GREEN
    D = textColor.DIM
    Z = "\\"
    I = "'"
    print('''
'''+G+'''  ,''-,.,----_'''+R+'''                                 _,
'''+G+''','         ..|'''+R+'''                             ,,-'
'''+G+'''| , --   ..._ '''+Z+R+'''                           /
'''+G+'''`'   ,       \/'''+R+'''                          ,'_,,   _
'''+G+''' )  `..-    |'''+R+'''                          ,,:   ,-'
'''+G+'''. :-    _> _,-'''+R+'''                         /  \   |
'''+G+'''".-. /'' ,' '''+R+'''                          |    |  |
'''+W+'''   {  |'' '''+R+'''     ,.............,        |   /  /
'''+W+'''   {{ || '''+R+'''   '''+C+'''__'''+R+'''/ \         ___ \ '''+C+'''...-'`'''+R+''' \  ,'''+C+'''-'''+R+'''','''+C+'''.___'''+R+'''
'''+C+'''  _'''+R+W+'''.{ '|'''+C+'''---`'''+R+''' / / \  ''         '''+Z+D+'''oo  '''+C+''',.__'''+R+'''`.      '''+C+'''\.'''+R+'''
'''+C+'''``'''+R+W+''' {  |' '''+R+'''   /.'   \    -     )  '''+Z+D+'''ooO    ,'''+R+I+W+R+Z+'''`'''+C+'''-.._ `'''+R+'''
'''+W+'''  ,' | '\ '''+R+C+'''^'''+R+'''/ .__.. \.____'''+C+'''='''+R+'''___'''+C+'''=''.'''+R+Z+D+'''OOO  | '''+W+'''.'''+R+'''\    '''+C+'''`:-'''+R+'''
'''+D+'''  ___  '''+R+'''          '''+C+'''`'^'   ';  '' ' ^'''+R+'''    '''+W+'''.'''+Y+'''.'''+R+'''_ -
'''+D+''' /,' `\.  '''+R+'''                     __   '''+D+'''o'''+R+'''.'''+W+'''.|'''+R+Y+''' |'''+I+W+'''|'''+D+'''O'''+R+'''
 '''+C+'''|||'''+D+'''-- '|  '''+C+'''\.        /' '''+R+'''      [__] '''+D+'''o'''+R+'''.'''+W+'''`'''+R+'''--'''+W+'''.'''+R+''' '''+W+'''['''+D+'''O'''+Z+D+'''o'''+R+'''  '''+C+'''_,'''+R+'''
 '''+C+'''```-''|+ ,'''+R+'''                   /--\   `[] '''+D+'''o'''+R+'''..'''+D+'''O'''+R+'''  '''+C+'''/ `'''+R+'''
'''+C+'''  `'   '  '``-....--`-------.-.........,-----'' \.'''+R+'''
    ''')

#==================================================
#   Fief Art 1: Wooden Fences
#==================================================
#                             ^
#         v                             ^
#   /\                                      /` /`
#  //`\                 ____               //`//`
#  //`\               ,'/||\`.             /`\//`
# ///`\  ___   __    ///||||\`\    __   __//`// `|
# ///`\ /`\`\_/`\`. /////||`\`\` ,///`_////`|///``|
# //\`\//`\`\/`|`|'\|O________O|//////`////`\///``|
#////`\O____O____[]O|O[]|--|[]O|O[]____O____O  ||'`
#|  ||_O[]__O_| |__O|O__|''|__O|O__| | O__[]O,'   |
#XX--. _  '  '  '   `  `0  0  ' '   ''   '  _ ,--X'
#  X_ \/`-._______  __========__  ____,,-\/' \/ X
# `  -/\   | \/|||\/==||||||||==\/||||\/ /\_|/\=  `
#    =---=_|_/\|||/\__||||||||__/\||||/\_==     ``
#  `    `      `     o========o`     `    `  `  `
#    `      `      `O/`     ` \O  `    `    `  `
#    `  `          O/ ' `  '   \O     `     `    `
#==================================================
def art_fief1(biome):
    C = biomeColor(biome)
    R = textColor.RESET
    G = textColor.GREEN
    Y = textColor.YELLOW
    Z = '\\'
    print('''
                             ^
         v                             ^
'''+G+'''   /\                                      /'''+Z+''' /'''+Z+'''
  //'''+Z+'''\                 '''+Y+'''____'''+G+'''               //'''+Z+'''//'''+Z+'''
  //'''+Z+'''\               '''+Y+''','/||\`.'''+G+'''             /'''+Z+'''\//'''+Z+'''
 ///'''+Z+'''\ '''+Y+''' ___   __    ///||||\`\    __   __'''+G+'''//'''+Z+'''// '''+Z+Z+'''
 ///'''+Z+'''\ '''+Y+'''/'''+Z+Z+Z+Z+'''_/'''+Z+Z+Z+'''. /////||'''+Z+Z+Z+Z+Z+''' ,///'''+Z+'''_////'''+Z+G+Z+'''///'''+Z+Z+Z+'''
 //'''+Z+Z+Z+Y+'''//'''+Z+Z+Z+Z+'''/'''+Z+Z+Z+Z+Z+Z+R+'''|O________O|'''+Y+'''//////'''+Z+'''////'''+Z+Z+''''''+G+'''///'''+Z+Z+Z+'''
////'''+Z+Z+R+'''O____O____[]O|O[]|--|[]O|O[]____O____O  ||'''+G+''''''+Z+Z+R+'''
|  ||_O[]__O_| |__O|O__|''|__O|O__| | O__[]O'''+C+''',' '''+R+'''  |
XX--. _'''+C+'''  '  '  '   `  `'''+R+'''0  0 '''+C+''' ' '   ''   ' '''+R+''' _ ,--X'
  X_ \/`-._______  __========__  ____,,-\/' \/ X
'''+C+''' ` '''+R+''' -/\   | \/|||\/==||||||||==\/||||\/ /\_|/\= '''+C+''' `'''+R+'''
    =---=_|_/\|||/\__||||||||__/\||||/\_==   '''+C+'''  ``'''+R+'''
'''+C+'''  `    `      `   '''+R+'''  o========o'''+C+'''`     `    `  `  `'''+R+'''
'''+C+'''    `      `      `'''+R+'''O/'''+C+'''`     ` '''+R+'''\O '''+C+''' `    `    `  `'''+R+'''
'''+C+'''    `  `          '''+R+'''O/'''+C+''' ' `  '   '''+R+'''\O '''+C+'''    `     `    `'''+R+'''
    ''')

#==================================================
#   Fief Art 2: Really Deep Trenches
#==================================================
#    \,/
#
#                    |>>>>    |>>>>           ^
#                    |   __   |
#             |>>>> [=|=|[]|=|=]     |>>>>
#          ___|___  []    .   []  ___|___
#         |||_|_||   [ (). () ]   ||_|_|||
#          \||   /__[  ||  ||  ]__\   ||/
#          [+| .|  _ .   _.   . _  |. |+]
#          [+|. | ['] . /||\ . ['] | .|+]
#          [+|  | ===  ||--||  === |  |+]
#_..__.,-''[+| .|  . . |====| . .  |. |+]---,- ..
#    |` | |______|_____|____|_____|______| | `|  `-
#    |` |______________|.  .|_____________ | `|
#    \  `|''||'|'|''|'||:  :||'|'||'||''|'|`  /
#     \=-=-==-==-===-=-o.  .o-=-=-=-===-==-=-/
# '       '            '  '  '   '       '
#==================================================
def art_fief2(biome):
    C = biomeColor(biome)
    R = textColor.RESET
    D = textColor.DIM
    print('''
    \,/

                    |'''+C+'''>>>> '''+R+'''   |'''+C+'''>>>>   '''+R+'''        ^
                    |   __   |
             |'''+C+'''>>>>'''+R+''' [=|=|[]|=|=]     |'''+C+'''>>>>'''+R+'''
          ___|___  []    .   []  ___|___
         |||_|_||   [ (). () ]   ||_|_|||
          \||   /__[  ||  ||  ]__\   ||/
          ['''+D+'''+'''+R+'''| .|  _ .   _.   . _  |. |'''+D+'''+'''+R+''']
          ['''+D+'''+'''+R+'''|. | ['] . /||\ . ['] | .|'''+D+'''+'''+R+''']
          ['''+D+'''+'''+R+'''|  | ===  ||--||  === |  |'''+D+'''+'''+R+''']
'''+C+'''_..__.,-'`'''+R+'''['''+D+'''+'''+R+'''| .|  . . |====| . .  |. |'''+D+'''+'''+R+''']'''+C+'''---,- ..'''+R+'''
'''+C+'''    |` | '''+R+'''|______|_____|____|_____|______|'''+C+''' | `|  `-'''+R+'''
'''+C+'''    |` |______________'''+R+'''|.  .|'''+C+'''_____________ | `|'''+R+'''
'''+C+'''    \ '''+R+''' `|''||'|'|''|'||:  :||'|'||'||''|'|` '''+C+''' /'''+R+'''
'''+C+'''     \=-=-==-==-===-=-'''+R+'''o.  .o'''+C+'''-=-=-=-===-==-=-/'''+R+'''
'''+C+''' '       '            '  '  '   '       ' '''+R+'''
    ''')

#==================================================
#   Fief Art 3: Tall Towers
#==================================================
#                                        v
#                       _/\_               ^
#        v          /\ /____\ /`
#                  /__\ |<>| /__`
#              _/\_|++| |<>| |++|_/`_
#             /____\[]| |<>| |[]/____`
#              |[]||++| |<>| |++||[]|
#              |[]||++|_|<>|_|++||[]|
# ___________  |__||_=-=-=-=-=-_||__|  ___________
#/_ _____    \_|^^^^^<={~00~}=>^^^^^|_/    _____ _`
#  |_____|_____ ' '` <= {__} =>` '`' _____|_____|
# /_____,'  _  |` '`<_=_/||\_=_> ``'|  _  `._____`
#O _______,'_\ |`' <|_=_|..|_=_|>`'`| /_`._______ O
# /________/   ``--.._=_|--|_=_,,--''   \________`
#     '         '    'o/`` `\o  '    ' '       '
#   '     '   ' '    o/ '  ' \o   '       '    '  '
#     '             O/ ' '  ' \O      '     '    '
#==================================================
def art_fief3(biome):
    C = biomeColor(biome)
    R = textColor.RESET
    D = textColor.DIM
    Y = textColor.YELLOW
    Z = '\\'
    print('''
                                        v
                       _/\_               ^
        v          /\ /____\ /'''+Z+'''
                  /__\ |<>| /__'''+Z+'''
              _/\_|++| |<>| |++|_/'''+Z+'''_
             /____'''+Z+D+'''[]'''+R+'''| |<>| |'''+D+'''[]'''+R+'''/____'''+Z+'''
              |[]||++| |<>| |++||[]|
              |[]||++|_|<>|_|++||[]|
'''+C+''' ___________  '''+R+'''|__||_=-=-=-=-=-_||__|'''+C+'''  ___________'''+R+'''
'''+C+'''/_ _____    \_'''+R+'''|^^^^^<='''+Y+'''{~00~}'''+R+'''=>^^^^^|'''+C+'''_/    _____ _`'''+R+'''
'''+C+'''  |_____|_____'''+R+''' ' '` '''+C+'''<'''+R+'''= {__} ='''+C+'''>'''+R+'''` '`' '''+C+'''_____|_____|'''+R+'''
'''+C+''' /_____,'  _  '''+R+'''|` '`'''+C+'''<'''+R+'''_=_/||\_=_'''+C+'''>'''+R+''' ``'|'''+C+'''  _  `._____`'''+R+'''
'''+C+'''O _______,'_\ '''+R+'''|`' '''+C+'''<'''+R+'''|_=_|..|_=_|'''+C+'''>'''+R+'''`'`|'''+C+''' /_`._______ O'''+R+'''
'''+C+''' /________/   ``'''+R+'''--.._=_|--|_=_'''+C+''',,'''+R+'''--'''+C+'''`'   \________`'''+R+'''
'''+C+'''     '         '    `'''+R+'''o/`` `\o '''+C+''' '    ' '       ' '''+R+'''
'''+C+'''   '     '   ' '   '''+R+''' o/ '  ' \o '''+C+'''  '       '    '  '''+R+'''
'''+C+'''     '          '''+R+'''   O/ ' '  ' \O  '''+C+'''    '     '    ' '''+R+'''
    ''')
    
#==================================================
#   Fief Art 4: In a Lake
#==================================================
#                                      v
#                 ^        />>>>
#                         /`
#                        /[]\                    ^
#               |>>>    <{==}>       |>>>
#       V      /^\       |--|       /^`
#              /=\       |[]|       /=`
#              |=|_=_=_=_|/\|_=_=_=_|=|
#              |# +0 _+_ 0''0 _+_ 0+ #|
#/--=--- -=-=--|#   -  o (__) o  -   #|---=-=  ----=
#   _____-  __ |# +_ -o(_|[]|_)o- _+ #| __-  __- __
#     -  =--  [|#+_ +_  |[[]]|  _+ _+#|]  __
#O       -    [{[{[_____|[[]]|_____]}]}]  =- __
#   _<]_   __  =--'-|==|=-=-=-|==|-_--=  __       -
#  _\__/  ____     _|==|_    -|==|[_]   ____=--   -
#   '-    -    --=  |==|      |==|\_/      -
#      =-     =--     -   -- --          -=      =-
#==================================================
def art_fief4(biome):
    C = biomeColor(biome)
    B = textColor.BLUE
    Y = textColor.CYAN
    R = textColor.RESET
    Z = '\\'
    print('''
                                      v
                ^        /'''+C+'''>>>>'''+R+'''
                        /'''+Z+'''
                       /[]\                    ^
              |'''+C+'''>>>'''+R+'''    <{==}>       |'''+C+'''>>>'''+R+'''
      V      /^\       |--|       /^'''+Z+'''
             /=\       |[]|       /='''+Z+'''
             |=|_=_=_=_|/\|_=_=_=_|=|
             |# +0 _+_ 0''0 _+_ 0+ #|
'''+B+'''--=---'''+R+''' '''+Y+'''-=-=--'''+R+'''|#   -  o (__) o  -   #|'''+B+'''---=-='''+R+'''  '''+Y+'''----='''+R+'''
  '''+Y+'''_____-'''+R+'''  '''+B+'''__ '''+R+'''|# +_ -o(_|[]|_)o- _+ #|'''+Y+''' __-'''+R+'''  '''+B+'''__- __'''+R+'''
'''+B+'''    -'''+R+'''  '''+Y+'''=--'''+R+'''  '''+C+'''['''+R+'''|#+_ +_  |[[]]|  _+ _+#|'''+C+'''] '''+R+''' '''+B+'''__'''+R+'''
'''+Y+'''       -'''+R+'''    '''+C+'''[{[{['''+R+'''_____|[[]]|_____'''+C+''']}]}]'''+R+'''  '''+Y+'''=-'''+R+''' '''+B+'''__'''+R+'''
  _<]_  '''+B+''' __'''+R+'''  '''+Y+'''=--'-'''+R+'''|==|=-=-=-|==|'''+B+'''-'''+R+'''_'''+B+'''--='''+R+'''  '''+Y+'''__'''+B+'''       -'''+R+'''
'''+B+''' _'''+R+'''\__/  '''+Y+'''____'''+R+'''     '''+B+'''_'''+R+'''|==|'''+Y+'''_'''+R+'''    '''+B+'''-'''+R+'''|==|[_]  '''+Y+''' ____=--'''+R+'''   '''+B+'''-'''+R+'''
'''+Y+'''  '- '''+R+''' '''+B+'''  -  '''+R+''' '''+Y+''' --= '''+R+''' |==|      |==|\_/   '''+B+'''   - '''+R+'''
'''+Y+'''     =- '''+R+'''    '''+B+'''=--  '''+R+'''  '''+Y+''' - '''+R+'''  '''+B+'''--'''+R+''' '''+Y+'''-- '''+R+'''        '''+B+''' -= '''+R+'''   '''+Y+'''  =-'''+R+'''
     ''')
    
#==================================================
#   Fief Art 5: On a Mountain
#==================================================
#            ,+.         /`
#          --''-:.      /__\          ^
#         /     V \   <`\--//>
#        ,       ,'`.  \(\/)/                     ,
#      _,`. /\,''    bO+|()|+Oo                  /
#     .   '`'       o+-(\/\/)-+o               _/,'
#    ,              (_('-00-')_)         v    ,'
#   /     v      <\_ -\=[~~]=/- _/>          /
#  ,              <|\ \|=--=|/ /|>          /
# /                |%\/:'__':\/%|         ,'
#/     _^_ /\ _/\_  \/# /==\ #\/  _/\_ /\`_^_
#--^=-/___\  /____\=\( |=/\=| )/=/____\  /___\---^-
#      ____ O ====__\( ||00|| )/__==== O ____
#_[]_./ == \ /\_,'=-|( ||''|| )/-=`._/\ / == \:;:;:
#--=-=``--..\ \__/  |( |-==-| )|  \__/ /,,--''\----
#[[[[[[[[[[[[[[[[[[/\__/=--=\__/\]]]]]]]]]]]]]]]]]]
#      '       '       ''''''    '         ' '
#==================================================
def art_fief5(biome):
    C = biomeColor(biome)
    D = textColor.DIM
    R = textColor.RESET
    N = textColor.CYAN
    E = textColor.RED
    Y = textColor.YELLOW
    Z = '\\'
    print('''
'''+D+'''            ,+.   '''+R+'''    '''+N+'''  /'''+Z+R+'''
'''+D+'''          --''-:. '''+R+'''     '''+N+'''/__\   '''+R+'''       ^
'''+D+'''         /    '''+R+''' V '''+D+'''\ '''+R+'''  '''+C+'''<'''+R+Z+'''\--//'''+C+'''>'''+R+'''
'''+D+'''        ,       ,'`.'''+R+'''  \(\/)/            '''+D+'''         ,'''+R+'''
'''+D+'''      _,`. /\,''  '''+R+'''  bO'''+C+'''+'''+R+'''|()|'''+C+'''+'''+R+'''Oo          '''+D+'''        /'''+R+'''
'''+D+'''     .   '`'   '''+R+'''    o'''+C+'''+'''+R+'''-(\/\/)-'''+C+'''+'''+R+'''o         '''+D+'''      _/,' '''+R+'''
'''+D+'''    ,'''+R+'''              (_('-'''+C+'''00'''+R+'''-')_)         v'''+D+'''    ,' '''+R+'''
'''+D+'''   /'''+R+'''     v      '''+C+'''<'''+R+'''\_ -\=[~~]=/- _/'''+C+'''> '''+R+'''     '''+D+'''    /'''+R+'''
'''+D+'''  ,'''+R+'''              '''+C+'''<'''+R+'''|\ \|=--=|/ /|'''+C+'''> '''+R+'''      '''+D+'''   /'''+R+'''
'''+D+''' /'''+R+'''                |'''+E+'''%'''+R+'''\/:'__':\/'''+E+'''%'''+R+'''|        '''+C+''' ,' '''+R+'''
'''+D+'''/'''+R+'''     '''+C+'''_^_'''+R+''' /\ _/\_  \/# /'''+Y+'''=='''+R+'''\ #\/  _/\_ /\`'''+C+'''_^_'''+R+'''
--^=-'''+C+'''/___'''+Z+R+'''  /____\=\( |'''+Y+'''='''+E+'''/'''+Z+Y+'''='''+R+'''| )/=/____\  '''+C+'''/___'''+Z+R+'''---^-
      ____ '''+C+'''O'''+R+''' ====__\( |'''+E+'''|'''+Y+'''00'''+E+'''|'''+R+'''| )/__==== '''+C+'''O'''+R+''' ____
_[]_./ == \ /\_,'=-|( |'''+E+'''|''|'''+R+'''| )/-=`._/\ / == \:;:;:
--=-=``--..\ \__/  |( |-==-| )|  \__/ /,,--''\----
'''+C+'''[['''+R+'''[['''+C+'''[['''+R+'''[['''+C+'''[['''+R+'''[['''+C+'''[['''+R+'''[['''+C+'''[['''+R+'''/\__/=--=\__/'''+Z+C+''']]'''+R+''']]'''+C+''']]'''+R+''']]'''+C+''']]'''+R+''']]'''+C+''']]'''+R+''']]'''+C+''']]'''+R+'''
'''+C+'''      '       '    '''+R+'''   ''''''  '''+C+'''  '         ' ' '''+R+'''
    ''')

#==================================================
#   Fief Art 6: Boiling Oil
#==================================================
#       ,-.._     _/=-=-=--=-=-=\_    v
#  ^   |  _,,'._ /|<.__.>~~<.__.>|`
#     /-''     '  \=|--|-__-|--|=/   _,-'`'--._
#   .'   /\________|===_/--\_===|___i____/\ `  `.
#   '   /__====_==_==_/[____]\_==_==_====__\ `-._`
#  /    /|_| _/'|/'\/[[| /\ |]]\/'\|'\_ |_|\     `.
# /     |/''|/.// \[[  //||`\  ]]/ `\.\|''\|      `
#|      /___/^^\-/_\==//}=={`\==/_\-/^^\___\  ^
#       |---]/\|-___-- {|--|} --___-|/\[---|
#      /|_/\_/\_/___\_/0\__/0\_/___\_/\_/\_|`
#  /\_/-==|| || |-=-| |'oUUo'| |-=-| || ||==-\_/`
#  |  `'  || ||  =-=  |oUUUUo|  =-=  || ||  +'  |
# `\< `'_|__|  +  |_|/  '__'  \|_|   + |__|_ ' >//
#\`\< '+'U  U   + U O  _[||]_  U U  +  O  U''+ >///
# `\_  ` |  | '   | |<|_||||_|>| |     |  |    _//
#\`\`\______________|_0_[--]_0_________|______/////
#      ' ~' ~ '  '~ ~ =-==-=-= ~ ~ '   ~  ~  '   '
#==================================================
def art_fief6(biome):
    C = biomeColor(biome)
    E = textColor.RED
    R = textColor.RESET
    D = textColor.DIM
    Y = textColor.YELLOW
    N = textColor.CYAN
    Z = '\\'
    I = "'"
    print('''
       ,/`\_     '''+E+'''_/=-=-=--=-=-=\_'''+R+'''    v
  ^   |  _,,'._ '''+N+'''/|'''+R+'''<.__.>'''+C+'''~~'''+R+'''<.__.>'''+N+'''|'''+Z+R+'''
     /-''     '  \=|'''+C+'''--'''+R+'''|-__-|'''+C+'''--'''+R+'''|=/   _,-'`'--._
   .'   '''+E+'''/\________'''+R+'''|===_/--\_===|'''+E+'''___'''+R+'''i'''+E+'''____/'''+Z+R+''' `  `.
   '   '''+E+'''/__'''+R+'''====_==_==_/[____]\_==_==_===='''+E+'''__'''+Z+R+''' `-._`
  /    '''+N+'''/'''+R+'''|_| _/'|/'\/'''+D+'''[['''+R+'''| '''+N+'''/\ '''+R+'''|'''+D+''']]'''+R+'''\/'\|'\_ |_|'''+N+Z+R+'''     `.
 /     |/''|/.// '''+Z+D+'''[['''+R+'''  //'''+Y+'''||'''+R+Z+'''\  '''+D+''']]'''+R+'''/ `\.\|''\|      `
|      /___/'''+N+'''^^'''+R+'''\-/_\==//}'''+Y+'''=='''+R+'''{'''+Z+'''\==/_\-/'''+N+'''^^'''+R+'''\___\  ^
       |---]/\|-___-- {'''+Y+'''|'''+R+D+'''--'''+R+Y+'''|'''+R+'''} --___-|/\[---|
      '''+E+'''/'''+R+'''|_'''+E+'''/'''+Z+R+'''_'''+E+'''/'''+Z+R+'''_/___\_/'''+N+'''0'''+R+'''\__/'''+N+'''0'''+R+'''\_/___\_'''+E+'''/'''+Z+R+'''_'''+E+'''/'''+Z+R+'''_|'''+E+Z+R+'''
  '''+E+'''/'''+Z+R+'''_/-==|| || |-=-| |'o'''+E+'''UU'''+R+'''o'| |-=-| || ||==-\_'''+E+'''/'''+Z+R+'''
  |  `'  || ||  =-=  |o'''+E+'''UUUU'''+R+'''o|  =-=  || ||  +'  |
'''+C+''' `\<'''+R+''' `'_|__|  +  |_|/  '__'  \|_|   + |__|_ ' '''+C+'''>//'''+R+'''
'''+C+'''\`\<'''+R+''' '+ '''+E+'''U  U'''+R+'''   + '''+E+'''U O'''+R+'''  _[||]_  '''+E+'''U U'''+R+'''  +  '''+E+'''O  U'''+R+''' '+ '''+C+'''>///'''+R+'''
'''+C+''' `\_ '''+R+''' ` '''+E+'''|  |'''+R+''' '   '''+E+'''| |'''+R+'''<|_||||_|>'''+E+'''| |     |  |'''+R+'''    '''+C+'''_//'''+R+'''
'''+C+'''\`\`\______________'''+R+''''''+E+'''|'''+R+''''''+C+'''_'''+R+'''0'''+C+'''_'''+R+'''[--]'''+C+'''_'''+R+'''0'''+C+'''_________'''+R+''''''+E+'''|'''+R+''''''+C+'''______/////'''+R+'''
     '''+C+''' ' '''+E+'''~'''+C+I+''' '''+E+'''~'''+C+''' '  '''+I+E+'''~ ~'''+R+''' =-==-=-= '''+E+'''~ ~'''+C+''' '   '''+E+'''~  ~'''+C+'''  '   ' '''+R+'''
    ''')

#==================================================
#   Farm Art: Rank 0
#==================================================
#  ,'  ,'   ,  ,-  ,           ,'   /           ,'
# ,'  /    /  /   /   ,' ,'   /   ,'  ,'  ,'   /  ,
#,'  /    /  /   /   /  ,'  ,'   /   /   /   .'  /
#==================================================
#==================================================
#   Farm Art: Rank 0 (new)
#==================================================
#  ,'  ,'   ,  ,-  ,           ,'   /           ,'
# ,'  /    /  /   /   ,' ,'   /   ,'  ,'  ,'   /  ,
#==================================================
def art_farm0():
    R = textColor.RESET
    D = textColor.DARK_GRAY
    G = textColor.GREEN
    print('''  '''+D+''','''+R+'''`  ,'  '''+D+''' ,'''+R+'''  ,'''+D+'''-'''+R+'''  ,           '''+D+''','''+R+'''`   '''+G+'''/'''+R+'''           ,'
 ,'  '''+G+'''/    /  /   /  '''+R+''' ,' ,'  '''+G+''' / '''+R+'''  ,'  ,'  ,'  '''+G+''' /'''+R+''' '''+D+''' ,'''+R+'''
    ''')

#==================================================
#   Farm Art: Rank 1
#==================================================
# / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / /
# / / / / / / / / / / / / / / / / / / / / / / / / /
#==================================================
#==================================================
#   Farm Art: Rank 1 (new)
#==================================================
# ` / ` / ` / ` / ` / ` / ` / ` / ` / ` / ` / ` / `
# / ` / ` / ` / ` / ` / ` / ` / ` / ` / ` / ` / ` /
#==================================================
def art_farm1():
    Y = textColor.YELLOW
    R = textColor.RESET
    print(''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' `
 '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+''' ` '''+Y+'''/'''+R+'''
    ''')

#==================================================
#   Farm Art: Rank 2
#==================================================
#[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
#[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
#[^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^ [^
#==================================================
#==================================================
#   Farm Art: Rank 2 (new)
#==================================================
#[^    [^    [^    [^    [^    [^    [^    [^    [^
#   [^    [^    [^    [^    [^    [^    [^    [^ 
#==================================================
def art_farm2():
    G = textColor.GREEN
    R = textColor.RESET
    print('''['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''
   ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+'''    ['''+G+'''^'''+R+''' 
    ''')

#==================================================
#   Farm Art: Rank 3
#==================================================
#[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
#[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
#[`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`][`~`]
#==================================================
#==================================================
#   Farm Art: Rank 3 (new)
#==================================================
#[`~`]  .  [`~`]  .  [`~`]  .  [`~`]  .  [`~`]  .
#  .  [`~`]  .  [`~`]  .  [`~`]  .  [`~`]  .  [`~`]
#==================================================
def art_farm3():
    R = textColor.RESET
    G = textColor.GREEN
    D = textColor.DARK_GRAY
    Y = textColor.YELLOW
    print('''['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  
  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']  '''+D+'''.'''+R+'''  ['''+G+'''`'''+Y+'''~'''+G+'''`'''+R+''']
    ''')

#==================================================
#   Farm Art: Rank 4
#==================================================
#[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
#[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
#[*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*][*&*]
#==================================================
#==================================================
#   Farm Art: Rank 4    (new)
#==================================================
# <^> [*&*] <^> [*&*] <^> [*&*] <^> [*&*] <^> [*&*]
#[*&*] <^> [*&*] <^> [*&*] <^> [*&*] <^> [*&*] <^> 
#==================================================
def art_farm4():
    R = textColor.RESET
    P = textColor.PURPLE
    G = textColor.GREEN
    print(''' '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+''']
['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' ['''+G+'''*'''+P+'''&'''+G+'''*'''+R+'''] '''+G+'''<'''+P+'''^'''+G+'''>'''+R+''' 
    ''')

#==================================================
#   Farm Art: Rank 5
#==================================================
#<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
#<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
#<(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)><(*)>
#==================================================
#==================================================
#   Farm Art: Rank 5    (new)
#==================================================
#<(*)> .-. <(*)> .-. <(*)> .-. <(*)> .-. <(*)> .-. 
# .-. <(*)> .-. <(*)> .-. <(*)> .-. <(*)> .-. <(*)>
#==================================================
def art_farm5():
    E = textColor.RED
    G = textColor.GREEN
    R = textColor.RESET
    print(''''''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. 
 .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+''' .'''+G+'''-'''+R+'''. '''+G+'''<'''+E+'''('''+G+'''*'''+E+''')'''+G+'''>'''+R+'''
    ''')

#==================================================
#   Farm Art: Rank 6
#==================================================
#|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
#|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
#|~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~||~@~|
#==================================================
#==================================================
#   Farm Art: Rank 6
#==================================================
# =Q= |~@~| =Q= |~@~| =Q= |~@~| =Q= |~@~| =Q= |~@~|
#|~@~| =Q= |~@~| =Q= |~@~| =Q= |~@~| =Q= |~@~| =Q= 
#==================================================
def art_farm6():
    C = textColor.CYAN
    G = textColor.GREEN
    M = textColor.MAGENTA
    Y = textColor.YELLOW
    R = textColor.RESET
    print(''' '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''|
|'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' |'''+Y+'''~'''+G+'''@'''+Y+'''~'''+R+'''| '''+M+'''='''+C+'''Q'''+M+'''='''+R+''' 
    ''')

def art_mountain():
    print(textColor.DARK_GRAY + '''M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-''' + textColor.RESET)
def art_forest():
    print(textColor.GREEN + '''^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-''' + textColor.RESET)
def art_plains():
    print(textColor.YELLOW + '''#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-''' + textColor.RESET)

#==================================================
#   Misc. Art: Globe
#==================================================
#                     ,---------.
#                 ,-'     ,--'' `-.
#              ,-'/   ..b,|        `..
#             /  |   ,'    __  ,..b | \
#            /   | _'   ,''  | \   ''  \
#           /`.  \,' _ ,/   ,>  |       \
#          / ,'     / '    \.   \_       \
#         ;  /     /        |    |     ,__:
#         :  \.   |    _,'       |     /  ;
#          \  |   \o'  `>         `.._/  /
#           \'     |     ".,.           /
#            \      |        :\    .....
#             \      `'.__.  /"   |   /
#              `-. ,b_     \ '    ',-'
#                 `-. `--.      ,-'
#                    `---'-----'
#==================================================
def art_globe():
    R = textColor.RESET
    B = textColor.BLUE
    G = textColor.GREEN
    Z = "\\"
    I = "'"
    print('''
'''+B+'''                    ,--------.
'''+B+'''                ,-'  '''+G+'''   ,--'' '''+B+'''`-.
'''+B+'''             ,-'''+I+G+'''/   .._,|     '''+B+'''   `..
'''+B+'''            /'''+G+'''  |   ,'    __  ,.., | '''+Z+'''
'''+B+'''           / '''+G+'''  | _'   ,''  | \   ''  '''+Z+'''
'''+G+'''          /`.  \,' _ ,/   ,>  |       '''+Z+'''
'''+G+'''         / ,'     / '    \.   \_       '''+Z+'''
'''+G+'''        ;  /     /        |    |     ,__:
'''+G+'''        :  \.   |    _,'       |     / '''+B+''' ;
'''+G+'''         \  |   \ '  `>         `.._/  '''+B+'''/
'''+B+Z+G+I+'''               |     ".,.        '''+B+'''  /
'''+B+'''           \ '''+G+'''     |        :\    .....
'''+B+'''            '''+R+G+'''      `'.__.  /"   |   /
'''+B+'''             `-.'''+G+''' ,._     '''+R+I+'''    ',-'
'''+G+'''                `-. `--.  '''+B+'''    ,-'
'''+G+'''                   `---'''+I+B+'''-----'
        ''')

#========================================================================
#   Misc. Art:  Dev Bricks
#========================================================================
# ___                                                                  _
#/__/|__                                                            __//|
#|__|/_/|__                   D E V T E S T                       _/_|_||
#|_|___|/_/|__                                                 __/_|___||
#|___|____|/_/|__                                           __/_|____|_||
#|_|___|_____|/_/|_________________________________________/_|_____|___||
#|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||
#|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||
#|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||
#|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/
#========================================================================
def art_devBricks():
    print('''
            ___                                                                  _
           /__/|__                                                            __//|
           |__|/_/|__                   D E V T E S T                       _/_|_||
           |_|___|/_/|__                                                 __/_|___||
           |___|____|/_/|__                                           __/_|____|_||
           |_|___|_____|/_/|_________________________________________/_|_____|___||
           |___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||
           |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||
           |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||
           |_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/

                ''')
from  tkinter  import  *

корень  =  Tk ()
f_top  =  Рамка ( корень )
lab  =  Этикетка ( ширина = 15 )
e1  =  Entry ( text = 'Код цвета' , width = 15 )
e1 . insert ( 0 , 'Код цвета' )
lab [ 'text' ] =  'Цвет'

def  insert ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# ff0000" )
    lab [ 'text' ] =  'Красный'
def  insert2 ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# ffa500" )
    lab [ 'text' ] =  'Оранжевый'
def  insert3 ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# ffff00" )
    lab [ 'text' ] =  'Жёлтый'
def  insert4 ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# 00ff00" )
    lab [ 'text' ] =  'Зелёный'
def  insert5 ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# 00ffff" )
    lab [ 'text' ] =  'Голубой'
def  insert6 ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# 0000ff" )
    lab [ 'text' ] =  'Синий'
def  insert7 ():
    e1 . удалить ( 0 , КОНЕЦ )
    e1 . вставить ( 0 , "# 800080" )
    lab [ 'text' ] =  'Фиолетовый'


b  =  Кнопка ( bg  =  '# ff0000' , command  =  insert , width = 3 )
b2  =  Кнопка ( bg  =  '# FFA500' , command  =  insert2 , width  =  3 )
b3  =  Кнопка ( bg  =  '# FFFF00' , command  =  insert3 , width  =  3 )
b4  =  Кнопка ( bg  =  '# 00FF00' , command  =  insert4 , width  =  3 )
b5  =  Кнопка ( bg  =  '# 00FFFF' , command  =  insert5 , width  =  3 )
b6  =  Кнопка ( bg  =  '# 0000FF' , command  =  insert6 , width  =  3 )
b7  =  Кнопка ( bg  =  '# 800080' , command  =  insert7 , width  =  3 )

лаборатория . pack ( padx  =  2 , pady  =  2 )
e1 . pack ( padx  =  2 , pady  =  2 )
f_top . pack ( padx  =  2 , pady  =  2 )
б . пакет ( сторона  =  ЛЕВЫЙ , padx =  1 , pady  =  5 )
b2 . пакет ( сторона  =  ЛЕВЫЙ , padx  =  1 , pady  =  5 )
b3 . пакет ( сторона  =  ЛЕВЫЙ , padx  =  1 , pady  =  5 )
b4 . пакет ( сторона  =  ЛЕВЫЙ , padx  =  1 , pady  =  5 )
b5 . пакет ( сторона  =  ЛЕВЫЙ , padx  =  1 , pady  =  5 )
b6 . пакет ( сторона  =  ЛЕВЫЙ , padx  =  1 , pady  =  5 )
b7 . пакет ( сторона  =  ЛЕВЫЙ , padx  =  1 , pady  =  5 )

корень . mainloop ()
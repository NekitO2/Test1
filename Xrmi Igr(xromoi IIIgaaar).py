import os
import threading
import time
import wave

import pyaudio
import pymorphy2


def zagruzk():
    for x in range(30):
        print('\033[37m {}' .format(f"Загрузка{'.'*(x+1)}"))
        time.sleep(0.3)
        os.system('cls')
    print('\033[37m {}' .format('\rЗагрузка',end='..............................100%\n'))
    print('\033[31m {}' .format('Получившийся текст:\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'))

zagruzka = threading.Thread(target = zagruzk)

def zvuk_zagruzki():
    CHUNK = 1024
    sound_loading = wave.open("zvuk-dial-up-modema-i-oshibki-windows-30516.wav", 'rb')
    p = pyaudio.PyAudio()
    stream_loading = p.open(format=p.get_format_from_width(sound_loading.getsampwidth()),
                    channels = sound_loading.getnchannels(),
                    rate = sound_loading.getframerate(),
                    output = True)
    data = sound_loading.readframes(CHUNK)
    while data != '':
        stream_loading.write(data)
        data = sound_loading.readframes(CHUNK)

zvuk_zagruzka = threading.Thread(target = zvuk_zagruzki)


def zvuk():
    CHUNK = 1024
    sound_keyboard = wave.open("Klaviatura.wav", 'rb')
    p = pyaudio.PyAudio()
    stream_keyboard = p.open(format = p.get_format_from_width(sound_keyboard.getsampwidth()),
                    channels = sound_keyboard.getnchannels(),
                    rate = sound_keyboard.getframerate(),
                    output = True)
    data = sound_keyboard.readframes(CHUNK)
    while data != '':
        stream_keyboard.write(data)
        data = sound_keyboard.readframes(CHUNK)

sound_keyboard_before_processing_sentence_1 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_2 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_3 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_4 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_5 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_6 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_7 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_8 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_9 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_10 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_11 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_12 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_13 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_14 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_15 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_16 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_17 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_18 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_19 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_20 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_21 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_22 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_23 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_24 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_25 = threading.Thread(target = zvuk)
sound_keyboard_before_processing_sentence_26 = threading.Thread(target = zvuk)

sound_keyboard_after_processing_sentence_1 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_2 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_3 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_4 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_5 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_6 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_7 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_8 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_9 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_10 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_11 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_12 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_13 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_14 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_15 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_16 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_17 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_18 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_19 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_20 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_21 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_22 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_23 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_24 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_25 = threading.Thread(target = zvuk)
sound_keyboard_after_processing_sentence_26 = threading.Thread(target = zvuk)

select_or_enter = int(input('1 == выбрать данные, 2 == ввести данные '))

resulting_sentence = 1

if select_or_enter == 1:
    print('1) Блоха, Орёл, Заяц')
    print('2) Игорь, Андрей, Кирилл')
    print('3) Ангелина, Арсений, Данил')
    what_text = int(input('Введите номер '))
    
    if what_text == 1:
       
        morph = pymorphy2.MorphAnalyzer()

        bloxaIm = 'блоха'
            
        gent = morph.parse(bloxaIm)[0].inflect({'gent'})
        bloxaRod = str(gent.word)
            
        accs = morph.parse(bloxaIm)[0].inflect({'accs'})
        bloxaVin = str(accs.word)
            
        loct = morph.parse(bloxaIm)[0].inflect({'loct'})
        bloxaPred = str(loct.word)

        if morph.parse(bloxaIm)[0].tag.gender == 'masc':
            bloxaPad = 1

        elif morph.parse(bloxaIm)[0].tag.gender == 'femn':
            bloxaPad = 2

        elif morph.parse(bloxaIm)[0].tag.gender == 'neut':
            bloxaPad = 3
        
        orelIm = 'орёл'
    
        gent = morph.parse(orelIm)[0].inflect({'gent'})
        orelRod = str(gent.word)
            
        datv = morph.parse(orelIm)[0].inflect({'datv'})
        orelDat = str(datv.word)

        if morph.parse(orelIm)[0].tag.gender == 'masc':
            orelPad = 1

        elif morph.parse(orelIm)[0].tag.gender == 'femn':
            orelPad = 2

        elif morph.parse(orelIm)[0].tag.gender == 'neut':
            orelPad = 3
        
        hareIm = 'заяц'

        gent = morph.parse(hareIm)[0].inflect({'gent'})
        hareRod = str(gent.word)
            
        datv = morph.parse(hareIm)[0].inflect({'datv'})
        hareDat = str(datv.word)

        accs = morph.parse(hareIm)[0].inflect({'accs'})
        hareVin = str(accs.word)

        if morph.parse(hareIm)[0].tag.gender == 'masc':
            harePad = 1

        elif morph.parse(hareIm)[0].tag.gender == 'femn':
            harePad = 2

        elif morph.parse(hareIm)[0].tag.gender == 'neut':
            harePad = 3

    elif what_text == 2:
        
        morph = pymorphy2.MorphAnalyzer()

        bloxaIm = 'игорь'
            
        gent = morph.parse(bloxaIm)[0].inflect({'gent'})
        bloxaRod = str(gent.word)
            
        accs = morph.parse(bloxaIm)[0].inflect({'accs'})
        bloxaVin = str(accs.word)
            
        loct = morph.parse(bloxaIm)[0].inflect({'loct'})
        bloxaPred = str(loct.word)

        if morph.parse(bloxaIm)[0].tag.gender == 'masc':
            bloxaPad = 1

        elif morph.parse(bloxaIm)[0].tag.gender == 'femn':
            bloxaPad = 2

        elif morph.parse(bloxaIm)[0].tag.gender == 'neut':
            bloxaPad = 3
        
        orelIm = 'андрей'
    
        gent = morph.parse(orelIm)[0].inflect({'gent'})
        orelRod = str(gent.word)
            
        datv = morph.parse(orelIm)[0].inflect({'datv'})
        orelDat = str(datv.word)

        if morph.parse(orelIm)[0].tag.gender == 'masc':
            orelPad = 1

        elif morph.parse(orelIm)[0].tag.gender == 'femn':
            orelPad = 2

        elif morph.parse(orelIm)[0].tag.gender == 'neut':
            orelPad = 3
        
        hareIm = 'кирилл'

        gent = morph.parse(hareIm)[0].inflect({'gent'})
        hareRod = str(gent.word)
            
        datv = morph.parse(hareIm)[0].inflect({'datv'})
        hareDat = str(datv.word)

        accs = morph.parse(hareIm)[0].inflect({'accs'})
        hareVin = str(accs.word)

        if morph.parse(hareIm)[0].tag.gender == 'masc':
            harePad = 1

        elif morph.parse(hareIm)[0].tag.gender == 'femn':
            harePad = 2

        elif morph.parse(hareIm)[0].tag.gender == 'neut':
            harePad = 3

    elif what_text == 3:
        
        morph = pymorphy2.MorphAnalyzer()

        bloxaIm = 'ангелина'
            
        gent = morph.parse(bloxaIm)[0].inflect({'gent'})
        bloxaRod = str(gent.word)
            
        accs = morph.parse(bloxaIm)[0].inflect({'accs'})
        bloxaVin = str(accs.word)
            
        loct = morph.parse(bloxaIm)[0].inflect({'loct'})
        bloxaPred = str(loct.word)

        if morph.parse(bloxaIm)[0].tag.gender == 'masc':
            bloxaPad = 1

        elif morph.parse(bloxaIm)[0].tag.gender == 'femn':
            bloxaPad = 2

        elif morph.parse(bloxaIm)[0].tag.gender == 'neut':
            bloxaPad = 3
        
        orelIm = 'арсений'
    
        gent = morph.parse(orelIm)[0].inflect({'gent'})
        orelRod = str(gent.word)
            
        datv = morph.parse(orelIm)[0].inflect({'datv'})
        orelDat = str(datv.word)

        if morph.parse(orelIm)[0].tag.gender == 'masc':
            orelPad = 1

        elif morph.parse(orelIm)[0].tag.gender == 'femn':
            orelPad = 2

        elif morph.parse(orelIm)[0].tag.gender == 'neut':
            orelPad = 3
        
        hareIm = 'данил'

        gent = morph.parse(hareIm)[0].inflect({'gent'})
        hareRod = str(gent.word)
            
        datv = morph.parse(hareIm)[0].inflect({'datv'})
        hareDat = str(datv.word)

        accs = morph.parse(hareIm)[0].inflect({'accs'})
        hareVin = str(accs.word)

        if morph.parse(hareIm)[0].tag.gender == 'masc':
            harePad = 1

        elif morph.parse(hareIm)[0].tag.gender == 'femn':
            harePad = 2

        elif morph.parse(hareIm)[0].tag.gender == 'neut':
            harePad = 3

elif select_or_enter == 2:
    
    morph = pymorphy2.MorphAnalyzer()

    bloxaIm = str(input('Введите какой - нибудь предмет в именительном падеже '))

    if morph.parse(bloxaIm)[0].tag.gender == 'masc':
        bloxaPad = 1

    elif morph.parse(bloxaIm)[0].tag.gender == 'femn':
        bloxaPad = 2

    elif morph.parse(bloxaIm)[0].tag.gender == 'neut':
        bloxaPad = 3

    morph = pymorphy2.MorphAnalyzer()
    
    if morph.parse(bloxaIm)[0].tag.animacy == 'inan':
            
        gent = morph.parse(bloxaIm)[0].inflect({'gent'})
        bloxaRod = gent.word()
            
        accs = morph.parse(bloxaIm)[0].inflect({'accs'})
        bloxaVin = accs.word()
            
        loct = morph.parse(bloxaIm)[0].inflect({'loct'})
        bloxaPred = loct.word()
            
    elif morph.parse(bloxaIm)[0].tag.animacy == 'anim':
        
        bloxaIm = bloxaIm.title()

        gent = morph.parse(bloxaIm)[0].inflect({'gent'})
        bloxaRod = gent.word.title()
            
        accs = morph.parse(bloxaIm)[0].inflect({'accs'})
        bloxaVin = accs.word.title()
            
        loct = morph.parse(bloxaIm)[0].inflect({'loct'})
        bloxaPred = loct.word.title()

    orelIm = str(input('Введите другой предмет в именительном падеже '))

    if morph.parse(orelIm)[0].tag.gender == 'masc':
        orelPad = 1

    elif morph.parse(orelIm)[0].tag.gender == 'femn':
        orelPad = 2

    elif morph.parse(orelIm)[0].tag.gender == 'neut':
        orelPad = 3
    
    if morph.parse(orelIm)[0].tag.animacy == 'inan':

        gent = morph.parse(orelIm)[0].inflect({'gent'})
        orelRod = gent.word()
            
        datv = morph.parse(orelIm)[0].inflect({'datv'})
        orelDat = datv.word()

    elif morph.parse(orelIm)[0].tag.animacy == 'anim':
            
        orelIm = orelIm.title()    
    
        gent = morph.parse(orelIm)[0].inflect({'gent'})
        orelRod = gent.word.title()
            
        datv = morph.parse(orelIm)[0].inflect({'datv'})
        orelDat = datv.word.title()
    
    hareIm = str(input('Введите третий предмет в именительном падеже '))

    if morph.parse(hareIm)[0].tag.gender == 'masc':
        harePad = 1

    elif morph.parse(hareIm)[0].tag.gender == 'femn':
        harePad = 2

    elif morph.parse(hareIm)[0].tag.gender == 'neut':
        harePad = 3

    rabotai = morph.parse(hareIm)[0]
    
    if morph.parse(hareIm)[0].tag.animacy == 'inan':

        gent = morph.parse(hareIm)[0].inflect({'gent'})
        hareRod = gent.word()
            
        datv = morph.parse(hareIm)[0].inflect({'datv'})
        hareDat = datv.word()

        accs = morph.parse(hareIm)[0].inflect({'accs'})
        hareVin = accs.word()
        
    elif morph.parse(hareIm)[0].tag.animacy == 'anim':

        hareIm = hareIm.title()

        gent = morph.parse(hareIm)[0].inflect({'gent'})
        hareRod = gent.word.title()
            
        datv = morph.parse(hareIm)[0].inflect({'datv'})
        hareDat = datv.word.title()

        accs = morph.parse(hareIm)[0].inflect({'accs'})
        hareVin = accs.word.title()    

sentence_1 = '- Кто там?' 

sentence_2 = '- Это я, добрый Ээх. Я здесь. '

sentence_3 = '- И я здесь! '

sentence_4 = '- А ты кто такой? Откуда взялся? '

sentence_5 = '- С того берега моря. '

sentence_6 = '- На чем приехал? '

if bloxaPad == 1:
    sentence_7 = f'- Оседлал хромого {bloxaVin}, сел и приехал. '

elif bloxaPad == 2:
    sentence_7 = f'- Оседлал хромую {bloxaVin}, сел и приехал. '

elif bloxaPad == 3:
    sentence_7 = f'- Оседлал хромое {bloxaVin}, сел и приехал. '

sentence_8 = '- Море, что, лужа? '

if orelPad == 1:
    sentence_9 = f'- Может и лужа, да только ту лужу {orelIm} не перелетел. '

elif orelPad == 2:
    sentence_9 = f'- Может и лужа, да только ту лужу {orelIm} не перелетелa. '

elif orelPad == 3:
    sentence_9 = f'- Может и лужа, да только ту лужу {orelIm} не перелетело. '

sentence_10 = f'- Значит, {orelIm} - птенец! '

if orelPad == 1:
    sentence_11 = '- Наверно, птенец. Да только тень от его крыльев город закрывает, в городе ночь настает. '

elif orelPad == 2:
    sentence_11 = '- Наверно, птенец. Да только тень от её крыльев город закрывает, в городе ночь настает. '

elif orelPad == 3:
    sentence_11 = '- Наверно, птенец. Да только тень от его крыльев город закрывает, в городе ночь настает. '

sentence_12 = '- Город-то, небось, крооохотный! '

if harePad == 1:
    sentence_13 = f'- Через тот город {hareIm} бежал - не перебежал. '

elif harePad == 2:
    sentence_13 = f'- Через тот город {hareIm} бежалa - не перебежалa. '

elif harePad == 3:
    sentence_13 = f'- Через тот город {hareIm} бежалo - не перебежалo. '

if harePad == 1:
    sentence_14 = f'- Выходит, {hareIm} маааленький! '

elif harePad == 2:
    sentence_14 = f'- Выходит, {hareIm} маааленькая! '

elif harePad == 3:
    sentence_14 = f'- Выходит, {hareIm} маааленькoe! '

if harePad == 1:
    sentence_15 = f'- {hareIm.title()} – как {hareIm}. Из его шкуры тулуп вышел. '

elif harePad == 2:
    sentence_15 = f'- {hareIm.title()} – как {hareIm}. Из её шкуры тулуп вышел. '

elif harePad == 3:
    sentence_15 = f'- {hareIm.title()} – как {hareIm}. Из его шкуры тулуп вышел. '
    
sentence_16 = '- Куда вышел? '

sentence_17 = f'- Вышел из того города, где {hareIm} бежал, на который тень от {orelRod} упала, и пошел, куда глаза глядят. '

sentence_18 = '- Чьи глаза??? '

if bloxaPad == 1:
    sentence_19 = f'- Глаза того тулупа, который из шкуры {hareRod} вышел, в городе, где ночь настает, когда над ним птенец пролетает верхом на хромом {bloxaPred}. '

elif bloxaPad == 2:
    sentence_19 = f'- Глаза того тулупа, который из шкуры {hareRod} вышел, в городе, где ночь настает, когда над ним птенец пролетает верхом на хромой {bloxaPred}. '

elif bloxaPad == 3:
    sentence_19 = f'- Глаза того тулупа, который из шкуры {hareRod} вышел, в городе, где ночь настает, когда над ним птенец пролетает верхом на хромом {bloxaPred}. '

sentence_20 = '- ЧЕГО?!!!! '

if bloxaPad == 1:
    sentence_21 = f'- Чего-чего. На хромом {bloxaPred} с того берега моря, которое {hareDat} не перелететь, {orelDat} не перебежать, хоть море - не море, а так - лужа посреди города, где тень от {bloxaRod} на {hareVin} упала и насмерть убила, а из шкуры {hareRod} тулуп вышел и пошел, куда глаза глядят. Тут {hareIm} кааак прыгнет! '

elif bloxaPad == 2:
    sentence_21 = f'- Чего-чего. На хромой {bloxaPred} с того берега моря, которое {hareDat} не перелететь, {orelDat} не перебежать, хоть море - не море, а так - лужа посреди города, где тень от {bloxaRod} на {hareVin} упала и насмерть убила, а из шкуры {hareRod} тулуп вышел и пошел, куда глаза глядят. Тут {hareIm} кааак прыгнет! '

elif bloxaPad == 3:
    sentence_21 = f'- Чего-чего. На хромом {bloxaPred} с того берега моря, которое {hareDat} не перелететь, {orelDat} не перебежать, хоть море - не море, а так - лужа посреди города, где тень от {bloxaRod} на {hareVin} упала и насмерть убила, а из шкуры {hareRod} тулуп вышел и пошел, куда глаза глядят. Тут {hareIm} кааак прыгнет! '

if harePad == 1:
    sentence_22 = f'- КАКОЙ {hareIm.upper()}??? '

elif harePad == 2:
    sentence_22 = f'- КАКАЯ {hareIm.upper()}??? '

elif harePad == 3:
    sentence_22 = f'- КАКOE {hareIm.upper()}??? '

if harePad == 1:
    sentence_23 = f'- Насмерть убитый – как прыгнет, куда глаза глядят, аж на тот берег моря, которое ни перелететь, ни перебежать, из которого тулуп вышел, на который тень от {bloxaRod} упала и {hareVin} убила, хоть {hareIm} – не {hareIm}, а {orelIm}! '

elif harePad == 2:
    sentence_23 = f'- Насмерть убитая – как прыгнет, куда глаза глядят, аж на тот берег моря, которое ни перелететь, ни перебежать, из которой тулуп вышел, на который тень от {bloxaRod} упала и {hareVin} убила, хоть {hareIm} – не {hareIm}, а {orelIm}! '

elif harePad == 3:
    sentence_23 = f'- Насмерть убитое – как прыгнет, куда глаза глядят, аж на тот берег моря, которое ни перелететь, ни перебежать, из которого тулуп вышел, на который тень от {bloxaRod} упала и {hareVin} убила, хоть {hareIm} – не {hareIm}, а {orelIm}! '

if harePad == 1 and orelPad == 1 and bloxaPad == 1:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 1 and bloxaPad == 2:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 1 and bloxaPad == 3:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 2 and bloxaPad == 1:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 2 and bloxaPad == 2:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 2 and bloxaPad == 3:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 3 and bloxaPad == 1:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 3 and bloxaPad == 2:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 1 and orelPad == 3 and bloxaPad == 3:
    sentence_24 = f'- КАКОЙ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 1 and bloxaPad == 1:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 1 and bloxaPad == 2:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 1 and bloxaPad == 3:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 2 and bloxaPad == 1:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 2 and bloxaPad == 2:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 2 and bloxaPad == 3:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 3 and bloxaPad == 1:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 3 and bloxaPad == 2:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 2 and orelPad == 3 and bloxaPad == 3:
    sentence_24 = f'- КАКАЯ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 1 and bloxaPad == 1:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 1 and bloxaPad == 2:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 1 and bloxaPad == 3:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКОЙ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 2 and bloxaPad == 1:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 2 and bloxaPad == 2:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 2 and bloxaPad == 3:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКАЯ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 3 and bloxaPad == 1:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКОЙ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 3 and bloxaPad == 2:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКАЯ {bloxaIm.upper()}??? '

elif harePad == 3 and orelPad == 3 and bloxaPad == 3:
    sentence_24 = f'- КАКОЕ {hareIm.upper()}??? КАКОЕ {orelIm.upper()}??? КАКОЕ {bloxaIm.upper()}??? '

if bloxaPad == 1:
    sentence_25 = f'- Повторить? Ну, значит, тот самый {bloxaIm} с того берега лужи…'

elif bloxaPad == 2:
    sentence_25 = f'- Повторить? Ну, значит, та самая {bloxaIm} с того берега лужи…'

elif bloxaPad == 3:
    sentence_25 = f'- Повторить? Ну, значит, то самое {bloxaIm} с того берега лужи…'

sentence_26 = '- АААААААААААААААААААА!!!!!!!!!! ДА ХВАААТИТ!!!!!!!!!'

d = 1

def nacalo():
    print('Исходный текст:')

nachalo = threading.Thread(target = nacalo)

def source_text_sentence_1():
    print(sentence_1)
    time.sleep(1)

source_text_before_processing_sentence_1 = threading.Thread(target = source_text_sentence_1)
source_text_after_processing_sentence_1 = threading.Thread(target = source_text_sentence_1)

def source_text_sentence_2():
    print(sentence_2)
    time.sleep(1)

source_text_before_processing_sentence_2 = threading.Thread(target = source_text_sentence_2)
source_text_after_processing_sentence_2 = threading.Thread(target = source_text_sentence_2)

def source_text_sentence_3():
    print(sentence_3)
    time.sleep(1)

source_text_before_processing_sentence_3 = threading.Thread(target = source_text_sentence_3)
source_text_after_processing_sentence_3 = threading.Thread(target = source_text_sentence_3)

def source_text_sentence_4():
    print(sentence_4)
    time.sleep(1)

source_text_before_processing_sentence_4 = threading.Thread(target = source_text_sentence_4)
source_text_after_processing_sentence_4 = threading.Thread(target = source_text_sentence_4)


def source_text_sentence_5():
    print(sentence_5)
    time.sleep(1)

source_text_before_processing_sentence_5 = threading.Thread(target = source_text_sentence_5)
source_text_after_processing_sentence_5 = threading.Thread(target = source_text_sentence_5)

def source_text_sentence_6():
    print(sentence_6)
    time.sleep(1)

source_text_before_processing_sentence_6 = threading.Thread(target = source_text_sentence_6)
source_text_after_processing_sentence_6 = threading.Thread(target = source_text_sentence_6)

def source_text_sentence_7():
    print(sentence_7)
    time.sleep(1)

source_text_before_processing_sentence_7 = threading.Thread(target = source_text_sentence_7)
source_text_after_processing_sentence_7 = threading.Thread(target = source_text_sentence_7)

def source_text_sentence_8():
    print(sentence_8)
    time.sleep(1)

source_text_before_processing_sentence_8 = threading.Thread(target = source_text_sentence_8)
source_text_after_processing_sentence_8 = threading.Thread(target = source_text_sentence_8)

def source_text_sentence_9():
    print(sentence_9)
    time.sleep(1)

source_text_before_processing_sentence_9 = threading.Thread(target = source_text_sentence_9)
source_text_after_processing_sentence_9 = threading.Thread(target = source_text_sentence_9)

def source_text_sentence_10():
    print(sentence_10)
    time.sleep(1)

source_text_before_processing_sentence_10 = threading.Thread(target = source_text_sentence_10)
source_text_after_processing_sentence_10 = threading.Thread(target = source_text_sentence_10)

def source_text_sentence_11():
    print(sentence_11)
    time.sleep(1)

source_text_before_processing_sentence_11 = threading.Thread(target = source_text_sentence_11)
source_text_after_processing_sentence_11 = threading.Thread(target = source_text_sentence_11)

def source_text_sentence_12():
    print(sentence_12)
    time.sleep(1)

source_text_before_processing_sentence_12 = threading.Thread(target = source_text_sentence_12)
source_text_after_processing_sentence_12 = threading.Thread(target = source_text_sentence_12)

def source_text_sentence_13():
    print(sentence_13)
    time.sleep(1)

source_text_before_processing_sentence_13 = threading.Thread(target = source_text_sentence_13)
source_text_after_processing_sentence_13 = threading.Thread(target = source_text_sentence_13)

def source_text_sentence_14():
    print(sentence_14)
    time.sleep(1)

source_text_before_processing_sentence_14 = threading.Thread(target = source_text_sentence_14)
source_text_after_processing_sentence_14 = threading.Thread(target = source_text_sentence_14)

def source_text_sentence_15():
    print(sentence_15)
    time.sleep(1)

source_text_before_processing_sentence_15 = threading.Thread(target = source_text_sentence_15)
source_text_after_processing_sentence_15 = threading.Thread(target = source_text_sentence_15)

def source_text_sentence_16():
    print(sentence_16)
    time.sleep(1)

source_text_before_processing_sentence_16 = threading.Thread(target = source_text_sentence_16)
source_text_after_processing_sentence_16 = threading.Thread(target = source_text_sentence_16)

def source_text_sentence_17():
    print(sentence_17)
    time.sleep(1)

source_text_before_processing_sentence_17 = threading.Thread(target = source_text_sentence_17)
source_text_after_processing_sentence_17 = threading.Thread(target = source_text_sentence_17)

def source_text_sentence_18():
    print(sentence_18)
    time.sleep(1)

source_text_before_processing_sentence_18 = threading.Thread(target = source_text_sentence_18)
source_text_after_processing_sentence_18 = threading.Thread(target = source_text_sentence_18)


def source_text_sentence_19():    
    print(sentence_19)
    time.sleep(1)

source_text_before_processing_sentence_19 = threading.Thread(target = source_text_sentence_19)
source_text_after_processing_sentence_19 = threading.Thread(target = source_text_sentence_19)

def source_text_sentence_20():
    print(sentence_20)
    time.sleep(1)

source_text_before_processing_sentence_20 = threading.Thread(target = source_text_sentence_20)
source_text_after_processing_sentence_20 = threading.Thread(target = source_text_sentence_20)

def source_text_sentence_21():
    print(sentence_21)
    time.sleep(1)

source_text_before_processing_sentence_21 = threading.Thread(target = source_text_sentence_21)
source_text_after_processing_sentence_21 = threading.Thread(target = source_text_sentence_21)
 
def source_text_sentence_22():
    print(sentence_22)
    time.sleep(1)

source_text_before_processing_sentence_22 = threading.Thread(target = source_text_sentence_22)
source_text_after_processing_sentence_22 = threading.Thread(target = source_text_sentence_22)

def source_text_sentence_23():
    print(sentence_23)
    time.sleep(1)

source_text_before_processing_sentence_23 = threading.Thread(target = source_text_sentence_23)
source_text_after_processing_sentence_23 = threading.Thread(target = source_text_sentence_23)

def source_text_sentence_24():
    print(sentence_24)
    time.sleep(1)

source_text_before_processing_sentence_24 = threading.Thread(target = source_text_sentence_24)
source_text_after_processing_sentence_24 = threading.Thread(target = source_text_sentence_24)

def source_text_sentence_25():
    print(sentence_25)
    time.sleep(1)

source_text_before_processing_sentence_25 = threading.Thread(target = source_text_sentence_25)
source_text_after_processing_sentence_25 = threading.Thread(target = source_text_sentence_25)

def source_text_sentence_26():
    print(sentence_26)
    time.sleep(1)

source_text_before_processing_sentence_26 = threading.Thread(target = source_text_sentence_26)
source_text_after_processing_sentence_26 = threading.Thread(target = source_text_sentence_26)

os.system('cls')

nachalo.start()

sound_keyboard_before_processing_sentence_1.start()
source_text_before_processing_sentence_1.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_2.start()
source_text_before_processing_sentence_2.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_3.start()
source_text_before_processing_sentence_3.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_4.start()
source_text_before_processing_sentence_4.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_5.start()
source_text_before_processing_sentence_5.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_6.start()
source_text_before_processing_sentence_6.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_7.start()
source_text_before_processing_sentence_7.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_8.start()
source_text_before_processing_sentence_8.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_9.start()
source_text_before_processing_sentence_9.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_10.start()
source_text_before_processing_sentence_10.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_11.start()
source_text_before_processing_sentence_11.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_12.start()
source_text_before_processing_sentence_12.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_13.start()
source_text_before_processing_sentence_13.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_14.start()
source_text_before_processing_sentence_14.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_15.start()
source_text_before_processing_sentence_15.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_16.start()
source_text_before_processing_sentence_16.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_17.start()
source_text_before_processing_sentence_17.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_18.start()
source_text_before_processing_sentence_18.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_19.start()
source_text_before_processing_sentence_19.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_20.start()
source_text_before_processing_sentence_20.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_21.start()
source_text_before_processing_sentence_21.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_22.start()
source_text_before_processing_sentence_22.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_23.start()
source_text_before_processing_sentence_23.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_24.start()
source_text_before_processing_sentence_24.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_25.start()
source_text_before_processing_sentence_25.start()
time.sleep(1)

sound_keyboard_before_processing_sentence_26.start()
source_text_before_processing_sentence_26.start()
time.sleep(1)

translate_or_not_translate = int(input('Переводить на китайский (1 == переводить, 2 == не переводить ) '))

if translate_or_not_translate == 1:
    print('')
    print('\033[31m {}' .format('Получившийся текст:\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'))
    def rabota(sentence_1, resulting_sentence):
        resulting_sentence = sentence_1.replace('А', '')
        resulting_sentence = resulting_sentence.replace('Е', '')
        resulting_sentence = resulting_sentence.replace('О', '')
        resulting_sentence = resulting_sentence.replace('а', '')
        resulting_sentence = resulting_sentence.replace('е', '')
        resulting_sentence = resulting_sentence.replace('о', '')
        resulting_sentence = resulting_sentence.replace('A', '')
        resulting_sentence = resulting_sentence.replace('E', '')
        resulting_sentence = resulting_sentence.replace('O', '')
        resulting_sentence = resulting_sentence.replace('а', '')
        resulting_sentence = resulting_sentence.replace('e', '')
        resulting_sentence = resulting_sentence.replace('o', '')
        def c(resulting_sentence):
            time.sleep(0.2)
            print('\033[37m {}' .format(resulting_sentence))
        c(resulting_sentence)
    
    def processing_text_sentence_1():
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_1 = threading.Thread(target = processing_text_sentence_1)
        
    def processing_text_sentence_2():
        sentence_1 = sentence_2
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_2 = threading.Thread(target = processing_text_sentence_2)

    def processing_text_sentence_3():    
        sentence_1 = sentence_3
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_3 = threading.Thread(target = processing_text_sentence_3)

    def processing_text_sentence_4():    
        sentence_4 = '- Ты кто такой? Откуда взялся? '
        sentence_1 = sentence_4
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_4 = threading.Thread(target = processing_text_sentence_4)

    def processing_text_sentence_5():    
        sentence_1 = sentence_5
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_5 = threading.Thread(target = processing_text_sentence_5)

    def processing_text_sentence_6():    
        sentence_1 = sentence_6
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_6 = threading.Thread(target = processing_text_sentence_6)

    def processing_text_sentence_7():    
        sentence_1 = sentence_7
        rabota(sentence_1, resulting_sentence)
        
    resulting_text_after_processing_sentence_7 = threading.Thread(target = processing_text_sentence_7)

    def processing_text_sentence_8():    
        sentence_1 = sentence_8
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_8 = threading.Thread(target = processing_text_sentence_8)

    def processing_text_sentence_9():    
        sentence_1 = sentence_9
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_9 = threading.Thread(target = processing_text_sentence_9)

    def processing_text_sentence_10():    
        sentence_1 = sentence_10
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_10 = threading.Thread(target = processing_text_sentence_10)

    def processing_text_sentence_11():    
        sentence_1 = sentence_11
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_11 = threading.Thread(target = processing_text_sentence_11)

    def processing_text_sentence_12():    
        sentence_1 = sentence_12
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_12 = threading.Thread(target = processing_text_sentence_12)

    def processing_text_sentence_13():    
        sentence_1 = sentence_13
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_13 = threading.Thread(target = processing_text_sentence_13)

    def processing_text_sentence_14():    
        sentence_1 = sentence_14
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_14 = threading.Thread(target =processing_text_sentence_14)

    def processing_text_sentence_15():    
        sentence_1 = sentence_15
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_15 = threading.Thread(target = processing_text_sentence_15)

    def processing_text_sentence_16():    
        sentence_1 = sentence_16
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_16 = threading.Thread(target = processing_text_sentence_16)

    def processing_text_sentence_17():    
        sentence_1 = sentence_17
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_17 = threading.Thread(target = processing_text_sentence_17)

    def processing_text_sentence_18():    
        sentence_1 = sentence_18
        rabota(sentence_1, resulting_sentence)
    
    resulting_text_after_processing_sentence_18 = threading.Thread(target = processing_text_sentence_18)

    def processing_text_sentence_19():
        sentence_1 = sentence_19
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_19 = threading.Thread(target = processing_text_sentence_19)

    def processing_text_sentence_20():    
        sentence_1 = sentence_20
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_20 = threading.Thread(target = processing_text_sentence_20)

    def processing_text_sentence_21():    
        sentence_1 = sentence_21
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_21 = threading.Thread(target = processing_text_sentence_21)

    def processing_text_sentence_22():    
        sentence_1 = sentence_22
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_22 = threading.Thread(target = processing_text_sentence_22)

    def processing_text_sentence_23():    
        sentence_1 = sentence_23
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_23 = threading.Thread(target = processing_text_sentence_23)

    def processing_text_sentence_24():    
        sentence_1 = sentence_24
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_24 = threading.Thread(target = processing_text_sentence_24)

    def processing_text_sentence_25():    
        sentence_1 = sentence_25
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_25 = threading.Thread(target = processing_text_sentence_25)

    def processing_text_sentence_26():    
        sentence_1 = sentence_26
        rabota(sentence_1, resulting_sentence)

    resulting_text_after_processing_sentence_26 = threading.Thread(target = processing_text_sentence_26)

    zvuk_zagruzka.start()
    zagruzka.start()
    time.sleep(11)
    
    os.system('cls')

    print('\033[37m {}' .format('Исходный текст:'))

    source_text_after_processing_sentence_1.start()
    source_text_after_processing_sentence_2.start()
    source_text_after_processing_sentence_3.start()
    source_text_after_processing_sentence_4.start()
    source_text_after_processing_sentence_5.start()
    source_text_after_processing_sentence_6.start()
    source_text_after_processing_sentence_7.start()
    source_text_after_processing_sentence_8.start()
    source_text_after_processing_sentence_9.start()
    source_text_after_processing_sentence_10.start()
    source_text_after_processing_sentence_11.start()
    source_text_after_processing_sentence_12.start()
    source_text_after_processing_sentence_13.start()
    source_text_after_processing_sentence_14.start()
    source_text_after_processing_sentence_15.start()
    source_text_after_processing_sentence_16.start()
    source_text_after_processing_sentence_17.start()
    source_text_after_processing_sentence_18.start()
    source_text_after_processing_sentence_19.start()
    source_text_after_processing_sentence_20.start()
    source_text_after_processing_sentence_21.start()
    source_text_after_processing_sentence_22.start()
    source_text_after_processing_sentence_23.start()
    source_text_after_processing_sentence_24.start()
    source_text_after_processing_sentence_25.start()
    source_text_after_processing_sentence_26.start()

    print('')  
    print('\033[31m {}' .format('Получившийся текст:\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'))

    sound_keyboard_after_processing_sentence_1.start()
    resulting_text_after_processing_sentence_1.start()
    time.sleep(1)
    
    sound_keyboard_after_processing_sentence_2.start()
    resulting_text_after_processing_sentence_2.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_3.start()
    resulting_text_after_processing_sentence_3.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_4.start()
    resulting_text_after_processing_sentence_4.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_5.start()
    resulting_text_after_processing_sentence_5.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_6.start()
    resulting_text_after_processing_sentence_6.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_7.start()
    resulting_text_after_processing_sentence_7.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_8.start()
    resulting_text_after_processing_sentence_8.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_9.start()
    resulting_text_after_processing_sentence_9.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_10.start()
    resulting_text_after_processing_sentence_10.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_11.start()
    resulting_text_after_processing_sentence_11.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_12.start()
    resulting_text_after_processing_sentence_12.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_13.start()
    resulting_text_after_processing_sentence_13.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_14.start()
    resulting_text_after_processing_sentence_14.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_15.start()
    resulting_text_after_processing_sentence_15.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_16.start()
    resulting_text_after_processing_sentence_16.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_17.start()
    resulting_text_after_processing_sentence_17.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_18.start()
    resulting_text_after_processing_sentence_18.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_19.start()
    resulting_text_after_processing_sentence_19.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_20.start()
    resulting_text_after_processing_sentence_20.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_21.start()
    resulting_text_after_processing_sentence_21.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_22.start()
    resulting_text_after_processing_sentence_22.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_23.start()
    resulting_text_after_processing_sentence_23.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_24.start()
    resulting_text_after_processing_sentence_24.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_25.start()
    resulting_text_after_processing_sentence_25.start()
    time.sleep(1)

    sound_keyboard_after_processing_sentence_26.start()
    resulting_text_after_processing_sentence_26.start()
    time.sleep(1)

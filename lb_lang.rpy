# localization utilities
# adds limited support for {en} and {ru} tags

#обратная совместимость, ибо заебешься вычищать meet из всех модов.
init -100 python:
    
    def miss(flnm):
        renpy.log(flnm.replace("images/1080","images"))
        return im.Image(flnm.replace("images/1080","images"))
    
    
    config.missing_image_callback = miss
        
    
    config_session = False

    def meet(who, name):
        gl = globals()
        names[who] = who
        gl[who+"_name"] = name
        
    def set_name(who, name):
        gl = globals()
        names[who] = who
        gl[who+"_name"] = name
        
    def make_names_unknown():
        
        set_name('mt_voice',u"Голос")
        set_name('FIXME_voice',u"Голос")
        set_name('odn',u"Одногруппник")
        set_name('message',u"Сообщение")
        set_name('dreamgirl',u"...")
        set_name('voice',u"Голос")
        set_name('me',u"Семен")
        set_name('dy',u"Голос из динамика")
        set_name('lk',u"Луркмор-кун")
        set_name('pi',u"Пионер")
        set_name('all',u"Пионеры")
        set_name('kids',u"Малышня")
        set_name('dreamgirl',u"...")
        set_name('bush',u"Голос")
        set_name('voices',u"Голоса")
            
        set_name('el',u"Пионер")
        set_name('un',u"Пионерка")
        set_name('dv',u"Пионерка")
        set_name('sl',u"Пионерка")
        set_name('us',u"Пионерка")
        set_name('mt',u"Вожатая")
        set_name('cs',u"Медсестра")
        set_name('mz',u"Пионерка")
        set_name('mi',u"Пионерка")
        set_name('uv',u"Странная девочка")
        set_name('sh',u"Пионер")
        
    def make_names_known():

        set_name('el',u"Электроник")
        set_name('un',u"Лена")
        set_name('dv',u"Алиса")
        set_name('sl',u"Славя")
        set_name('us',u"Ульяна")
        set_name('mt',u"Ольга Дмитриевна")
        set_name('cs',u"Виола")
        set_name('mz',u"Женя")
        set_name('mi',u"Мику")
        set_name('uv',u"Юля")
        set_name('sh',u"Шурик")
            
init 100 python:
    
    colors['dy'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
    store.names_list.append('dy')
    
    if not "dy" in names.keys():
        names["dy"] = "dy"
    
    for i in store.names_list:
        if not i in names.keys():
            names[i] = i
        
    

init python:
    import re
    if  persistent.text_tag_lang == None:
        persistent.text_tag_lang = "en"
        
    for item in (item for item in renpy.game.script.namemap.values() if isinstance(item, renpy.ast.Say)):
        if  persistent.text_tag_lang != 'ru':
            item.what = re.sub(ur'{en}(.*?){/en}', u'{i}\\1{/i}', item.what, flags=re.UNICODE)
            item.what = re.sub(ur'{ru}.*?{/ru}',   u'',           item.what, flags=re.UNICODE)
        else:
            item.what = re.sub(ur'{en}.*?{/en}',   u'',           item.what, flags=re.UNICODE)
            item.what = re.sub(ur'{ru}(.*?){/ru}', u'{i}\\1{/i}', item.what, flags=re.UNICODE)

label check_text_tag_lang:
    $ tmp_text_tag_lang = "русский" if persistent.text_tag_lang == "ru" else "английский"
    menu:
        "Сейчас при наличии перевода используется %(tmp_text_tag_lang)s язык."
        "OK, оставить!":
            pass
        "НЕТ, поменять и перезапустить игру!":
            $ persistent.text_tag_lang = "ru" if persistent.text_tag_lang != "ru" else "en"
            # no renpy.reload_script() in 6.16 T_T
            $ renpy.utter_restart()
    return           
        
label text_tag_lang_test:
    call check_text_tag_lang
    "{en}Nya!{/en}{ru}Ня!{/ru}"
    "{en}Kawaii!{/en}{ru}Кавай!{/ru} {en}Desu!{/en}{ru}Десу!{/ru}"

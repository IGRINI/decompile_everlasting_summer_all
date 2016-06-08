
python early:
    mods = {}
    mod_tags = {}
    filters = {}

init -1001:

    transform backdrop_trans:
        xalign -0.2
        linear 2.0 xalign 0.0
        pause 3.0

    transform achievement_trans:
        align (1.1, 0.97)
        ease 1.0 align (0.85, 0.97)
        ease 0.5 align (0.95, 0.97)
        pause 1.5
        ease 0.5 align (1.5, 0.97)

    transform lang_ru_ground:
        align (0.5, 0.3)
        ease 0.5 align (0.2, 0.3)
        linear 1.0 align (1.4, 0.3)

    transform lang_ru_hover:
        align (0.5, 0.3)
        pause 1.5
        ease 1.0 align (0.5, 0.3)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_en_ground:
        align (0.5, 0.5)
        ease 0.5 align (0.2, 0.5)
        linear 1.0 align (1.4, 0.5)

    transform lang_en_hover:
        align (0.5, 0.5)
        pause 1.5
        ease 1.0 align (0.5, 0.5)
        linear 1.5 zoom 1.5
        pause 1.5

    transform lang_es_ground:
        align (0.5, 0.7)
        ease 0.5 align (0.2, 0.7)
        linear 1.0 align (1.4, 0.7)

    transform lang_es_hover:
        align (0.5, 0.7)
        pause 1.5
        ease 1.0 align (0.5, 0.7)
        linear 1.5 zoom 1.5
        pause 1.5

    image backdrop_back = "images/anim/backdrop/back.jpg"

    image backdrop_new:
        pause 0.1
        "images/anim/backdrop/1.png"
        pause 0.1
        "images/anim/backdrop/2.png"
        pause 0.1
        "images/anim/backdrop/3.png"
        pause 0.1
        "images/anim/backdrop/2.png"
        repeat

    $ style.backdrop_text = Style(style.default)
    $ style.backdrop_text.color = "#fff"
    $ style.backdrop_text.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.backdrop_text.drop_shadow_color = "#000"
    $ style.backdrop_text.italic = False
    $ style.backdrop_text.bold = False
    $ style.backdrop_text.size = 140

init 5 python:

    ach_table = {
        "main_bad" : {
            None : "main_bad",
            "english" : "main_bad",
            "spanish" : "main_bad"
            },
        "main_good" : {
            None : "main_good",
            "english" : "main_good_en",
            "spanish" : "main_good_en"
            },
        "mi" : {
            None : "mi",
            "english" : "mi",
            "spanish" : "mi"
            },
        "un_bad" : {
            None : "un_bad",
            "english" : "un_bad_en",
            "spanish" : "un_bad_es"
            },
        "un_good" : {
            None : "un_good",
            "english" : "un_good_en",
            "spanish" : "un_good_es"
            },
        "us_bad" : {
            None : "us_bad",
            "english" : "us_bad_en",
            "spanish" : "us_bad_es"
            },
        "us_good" : {
            None : "us_good",
            "english" : "us_good_en",
            "spanish" : "us_good_es"
            },
        "dv_bad" : {
            None : "dv_bad",
            "english" : "dv_bad_en",
            "spanish" : "dv_bad_es"
            },
        "dv_good" : {
            None : "dv_good",
            "english" : "dv_good_en",
            "spanish" : "dv_good_es"
            },
        "sl_bad" : {
            None : "sl_bad",
            "english" : "sl_bad_en",
            "spanish" : "sl_bad_es"
            },
        "sl_good" : {
            None : "sl_good",
            "english" : "sl_good_en",
            "spanish" : "sl_good_en"
            },
        "uv_city" : {
            None : "uv_city",
            "english" : "uv_city",
            "spanish" : "uv_city"
            },
        "uv_unknown_fucken_shit" : {
            None : "uv_good",
            "english" : "uv_good_en",
            "spanish" : "uv_good_es"
            }
        }



    import renpy.store as store

    def show_achievement(img):
        renpy.play(sfx_achievement)
        renpy.show(ach_table[img][_preferences.language], [achievement_trans], layer="overlay")
        renpy.pause(3.5)
        renpy.hide(ach_table[img][_preferences.language])

    class FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)

    def on_load_callback(slot):
        try:
            if persistent.on_save_timeofday[slot]:
                persistent.timeofday = persistent.on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.on_save_timeofday[slot][1]
                persistent.font_size = persistent.on_save_timeofday[slot][2]
                
                _preferences.volumes['music'] = persistent.on_save_timeofday[slot][3]
                _preferences.volumes['sfx'] = persistent.on_save_timeofday[slot][4]
                _preferences.volumes['voice'] = persistent.on_save_timeofday[slot][5]
        
        except:
            pass

    def on_save_callback(slot):
        if not persistent.on_save_timeofday:
            persistent.on_save_timeofday={}
        
        persistent.on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])

    def do_rollback(cnt):
        if not d2_cardgame_block_rollback:
            k=cnt[0]
            renpy.rollback(True, k+1)



    def new_chapter(day_number,chapter_name="",mode="adv",music_stop=False):
        global save_name
        global _window_subtitle
        
        
        
        
        renpy.scene()
        renpy.show("bg black")
        renpy.pause(0.5)
        
        if backdrop == "prologue":
            
            
            
            pass
        elif backdrop == "epilogue":
            
            renpy.show("backdrop_back")
            renpy.show("day_num",what=Text(translation["DayX"][_preferences.language],style=style.backdrop_text,ypos=0.46,xpos=0.46))
            renpy.show("backdrop_new")
            renpy.transition(dissolve)
            renpy.pause(1.0)
        else:
            dn = translation["DayN"][_preferences.language]+u' %d'%(day_number)
            
            renpy.show("backdrop_back")
            renpy.show("day_num",what=Text(dn,style=style.backdrop_text,ypos=0.46,xpos=0.46))
            renpy.show("backdrop_new")
            renpy.transition(dissolve)
            renpy.pause(1.0)
            if backdrop == "dv":
                renpy.show("dv normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if backdrop == "us":
                renpy.show("us normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if backdrop == "sl":
                renpy.show("sl normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
            if backdrop == "un":
                renpy.show("un normal pioneer", [backdrop_trans])
                renpy.transition(dissolve)
                renpy.pause(2.0)
        
        
        
        
        if music_stop:
            for i in range(0,8):
                renpy.music.stop(channel=i)
        if day_number != -1 and day_number != 0:
            dn = translation["DayN"][_preferences.language]+u' %d'%(day_number)
            save_name = chapter_name
        
        
        else:
            pass
            
            save_name = chapter_name
        
        
        
        
        if  backdrop != "prologue":
            renpy.pause(3.0)
            renpy.scene()
            renpy.show("bg black")
            renpy.transition(dissolve)
            renpy.pause(2.0)
        
        if (mode=="adv") :
            set_mode_adv()
        else:
            set_mode_nvl()

    def disable_all_zones():
        store.map.disable_all_zones()
    def enable_all_zones():
        store.map.enable_all_zones()
    def set_zone(name,label):
        store.map.set_zone(name,label)
    def reset_zone(name):
        store.map.reset_zone(name)
    def enable_empty_zone(name):
        store.map.enable_empty_zone(name)
    def reset_current_zone():
        store.map.reset_current_zone()
    def disable_current_zone():
        store.map.disable_current_zone()
    def been_there():
        return store.map.been_there()
    def set_chibi(name,ch):
        store.map.set_chibi(name,ch)
    def reset_chibi(name):
        store.map.reset_chibi(name)
    def show_map():
        ui.jumps("_show_map")()

    def day_time():
        any_time('day')
        persistent.timeofday='day'
    def sunset_time():
        any_time('sunset')
        persistent.timeofday='sunset'
    def night_time():
        any_time('night')
        persistent.timeofday='night'
    def prolog_time():
        any_time('prolog')
        persistent.timeofday='prologue'


    def init_map_zones():
        init_map_zones_realization(store.map_zones,"nothing_here")

    def possible_skip(text, lbl):
        if  skip_text_blocks:
            say("",text)
            ui.jumps(lbl)()

    real_map_event = renpy.display.behavior.map_event
    my_map_event = lambda ev, name: False
    real_renpy_run = renpy.display.behavior.run
    my_renpy_run = lambda name: True

    def nonsafe_noskip_mode():
        
        
        
        
        renpy.display.behavior.map_event = my_map_event
        renpy.display.behavior.run = my_renpy_run

    def nonsafe_skip_mode():
        renpy.display.behavior.map_event = real_map_event
        renpy.display.behavior.run = real_renpy_run



    real_sound_play = renpy.sound.play




label start:
    $ renpy.music.stop()
    $ skip_text_blocks = True
    $ renpy.block_rollback()


    $ init_map_zones()

    python:
        if persistent.jump_to:
            j = persistent.jump_to
            persistent.jump_to = False
            renpy.jump(j)

    jump prologue

label splashscreen:

    python:

        if not persistent.set_volumes:
            
            persistent.lan_chosen = False
            persistent.licensed = False
            
            persistent.timeofday='prologue'
            
            persistent.choices = []
            
            persistent.show_achievements = True
            
            persistent.show_hentai_ach = False
            
            _preferences.language = None
            
            persistent.set_volumes = True
            persistent.achievement = True
            persistent.collector = True
            
            persistent.font_size = "small"
            persistent.hentai = False
            
            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .75

    jump splashscreen_2

label splashscreen_2:

    $ prolog_time()

    if not persistent.lan_chosen:

        scene black

        python:
            ui.imagebutton("images/misc/russian_ground.png", "images/misc/russian_hover.png", clicked = ui.returns("None"), align = (0.5, 0.3))

            ui.imagebutton("images/misc/english_ground.png", "images/misc/english_hover.png", clicked = ui.returns("english"), align = (0.5, 0.5))

            ui.imagebutton("images/misc/spanish_ground.png", "images/misc/spanish_hover.png", clicked = ui.returns("spanish"), align = (0.5, 0.7))

            result = ui.interact()
            if result == "None":
                _preferences.language = None
                renpy.show("ru_hover", [lang_ru_hover])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_ground", [lang_es_ground])
            elif result == "english":
                _preferences.language = "english"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_hover", [lang_en_hover])
                renpy.show("es_ground", [lang_es_ground])
            elif result == "spanish":                                   
                _preferences.language = "spanish"
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_ground", [lang_en_ground])
                renpy.show("es_hover", [lang_es_hover])




            persistent.lan_chosen = True

        $ renpy.pause(4.5, hard=True)

        if _preferences.language != None:
            $ renpy.utter_restart()

    if not persistent.licensed:

        scene black

        $ lic_tab = "        "
        $ lic_tabQ = "                                              "
        $ lic_tabY = "                                                                                          "
        $ lic_tabN = "                                                                                      "
        $ lic_tabY2 = "                                                                                    "
        if _preferences.language == None:
            menu:
                "%(lic_tab)s%(lic_tab)s{color=#aaa}Вы принимаете условия {a=http://creativecommons.org/licenses/by-nc-sa/4.0/deed.ru}CC-BY-NC-SA-4.0{/a} в отношении данной игры?\n\n{size=-10}Вы можете свободно:\n\n%(lic_tab)s {b}Делиться{/b} – копировать и распространять материал на любом носителе и в любом формате.\n%(lic_tab)s {b}Адаптировать{/b} – делать ремиксы, видоизменять и создавать новое, опираясь на этот материал.\n\nПри обязательном соблюдении следующих условий:\n\n%(lic_tab)s {b}Attribution{/b} – вы должны указать авторство, предоставить ссылку на лицензию и обозначить изменения, если они были сделаны.\n%(lic_tab)s {b}NonCommercial{/b} – вы не вправе использовать этот материал в коммерческих целях.\n%(lic_tab)s {b}ShareAlike{/b} – если вы перерабатываете материал игры, вы должны распространять переделанные вами части на условиях той же лицензии.{/size}{/color}\n"
                "{u}Да, я принимаю условия.{/u}\n":
                    pass
                "{u}Нет, я не принимаю условия.{/u}":
                    $ renpy.quit()

        elif _preferences.language == "english":
            menu:
                "%(lic_tab)s%(lic_tab)s{color=#aaa}Do you accept the terms of {a=http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en}CC-BY-NC-SA-4.0{/a} concerning this game?\n\n{size=-10}You are free to::\n\n%(lic_tab)s {b}Share{/b} – copy and redistribute the material in any medium or format.\n%(lic_tab)s {b}Adapt{/b} – remix, transform, and build upon the material.\n\nUnder the following terms::\n\n%(lic_tab)s {b}Attribution{/b} – You must give appropriate credit, provide a link to the license, and indicate if changes were made.\n%(lic_tab)s {b}NonCommercial{/b} – You may not use the material for commercial purposes.\n%(lic_tab)s {b}ShareAlike{/b} – If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.{/size}{/color}\n"
                "{u}Yes, I accept these terms and conditions.{/u}\n":
                    pass
                "{u}No, I reject these terms and conditions.{/u}":
                    $ renpy.quit()

        elif _preferences.language == "spanish":
            menu:
                "%(lic_tab)s%(lic_tab)s{color=#aaa}¿Aceptas los términos de uso {a=http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en}CC-BY-NC-SA-4.0{/a} respecto a este videojuego?\n\n{size=-10}Usted es libre para::\n\n%(lic_tab)s {b}Compartir{/b} – copiar y redistribuir el material en cualquier medio o formato.\n%(lic_tab)s {b}Adaptar{/b} – remezclar, transformar y crear a partir del material.\n\nBajo las condiciones siguientes::\n\n%(lic_tab)s {b}Reconocimiento{/b} – Debe reconocer adecuadamente la autoría, proporcionar un enlace a la licencia e indicar si se han realizado cambios.\n%(lic_tab)s {b}NoComercial{/b} – No puede utilizar el material para una finalidad comercial.\n%(lic_tab)s {b}CompartirIgual{/b} – Si remezcla, transforma o crea a partir del material, deberá difundir sus contribuciones bajo la misma licencia que el original.{/size}{/color}\n"
                "{u}Sí, acepto estos términos y condiciones.{/u}\n":
                    pass
                "{u}No, rechazo estos términos y condiciones.{/u}":
                    $ renpy.quit()

    scene soviet_games
    with dissolve

    if _preferences.language == None:
        if persistent.achievement:
            play sound sfx_achievement
            show achievement:
                align (1.1, 0.97)
                ease 1.0 align (0.85, 0.97)
                ease 0.5 align (0.95, 0.97)
                pause 1.5
                ease 0.5 align (1.5, 0.97)
            $ persistent.achievement = False

    if not persistent.licensed and not config.developer:
        $ renpy.pause(3.5, hard = True)
    else:
        pause(3.5)

    if _preferences.language == None:
        scene disclaimer
        with dissolve
    elif _preferences.language == "english":
        scene disclaimer_en
        with dissolve
    elif _preferences.language == "spanish":
        scene disclaimer_es
        with dissolve
    if not persistent.licensed and not config.developer:
        $ renpy.pause(20, hard = True)
    else:
        pause(20)
    pause

    $ persistent.licensed = True

    pause(1)

    python:
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")
        hour = int(hour)

    if hour in [22,23,24,0,1,2,3,4,5,6]:
        scene splashscreen_night with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_night with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
        return
    if hour in [20,21] or hour in [7,8]:
        scene splashscreen_sunset with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_sunset with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
        return
    else:
        scene splashscreen_day with dissolve:
            pos (0,0)
            linear 4.0 pos (0,-1080)
        $ renpy.pause(4)
        show logo_day with dissolve2:
            pos (400,150)
        $ renpy.pause(3)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

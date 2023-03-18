# League of Legends auto accept

---

Option to enable it urself manually or fully automatic for each game.

![v1.0.0](https://user-images.githubusercontent.com/35658558/213885042-942d8d4c-211f-4a84-9f7a-476392063271.png)
![v1.2.0](https://i.imgur.com/985tpzq.png)
![v2.0.0](https://i.imgur.com/3rRVHep.png)

Already compiled file (the .exe) download link :

- [v1.0.0](https://github.com/Tom-Hartmann/Queue-accepter/releases/tag/v1.0.0)
- [v1.2.0](https://github.com/Tom-Hartmann/Queue-accepter/releases/tag/v1.2.0)
- [v1.5.0](https://github.com/Tom-Hartmann/Queue-accepter/releases/tag/v1.5.0)
- [v2.0.0](https://github.com/Tom-Hartmann/Queue-accepter/releases/tag/v2.0.0)
Features:

- Click on the on/off button to begin the search of a starting game or click on automode to let the program activate and deactivate the queue accepter.
- The programm will automatically set to "off" once it found the game so no risk of clicking somewhere once you've started the game.
- Automode will deactivate once you are in Preparation and ingame, once you are back out it will reactivate the searching.
- If someone didn't accept the game the program will switch to "on" mode to search again
- If you select Lock, it will autolock in the chamption you have pre selected.
- Check the config.json for extra options to turn off or on with false/true statements.
- If you select Ban, it will autoban the chamption named in the config.json file. Default beeing shaco. Note that this only works if you write the name correct! I will put most champs below so you can check without needing to go ingame.
- That's it !

Champions:

```html
Aatrox,Ahri,Akali,Akshan,Alistar,Amumu,Anivia,Annie,Aphelios,Ashe,Aurelion
Sol,Azir,Bard,Bel'Veth,Blitzcrank,Brand,Braum,Caitlyn,Camille,Cassiopeia,Cho'Gath,Corki,Darius,Diana,Draven,Dr.
Mundo,Ekko,Elise,Evelynn,Ezreal,Fiddlesticks,Fiora,Fizz,Galio,Gangplank,Garen,Gnar,Gragas,Graves,Gwen,Hecarim,Heimerdinger,Illaoi,Irelia,Ivern,Janna,Jarvan
IV,Jax,Jayce,Jhin,Jinx,Kai'Sa,Kalista,Karma,Karthus,Kassadin,Katarina,Kayle,Kayn,Kennen,Kha'Zix,Kindred,Kled,Kog'Maw,LeBlanc,Lee
Sin,Leona,Lillia,Lissandra,Lucian,Lulu,Lux,Malphite,Malzahar,Maokai,Master
Yi,Miss
Fortune,Mordekaiser,Morgana,Nami,Nasus,Nautilus,Neeko,Nidalee,Nilah,Nocturne,Nunu
&
Willump,Olaf,Orianna,Ornn,Pantheon,Poppy,Pyke,Qiyana,Quinn,Rakan,Rammus,Rek'Sai,Rell,Renata
Glasc,Renekton,Rengar,Riven,Rumble,Ryze,Samira,Sejuani,Senna,Seraphine,Sett,Shaco,Shen,Shyvana,Singed,Sion,Sivir,Skarner,Sona,Soraka,Swain,Sylas,Syndra,Tahm
Kench,Taliyah,Talon,Taric,Teemo,Thresh,Tristana,Trundle,Tryndamere,Twisted
Fate,Twitch,Udyr,Urgot,Varus,Vayne,Veigar,Vel'Koz,Vex,Vi,Viego,Viktor,Vladimir,Volibear,Warwick,Wukong,Xayah,Xerath,Xin
Zhao,Yasuo,Yone,Yorick,Yuumi,Zac,Zed,Zeri,Ziggs,Zilean,Zoe,Zyra
```

How to add your own language (English already included) EXAMPLE:

- Take a screenshot of the "accept" button of your game and cut it to only have the button using any image edit software (from paint to photoshop the choice is yours) and rename it "accept.png"
- Do the same when someone doesn't accept the game (just take a part of the sentence like "declined ready check") and rename it "notaccept.png"
- Copy the balance.png into your folder, it should be the same for all language, if it does not activate for you just take a new screenshot of the balances like shown in the picture.
- The pictures don't have to be precise just be carefull you don't have any background showing and save them to .png
- Create a new folder inside the "Languages" one (call it wathever you want but i reccomand using the language you're aiming to add) and put the two images you just cropped inside it.
- Open the "config.json" file located in the "Languages" folder. Change the first line to "Language = [The name of the folder you just created]"
- This should work !

How to compile the code into an .exe using cx_Freeze (https://cx-freeze.readthedocs.io/en/latest/index.html):

- Install cx_Freeze (by using pip : most likely by typing "python -m pip install --upgrade cx_Freeze" or "python3 -m pip install --upgrade cx_Freeze" on your command prompt)
- Open your command prompt and move to the directory where the script are
- Type "python setup.py build" or "python3 setup.py build" depending on your version of python
- The .exe should appear in "\build\exe.win-amd64-3.9\\" ("exe.win-amd64-3.9" will change according to your os and python version)
- Copy the "Language" folder and "icon.ico" in the same folder as your .exe
- Enjoy !

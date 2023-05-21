# MatProgCsom-hf Blackjack Kártyaszámlálás
Projektünk a blackjack kártyaszámlálást mutatja be. A blackjack egy olyan kaszinójáték, ahol a cél az, hogy közelebb jussunk vagy elérjük a 21-es pontszámot a kiosztott kártyák segítségével anélkül, hogy túllépnénk ezen a pontszámon. A játékban minden felfordított lap után döntenünk kell, hogy megállunk vagy még egyet húzunk. Ezen kívül két további speciális helyzetekben fennálló lépést is megvalósítottunk. Ha az eredeti két lap alapján úgy érezzük, hogy jó esélyünk van nyerni, akkor választhatjuk a duplázás opciót. Ebben az esetben a tétet megduplázzuk viszont csak egy további lapot kapunk. Ha az eredeti két lap azonos értékű, akkor választhatjuk a split opciót. Ebben az esetben két külön kézzel játszunk tovább.

A feltöltött „wo_counting” fájl lehetővé teszi a blackjack kipróbálását és elsajátítását. A program elindítása után meg kell adnunk a játék főbb jellemzőit, mint a paklik száma, a nálunk lévő pénzösszeg, a minimális tét mértéke. Ezeket egyszer kéri be a program. Az alábbiakban bemutatunk egy példa lefutást:
```
Number of decks? 4
Starting amount?100
Minimum bet?10
```
Ezután egy-egy játék során meg kell adnunk az aktuális tétet, ezek után láthatjuk az első két kártyánkat, illetve az osztó egyik lapját.
```
Your bet? 10
Your cards:
┌───────┐
│ 2     │
│       │
│       │
│     2 │
└───────┘
┌───────┐
│ Q     │
│       │
│       │
│     Q │
└───────┘
Dealer's first card: 
┌───────┐
│ 5     │
│       │
│       │
│     5 │
└───────┘
```
Most meg kell hoznunk a döntést, hogy két azonos értékű lap esetén splitelünk-e, illetve szeretnénk-e duplázni. Ezután már csak hit, stand opciókat választhatunk. A végén a program rákérdez, hogy szeretnénk-e mégegyet játszani, ha nem kiírja a statisztikákat.
```
Do [y]ou wa[n]t to double down?n
Choose: [h]it of [s]tand? h
┌───────┐
│ 2     │
│       │
│       │
│     2 │
└───────┘
Choose: [h]it of [s]tand? h
┌───────┐
│ 5     │
│       │
│       │
│     5 │
└───────┘
Choose: [h]it of [s]tand? s
Dealer's turn
┌───────┐
│ Q     │
│       │
│       │
│     Q │
└───────┘
┌───────┐
│ Q     │
│       │
│       │
│     Q │
└───────┘
You won :)

 Do [y]ou want to play o[n]e more time?n

 You played  1  games, won  1  out of these.
Your balance is  110 .
```
A kártyaszámlálás a blackjack játék stratégiai része, amely lehetővé teszi, hogy előre jelezzük a következő kártyák értékét és ennek alapján döntsünk. A kártyák értékének figyelemmel kísérése segít a játékosnak előnyt szerezni a kaszinóval szemben, mivel ez lehetőséget ad arra, hogy előnyös helyzetben nagyobb téttel játszva növelje a nyerési esélyeit. Az egyes játékok során az optimális blackjack stratégiával játszunk.

![image](https://github.com/tali2001/MatProgCsom-hf/assets/128598130/b8234a6a-3a76-494a-a166-0724b87f31df)

A kártyaszámlálás alapja az, hogy figyelemmel követjük a kártyák értékét a játék során. Általában a kártyák magas és alacsony értékére koncentrálunk. A magas értékű kártyák (ászok, 10-esek, jumbók, királyok, dámák) előnyösek a játékos számára, míg az alacsony értékű kártyák inkább a kaszinó javára válnak. Ha magas értékű kártyák maradnak a pakliban, akkor a játékosnak előnye származik, mivel növekszik az esélye a 21-hez közelítő kéz létrehozására. A projektünkben a következő ismert stratégiákat próbáltuk ki: 'Hi-Lo','Hi-Opt I','Hi-Opt II','KO','Omega II','Red 7','Halves','Zen Count','10 Count'. Minden esetben a különböző lapokhoz különböző értékeket rendelünk és az eddig felfordított lapok értékösszege alapján határozzuk meg, hogy a következő játék során milyen nagy tétet teszünk fel. 

![image](https://github.com/tali2001/MatProgCsom-hf/assets/128598130/cb64d4f6-80bf-4cf9-9a86-5178b838b44d)

A „w_counting” fájl tartalmazza a megvalósított kártyaszámláló programunkat. Egy-egy stratégia, illetve pakliszám esetét a start_playing(n, nr, money, minbet, strategy) függvény meghívásával vizsgálhatunk meg, ahol a paraméter sorban: a lejátszani kívánt játékok száma, a paklik száma, a kezdeti pénzösszeg, minimális tét, stratégia (ez a fenti listából válaszható). Próbáltunk olyan stratégiákat és olyan helyzeteket vizsgálni, amelyek életszerűek, azaz elképzelhető, hogy egy ember fejben tudja őket tartani, számolni; illetve például az első grafikon esetén reálisnak ítéljük, hogy valaki 20 meccset lejátszik egy asztalnál.

Összehasonlításképpen: house edge különböző pakliszámok esetén:
```
1 – 0.17%
2 – 0.46%
4 – 0.60%
6 – 0.64%
8 – 0.66%
```
Eredmények fix 20 futtatással x 5000:

![kep_jo 500x20](https://github.com/tali2001/MatProgCsom-hf/assets/128598130/2f58fd57-bd67-4601-9a4b-f8f1701972e2)

Eredmények úgy, hogy változtatjuk a játékok számát a pakli méretével arányosan (de az össz futtatásszám fix):

![kep_valtozik a paklival a futtatasok szama, ossz fix _ ossz=1000](https://github.com/tali2001/MatProgCsom-hf/assets/128598130/671f857e-c262-4a36-a635-5946bbb45a3b)

![valtozik](https://github.com/tali2001/MatProgCsom-hf/assets/128598130/632a7e57-5f2e-46d4-ab8a-2526a0aa75d9)

Eredményeink értékelése, magyarázatok: bővebben az előadáson.



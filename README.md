# Project "Halle 7"
A little game from Martin & David.

`Repository: Private`


# 1.0 Hilfreiche Links
https://trinket.io/features/pygame -> Beispiel eines pygames
https://pixlr.com/de/express/ -> Erstellen der Bilder (Einfach)
https://pixlr.com/de/editor/ -> Erstellen der Bilder (Schwer)

# 2.0 Eingebaute Funktionen von Martin - Wie benutze ich diese?

# 2.1 Logs senden
```
from src.import import log
log.log(type="global").info("TEXT_HIER")
```
**Bemerkung:** Es kann .debug, .info, .warning, .error oder .critical verwendet werden. **Mehr Information dazu weiter unten**

# 2.2 Auf die Config-Datei zugreifen 
```
from src.imports import data
wichtiger_string_oder_int = data.DATABASE_PATH
```
**Bemerkung:** Beispiel jetzt mit dem wert von DATABASE_PATH, kann verändert werden

# 3.0 Einstufungen der Logs

`.debug`
Debug steht **unter** Info, und ist nur eine kleine nebeninformation die in der Konsole **nicht** Angezeigt wird, sondern nur in den Dateien.

`.info`
Info ist eine **stink normale** Information darüber, was gerade im Programm passiert. Wird in der Konsole Angezeigt.

`.warning`
Warning ist eine **wichtigere** Information darüber, was gerade im Programm passiert. Wird in der Konsole angezeigt.

`.error`
Error ist eine **sehr wichtige** Information darüber, was gerade im Programm passiert. Wird in der Konsole angezeigt.

`.critical`
Critical ist eine **superwichtige** Information darüber, was gerade im Programm passiert. **Falls ein Critical Angezeigt wird, steht ein Fehler im Programm vor, der so groß ist, dass es nicht Funktioniert!** Wird in der Konsole Angezeigt.

# 4.0 root & global

`global`
Eine **stink normale** Information + es werden auch Informationen von externen packages Angezeigt. Wird in der Konsole angezeigt

`root`
Eine **stink normale** Information. Wird in der Konsole angezeigt

# 5.0 Verwendung der Datenbank

**Wichtig:** Wenn keine einzige Datenbank vorhanden ist, wird der DataBase Manager durchgehend auf dem Status "noch am laden" sein!

# 5.1 Erstellen einer neuen Datenbank
```
import src.classes.db.file.dbcreator as DBC
import src.classes.db.dbmanager as DBM

DBC.create_db("name_der_datenbank")
DBM.__load__()
```
**Bemerkung:** 
- Hier wird eine neue Datenbank sowie der Datenbank Manager geladen.

# 5.2 Befehle der Datenbank
```
DELETE from {} WHERE id={} AND type='{}'
UPDATE {} SET content='{}' WHERE id={} AND type='{}'
INSERT INTO {} VALUES ({}, '{}', '{}')
SELECT * FROM {} WHERE id={} AND type='{}'
```
**Bemerkungen:** 
- Strings sind mit '' gekennzeichnet.
- Beim SELECT den Rückgabewert mit [1][0][0] kennzeichnen, um direkt den ersten Wert zu erhalten.

# 5.3 Execute in der Datenbank (Befehl durchgeben)
```
from src.imports import db
db.execute("""BEFEHL""".format())
```
**Bemerkungen:**
- Gibt False zurück, wenn etwas schief gelaufen ist (sonst True) (steht auch von selbst in der Konsole)
- Bei einem SELECT wird auch die Liste mitgegeben

# 5.3 Pointer auf eine Datenbank setzen
```
from src.imports import db
db.point("name_des_tables")
```
**Bemerkungen:**
- Der Wert name_des_tables ist aus der `structure.db.json` zu entnehmen!
- Wenn der String nicht da, oder None ist, so wird der Pointer zurückgesezt. (Pointer zeigt auf keine Datenbank mehr)

# 6.0 Verwendung von easydb

Die vereinfachte Version der normalen Datenbank version.

# 6.1 import
```
from src.imports import easydb as easydb
```

# 6.2 Pointer setzen
```
easydb.point("name-der-datenbank")
```
**ACHTUNG:** Dieser Pointer funktioniert NUR MIT EASYDB, NICHT MIT DER NORMALEN DB FUNKTION!!!!!!!!

**Rückgabewert:** Sendet False/True zurück, je nach dem ob es funktioniert hat. Fehler werden von selbst in die Konsole gesendet.

# 6.3 Datenbank auslesen
```
easydb.read("name-des-tables")
```

**Rückgabewert:** False oder der gelesene Wert.

# 6.4 Gesamten Datensatz löschen

```
easydb.delete("name-des-tables")
```

**Rückgabewert:** True oder False, je nach dem, ob es funktioniert hat.

# 6.5 Datensatz als str hinzufügen

```
easydb.send("ISTWERT","str","name-des-tables","wert")
```
**ISTWERT** und **str** bleiben hierblei immer gleich.

**Rückgabewert:** True oder False, je nach dem, ob es funktioniert hat.

# 6.5 Datensatz als int hinzufügen

```
easydb.send("ISTWERT","int","name-des-tables","wert")
```
**ISTWERT** und **int** bleiben hierblei immer gleich.

**Rückgabewert:** True oder False, je nach dem, ob es funktioniert hat.

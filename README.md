# Project "variable-sqlite3-database"
Ein einfaches Modul für zukünftige Projekte, um einen schnellen Start zu ermöglichen.


`Repository: Public`


# 1.0 Hilfreiche Links
None

# 2.0 Eingebaute Funktionen

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

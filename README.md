# Project "Halle 7"
A little game from Martin & David.

`Repository: Private`


# Hilfreiche Links
https://trinket.io/features/pygame -> Beispiel eines pygames
https://pixlr.com/de/express/ -> Erstellen der Bilder (Einfach)
https://pixlr.com/de/editor/ -> Erstellen der Bilder (Schwer)

# Eingebaute Funktionen von Martin - Wie benutze ich diese?

`Basisimport (muss in jener Datei für die Funktion sein!)`
import src.imports as SI


`Auf die Datenbank zugreifen` (nicht ganz fertig)
wichtiger_string_oder_int = SI.db.TODO

`Logs senden`
SI.log.log(type="global").info("TEXT_HIER")
^
Es kann .debug, .info, .warning, .error oder .critical sein. `Mehr Information dazu weiter unten`

`Auf die Config-Datei zugreifen` (beispiel jetzt mit dem wert von DATABASE_PATH, kann verändert werden)
wichtiger_string_oder_int = SI.data.DATABASE_PATH


# Einstufungen der Logs

`.debug`
Debug steht **unter** Info, und ist nur eine kleine nebeninformation die in der Konsole **nicht** Angezeigt wird, sondern nur in den Dateien.

`.info`
Info ist eine **stink normale** Information darüber, was gerade im Programm passiert. Wird in der Konsole Angezeigt.

`.warning`
Warning ist eine **wichtigere** Information darüber, was gerade im Programm passiert. Wird in der Konsole Angezeigt.

`.error`
Error ist eine **sehr wichtige** Information darüber, was gerade im Programm passiert. Wird in der Konsole Angezeigt.

`.critical`
Critical ist eine **superwichtige** Information darüber, was gerade im Programm passiert. **Falls ein Critical Angezeigt wird, steht ein Fehler im Programm vor, der so groß ist, dass es nicht Funktioniert!** Wird in der Konsole Angezeigt.

# root & global

`global`
Eine **stink normale** Information + es werden auch Informationen von externen packages Angezeigt. Wird in der Konsole Angezeigt

`root`
Eine **stink normale** Information. Wird in der Konsole Angezeigt

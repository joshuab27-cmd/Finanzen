# Vier-Monats-Finanzplan

Web-App zum Planen von Gehalt, monatlichen und einmaligen Ausgaben in Vier-Monats-Fenstern, mit ETF-Sparplan, konservativer Hochrechnung und Analyse vermeidbarer Ausgaben.

**App öffnen:** https://joshuab27-cmd.github.io/Finanzen/

- Die Daten bleiben auf deinem Gerät (Browser-Speicher). Es gibt keinen Server.
- Die App ist installierbar (iPhone: Safari → Teilen → „Zum Home-Bildschirm“, Android: Chrome → „App installieren“) und funktioniert offline.
- Backups machst du unter dem Pfeil-Symbol oben rechts („Daten & Backup“).

## Dateien

- `app.html`: Quelle der App (wird auch als Claude-Artifact veröffentlicht)
- `build.py`: erzeugt daraus `index.html` und `sw.js` (nach jeder Änderung an `app.html` ausführen: `python3 build.py`)
- `manifest.webmanifest`, `sw.template.js`, `icons/`: Dateien für die installierbare Web-App

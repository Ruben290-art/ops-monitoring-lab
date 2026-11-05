# Projekt im Gespräch erklären

## 30-Sekunden-Version

> Nach einem technischen Gespräch habe ich ein persönliches Lernprojekt aufgebaut, um mich praktisch mit Ansible und Checkmk zu beschäftigen. Ein kleiner Linux-Dienst stellt einen Health-Endpunkt bereit. Eine Ansible-Rolle installiert den Dienst und einen Checkmk-kompatiblen Local Check. Automatisierte Tests prüfen erreichbare, nicht erreichbare und ungültige Antworten. Wichtig war mir nicht nur, dass es funktioniert, sondern dass Installation, Fehlerfälle und Grenzen nachvollziehbar dokumentiert sind.

## Ehrliche Abgrenzung

> Das ist ein persönliches Lab und keine produktive Hochverfügbarkeitsumgebung. Ich habe damit die Grundlagen praktisch angewendet, aber ich würde daraus noch keine produktive Checkmk- oder Ansible-Erfahrung ableiten.

## Technische Rückfragen vorbereiten

- Warum Ansible? Wiederholbare, lesbare Konfiguration und idempotente Aufgaben.
- Warum Checkmk Local Check? Kleiner eigener Service-Check mit klar definiertem Ausgabeformat.
- Welche Zustände? `0 OK`, `1 WARN`, `2 CRIT`, `3 UNKNOWN`.
- Was passiert bei Ausfall? Der Check gibt CRIT aus, ohne einen Traceback zu erzeugen.
- Wie wird getestet? Unit-Tests mocken HTTP-Antworten; CI führt Tests und Syntaxprüfung aus.
- Nächster Schritt? Logs zentral sammeln und einen Rolling-Update-/Rollback-Ablauf dokumentieren.


# Learning Log

## Ausgangspunkt

Vor diesem Projekt hatte ich noch keine praktische Projekterfahrung mit Checkmk und Ansible. Ziel war, die Konzepte nicht nur theoretisch zu lesen, sondern einen kleinen, überprüfbaren Ablauf selbst umzusetzen.

## Was ich umgesetzt habe

- Health-Endpunkt eines Linux-Dienstes
- Checkmk-Ausgabe mit Zuständen OK, CRIT und UNKNOWN
- reproduzierbare Bereitstellung mit einer Ansible-Rolle
- systemd Service Unit und Restart-Handler
- Unit-Tests für relevante Fehlerfälle
- CI-Prüfung bei Push und Pull Request

## Was ich noch nicht behaupte

- Betrieb eines produktiven Checkmk-Servers
- produktive Erfahrung mit hochverfügbaren Leitstellensystemen
- Administration eines Proxmox-Clusters
- produktive Erfahrung mit Terraform oder Elastic Stack

## Wichtigste Erkenntnis

Bei einem unbekannten technischen Problem reicht „funktioniert nicht“ nicht aus. Ein sinnvoller Arbeitsstand enthält:

1. das erwartete Verhalten,
2. das beobachtete Verhalten,
3. die bereits durchgeführten Prüfungen,
4. relevante Logs oder Fehlermeldungen,
5. die nächste Hypothese oder eine konkrete Frage an das Team.


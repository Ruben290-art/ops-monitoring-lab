# Linux Service Automation & Monitoring Lab

Persönliches Lernprojekt zur automatisierten Bereitstellung und Überwachung eines kleinen Linux-Dienstes.

## Ziel

Das Projekt demonstriert einen vollständigen, nachvollziehbaren Ablauf:

1. Ein kleiner Python-Dienst stellt einen Health-Endpunkt bereit.
2. Ansible installiert und konfiguriert den Dienst reproduzierbar.
3. Ein lokaler Check liefert den Zustand im Checkmk-Format.
4. Automatisierte Tests prüfen OK-, CRIT- und UNKNOWN-Fälle.
5. GitHub Actions führt die Tests bei jeder Änderung aus.

Das Projekt ist ein **persönliches Lernprojekt**. Es bildet keine produktive Leitstellenumgebung nach und ersetzt keine Hochverfügbarkeits- oder Sicherheitsarchitektur.

## Technologien

- Python 3
- Linux und systemd
- Ansible
- Checkmk Local Check Format
- GitHub Actions
- `unittest`

## Architektur

```text
HTTP Client
    |
    v
Python Health Service (:8080/health)
    ^
    |
Checkmk Local Check
    |
    v
0 OK / 2 CRIT / 3 UNKNOWN

Ansible -> Service, systemd Unit und Monitoring-Skript
```

## Lokal testen

```bash
python3 app/status_service.py
```

In einem zweiten Terminal:

```bash
python3 monitoring/check_app_service.py
python3 -m unittest discover -s tests -v
```

Erwartete Check-Ausgabe:

```text
0 "Portfolio App Health" response_ms=... Service reachable, status=ok
```

## Mit Ansible auf einem Linux-Testsystem bereitstellen

Voraussetzungen: Linux oder WSL, Python 3, Ansible und Berechtigung für `sudo`.

```bash
cd ansible
ansible-playbook -i inventory/local.ini site.yml --ask-become-pass
```

Danach:

```bash
systemctl status portfolio-status-service
curl http://127.0.0.1:8080/health
/usr/lib/check_mk_agent/local/check_portfolio_app
```

Mit Check Mode kann die geplante Änderung vorher geprüft werden:

```bash
ansible-playbook -i inventory/local.ini site.yml --check --diff --ask-become-pass
```

## Fehlerfall simulieren

```bash
sudo systemctl stop portfolio-status-service
/usr/lib/check_mk_agent/local/check_portfolio_app
```

Der Check muss dann den Zustand `2` (CRIT) oder `3` (UNKNOWN) melden, ohne einen Python-Traceback auszugeben.

## Bewusst begrenzter Umfang

- keine echte Hochverfügbarkeitsumgebung
- kein produktiver Checkmk-Server
- kein Proxmox-Cluster
- keine geheimen Zugangsdaten
- keine Kundendaten

Die nächsten Ausbaustufen stehen in [ROADMAP.md](ROADMAP.md).


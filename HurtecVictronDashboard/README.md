# Hurtec & Victron Dashboard

This project provides a small yet functional dashboard application that can be
run on both desktop systems and the Raspberry Pi.  It offers a tabbed web
interface for monitoring multiple sites and exposes a tiny HTTP API for remote
control.  Configuration is persisted to ``config.json`` so the application
remembers all added tabs.

### Running

```bash
make run
```

The application loads tab definitions from ``config.json`` if it exists, or
``config/default_config.json`` otherwise.  A Flask server is started on port
``8765`` to allow remote tab management:

```bash
curl -X POST http://localhost:8765/tabs -H 'Content-Type: application/json' \
    -d '{"url": "https://example.com", "name": "Example"}'
```

### Building an executable

Use the packaging script which relies on PyInstaller.  The resulting executable
can be copied to either Windows or Raspberry Pi machines:

```bash
python3 scripts/package.py
```

The resulting binary is placed in `dist/`.

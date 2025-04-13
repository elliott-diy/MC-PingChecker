# Minecraft API Ping Checker

A small Python script to check latency to Minecraft and Mojang API servers. Useful for claiming Minecraft usernames.

## What it does

- Sends 5 HTTPS requests to each API
- Measures how long it takes to get a response
- Prints the average ping time in milliseconds

## Requirements

- Python 3.7+
- Install colorama:

```bash
pip install colorama
```

## Run it

```
python ping.py
```

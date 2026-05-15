# FIRST CTF Scoreboard

Live scoreboard for FIRST CTF events, featuring real-time score updates, countdown timer, score trend graph, announcements feed, and latest submissions.

![Final Results Screenshot](screenshots/results.png)

## Features

- Real-time scoreboard with auto-scroll and periodic refresh
- Countdown timer to CTF end
- Score trend graph (top 10 teams over time)
- Auto-rolling announcements from CTFd notifications
- Latest submissions feed
- Gold/silver/bronze podium styling for top 3
- Neon hacker theme aligned with CTFd instance
- 4K display support

## Configuration

All parameters are configured via environment variables:

| Variable         | Description                        | Default                                          |
|------------------|------------------------------------|--------------------------------------------------|
| `CTFD_BASE_URL`  | CTFd API base URL                  | `https://ctfdev.firstseclounge.org/api/v1`       |
| `CTFD_API_KEY`   | CTFd API token (optional)          | *(empty)*                                        |
| `CTF_DEADLINE`   | Countdown end date                 | `December 12 2025 16:00:00 GMT+0100`             |
| `CTF_TITLE`      | Title displayed on the scoreboard  | `FIRST CTF 2025`                                 |

## Local setup

Requires Python 3 and virtualenv.

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

export CTFD_BASE_URL=https://ctf.firstseclounge.org/api/v1
export CTFD_API_KEY=ctfd_xxxxxxxxxxxx
export CTF_DEADLINE="June 25 2026 17:00:00 GMT+0200"
export CTF_TITLE="FIRST CTF 2026"

python app.py
```

Visit http://localhost:8080

## Docker setup

Build the container:

```bash
docker build -t scoreboard .
```

Run the container:

```bash
docker run -p 8888:80 -d \
  -e CTFD_BASE_URL=https://ctf.firstseclounge.org/api/v1 \
  -e CTFD_API_KEY=ctfd_xxxxxxxxxxxx \
  -e CTF_DEADLINE="June 25 2026 17:00:00 GMT+0200" \
  -e CTF_TITLE="FIRST CTF 2026" \
  --name scoreboard \
  scoreboard
```

## Deployment (scoreboard.ctfsig.org)

The scoreboard runs as a Docker container on the CTF infrastructure. To redeploy:

```bash
rsync -avz --exclude='env/' --exclude='__pycache__/' --exclude='.git/' ./ ubuntu@scoreboard.ctfsig.org:/home/ubuntu/Scoreboard/

ssh ubuntu@scoreboard.ctfsig.org "cd /home/ubuntu/Scoreboard && \
  sudo docker build -t scoreboard . && \
  sudo docker stop scoreboard && \
  sudo docker rm scoreboard && \
  sudo docker run -p 8888:80 -d --name scoreboard \
    -e CTFD_BASE_URL=https://ctfdev.firstseclounge.org/api/v1 \
    -e CTF_DEADLINE='June 18 2026 16:00:00 GMT-0600' \
    -e CTF_TITLE='FIRST CTF 2026' \
    scoreboard"
```

## Routes

| Path             | Description                              |
|------------------|------------------------------------------|
| `/`              | Redirects to `/scoreboard`               |
| `/scoreboard`    | Main display (embeds all other panes)    |
| `/data`          | Team rankings (loaded via AJAX)          |
| `/latest`        | Latest submissions (loaded via AJAX)     |
| `/trenddata`     | Score trend JSON for Chart.js            |
| `/notifications` | CTFd announcements (loaded via AJAX)     |
| `/timer`         | Standalone countdown page                |
| `/results`       | Final results page                       |

## Tech stack

- Python 3 / Flask / Gunicorn
- Chart.js (score trend graph)
- jQuery (AJAX data loading)
- Google Fonts: Orbitron, VT323, Fira Code

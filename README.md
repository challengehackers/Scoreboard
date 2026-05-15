# GCTF2017-Scoreboard updated for FIRSTCON25

![Final Results Screenshot](screenshots/results.png)

## Configuration

All parameters are configured via environment variables:

| Variable         | Description                        | Default                                          |
|------------------|------------------------------------|--------------------------------------------------|
| `CTFD_BASE_URL`  | CTFd API base URL                  | `https://ctfdev.firstseclounge.org/api/v1`       |
| `CTFD_API_KEY`   | CTFd API token (optional)          | *(empty)*                                        |
| `CTF_DEADLINE`   | Countdown end date                 | `December 12 2025 16:00:00 GMT+0100`             |
| `CTF_TITLE`      | Title displayed on the scoreboard  | `FIRST CTF 2025`                                 |

## Local setup

* Requires Python3 and virtualenv

```bash
virtualenv -p /usr/bin/python3 env
source env/bin/activate
pip install -r requirements.txt

export CTFD_BASE_URL=https://ctf.firstseclounge.org/api/v1
export CTFD_API_KEY=ctfd_xxxxxxxxxxxx
export CTF_DEADLINE="June 25 2026 17:00:00 GMT+0200"
export CTF_TITLE="FIRST CTF 2026"

python app.py
```

* Visit http://localhost:8080

## Docker setup

* Build the container
```bash
docker build -t scoreboard .
```

* Run the container in background
```bash
docker run -p 8888:80 -d \
  -e CTFD_BASE_URL=https://ctf.firstseclounge.org/api/v1 \
  -e CTFD_API_KEY=ctfd_xxxxxxxxxxxx \
  -e CTF_DEADLINE="June 25 2026 17:00:00 GMT+0200" \
  -e CTF_TITLE="FIRST CTF 2026" \
  scoreboard
```

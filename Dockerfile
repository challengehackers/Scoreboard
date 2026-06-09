FROM python:3.10
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENV CTFD_BASE_URL=https://ctf.firstseclounge.org/api/v1
ENV CTFD_API_KEY=
ENV CTF_DEADLINE="June 18 2026 16:00:00 GMT-0600"
ENV CTF_START="June 15 2026 10:00:00 GMT-0600"
ENV CTF_TITLE="FIRST CTF 2026"
ENV CTF_REGISTRATION_URL=https://ctf.firstseclounge.org
ENV CTF_REGISTRATION_CODE=
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]

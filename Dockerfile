FROM python:3.10
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENV CTFD_BASE_URL=https://ctfdev.firstseclounge.org/api/v1
ENV CTFD_API_KEY=
ENV CTF_DEADLINE="December 12 2025 16:00:00 GMT+0100"
ENV CTF_TITLE="FIRST CTF 2025"
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]

import os

BASEURL = os.environ.get('CTFD_BASE_URL', 'https://ctf.firstseclounge.org/api/v1')
API_KEY = os.environ.get('CTFD_API_KEY', '')
CTF_DEADLINE = os.environ.get('CTF_DEADLINE', 'June 18 2026 16:00:00 GMT-0600')
CTF_START = os.environ.get('CTF_START', 'June 15 2026 10:00:00 GMT-0600')
CTF_TITLE = os.environ.get('CTF_TITLE', 'FIRST CTF 2026')
CTF_REGISTRATION_URL = os.environ.get('CTF_REGISTRATION_URL', 'https://ctf.firstseclounge.org')
CTF_REGISTRATION_CODE = os.environ.get('CTF_REGISTRATION_CODE', '')

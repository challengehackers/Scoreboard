import os

BASEURL = os.environ.get('CTFD_BASE_URL', 'https://ctfdev.firstseclounge.org/api/v1')
API_KEY = os.environ.get('CTFD_API_KEY', '')
CTF_DEADLINE = os.environ.get('CTF_DEADLINE', 'December 12 2025 16:00:00 GMT+0100')
CTF_TITLE = os.environ.get('CTF_TITLE', 'FIRST CTF 2025')

"""
File: main.py
Author: Chuncheng Zhang
Date: 2024-05-31
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Main entrance for the web server

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-05-31 ------------------------
# Requirements and constants
import asyncio

from fastapi import FastAPI, Request
from fastapi import responses
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pathlib import Path

from loguru import logger

import mimetypes
mimetypes.add_type('application/x-font-woff', '.woff')

# ----------------------------------------------------------------


class Options:
    root = Path(__file__).parent


# %% ---- 2024-05-31 ------------------------
# Function and class
app = FastAPI()

app.mount('/static', StaticFiles(directory='web/static'), name='static')
app.mount("/asset", StaticFiles(directory="asset"), name="asset")

jinja2_template = Jinja2Templates(directory='web/template')


# ------------------------------------------------------------------------------
@app.get('/')
async def root(request: Request):
    return jinja2_template.TemplateResponse('root.html', dict(request=request))


# ------------------------------------------------------------------------------
@app.get(
    '/readme',
    response_class=responses.PlainTextResponse,
)
async def readme():
    return open(Options.root.joinpath('README.md')).read()


# ------------------------------------------------------------------------------
@app.get('/index')
async def index(request: Request):
    logger.debug(f'Got {request}')
    return jinja2_template.TemplateResponse('index.html', dict(request=request))

# %% ---- 2024-05-31 ------------------------
# Play ground


# %% ---- 2024-05-31 ------------------------
# Pending


# %% ---- 2024-05-31 ------------------------
# Pending

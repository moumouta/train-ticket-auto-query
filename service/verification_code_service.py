from tkinter import Image
import requests
import io
from dataclasses import dataclass
from service.common import *
from flask import Request, Response
from typing import List


@dataclass
class VerifyCodeResult(DataclassInstance):
    result: bool

@dataclass
class ReturnBody(DataclassInstance):
    status: int
    msg: str
    data: List


def generate_verification_code(client: requests.Session, host: str, headers: dict):
    """
    /api/v1/verifycode/generate GET
    """
    url = "/api/v1/verifycode/generate"
    response = client.request(url=host + url, method='GET', headers=headers)
    # image_bytes = io.BytesIO(response.content)
    # image = Image.open(image_bytes)
    return response
    # return image


def verify_code(client: requests.Session, verify_code: str, host: str, headers: dict):
    """
    /api/v1/verifycode/verify/{verifyCode} GET
    """
    url = f"/api/v1/verifycode/verify/{verify_code}"
    response = client.request(url=host + url, method='GET', headers=headers)
    return response.json()

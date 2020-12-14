from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Digits(BaseModel):
    digits: Optional[List[int]]


@app.post("/ping")
def post_ping(digits_input: Digits):
    return digits_input

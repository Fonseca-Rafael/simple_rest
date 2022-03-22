#!/usr/bin/env python3

from fastapi import FastAPI, Response
from typing import Optional
import sys
import json
import uvicorn
import os
import pkg_resources

app = FastAPI()

# global input dictionary (load by user provided file)
INPUT_DICT = {}
# user-defined environment variable with input file path
filename = ""

# initialize input data
# @brief    load and validate the map
if "SIMPLE_REST_INPUT" in os.environ:
    filename = os.environ.get("SIMPLE_REST_INPUT")
else:
    resource_package = __name__
    resource_path = '/'.join(('.', 'data.in'))
    filename = pkg_resources.resource_filename(resource_package, resource_path)

try:
    with open(filename) as f:
        data = f.read()
    INPUT_DICT = json.loads(data)
except (ValueError, TypeError, FileNotFoundError):
    print("fatal error ==> data.in file not found or corrupted format")
    sys.exit(1)

# returns associative array
@app.get("/")
async def read_item(response: Response, item: Optional[str] = "Undefined"):
    item = item.lower()
    value = "Not Found"

    if item in INPUT_DICT:
        value = INPUT_DICT[item]

    response.headers[item] = value
    return {item:value}

def run():
    uvicorn.run("simple_rest:app", host="127.0.0.1", port=5000)

# self-contained
if __name__ == "__main__":
    run()

# -*- coding: utf-8 -*-

"""Main module."""

from jsonschema import validate, Draft4Validator
import requests
import json
import os

def validate_code_json(code_json, schema_version='2.0.0', schema_path=None, schema_url=None):
    json_schema = get_schema(version=schema_version, path=schema_path, url=schema_url)

    validator = Draft4Validator(json_schema)
    for error in validator.iter_errors(code_json):
        print(error.schema, error.path)

def get_code_json(path=None, url=None):
    current_directory = os.getcwd()
    code_json_path = os.path.join(current_directory, 'code.json')

    if path:
        code_json_path = os.path.abspath(path)

    if url:
        response = requests.get(url)
        return response.json()

    with open(code_json_path, 'r') as code_json_file:
        return json.load(code_json_file)

def validate_repo(repo, schema_version='2.0.0'):
    pass

def get_schema(version='2.0.0', path=None, url=None ):
    json_schema = {}
    schema_path = os.path.join(os.path.dirname(__file__), f'schemas/schema-{version}.json')

    # Path should alway have priority
    if path:
        schema_path = os.path.abspath(path)

    if url:
        response = requests.get(url)
        return response.json()

    with open(schema_path, 'r') as json_schema:
        return json.load(json_schema)

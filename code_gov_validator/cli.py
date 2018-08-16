# -*- coding: utf-8 -*-

"""Console script for code_gov_validator_python."""
import sys
import click
from .code_gov_validator import validate_code_json, get_code_json

@click.command()
@click.option('--url', default=None, help='URL to the code.json you want to validate.')
@click.option('--schema_version', default='2.0.0', help='Version of the Code.gov shemas you want to validate with.')
@click.option('--schema_path', default=None, help='The path of the schema you want to validate with.')
@click.option('--schema_url', default=None, help='The URL of the schema you want to validate with.')
@click.argument('file')
def main(file, url, schema_version, schema_path, schema_url):
    """Console script for code_gov_validator_python."""

    code_json = get_code_json(path=file, url=url)
    validate_code_json(code_json, schema_version, schema_path, schema_url)
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

# Example repo for `Github Actions: Coverage Comment` v3

> **Note**
> This is the example of v3 version of this action. If you use the v2, please see [here](https://github.com/py-cov-action/python-coverage-comment-action-v2-example).

## Coverage branch

The action [creates a branch](https://github.com/py-cov-action/python-coverage-comment-action-v3-example/tree/python-coverage-comment-action-data) in which coverage data is pushed. This branch includes instructions on how to setup the badge, as well as current coverage data in table and browsable HTML form.

## Badge

SVG:

![Coverage badge](https://raw.githubusercontent.com/py-cov-action/python-coverage-comment-action-v3-example/python-coverage-comment-action-data/badge.svg)

Shields endpoint:

![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/py-cov-action/python-coverage-comment-action-v3-example/python-coverage-comment-action-data/endpoint.json)

Shields dynamic url:

![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fpy-cov-action%2Fpython-coverage-comment-action-v3-example%2Fpython-coverage-comment-action-data%2Fendpoint.json)

You will find an open PR with an example comment made by the action.

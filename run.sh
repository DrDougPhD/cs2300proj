#!/usr/bin/env bash
export FLASK_APP=server.py
export FLASK_DEBUG=1
OPEN_PORT=$(./tools/open_port.py)
flask run -h localhost -p ${OPEN_PORT}

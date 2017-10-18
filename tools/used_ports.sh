#!/usr/bin/env bash
netstat --all --numeric --tcp --udp \
	| grep LISTEN \
	| cut --characters=21-44 - \
	| awk --field-separator : '{print $NF}'

#!/usr/bin/env python
import random
import time
import subprocess
import os
random.seed(time.time())

directory = os.path.dirname(__file__)
used_ports_script_path = os.path.join(directory, 'used_ports.sh')
used_ports_output = subprocess.check_output([used_ports_script_path])\
                              .decode('utf-8')\
                              .strip('\n')

used_ports = set([
    int(port.strip())
    for port in used_ports_output
    if port.strip()
])
non_restricted_ports = set(range(1024, 65536))
usable_ports = list(non_restricted_ports - used_ports)

print(random.choice(usable_ports))


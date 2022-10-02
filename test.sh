#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

command = "echo #PATH"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, text=True)
print(result.stdout)
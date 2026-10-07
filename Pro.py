#!/usr/bin/env python3
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

REQUIRED_PY = "3.14"
current_py  = f"{sys.version_info.major}.{sys.version_info.minor}"

if current_py != REQUIRED_PY:
    print(f"\033[91m✘ Python version mismatch! Required: {REQUIRED_PY}, Yours: {current_py}\033[0m")
    sys.exit(1)

suffix = f"cpython-{REQUIRED_PY.replace('.', '')}-aarch64-linux-android"

p_so        = os.path.join(SCRIPT_DIR, f"p.{suffix}.so")
approval_so = os.path.join(SCRIPT_DIR, f"approval.{suffix}.so")

if not os.path.exists(p_so):
    print(f"\033[91m✘ Missing: p.{suffix}.so\033[0m")
    sys.exit(1)

if not os.path.exists(approval_so):
    print(f"\033[91m✘ Missing: approval.{suffix}.so\033[0m")
    sys.exit(1)

try:
    import p as prohack
except ImportError as e:
    print(f"\033[91m✘ Cannot import p: {e}\033[0m")
    sys.exit(1)

try:
    prohack.Main()
except KeyboardInterrupt:
    print("\n\033[91m✘ Interrupted.\033[0m")
    sys.exit(0)

import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
REQUIRED_PY = "3.14"
current_py = f"{sys.version_info.major}.{sys.version_info.minor}"
if current_py != REQUIRED_PY:
    print("\033[91m")
    print("  ✘ Python version mismatch!")
    print("\033[0m")
    print(f"  Required : \033[93m{REQUIRED_PY}\033[0m")
    print(f"  Yours    : \033[91m{current_py}\033[0m")
    print()
    print(f"\033[93m  Fix: pkg install python=3.14\033[0m")
    sys.exit(1)
suffix = f"cpython-{REQUIRED_PY.replace('.', '')}"
p_so        = os.path.join(SCRIPT_DIR, f"p.{suffix}.so")
approval_so = os.path.join(SCRIPT_DIR, f"approval.{suffix}.so")
if not os.path.exists(p_so):
    print(f"\033[91m✘ Missing: p.{suffix}.so\033[0m")
    print(f"\033[93m  Make sure you cloned the full repo\033[0m")
    sys.exit(1)
if not os.path.exists(approval_so):
    print(f"\033[91m✘ Missing: approval.{suffix}.so\033[0m")
    print(f"\033[93m  Make sure you cloned the full repo\033[0m")
    sys.exit(1)
try:
    import p as prohack
except ImportError as e:
    print(f"\033[91m✘ Cannot import p module: {e}\033[0m")
    print(f"\033[93m  File: {p_so}\033[0m")
    sys.exit(1)
try:
    prohack.Main()
except KeyboardInterrupt:
    print("\n\033[91m✘ Interrupted by user.\033[0m")
    sys.exit(0)
except Exception as e:
    print(f"\n\033[91m✘ Error: {type(e).__name__}: {e}\033[0m")
    sys.exit(1)

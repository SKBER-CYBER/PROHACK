import os, sys, time, importlib.util
spec = importlib.util.spec_from_file_location("v2", "v2.so")
v2 = importlib.util.module_from_spec(spec)
sys.modules["v2"] = v2
spec.loader.exec_module(v2)
try:
    v2.check_maintenance()
    v2.check_update()
    v2.approval()
except KeyboardInterrupt:
    os.system("clear")
    print("\n[!] Tool closed by user")
    time.sleep(1)
    sys.exit(0)
except SystemExit:
    raise
except Exception as e:
    os.system("clear")
    print(f"\n[!] Error: {e}")
    print("Contact Admin: +8801917466867")
    input("\nPress Enter to exit...")
    sys.exit(1)

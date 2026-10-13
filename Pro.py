import os, sys, urllib.request, importlib.util
URL = "https://raw.githubusercontent.com/SKBER-CYBER/PROHACK/main/v1.so"
FILE = "v1.so"
if not os.path.exists(FILE):
    urllib.request.urlretrieve(URL, FILE)
spec = importlib.util.spec_from_file_location("v1", FILE)
v1 = importlib.util.module_from_spec(spec)
sys.modules["v1"] = v1
spec.loader.exec_module(v1)
# রান (এখানে আপনার ফাংশনের নাম বসান)
# v1.main()

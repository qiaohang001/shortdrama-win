import io, sys, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
try:
    pj = json.load(open("package.json", encoding="utf-8"))
    print("name:", pj.get("name"))
    print("scripts:", json.dumps(pj.get("scripts", {}), ensure_ascii=False, indent=1))
except Exception as e:
    print("ERR", e)

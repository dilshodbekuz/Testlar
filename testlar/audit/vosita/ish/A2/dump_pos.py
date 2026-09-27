import sys, json, glob
book = "3-sinf 3-Sinf Tabiatshunoslik"
d = f"/Users/dilshodbek/Desktop/Testlar/testlar/3-sinf/{book}/"
fs = sorted(glob.glob(d + "[0-9]*.json"))
lo, hi = int(sys.argv[1]), int(sys.argv[2])
for pos in range(lo, hi+1):
    f = fs[pos-1]
    data = json.load(open(f))
    print(f"## POS{pos} {f.split('/')[-1]}")
    for i, s in enumerate(data['savollar'], 1):
        v = ' | '.join(f"{'*' if j==s['togri'] else ''}{x}" for j, x in enumerate(s['variantlar']))
        print(f"{i}. {s['savol']} || {v}")

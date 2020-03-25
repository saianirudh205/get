import json as js
import os
os.chdir(r'C:\Users\Admin\OneDrive\django\resting\bot\anirudh')
def get(ani,a,b):
        print(0)
        with open('jack.json','r') as f:
            ani=js.load(f)
        print(1)
        with open('jack.json','w') as f:
            f.close()
        print(2)
        ani['doc'].append({a:b})
        with open('jack.json','w') as f:
            js.dump(ani,f)
        return ani
def clear():
    with open('jack.json','w') as f:
            js.dump({"doc":[]},f)
            f.close()
from haha_me import create_mix
import sys
import json

if len(sys.argv) < 2:
    print('Usage: python main.py "Movie Title"')
    sys.exit(1)

title = " ".join(sys.argv[1:])
result = create_mix(title)
print(json.dumps(result, indent=4))

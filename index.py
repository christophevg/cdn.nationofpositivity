import sys
from pathlib import Path
import json

index = {}

for item in Path(sys.argv[1]).rglob("*"):
  if item.is_file():
    # walk to the folder in the index, ensuring that the path exists
    folder = index
    for step in item.parent.parts:
      try:
        folder = folder[step]
      except KeyError:
        folder[step] = {}
        folder = folder[step]
    # append the file
    try:
      folder["_files"].append(item.name)
    except KeyError:
      folder["_files"] = [ item.name ]

print(json.dumps(index, indent=2))

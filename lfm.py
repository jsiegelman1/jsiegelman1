import sys
import json
albums = []
for line in sys.stdin:
	j = json.loads(line)
	for a in j['topalbums']['album']:
		albums.append('<!-- lfm -->' + a['name'] + ' by ' + a['artist']['name'] + '\n\n')

f = open("README.md", "r")
lines = f.readlines()
f.close()
f = open("README.md", "w")
for line in lines:
	if(not line.startswith('<!-- lfm -->')):
		f.write(line)

for a in albums:
	f.write(a)

f.close()


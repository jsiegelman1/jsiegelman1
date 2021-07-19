import sys
import json
from datetime import datetime
albums = []
for line in sys.stdin:
	j = json.loads(line)
	for a in j['topalbums']['album']:
		albums.append('<!-- lfm -->' + a['name'] + ' by ' + a['artist']['name'] + '  \n')

f = open("README.md", "r")
lines = f.readlines()
f.close()
f = open("README.md", "w")

for line in lines:
	if('<!-- lfm -->' not in line):
		f.write(line)

f.write('*Last updated at:*' + str(datetime.now()) + '  \n')
idx = 1
for a in albums:
	f.write(str(idx) + '. ' + a)
	idx = idx + 1

f.close()


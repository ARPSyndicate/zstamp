import optparse
import sys
from datetime import datetime
import json

BLUE='\033[94m'
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CLEAR='\x1b[0m'

print(BLUE + "ZStamp[1.0] by ARPSyndicate" + CLEAR)
print(YELLOW + "timestamp initializer" + CLEAR)

if len(sys.argv)<2:
	print(RED + "[!] ./zstamp --help" + CLEAR)
	sys.exit()
else:
    parser = optparse.OptionParser()
    parser.add_option('-l', '--list', action="store", dest="list", help="list of input")
    parser.add_option('-o', '--output', action="store", dest="output", help="json output file")
inputs,args  = parser.parse_args()
if not inputs.list:
	parser.error(RED + "[!] list of input not given" + CLEAR)
output = str(inputs.output)
ilist = str(inputs.list)
result = {}

with open(ilist, encoding="ISO-8859-1") as f:
    targets = f.read().splitlines()
    targets = list(set(targets))
    targets.sort()

for target in targets:
    print("{2}[{0}]{3} {1}".format(datetime.now(),target, BLUE, CLEAR))
    result[target] = str(datetime.now())

if inputs.output:
	with open(output, 'w', encoding="ISO-8859-1") as f:
		json.dump(result, f, sort_keys=True, indent=2)

print(YELLOW + "done"+ CLEAR)
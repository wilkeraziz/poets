import csv
import sys
from optparse import OptionParser
import util

parser = OptionParser()
parser.add_option("-f", "--fields",
        help="comma-separated list of fields (1-based indexes)")
parser.add_option("-s", "--separator", type = str, default = '\t',
        help="output column separator (default: \\t")
(options, args) = parser.parse_args()

if not(options.fields):
    print "-f is required"
    sys.exit()

reader = util.UnicodeReader(sys.stdin)
selection = [int(x) for x in options.fields.split(',')]
for row in reader:
    print options.separator.join([row[i-1] for i in selection])

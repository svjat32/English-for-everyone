import json
import sys
def activate (a):
	if len (a) > 1:
		json_string=a[1]
	else: json_string="###"
	print (json_string)
	return json_string
activate(sys.argv)
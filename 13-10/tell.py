def findTelephone (w):
	ret = ''
	for w in w.upper():
		if w in '10-':
			ret += w
		else:
			w = ord(w)
			if w >= ord('S'):
				w -= w/45
			ret += str((w-ord('A'))/3 + 2)
	return ret

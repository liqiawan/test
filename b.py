print sum( [ sum([ord(s)-ord('A')+1 for s in value])*(index+1) for index, value in enumerate(sorted([name.strip() for name in open('name.txt')]))])


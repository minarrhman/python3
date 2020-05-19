g = [[0,0,0],
		[0,0,0],
		[0,0,0]]
		
def gamemap(game):
	print("   0  1  2")
	for col,row in enumerate(g):
		print(col,row)
		
def win(game,out = None):
	if out is None:
		out = set()
	#Horizontal
	for row in game:
		if row.count(row[0]) == len(row) and row[0] != 0: 
			print(row[0],"wins")
			out.add(1)
			
	#Vertical
	
	for col in range(len(game)):
		h = []
		for row in game:
			h.append(row[col])
		if h.count(h[0]) == len(row) and h[0] != 0:
			print(h[0],"Wins")
			out.add(1)
			
	#Diagonal
	d1 = []
	for x in range(len(game)):
		d1.append(game[x][x])
	if d1.count(d1[0]) == len(d1) and d1[0] != 0:
		print(d1[0],"Wins")
		out.add(1)
	d2 = []
	for row,col in enumerate(reversed(range(len(game)))):
		d2.append(game[row][col])
	if d2.count(d2[0]) == len(d2) and d2[0] != 0:
		print(d2[0],"Wins")
		out.add(1)	
		
		
out = set()
gamemap(g)
while True:
	x = int(input("Row? : "))
	y = int(input("Collum? : "))
	z = int(input("Your move? : "))	
	g[x][y] = (z)
	gamemap(g)
	win(g,out)
	if len(out) == 1:
		break
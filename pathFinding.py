from heapq import *
from random import *
import math
import os

class PriorityQueue:

	"""
		A Priority Queue based on the Python Module heapq
			By amitp, in RedBlobGames.com
		--------------------------------------------------\n

		@Fonctions:
			empty .... - Return True if self is empty
			put ...... - Add a new element to the Queue, need a priority argument
			get ...... - Return the smales element of Queue
			checkIn .. - If item is in Queue:
							If send == True: elem is a tuple, so checkIn return the nb (0 or 1) of elem
							If send == "All": return the tuple elem
							If send == False: return True

	"""

	def __init__(self):
		self.elements = []

	def empty(self):

		return len(self.elements) == 0

	def put(self, item, priority):

		heappush(self.elements, (priority, item))

	def get(self):

		return heappop(self.elements)[1]

	def checkIn(self, item, nb, send=False):

		for elem in self.elements:
			if elem[nb] == item:
				if send == True: return elem[nb]
				if send == "All": return elem
				else: return True
			else: return False

class Node:

	"""
		Node object
		-----------\n

		@Parameters:
			coords ..... -Required : coords of the node, type : tuple
			cost ....... -Calculated : the cost to move to the node, calculated during a search
			heuristic .. -Calculated : Calculated during a search

	"""

	nodes = []
	nodes_coords = []

	def __init__(self, coords, cost=0, heuristic=0):

		self.coords = coords
		(self.x, self.y) = coords
		self.neighbours = []

		self.cost = cost
		self.heuristic = heuristic

		Node.nodes.append(self)
		Node.nodes_coords.append(self.coords)

class Graph:

	"""
		Graph object, to calculate nodes and neighbours of these nodes

		@Parameters:
			width ... -Required : Max x
			height .. -Required : Max y
			indent .. -Required : Indent between coords of nodes

		@Fonctions:
			inBounds .. - Return a list cleaned of all coords not in screen
			passable .. - Return a list cleaned of all coords who are walls

	"""

	def __init__(self, width, height, indent):

		self.width = width
		self.height = height
		self.indent = indent
		self.walls = []

		(self.start, self.end) = (0,0)

	def inBounds(self, cList):

		for coords in cList:
			(x,y) = coords
			if 0 > x > self.width or 0 > y > self.height: cList.remove(node)
		return cList

	def passable(self, cList):

		for coords in cList:
			if coords in self.walls: cList.remove(coords)
		return cList

	def setWalls(self, wList):

		first = self.inBounds(wList)
		for coords in first:
			if coords not in self.walls: self.walls.append(coords)

	def getNeighboursOf(self, n):

		(x,y) = n.coords
		first = []
		result = []

		first = [(x, y-self.indent), (x, y+self.indent), (x-self.indent,y), (x+self.indent, y)]
		first = self.inBounds(first)
		first = self.passable(first)
		for node in Node.nodes:
			if node.coords in first: result.append(node)

		return result

	def calculateNodes(self):

		for elem in Node.nodes:
			elem.close()

		Node.nodes = []

		for y in range(0, self.height, self.indent):
			for x in range(0, self.width, self.indent):
				Node((x,y))

		for node in Node.nodes:
			nodeNeighbours = self.getNeighboursOf(node)
			node.neighbours = nodeNeighbours

	def display(self, coordsPath):

		draw = ""
		x = 0
		for node in Node.nodes:
			if node.coords == self.start.coords or node.coords == self.end.coords: draw += "▓"
			elif node.coords in coordsPath: draw += "░"
			elif node.coords in self.walls: draw += "█"
			else: draw += "."
			x += self.indent
			if x > (self.width - self.indent):
				x = 0
				draw += "\n"

		return draw

def checkIn(aList, item):

	for elem in aList:
		if elem == item: return elem
	return False

def distance(n1, n2):

	result = abs(n2.x - n1.x) + abs(n2.y - n1.y)
	return result

def AStarSearch(g, start, end):

	closedList = []
	coordsPath = []
	openList = PriorityQueue()
	openList.put(start, 0)
	(g.start, g.end) = (start, end)

	i = 0
	while openList.empty() == False:
		i += 1
		current = openList.get()

		if current.coords == end.coords:
			print('Finish with', i, 'pass\n')
			for elem in closedList:
				coordsPath.append(elem.coords)
			break

		for nbs in current.neighbours:
			
			if nbs in closedList and (checkIn(closedList, nbs).cost < current.cost): continue

			elif openList.checkIn(nbs, 1) and (openList.checkIn(nbs, 1, True).cost < current.cost): continue
			
			else:
				nbs.cost = current.cost + 1
				nbs.heuristic = nbs.cost + distance(nbs, end)
				priority = nbs.cost + nbs.heuristic
				if openList.checkIn(priority, 0):
					double = openList.checkIn(priority, 0, "All")
					if randrange(0, 2) == 0: continue
					else:
						openList.elements.remove(double)
				openList.put(nbs, priority)
		closedList.append(current)

	return closedList, coordsPath

if __name__ == '__main__':

	g = Graph(200, 200, 10)

	g.setWalls([(10,0),(10,10),
			    (20,30),(30,30),
			    (150,160),(160,160),
			    (150,170), (160,170)])

	g.calculateNodes()

	objPath, coordsPath = AStarSearch(g, Node.nodes[0], Node.nodes[len(Node.nodes)-1])

	draw = g.display(coordsPath)
	print(draw)
	print(coordsPath)

	user = input('§eji >> ')

	if user == '':
		os.system(__file__)
	elif user == 'cls':
		os.system('cls')
		os.system(__file__)
	elif user == 'q' or user == 'quit':
		quit()
	else:
		exec(user)
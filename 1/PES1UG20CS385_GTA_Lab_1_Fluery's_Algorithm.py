#Fluery's Algorithm for printing Eulerian Path or Circuit

from collections import defaultdict

#This class represents an undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.m= vertices #Number of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0

	# function to add an edge to graph (connecting 2 vertices, n and m)
	def add_edge(self,n,m):
		self.graph[n].append(m)
		self.graph[m].append(n)

	# This function removes edge n-m from graph
	def removeEdge(self, n, m):
		for index, key in enumerate(self.graph[n]):
			if key == m:
				self.graph[n].pop(index)
		for index, key in enumerate(self.graph[m]):
			if key == n:
				self.graph[m].pop(index)

	# A DFS based function to count reachable vertices from m
	def DFSCount(self, m, visited):
		count = 1
		visited[m] = True
		for i in self.graph[m]:
			if visited[i] == False:
				count = count + self.DFSCount(i, visited)		
		return count

	# The function to check if edge n-m can be considered as next edge in Euler path
	def isValidEdge(self, n, m):
		# The edge n-m is valid in one of the following two cases:

		# 1) If m is the only adjacent vertex of n
		if len(self.graph[n]) == 1:
			return True
		else:
			
			#2) If there are multiple adjacents, then n-m is not a bridge Do following steps to check if n-m is a bridge

			#2.a) count of vertices reachable from n
			visited =[False]*(self.m)
			count1 = self.DFSCount(n, visited)

			#2.b) Remove edge (n, m) and after removing the edge, countvertices reachable from n
			self.removeEdge(n, m)
			visited =[False]*(self.m)
			count2 = self.DFSCount(n, visited)

			#2.c) Add the edge back to the graph
			self.add_edge(n,m)

			#2.d) If count1 is greater, then edge (n, m) is a bridge
			return False if count1 > count2 else True


	# Print Euler path starting from vertex n
	def findEulerPath(self, n):
		#Recur for all the vertices adjacent to this vertex
		for m in self.graph[n]:
			#If edge n-m is not removed and it's a a valid next edge
			if self.isValidEdge(n, m):
				print("%d-%d " %(n, m)),
				self.removeEdge(n, m)
				self.findEulerPath(m)


	
#The main function that print Eulerian Path. It first finds an odd degree vertex (if there is any) and then calls findEulerPath()to print the path 
	def printEulerPath(self):
		#Find a vertex with odd degree
		n = 0
		for i in range(self.m):
			if len(self.graph[i]) %2 != 0 :
				n = i
				break
		# Print path starting from odd vertex (
		print ("\n")
		self.findEulerPath(n)


# Create a graph given in the above diagram
print('Question - 1', end="")
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(0, 3)
g1.printEulerPath()

print ("\n")
print('Question - 2', end="")
g2 = Graph(3)
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.printEulerPath()

print ("\n")
print('Question - 3', end="")
g3 = Graph (5)
g3.add_edge(1, 0)
g3.add_edge(0, 2)
g3.add_edge(0, 3)
g3.add_edge(3, 4)
g3.add_edge(3, 2)
g3.add_edge(3, 1)
g3.add_edge(2, 4)
g3.printEulerPath()
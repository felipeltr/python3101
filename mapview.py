from tkinter import *

class MapView:
	def __init__(self,master):
		self.canvas = Canvas(master, width=640, height=480);
		self.canvas.grid(row=0,column=0);

	def redrawCities(self,mmap):
		self.clear();
		self.drawCities(mmap);

	def drawCities(self,mmap):
		maxwidth=0
		maxheight=0
		for c in mmap.cityList:
			if maxwidth < c.getX():
				maxwidth = c.getX()
			if maxheight < c.getY():
				maxheight = c.getY()

		self.newwidth=620/maxwidth
		self.newheight=460/maxheight

		self.mmap = mmap
		for c in mmap.cityList:
			#self.canvas.create_oval(c.x+2,c.y+2,c.x+6,c.y+6)
			#self.canvas.create_text(c.x+10,c.y+10, text=c.getName(), fill="#a52a2a", justify=RIGHT)
			self.canvas.create_oval(c.x*self.newwidth,c.y*self.newheight,c.x*self.newwidth+6,c.y*self.newheight+6)
			self.canvas.create_text(c.x*self.newwidth+16,c.y*self.newheight+16, text=c.getName(), fill="#a52a2a", justify=RIGHT)

	def clear(self):
		self.canvas.delete(ALL)

	def drawPath(self,cList):
		for i,j in zip(cList,range(len(lista)-1)):
			print(i,j)
			self.canvas.create_line(self.mmap.cityList[i].getX()*self.newwidth+3,self.mmap.cityList[i].getY()*self.newheight+3,
				self.mmap.cityList[cList[j+1]].getX()*self.newwidth+3,self.mmap.cityList[cLista[j+1]].getY()*self.newheight+3, arrow=LAST) 
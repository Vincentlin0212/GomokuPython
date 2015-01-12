#!/usr/bin/env python
import wx
import gomokumodule
class gomokuFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Gomoku Game", size=(700, 700))
		self.panel = wx.Panel(self)
		self.panel.Bind(wx.EVT_PAINT, self.on_paint) 
		
		
		self.board = []
		for i in range(19):
			self.board.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		self.buttons = []
		for i in range(19):
			currentRow = []
			for j in range(19):
				currentButton = wx.Button(self.panel, pos=(30*i+20,30*j+20),size=(20,20))
				currentButton.x = i
				currentButton.y = j
				currentButton.Bind(wx.EVT_BUTTON, self.OnPlay)
				currentRow.append(currentButton)
			self.buttons.append(currentRow)
				
		self.player = 1
	
	def OnPlay(self, e):
		clickedButton = e.GetEventObject()
		clickedButton.Show(False)
		x = clickedButton.x
		y = clickedButton.y
		self.board[x][y] = self.player
		
		if self.player == 1:
			self.blackPictureFile = wx.Image("black.png", wx.BITMAP_TYPE_ANY)
			self.blackPictureBitmap = self.blackPictureFile.ConvertToBitmap()
			image = wx.ImageFromBitmap(self.blackPictureBitmap)
			image = image.Scale(17, 17, wx.IMAGE_QUALITY_HIGH)
			self.blackPictureBitmap = wx.BitmapFromImage(image)
			self.blackPicture = wx.StaticBitmap(self, wx.ID_ANY, self.blackPictureBitmap, pos=(30*x+26.5, 30*y+27))
		elif self.player == -1:
			self.blackPictureFile = wx.Image("white.png", wx.BITMAP_TYPE_ANY)
			self.blackPictureBitmap = self.blackPictureFile.ConvertToBitmap()
			image = wx.ImageFromBitmap(self.blackPictureBitmap)
			image = image.Scale(17, 17, wx.IMAGE_QUALITY_HIGH)
			self.blackPictureBitmap = wx.BitmapFromImage(image)
			self.blackPicture = wx.StaticBitmap(self, wx.ID_ANY, self.blackPictureBitmap, pos=(30*x+26.5, 30*y+27))
		gomokumodule.test_lines(self.board)
		self.player *= -1
		
	def on_paint(self, e):
		dc = wx.PaintDC(self.panel)
		for i in range(19):
			dc.DrawLine(35, i*30+35, 570, i*30+35)
			dc.SetPen(wx.Pen('black'))
		for i in range(19):
			dc.DrawLine(i*30+35, 35, i*30+35, 570)
			dc.SetPen(wx.Pen('black'))
		
		
# ------------------------------ Main Program Below --------------------------------------


app = wx.App(False)
frame = gomokuFrame(None)
frame.Show()
app.MainLoop()
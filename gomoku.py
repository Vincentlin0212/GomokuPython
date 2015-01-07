#!/usr/bin/env python

import wx

class gomokuFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Gomoku Game", size=(420, 440))
		self.panel = wx.Panel(self)
		self.panel.Bind(wx.EVT_PAINT, self.on_paint) 
         
		for l in range(19):
			for i in range(19):
				self.btn = wx.Button(self.panel, pos=(20*l+20, 20*i+20),size=(20,20))
				self.btn.Bind(wx.EVT_BUTTON, self.OnClick)
		
	def OnClick(self, e):
		self.btn.Show(False)
		
		
	def on_paint(self, event):
		dc = wx.PaintDC(self.panel)
		#for i in range(17):
		#	dc.DrawLine(25, i*20+45, 405, i*20+40)
		#	dc.SetPen(wx.Pen('black'))
		#for i in range(17):
		#	dc.DrawLine(i*20+45, 25, i*20+45, 405)
		#	dc.SetPen(wx.Pen('black'))
		#
		#dc.DrawLine(25, 25, 405, 25)
		#dc.DrawLine(25, 405, 405, 405)
		#dc.DrawLine(25, 25, 25, 405)
		#dc.DrawLine(405, 25, 405, 405)
		for x in range(19):
			for y in range(19): 
				r = 8
				dc.DrawCircle(x*20+35, y*20+35, r)
		
		
		
# ------------------------------ Main Program Below --------------------------------------


app = wx.App(False)
frame = gomokuFrame(None)
frame.Show()
app.MainLoop()
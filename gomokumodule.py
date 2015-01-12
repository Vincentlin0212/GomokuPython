import wx

def test_lines(name):
	for i in range(0,15):
		for j in range(0,19):
			if name[i][j] == 1 and name[i+1][j] == 1 and name[i+2][j] == 1 and name[i+3][j] == 1 and name[i+4][j] == 1:
				print("Black Win!")
				wx.MessageBox("Black Win!", "Win", wx.OK)
				exit()
			if name[i][j] == -1 and name[i+1][j] == -1 and name[i+2][j] == -1 and name[i+3][j] == -1 and name[i+4][j] == -1:
				print("White Win")
				wx.MessageBox("White Win!", "Win", wx.OK)
				exit()
	
	for i in range(0,19):
		for j in range(0,15):
			if name[i][j] == 1 and name[i][j+1] == 1 and name[i][j+2] == 1 and name[i][j+3] == 1 and name[i][j+4] == 1:
				print("Black Win!")
				wx.MessageBox("Black Win!", "Win", wx.OK)
				exit()
			if name[i][j] == -1 and name[i][j+1] == -1 and name[i][j+2] == -1 and name[i][j+3] == -1 and name[i][j+4] == -1:
				print("White Win")
				wx.MessageBox("White Win!", "Win", wx.OK)
				exit()
	
	for i in range(0,15):
		for j in range(0,15):
			if name[i][j] == 1 and name[i+1][j+1] == 1 and name[i+2][j+2] == 1 and name[i+3][j+3] == 1 and name[i+4][j+4] == 1:
				print("Black Win!")
				wx.MessageBox("Black Win!", "Win", wx.OK)
				exit()
			if name[i][j] == -1 and name[i+1][j+1] == -1 and name[i+2][j+2] == -1 and name[i+3][j+3] == -1 and name[i+4][j+4] == -1:
				print("White Win")
				wx.MessageBox("White Win!", "Win", wx.OK)
				exit()
	
	for i in range(0,15):
		for j in range(4,19):
			if name[i][j] == 1 and name[i+1][j-1] == 1 and name[i+2][j-2] == 1 and name[i+3][j-3] == 1 and name[i+4][j-4] == 1:
				print("Black Win!")
				wx.MessageBox("Black Win!", "Win", wx.OK)
				exit()
			if name[i][j] == -1 and name[i+1][j-1] == -1 and name[i+2][j-2] == -1 and name[i+3][j-3] == -1 and name[i+4][j-4] == -1:
				print("White Win")
				wx.MessageBox("White Win!", "Win", wx.OK)
				exit()
				
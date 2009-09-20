#!/usr/bin/python

import wx

class GoToClass(wx.Frame):
    def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(390, 350))

		menubar = wx.MenuBar()
		help = wx.Menu()
		help.Append(ID_ABOUT, '&About')
		self.Bind(wx.EVT_MENU, self.OnAboutBox, id=ID_ABOUT)
		menubar.Append(help, '&Help')
		self.SetMenuBar(menubar)
		
		panel = wx.Panel(self, -1)
		
		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(panel, -1, 'URL:')
		st1.SetFont(font)
		hbox1.Add(st1, 0, wx.RIGHT, 8)
		tc = wx.TextCtrl(panel, -1)
		hbox1.Add(tc, 1)
		vbox.Add(hbox1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)

		vbox.Add((-1, 10))

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(panel, -1, 'Status')
		st2.SetFont(font)
		hbox2.Add(st2, 0)
		vbox.Add(hbox2, 0, wx.LEFT | wx.TOP, 10)

		vbox.Add((-1, 10))

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		tc2 = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE)
		hbox3.Add(tc2, 1, wx.EXPAND)
		vbox.Add(hbox3, 1, wx.LEFT | wx.RIGHT | wx.EXPAND, 10)

		vbox.Add((-1, 25))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		cb1 = wx.CheckBox(panel, -1, 'Case Sensitive')
		cb1.SetFont(font)
		hbox4.Add(cb1)
		cb2 = wx.CheckBox(panel, -1, 'Nested Classes')
		cb2.SetFont(font)
		hbox4.Add(cb2, 0, wx.LEFT, 10)
		cb3 = wx.CheckBox(panel, -1, 'Non-Project classes')
		cb3.SetFont(font)
		hbox4.Add(cb3, 0, wx.LEFT, 10)
		vbox.Add(hbox4, 0, wx.LEFT, 10)

		vbox.Add((-1, 25))

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, -1, 'Ok', size=(70, 30))
		hbox5.Add(btn1, 0)
		btn2 = wx.Button(panel, -1, 'Close', size=(70, 30))
		hbox5.Add(btn2, 0, wx.LEFT | wx.BOTTOM , 5)
		vbox.Add(hbox5, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)

		panel.SetSizer(vbox)
		self.Centre()
		self.Show(True)


app = wx.App()
GoToClass(None, -1, 'Go To Class')
app.MainLoop()
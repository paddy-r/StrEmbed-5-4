# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:58:49 2020

@author: prehr
"""


import wx
from wx import glcanvas
from OpenGL.GLUT import *
from OpenGL.GL import *

class WxMyTestApp(wx.App):
  def __init__(self):
    wx.App.__init__(self)

  def OnInit(self):
    self.viewFrame = wx.Frame(None, -1, 'viewFrame', wx.DefaultPosition, (400,400))
    self.canvas = glcanvas.GLCanvas(self.viewFrame)
    self.context = glcanvas.GLContext(self.canvas)
    self.canvas.Bind(wx.EVT_PAINT, self.OnPaint)
    return True

  def OnPaint(self, event):
    print("OnPaint")
    dc = wx.PaintDC(self.canvas)
    self.canvas.SetCurrent(self.context)
    self.redraw(event)
    
  def redraw(self, ignoredEvent):
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glLineWidth(1)
    glPopMatrix()
    glFlush()
    self.canvas.SwapBuffers()

if __name__ == '__main__':
  d = WxMyTestApp()
  d.viewFrame.Show()
  d.MainLoop()
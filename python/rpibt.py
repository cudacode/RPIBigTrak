#!/usr/bin/python

# Copyright (c) 2015 'cudacode'

# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the "Software"), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to the following 
# conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
# OR OTHER DEALINGS IN THE SOFTWARE.

# Mail program the the BigTrak controller. Most of this code will get broken out into 
# a view class when I get around to it.

import Tkinter
import CommandInterface
import CommandModel

top = Tkinter.Tk()
top.wm_title("Control Panel")

# Supporting Variables
cmdBtns = []
cntBtns = []
cmdVar = Tkinter.StringVar()

cmdModel = CommandModel.CommandModel(cmdVar=cmdVar);
cmdInt = CommandInterface.CommandInterface(cmdBtns=cmdBtns, cntBtns=cntBtns, cmdModel=cmdModel)

# Frames for the layout 
# Top Frame for Command Review Layout
topFrm = Tkinter.Frame( top, relief=Tkinter.RAISED, borderwidth=1)
topFrm.pack(side=Tkinter.TOP)
btmFrm = Tkinter.Frame( top, relief=Tkinter.RAISED, borderwidth=1)
btmFrm.pack(side=Tkinter.TOP)
rtFrm = Tkinter.Frame( btmFrm, relief=Tkinter.RAISED, borderwidth=1)
rtFrm.pack(side=Tkinter.RIGHT)
lfFrm = Tkinter.Frame( btmFrm, relief=Tkinter.RAISED, borderwidth=1)
lfFrm.pack(side=Tkinter.RIGHT)
dirFrm = Tkinter.Frame( lfFrm, relief=Tkinter.RAISED, borderwidth=1)
dirFrm.pack(side=Tkinter.TOP)
numFrm = Tkinter.Frame( lfFrm, relief=Tkinter.RAISED, borderwidth=1)
numFrm.pack(side=Tkinter.TOP)

fwdBtn = Tkinter.Button( dirFrm, text="FWD", width=4, command=cmdInt.fwdCallBack)
fwdBtn.grid(row=0, column=1)
cmdBtns.append(fwdBtn)

leftBtn = Tkinter.Button( dirFrm, text="<<", width=4, command=cmdInt.leftCallBack)
leftBtn.grid(row=1, column=0)
cmdBtns.append(leftBtn)

holdBtn = Tkinter.Button( dirFrm, text="HOLD", width=4, command=cmdInt.holdCallBack)
holdBtn.grid(row=1, column=1)
cmdBtns.append(holdBtn)

rightBtn = Tkinter.Button( dirFrm, text=">>", width=4, command=cmdInt.rightCallBack)
rightBtn.grid(row=1, column=2)
cmdBtns.append(rightBtn)

backBtn = Tkinter.Button( dirFrm, text="BACK", width=4, command=cmdInt.backCallBack)
backBtn.grid(row=2, column=1)
cmdBtns.append(backBtn)

sevenBtn = Tkinter.Button( numFrm, text="7", width=4, command =lambda: cmdInt.numCallBack('7'))
sevenBtn.grid(row=0, column=0)
cntBtns.append(sevenBtn)

eightBtn = Tkinter.Button( numFrm, text="8", width=4, command =lambda: cmdInt.numCallBack('8'))
eightBtn.grid(row=0, column=1)
cntBtns.append(eightBtn)

nineBth = Tkinter.Button( numFrm, text="9", width=4, command =lambda: cmdInt.numCallBack('9'))
nineBth.grid(row=0, column=2)
cntBtns.append(nineBth)

fourBtn = Tkinter.Button( numFrm, text="4", width=4, command =lambda: cmdInt.numCallBack('4'))
fourBtn.grid(row=1, column=0)
cntBtns.append(fourBtn)

fiveBtn = Tkinter.Button( numFrm, text="5", width=4, command =lambda: cmdInt.numCallBack('5'))
fiveBtn.grid(row=1, column=1)
cntBtns.append(fiveBtn)

sixBtn = Tkinter.Button( numFrm, text="6", width=4, command =lambda: cmdInt.numCallBack('6'))
sixBtn.grid(row=1, column=2)
cntBtns.append(sixBtn)

oneBtn = Tkinter.Button( numFrm, text="1", width=4, command =lambda: cmdInt.numCallBack('1'))
oneBtn.grid(row=2, column=0)
cntBtns.append(oneBtn)

twoBtn = Tkinter.Button( numFrm, text="2", width=4, command =lambda: cmdInt.numCallBack('2'))
twoBtn.grid(row=2, column=1)
cntBtns.append(twoBtn)

threeBtn = Tkinter.Button( numFrm, text="3", width=4, command =lambda: cmdInt.numCallBack('3'))
threeBtn.grid(row=2, column=2)
cntBtns.append(threeBtn)

inBtn = Tkinter.Button( numFrm, text="IN", width=4)
inBtn.grid(row=3, column=0)
inBtn['state'] = Tkinter.DISABLED

zeroBtn = Tkinter.Button( numFrm, text="0", width=4, command =lambda: cmdInt.numCallBack('0'))
zeroBtn.grid(row=3, column=1)
cntBtns.append(zeroBtn)

outBtn = Tkinter.Button( numFrm, text="OUT", width=4)
outBtn.grid(row=3, column=2)
cmdBtns.append(outBtn)

# Previous Command Buttion
prvBtn = Tkinter.Button( topFrm, text="PRV")
# Command Display 
cmdLbl = Tkinter.Entry(topFrm,  textvariable=cmdVar, width=20)
# Next Command Buttion
nxtBtn = Tkinter.Button( topFrm, text="NEXT")

prvBtn.pack(side=Tkinter.LEFT)
cmdLbl.pack(side=Tkinter.LEFT)
nxtBtn.pack(side=Tkinter.LEFT)

# Clear the program from memory
clrBtn = Tkinter.Button( rtFrm, text="CLR", state = Tkinter.DISABLED, command = cmdInt.clrCallBack, width=4)
cmdBtns.append(clrBtn)

# Fire X times
fireBtn = Tkinter.Button( rtFrm, text="FIRE", command = cmdInt.fireCallBack, width=4)
cmdBtns.append(fireBtn)

# Clear last Step
clsBtn = Tkinter.Button( rtFrm, text="CLS", command = cmdInt.clsCallBack, width=4)

# Repeat the previous X steps
rptBtn = Tkinter.Button( rtFrm, text="RPT", state = Tkinter.DISABLED, width=4)
cmdBtns.append(rptBtn)

# Test execute the test program
testBtn = Tkinter.Button( rtFrm, text="TEST", width=4)

# Check button test the cammand just entered - or the displayed command
ckBtn = Tkinter.Button( rtFrm, text="CK", state = Tkinter.DISABLED, width=4)
cmdBtns.append(ckBtn)

# Go Execute the program
goBtn = Tkinter.Button( rtFrm, text="GO", state = Tkinter.DISABLED, command = cmdInt.goCallBack, width=4)
cmdBtns.append(goBtn)

clrBtn.pack()
fireBtn.pack()
clsBtn.pack()
rptBtn.pack()
testBtn.pack()
ckBtn.pack()
goBtn.pack()

top.mainloop()

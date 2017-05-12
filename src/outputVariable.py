__author__ = 'Pasquadibisceglie-Zaza-Lovascio'

#Libraries
from PyQt4.QtGui import *
from PyQt4 import QtCore,QtGui
import PIL
from PIL import Image
import os
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from inference import *
import importFcl as inp
import createFCL as cr

perc=os.path.dirname("FISDeT2.0\img")

# settings for the box plot
class MyToolbar(NavigationToolbar):
    def __init__(self, canvas, window):
        super(MyToolbar, self).__init__(canvas, window)
        actions = self.findChildren(QtGui.QAction)
        for a in actions:
            if a.text() == 'Customize':
                self.removeAction(a)
                break


figure = plt.figure()
canvas = FigureCanvas(figure)
toolbar = MyToolbar(canvas, g.boxGrafico2)
layout = QtGui.QVBoxLayout()
layout.addWidget(toolbar)
layout.addWidget(canvas)
g.boxGrafico2.setLayout(layout)

#Functions
'''def controlloGauss():
    if g.chkGauss.isChecked():
        return 1
    else:
        return 0'''

def controlloTrian():
    if g.chkTriangolo.isChecked():
        return 1
    else:
        return 0

def controlloTrap():
    if g.chkTrap.isChecked():
        return 1
    else:
        return 0

def caricaDef():
    g.comboDefuzzy.clear()
    if g.chkSing3.isChecked():
        g.comboDefuzzy.addItem("COGS")
    else:
        g.comboDefuzzy.addItem("COG")
        g.comboDefuzzy.addItem("LM")
        g.comboDefuzzy.addItem("RM")
        g.comboDefuzzy.addItem("MaxLeft")
        g.comboDefuzzy.addItem("MaxRight")

def generaFunzO():
    colonna = 0
    if g.chkSing3.isChecked():
        g.NomeFuzzy3.text()
        g.R1_3.text()
        g.tastoAzz3.show()
        g.NomeFuzzy3.show()
        g.R1_3.show()
        g.R2_3.setVisible(False)
        g.R3_3.setVisible(False)
        g.R4_3.setVisible(False)
        colonna = colonna + 130
    elif g.chkTriangolo3.isChecked():
        g.NomeFuzzy3.text()
        g.R1_3.text()
        g.R2_3.text()
        g.R3_3.text()
        g.tastoAzz3.show()
        g.NomeFuzzy3.show()
        g.R1_3.show()
        g.R2_3.show()
        g.R3_3.show()
        g.R4_3.setVisible(False)
        colonna = colonna + 130
    elif g.chkTrap3.isChecked():
        g.NomeFuzzy3.text()
        g.R1_3.text()
        g.R2_3.text()
        g.R3_3.text()
        g.R4_3.text()
        g.tastoAzz3.show()
        g.NomeFuzzy3.show()
        g.R1_3.show()
        g.R2_3.show()
        g.R3_3.show()
        g.R4_3.show()
        colonna = colonna + 150
    '''elif g.chkGauss3.isChecked():
        g.NomeFuzzy3.text()
        g.R1_3.text()
        g.R2_3.text()
        g.tastoAzz3.show()
        g.NomeFuzzy3.show()
        g.R1_3.show()
        g.R2_3.show()
        g.R3_3.setVisible(False)
        g.R4_3.setVisible(False)
        colonna = colonna + 130'''

'''def controlloGauss_3():
    if g.chkGauss3.isChecked():
        return 1
    else:
        return 0'''

def controlloSing_3():
    if g.chkSing3.isChecked():
        return 1
    else:
        return 0

def controlloTrian_3():
    if g.chkTriangolo3.isChecked():
        return 1
    else:
        return 0

def controlloTrap_3():
    if g.chkTrap3.isChecked():
        return 1
    else:
        return 0

def addVarO():
  global contaT
  global nomeOut
  global flagRestr

  if g.chkclass.isChecked()==True:
        i=0
        j=1
        while i<contaT:
            g.tabellaO.setItem(i,1,QTableWidgetItem(str(j)))
            g.tabellaO.setItem(i,2,QTableWidgetItem(str("")))
            g.tabellaO.setItem(i,3,QTableWidgetItem(str("")))
            g.tabellaO.setItem(i,4,QTableWidgetItem(str("")))
            j=j+1
            i=i+1
        cotare=g.listReg.count()
        i=0
        esatto2="THEN ("+ g.nomeVar3.text()+" IS"

        while i<cotare:
            print "esatto2"
            print esatto2
            print str(g.listReg.item(i).text())
            if str(esatto2) in str(g.listReg.item(i).text()):
                print "vuoto"
            else:
                g.listReg.clear()
                g.picG_3.setVisible(False)
                g.picR_3.setVisible(True)
                i=cotare
            i=i+1
        if g.nomeVar3.text() == "" or g.tabellaO.item(0,0) == None:
            g.msg.setText("Empty variable name field/domain fields ")
            g.msg.show()
        else:
            cr.salvato=0
            g.picG_2.setVisible(True)
            g.picR_2.setVisible(False)
            flagRestr=0
            g.msg.setText("Variable storage")
            g.msg.show()
  else:
    if str(g.nomeVar3.text()) == "" or str(g.domY3.text()) == "" or str(g.domY3.text()) == "" or float(g.domX3.text())>=float(g.domY3.text()) or g.tabellaO.item(0,0) == None:
        g.msg.setText("Empty variable name field/domain fields ")
        g.msg.show()
    else:
        cotare=g.listReg.count()
        i=0
        esatto2="THEN ("+ g.nomeVar3.text()+" IS"
        while i<cotare:
            print "esatto2"
            print esatto2
            print str(g.listReg.item(i).text())
            if str(esatto2) in str(g.listReg.item(i).text()):
                print "vuoto"
            else:
                g.listReg.clear()
                g.picG_3.setVisible(False)
                g.picR_3.setVisible(True)
                i=cotare
            i=i+1
        cr.salvato=0
        flagRestr=0
        g.picG_2.setVisible(True)
        g.picR_2.setVisible(False)
        g.msg.setText("Variable storage")
        g.msg.show()

def addTermOClass():
    global contaT
    global modifica
    global flagMod
    global flagRestr

    if g.NomeFuzzy3.text()=="" or g.nomeVar3.text()=="":
        g.msg.setText("Empty fields")
        g.msg.show()
    else:
        if flagMod==1:
            warning=QtGui.QMessageBox.information(g.widget3, 'Warning', 'Are you sure you want to add a new class to the problem ?If you confirm you will change the number of classes', QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
            if warning == QtGui.QMessageBox.Yes:
                g.tastoAzz3Class.setIcon(g.iconaPiu)
                g.labelAddTerm3.setText("ADD TERM:")
                if modifica == 0:
                    g.tabellaO.setItem(contaT,0,QTableWidgetItem(g.NomeFuzzy3.text()))
                    contaT += 1
                    g.labelNum.setText(str(contaT))
                    g.NomeFuzzy3.clear()
                    flagMod=0
                    flagRestr=1
                else:
                    if g.NomeFuzzy3.text()==nomeOut:
                        print "vuoto"
                    else:
                        i=0
                        print "out"
                        esatto3=str(g.nomeVar3.text())+ " IS "+nomeOut

                        cotare=g.listReg.count()
                        while i<cotare:
                            print "esatto3"
                            print esatto3
                            print(str(g.listReg.item(i).text()))
                            #if str(g.listReg.item(i).text()).find(esatto3)!=-1:
                            if str(esatto3) in str(g.listReg.item(i).text()):
                                print"NOCLASS mod"
                                g.listReg.takeItem(i)
                                cotare=cotare-1
                                i=-1
                            i=i+1
                        cr.salvato=0
                    g.tastoAgg3.setStyleSheet('color: white; background-color: rgb(61,78,121);')
                    g.tastoAgg3.setEnabled(True)
                    g.tastoDelTermOClass.setEnabled(True)
                    flagRestr=1
                    g.tabellaO.setItem(g.tabellaO.currentRow(),0,QTableWidgetItem(g.NomeFuzzy3.text()))
                    g.NomeFuzzy3.clear()
                    modifica = 0
            else:
                g.NomeFuzzy3.clear()
        else:
                g.tastoAzz3Class.setIcon(g.iconaPiu)
                g.labelAddTerm3.setText("ADD TERM:")
                if modifica == 0:
                    g.tabellaO.setItem(contaT,0,QTableWidgetItem(g.NomeFuzzy3.text()))
                    contaT += 1
                    g.labelNum.setText(str(contaT))
                    g.NomeFuzzy3.clear()
                    flagMod=0
                    flagRestr=1
                else:
                    if g.NomeFuzzy3.text()==nomeOut:
                        print "vuoto"
                    else:
                        i=0

                        esatto3=str(g.nomeVar3.text())+" IS "+nomeOut
                        cotare=g.listReg.count()
                        while i<cotare:
                            print "esatto3"
                            print(esatto3)

                            if str(esatto3) in str(g.listReg.item(i).text()):
                                print"NOCLASS mod"
                                g.listReg.takeItem(i)
                                cotare=cotare-1
                                i=-1
                            i=i+1
                        cr.salvato=0
                    g.tastoAgg3.setStyleSheet('color: white; background-color: rgb(61,78,121);')
                    g.tastoAgg3.setEnabled(True)
                    g.tastoDelTermOClass.setEnabled(True)
                    flagRestr=1
                    g.tabellaO.setItem(g.tabellaO.currentRow(),0,QTableWidgetItem(g.NomeFuzzy3.text()))
                    g.NomeFuzzy3.clear()
                    modifica = 0

def deleteTermOClass():
 global contaT
 global flagMod
 global nomeOut
 global flagRestr

 flag=0
 for item in g.tabellaO.selectedItems():
        print "selectedItems", item.text()
        flag=1
 if flagMod==1:
        warning=QtGui.QMessageBox.information(g.widget3, 'Warning', 'Are you sure you want to delete the class of the problem ?If you confirm you will change the number of classes', QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
        if warning == QtGui.QMessageBox.Yes:
            if flag==0:
                g.msg.setText("Invalid selected row/Empty list")
                g.msg.show()
                g.tabellaO.clearSelection()
            elif contaT == 1:
                nomeOut=g.tabellaO.item(g.tabellaO.currentRow(),0).text()
                g.tabellaO.removeRow(g.tabellaO.currentRow())
                contaT=contaT-1
                g.labelNum.setText(str(contaT))
                flagMod=0
                i=0
                cotare=g.listReg.count()
                while i<cotare:
                    if str(nomeOut) in str(g.listReg.item(i).text()):
                        print"NOCLASS mod"
                        g.listReg.takeItem(i)
                        cotare=cotare-1
                        i=-1
                    i=i+1
                cr.salvato=0
                flagRestr=1
            else:
                nomeOut=g.tabellaO.item(g.tabellaO.currentRow(),0).text()
                g.tabellaO.removeRow(g.tabellaO.currentRow())
                contaT=contaT-1
                g.labelNum.setText(str(contaT))
                flagMod=0
                i=0
                cotare=g.listReg.count()
                while i<cotare:
                    if str(nomeOut) in str(g.listReg.item(i).text()):
                        print"NOCLASS mod"
                        g.listReg.takeItem(i)
                        cotare=cotare-1
                        i=-1
                    i=i+1
                cr.salvato=0
                flagRestr=1
 else:
            if flag==0:
                g.msg.setText("Invalid selected row/Empty list")
                g.msg.show()
                g.tabellaO.clearSelection()
            elif contaT == 1:
                g.tabellaO.removeRow(g.tabellaO.currentRow())
                contaT=contaT-1
                g.labelNum.setText(str(contaT))
                i=0
                cotare=g.listReg.count()
                while i<cotare:
                    if str(nomeOut) in str(g.listReg.item(i).text()):
                        print"NOCLASS mod"
                        g.listReg.takeItem(i)
                        cotare=cotare-1
                        i=-1
                        i=i+1
                cr.salvato=0
                flagRestr=1
            else:
                g.tabellaO.removeRow(g.tabellaO.currentRow())
                contaT=contaT-1
                g.labelNum.setText(str(contaT))
                i=0
                cotare=g.listReg.count()
                while i<cotare:
                    if str(nomeOut) in str(g.listReg.item(i).text()):
                        print"NOCLASS mod"
                        g.listReg.takeItem(i)
                        cotare=cotare-1
                        i=-1
                    i=i+1
                cr.salvato=0
                flagRestr=1

def modTermOClass():
    global modifica
    global temp
    global nomeOut
    global flagRestr

    flag=0
    for item in g.tabellaO.selectedItems():
            print "selectedItems", item.text()
            flag=1
    if flag==0:
        g.msg.setText("Invalid selected row/Empty list")
        g.msg.show()
        g.tabellaO.clearSelection()
    else:
        g.labelAddTerm3.setText("MODIFY TERM:")
        g.tastoAzz3Class.setIcon(g.iconaApply)
        g.NomeFuzzy3.setText(g.tabellaO.item(g.tabellaO.currentRow(),0).text())
        nomeOut=g.tabellaO.item(g.tabellaO.currentRow(),0).text()
        modifica=1
        g.labelNum.setText(str(contaT))
        flagRestr=1
        g.tastoDelTermOClass.setEnabled(False)
        g.tastoAgg3.setStyleSheet('background-color(231,231,231);')
        g.tastoAgg3.setEnabled(False)


def addTermO():
    global contaT
    global modifica
    global flagRestr

    g.tastoAzz3_2.setVisible(False)
    g.tastoAzz3.setVisible(True)
    if modifica == 0:
        '''if g.chkGauss3.isChecked():
            g.chkTriangolo3.setEnabled(False)
            g.chkSing3.setEnabled(False)
            g.chkTrap3.setEnabled(False)'''
        if g.chkTrap3.isChecked():
            g.chkTriangolo3.setEnabled(False)
            g.chkSing3.setEnabled(False)
            # g.chkGauss3.setEnabled(False)
        elif g.chkTriangolo3.isChecked():
            g.chkTrap3.setEnabled(False)
            g.chkSing3.setEnabled(False)
            # g.chkGauss3.setEnabled(False)
        else:
            g.chkTriangolo3.setEnabled(False)
            g.chkTrap3.setEnabled(False)
            # g.chkGauss3.setEnabled(False)
        flagRestr=1
        g.tabellaO.setItem(contaT,0,QTableWidgetItem(g.NomeFuzzy3.text()))
        g.tabellaO.setItem(contaT,1,QTableWidgetItem(g.R1_3.text()))
        g.tabellaO.setItem(contaT,2,QTableWidgetItem(g.R2_3.text()))
        g.tabellaO.setItem(contaT,3,QTableWidgetItem(g.R3_3.text()))
        g.tabellaO.setItem(contaT,4,QTableWidgetItem(g.R4_3.text()))
        contaT += 1
        g.NomeFuzzy3.clear()
        g.R1_3.clear()
        g.R2_3.clear()
        g.R3_3.clear()
        g.R4_3.clear()
        graficiO()
    else:
        g.tabellaO.setItem(g.tabellaO.currentRow(),0,QTableWidgetItem(g.NomeFuzzy3.text()))
        g.tabellaO.setItem(g.tabellaO.currentRow(),1,QTableWidgetItem(g.R1_3.text()))
        g.tabellaO.setItem(g.tabellaO.currentRow(),2,QTableWidgetItem(g.R2_3.text()))
        g.tabellaO.setItem(g.tabellaO.currentRow(),3,QTableWidgetItem(g.R3_3.text()))
        g.tabellaO.setItem(g.tabellaO.currentRow(),4,QTableWidgetItem(g.R4_3.text()))
        graficiO()
        g.NomeFuzzy3.clear()
        g.R1_3.clear()
        g.R2_3.clear()
        g.R3_3.clear()
        g.R4_3.clear()
        g.tabellaO.clearSelection()
        modifica = 0


def modVarO():
    global modifica
    global temp
    global nomeOut
    global flagRestr

    flag=0
    for item in g.tabellaO.selectedItems():
            print "selectedItems", item.text()
            flag=1
    if flag==0:
        g.msg.setText("Invalid selected row/Empty list")
        g.msg.show()
        g.tabellaO.clearSelection()
    else:
        flagRestr=1
        g.tastoDelTermO.setEnabled(False)
        g.tastoAgg3.setEnabled(False)
        g.tastoAgg3.setStyleSheet("background-color:rgb(231,231,231)")
        g.labelAddTerm3.setText("MODIFY TERM:")
        g.tastoAzz3.setIcon(g.iconaApply)
        g.tastoAzz3_2.setIcon(g.iconaApply)
        nomeOut=g.tabellaO.item(g.tabellaO.currentRow(),0).text()
        if (str(g.tabellaO.item(g.tabellaO.currentRow(),2).text()) == "") and (str(g.tabellaO.item(g.tabellaO.currentRow(),3).text()) == "") and (str(g.tabellaO.item(g.tabellaO.currentRow(),4).text()) == ""):
            g.NomeFuzzy3.setVisible(True)
            g.chkSing3.setChecked(True)
            g.R1_3.setVisible(True)
            g.R2_3.setVisible(False)
            g.R3_3.setVisible(False)
            g.R4_3.setVisible(False)
            g.R1_3.clear()
            g.R2_3.clear()
            g.R3_3.clear()
            g.R4_3.clear()
            g.NomeFuzzy3.setText(g.tabellaO.item(g.tabellaO.currentRow(),0).text())
            g.R1_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),1).text())
        elif (str(g.tabellaO.item(g.tabellaO.currentRow(),3).text()) == "") and (str(g.tabellaO.item(g.tabellaO.currentRow(),4).text()) == ""):
            g.NomeFuzzy3.setVisible(True)
            # g.chkGauss3.setChecked(True)
            g.R1_3.setVisible(True)
            g.R2_3.setVisible(True)
            g.R3_3.setVisible(False)
            g.R4_3.setVisible(False)
            g.R1_3.clear()
            g.R2_3.clear()
            g.R3_3.clear()
            g.R4_3.clear()
            g.NomeFuzzy3.setText(g.tabellaO.item(g.tabellaO.currentRow(),0).text())
            g.R1_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),1).text())
            g.R2_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),2).text())
        elif  (str(g.tabellaO.item(g.tabellaO.currentRow(),4).text()) == ""):
            g.chkTriangolo3.setChecked(True)
            g.R1_3.clear()
            g.R2_3.clear()
            g.R3_3.clear()
            g.R4_3.clear()
            g.NomeFuzzy3.setText(g.tabellaO.item(g.tabellaO.currentRow(),0).text())
            g.R1_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),1).text())
            g.R2_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),2).text())
            g.R3_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),3).text())
            g.NomeFuzzy3.setVisible(True)
            g.R1_3.setVisible(True)
            g.R2_3.setVisible(True)
            g.R3_3.setVisible(True)
            g.R4_3.setVisible(False)
        else :
            g.chkTrap3.setChecked(True)
            g.R1_3.clear()
            g.R2_3.clear()
            g.R3_3.clear()
            g.R4_3.clear()
            g.NomeFuzzy3.setText(g.tabellaO.item(g.tabellaO.currentRow(),0).text())
            g.R1_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),1).text())
            g.R2_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),2).text())
            g.R3_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),3).text())
            g.R4_3.setText(g.tabellaO.item(g.tabellaO.currentRow(),4).text())
            g.NomeFuzzy3.setVisible(True)
            g.R1_3.setVisible(True)
            g.R2_3.setVisible(True)
            g.R3_3.setVisible(True)
            g.R4_3.setVisible(True)
        temp = g.NomeFuzzy3.text()
        g.tastoAzz3.setVisible(False)
        g.tastoAzz3_2.setVisible(True)
        g.widget3.show()

def deleteTermO():
 global contaT
 global nomeOut
 global flagRestr

 flag=0
 for item in g.tabellaO.selectedItems():
        print "selectedItems", item.text()
        flag=1
 if flag==0:
        g.msg.setText("Invalid selected row/Empty list")
        g.msg.show()
        g.tabellaO.clearSelection()
 elif contaT == 1:
    g.chkclass.setEnabled(True)
    g.picG_3.setVisible(False)
    g.picR_3.setVisible(True)
    nomeOut=g.tabellaO.item(g.tabellaO.currentRow(),0).text()
    g.tabellaO.removeRow(g.tabellaO.currentRow())
    contaT=contaT-1
    graficiO()
    g.chkTriangolo3.setEnabled(True)
    g.chkTrap3.setEnabled(True)
    # g.chkGauss3.setEnabled(True)
    g.chkSing3.setEnabled(True)
    i=0
    cotare=g.listReg.count()
    flagRestr=1
    while i<cotare:
        if str(nomeOut) in str(g.listReg.item(i).text()):
            print"NOCLASS mod"
            g.listReg.takeItem(i)
            cotare=cotare-1
            i=-1
        i=i+1
    cr.salvato=0
 else:
    flagRestr=1
    nomeOut=g.tabellaO.item(g.tabellaO.currentRow(),0).text()
    g.tabellaO.removeRow(g.tabellaO.currentRow())
    contaT=contaT-1
    i=0
    cotare=g.listReg.count()
    while i<cotare:
        if str(nomeOut) in str(g.listReg.item(i).text()):
            g.listReg.takeItem(i)
            cotare=cotare-1
            i=-1
        i=i+1
    cr.salvato=0
    graficiO()

def modTermO():
    global flagRestr

    cotare=g.listReg.count()
    if nomeOut==g.NomeFuzzy3.text():
        print "vuoto"
    else:
        i=0
        esatto4=str(g.nomeVar3.text())+" IS "+nomeOut
        while i<cotare:
            if str(esatto4) in str(g.listReg.item(i).text()):
                print "ciao"
                g.listReg.takeItem(i)
                cotare=cotare-1
                i=-1
            i=i+1
        cr.salvato=0
    flagRestr=1
    g.tastoAgg3.setStyleSheet('color:white; background-color: rgb(61,78,121);')
    g.tastoDelTermO.setEnabled(True)
    g.tastoAgg3.setEnabled(True)
    g.tabellaO.setItem(g.tabellaO.currentRow(),0,QTableWidgetItem(str(g.NomeFuzzy3.text())))
    g.tabellaO.setItem(g.tabellaO.currentRow(),1,QTableWidgetItem(str(g.R1_3.text())))
    g.tabellaO.setItem(g.tabellaO.currentRow(),2,QTableWidgetItem(str(g.R2_3.text())))
    g.tabellaO.setItem(g.tabellaO.currentRow(),3,QTableWidgetItem(str(g.R3_3.text())))
    g.tabellaO.setItem(g.tabellaO.currentRow(),4,QTableWidgetItem(str(g.R4_3.text())))
    graficiO()
    g.NomeFuzzy3.clear()
    g.R1_3.clear()
    g.R2_3.clear()
    g.R3_3.clear()
    g.R4_3.clear()
    g.tastoAzz3_2.setVisible(False)
    g.tastoAzz3.setVisible(True)

def home3():
    global flagRestr

    i=0
    c=0
    if flagRestr==1:
        g.msg.setText("You must save the variable")
        g.msg.show()
    else:
        while i<g.tabellaO.rowCount():
            if (g.tabellaO.item(i,0)) == None:
                print "vuoto"
            else:
                c=c+1
            i=i+1
        if c==0:
            g.picG_2.setVisible(False)
            g.picR_2.setVisible(True)
        if cr.salvato==0:
            g.picR_4.setVisible(True)
            g.picG_4.setVisible(False)
        else:
            g.picR_4.setVisible(False)
            g.picG_4.setVisible(True)
        g.NomeFuzzy3.clear()
        g.R1_3.clear()
        g.R2_3.clear()
        g.R3_3.clear()
        g.R4_3.clear()
        g.widget3.close()
        g.menu.show()

def menuWidg3():
 if g.tabellaO.item(0,0) == None:
    '''plt.xlim(0, 100)
    plt.ylim(0, 1.2)
    plt.savefig(perc+str(contaGraf)+".png")
    img = Image.open(perc+str(contaGraf)+".png")
    img = img.resize((500,195), PIL.Image.ANTIALIAS)
    img.save(perc+str(contaGraf)+".png")
    scene = QGraphicsScene()
    scene.addPixmap(QPixmap(perc+str(contaGraf)+".png"))
    g.boxGrafico2.setScene(scene)
    plt.close()
    os.remove(perc+str(contaGraf)+".png")'''
 else:
    if g.chkclass.isChecked()==True:
        g.menu.close()
        g.widget3.show()
    else:
        graficiO()
        g.menu.close()
        g.widget3.show()
 g.menu.close()
 g.widget3.show()

def is_numberF(s):
    try:
        n = str(float(s))
        if n == "nan" or n == "inf" or n == "-inf": return False
    except ValueError:
        try:
            complex(s)
        except ValueError:
            return False
    return True

def is_numberI(s):
    try:
        n = str(int(s))
        if n == "nan" or n == "inf" or n == "-inf": return False
    except ValueError:
        try:
            complex(s)
        except ValueError:
            return False
    return True

def ControlloW3():
    if (g.nomeVar3.text() == "" or g.NomeFuzzy3.text() == "" or g.domX3.text() == "" or g.domY3.text() == ""):
        g.msg.setText("Empty variable name field ")
        g.msg.show()
    else:
        if (is_numberF(str(g.domX3.text())) == False or is_numberF(str(g.domY3.text())) == False or float(
                    g.domX3.text()) > float(g.domY3.text())):
            g.msg.setText("Wrong variable domain field/empty field")
            g.msg.show()
        if (controlloSing_3() == 1):
            if (is_numberF(str(g.R1_3.text())) == False or float(g.R1_3.text()) < float(g.domX3.text()) or float(
                        g.R1_3.text()) > float(g.domY3.text()) or g.R1_3.text() == ""):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                addTermO()
                g.labelAddTerm3.setText("ADD TERM:")
                g.tastoAzz3.setIcon(g.iconaPiu)
                g.tastoAzz3_2.setIcon(g.iconaPiu)
            '''elif (controlloGauss_3() == 1):
                if (is_numberF(str(g.R1_3.text())) == False
                    or is_numberF(str(g.R2_3.text())) == False
                    or float(g.R1_3.text()) < float(g.domX3.text())
                    or float(g.R1_3.text()) > float(g.domY3.text())
                    or g.R1_3.text() == "" or g.R2_3.text() == "" ):

                    g.msg.setText("Wrong term domain field/empty field ")
                    g.msg.show()
                else:
                    addTermO()
                    g.labelAddTerm3.setText("ADD TERM:")
                    g.tastoAzz3.setIcon(g.iconaPiu)
                    g.tastoAzz3_2.setIcon(g.iconaPiu)'''
        elif (controlloTrian_3() == 1):
            if (is_numberF(str(g.R1_3.text())) == False or is_numberF(str(g.R2_3.text())) == False or is_numberF(
                        str(g.R3_3.text())) == False or float(g.R1_3.text()) < float(g.domX3.text()) or float(
                        g.R3_3.text()) > float(
                        g.domY3.text()) or g.R1_3.text() == "" or g.R2_3.text() == "" or g.R3_3.text() == "" or float(
                        g.R1_3.text()) > float(g.R2_3.text()) or float(g.R2_3.text()) > float(g.R3_3.text()) or float(
                        g.R1_3.text()) > float(g.R3_3.text())):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                addTermO()
                g.labelAddTerm3.setText("ADD TERM:")
                g.tastoAzz3.setIcon(g.iconaPiu)
                g.tastoAzz3_2.setIcon(g.iconaPiu)
        elif (controlloTrap_3() == 1):
            if (is_numberF(str(g.R2_3.text())) == False or is_numberF(str(g.R3_3.text())) == False or is_numberF(
                        str(g.R4_3.text())) == False or float(g.R1_3.text()) < float(g.domX3.text()) or float(
                        g.R4_3.text()) > float(
                        g.domY3.text()) or g.R1_3.text() == "" or g.R2_3.text() == "" or g.R3_3.text() == "" or g.R4_3.text() == "" or is_numberF(
                        str(g.R1_3.text())) == False or float(g.R1_3.text()) > float(g.R2_3.text()) or float(
                        g.R2_3.text()) > float(g.R3_3.text()) or float(g.R3_3.text()) > float(g.R4_3.text()) or float(
                        g.R1_3.text()) > float(g.R4_3.text())):
                g.msg.setText("Wrong term domain field/empty field")
                g.msg.show()
            else:
                addTermO()
                g.labelAddTerm3.setText("ADD TERM:")
                g.tastoAzz3.setIcon(g.iconaPiu)
                g.tastoAzz3_2.setIcon(g.iconaPiu)

def ControlloW3_3():
    if (g.nomeVar3.text() == "" or g.NomeFuzzy3.text() == "" or g.domX3.text() == "" or g.domY3.text() == ""):
        g.msg.setText("Empty variable name field ")
        g.msg.show()
    else:
        if (is_numberF(str(g.domX3.text())) == False or is_numberF(str(g.domY3.text())) == False or float(
                    g.domX3.text()) > float(g.domY3.text())):
            g.msg.setText("Wrong variable domain field/empty field")
            g.msg.show()
        if (controlloSing_3() == 1):
            if (is_numberF(str(g.R1_3.text())) == False or float(g.R1_3.text()) < float(g.domX3.text()) or float(
                        g.R1_3.text()) > float(g.domY3.text()) or g.R1_3.text() == ""):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                modTermO()
                g.labelAddTerm3.setText("ADD TERM:")
                g.tastoAzz3.setIcon(g.iconaPiu)
                g.tastoAzz3_2.setIcon(g.iconaPiu)
            '''
            elif (controlloGauss_3() == 1):
                if (is_numberF(str(g.R1_3.text())) == False or is_numberF(str(g.R2_3.text())) == False or float(
                            g.R1_3.text()) < float(g.domX3.text()) or float(g.R2_3.text()) > float(
                            g.domY3.text()) or g.R1_3.text() == "" or g.R2_3.text() == "" or float(g.R1_3.text()) > float(
                            g.R2_3.text())):
                    g.msg.setText("Wrong term domain field/empty field ")
                    g.msg.show()
                else:
                    modTermO()
                    g.labelAddTerm3.setText("ADD TERM:")
                    g.tastoAzz3.setIcon(g.iconaPiu)
                    g.tastoAzz3_2.setIcon(g.iconaPiu)'''
        elif (controlloTrian_3() == 1):
            if (is_numberF(str(g.R1_3.text())) == False or is_numberF(str(g.R2_3.text())) == False or is_numberF(
                        str(g.R3_3.text())) == False or float(g.R1_3.text()) < float(g.domX3.text()) or float(
                        g.R3_3.text()) > float(
                        g.domY3.text()) or g.R1_3.text() == "" or g.R2_3.text() == "" or g.R3_3.text() == "" or float(
                        g.R1_3.text()) > float(g.R2_3.text()) or float(g.R2_3.text()) > float(g.R3_3.text()) or float(
                        g.R1_3.text()) > float(g.R3_3.text())):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                modTermO()
                g.labelAddTerm3.setText("ADD TERM:")
                g.tastoAzz3.setIcon(g.iconaPiu)
                g.tastoAzz3_2.setIcon(g.iconaPiu)
        elif (controlloTrap_3() == 1):
            if (is_numberF(str(g.R2_3.text())) == False or is_numberF(str(g.R3_3.text())) == False or is_numberF(
                        str(g.R4_3.text())) == False or float(g.R1_3.text()) < float(g.domX3.text()) or float(
                        g.R4_3.text()) > float(
                        g.domY3.text()) or g.R1_3.text() == "" or g.R2_3.text() == "" or g.R3_3.text() == "" or g.R4_3.text() == "" or is_numberF(
                        str(g.R1_3.text())) == False or float(g.R1_3.text()) > float(g.R2_3.text()) or float(
                        g.R2_3.text()) > float(g.R3_3.text()) or float(g.R3_3.text()) > float(g.R4_3.text()) or float(
                        g.R1_3.text()) > float(g.R4_3.text())):
                g.msg.setText("Wrong term domain field/empty field")
                g.msg.show()
            else:
                modTermO()
                g.labelAddTerm3.setText("ADD TERM:")
                g.tastoAzz3.setIcon(g.iconaPiu)
                g.tastoAzz3_2.setIcon(g.iconaPiu)


def graficiO():
        global y1
        global y2
        global listaGaussI
        global listaTrianI
        global rv2
        global contaGraf
        listaPoly=[]
        listaGauss=[]
        listaSing=[]
        y1=[]
        y2=[]

        i=0
        c=0
        while i<g.tabellaO.rowCount():
            if (g.tabellaO.item(i,0)) == None:
                print "vuoto"
            else:
                c=c+1
            i=i+1
        i=0
        while i < c:

            # se il termine inserito ha una funzione di membership singleton
            if str(g.tabellaO.item(i,2).text()) == "" and str(g.tabellaO.item(i,3).text()) == "" and str(g.tabellaO.item(i,4).text()) == "":
                listaSing.append(float(str(g.tabellaO.item(i,1).text())))

            # se il termine inserito ha una funzione di membership gaussiana
            elif str(g.tabellaO.item(i,3).text()) == "" and str(g.tabellaO.item(i,4).text()) == "":

                x1 = float(str(g.tabellaO.item(i,1).text()))
                x2 = float(str(g.tabellaO.item(i,2).text()))
                xmedio = (x1 + x2) / 2

                # norm definisce una variabile aleatoria normale (con media "loc" e deviazione standard "scale")
                rv2 = norm(loc=x1, scale=x2)

                # arange(start, stop, step) crea un array con i valori tra start e stop
                '''
                k = (np.arange(float(str(g.tabellaO.item(i,1).text())),
                               float(str(g.tabellaO.item(i,2).text())),
                               .00111))'''

                k = np.arange(float(g.domX3.text()),
                              float(g.domY3.text()),
                              .00111)

                listaGauss.append(k)
                y2.append(rv2)

            # se il termine inserito ha una funzione di membership triangolare
            elif str(g.tabellaO.item(i,4).text()) == "":
                listaPoly.append(float(str(g.tabellaO.item(i,1).text())))
                y1.append(0)
                listaPoly.append(float(str(g.tabellaO.item(i,2).text())))
                y1.append(1)
                listaPoly.append(float(str(g.tabellaO.item(i,3).text())))
                y1.append(0)

            # se il termine inserito ha una funzione di membership trapezoidale
            else:
                listaPoly.append(float(str(g.tabellaO.item(i,1).text())))
                y1.append(0)
                listaPoly.append(float(str(g.tabellaO.item(i,2).text())))
                y1.append(1)
                listaPoly.append(float(str(g.tabellaO.item(i,3).text())))
                y1.append(1)
                listaPoly.append(float(str(g.tabellaO.item(i,4).text())))
                y1.append(0)
            i=i+1


        i=0

        # plot the function
        ax = figure.add_subplot(111)
        ax.hold(False)
        ax.vlines(listaSing, 0, 1)
        ax.plot(listaPoly, y1)

        while i < len(listaGauss):
            ax.plot(listaGauss[i], y2[i].pdf(listaGauss[i]))
            i += 1

        canvas.draw()
        contaGraf += 1

        del listaPoly[0:len(listaPoly)]
        del y1[0:len(y1)]
        del listaGauss[0:len(listaGauss)]
        del y2[0:len(y2)]

def classificazione():
    global contaT
    global flagMod

    if g.chkclass.isChecked()==True:
        if inp.flagWarning==0:
            warning=QtGui.QMessageBox.information(g.widget3, 'Warning', 'Do you really want to change the type? If confirmed you will be lost all data outuput', QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
            if warning==QtGui.QMessageBox.Yes :
                g.chkTrap3.setVisible(False)
                g.chkSing3.setVisible(False)
                g.chkTriangolo3.setVisible(False)
                # g.chkGauss3.setVisible(False)
                g.domX3.setVisible(False)
                g.domY3.setVisible(False)
                g.boxGrafico2.setVisible(False)
                g.comboDefuzzy.setVisible(False)
                g.NomeFuzzy3.setVisible(True)
                g.NomeFuzzy3.setGeometry(85, 175, 157, 21)
                g.labelNumClass.setVisible(True)
                g.labelDefuzzy.setVisible(False)
                g.labelNum.setVisible(True)
                g.tastoAzz3.setVisible(True)
                g.comboAccu.setVisible(True)
                g.labelAccu.setVisible(True)
                g.tastoAzz3Class.setVisible(True)
                g.tastoAzz3.setVisible(False)
                g.tastoModTermOClass.setVisible(True)
                g.tastoDelTermOClass.setVisible(True)
                g.tastoModTermO.setVisible(False)
                g.tastoDelTermO.setVisible(False)
                g.labelDom.setVisible(False)
                g.labelInfoDom.setVisible(False)
                g.domX3.clear()
                g.domY3.clear()
                g.R1_3.setVisible(False)
                g.R2_3.setVisible(False)
                g.R3_3.setVisible(False)
                g.R4_3.setVisible(False)
                g.labelFunz.setVisible(False)
                g.testWidget.setFixedSize(760,660)
                g.frameDict.setVisible(True)
                g.tabInfDict.setVisible(True)
                g.tastoMenuTest.setGeometry(650, 620, 75, 31)
                g.frameTestOut.setVisible(False)
                g.tabInfOut.setVisible(False)
                g.tabellaO.clear()
                g.nomeVar3.clear()
                g.labelNum.setText("0")
                contaT=0
                plt.xlim(0, 100)
                plt.ylim(0, 1.2)
                plt.savefig(perc+str(contaGraf)+".png")
                img = Image.open(perc+str(contaGraf)+".png")
                img = img.resize((500,195), PIL.Image.ANTIALIAS)
                img.save(perc+str(contaGraf)+".png")
                scene = QGraphicsScene()
                scene.addPixmap(QPixmap(perc+str(contaGraf)+".png"))
                g.boxGrafico2.setScene(scene)
                plt.close()
                os.remove(perc+str(contaGraf)+".png")
            else:
                g.chkclass.setChecked(False)
        else:
                g.chkTrap3.setVisible(False)
                g.chkSing3.setVisible(False)
                g.chkTriangolo3.setVisible(False)
                # g.chkGauss3.setVisible(False)
                g.domX3.setVisible(False)
                g.domY3.setVisible(False)
                g.boxGrafico2.setVisible(False)
                g.comboDefuzzy.setVisible(False)
                g.NomeFuzzy3.setVisible(True)
                g.NomeFuzzy3.setGeometry(85, 175, 157, 21)
                g.labelNumClass.setVisible(True)
                g.labelDefuzzy.setVisible(False)
                g.labelNum.setVisible(True)
                g.tastoAzz3.setVisible(True)
                g.comboAccu.setVisible(True)
                g.labelAccu.setVisible(True)
                g.tastoAzz3Class.setVisible(True)
                g.tastoAzz3.setVisible(False)
                g.tastoModTermOClass.setVisible(True)
                g.tastoDelTermOClass.setVisible(True)
                g.tastoModTermO.setVisible(False)
                g.tastoDelTermO.setVisible(False)
                g.labelDom.setVisible(False)
                g.labelInfoDom.setVisible(False)
                g.domX3.clear()
                g.domY3.clear()
                g.R1_3.setVisible(False)
                g.R2_3.setVisible(False)
                g.R3_3.setVisible(False)
                g.R4_3.setVisible(False)
                g.labelFunz.setVisible(False)
                g.testWidget.setFixedSize(760,660)
                g.frameDict.setVisible(True)
                g.tabInfDict.setVisible(True)
                g.tastoMenuTest.setGeometry(650, 620, 75, 31)
                g.frameTestOut.setVisible(False)
                g.tabInfOut.setVisible(False)
                plt.xlim(0, 100)
                plt.ylim(0, 1.2)
                plt.savefig(perc+str(contaGraf)+".png")
                img = Image.open(perc+str(contaGraf)+".png")
                img = img.resize((500,195), PIL.Image.ANTIALIAS)
                img.save(perc+str(contaGraf)+".png")
                scene = QGraphicsScene()
                scene.addPixmap(QPixmap(perc+str(contaGraf)+".png"))
                g.boxGrafico2.setScene(scene)
                plt.close()
                os.remove(perc+str(contaGraf)+".png")
                flagMod=1
    else:
        if inp.flagWarning==0:
            warning=QtGui.QMessageBox.information(g.widget3, 'WARNING', 'Do you really want to change the type? \nIf confirmed you will be lost all data outuput', QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
            if warning==QtGui.QMessageBox.Yes :
                g.chkTrap3.setVisible(True)
                g.chkSing3.setVisible(True)
                g.chkTriangolo3.setVisible(True)
                # g.chkGauss3.setVisible(True)
                # g.chkGauss3.setEnabled(True)
                g.chkTrap3.setEnabled(True)
                g.chkTriangolo3.setEnabled(True)
                g.chkSing3.setEnabled(True)
                g.domX3.setVisible(True)
                g.domY3.setVisible(True)
                g.boxGrafico2.setVisible(True)
                g.comboDefuzzy.setVisible(True)
                g.NomeFuzzy3.setVisible(False)
                g.NomeFuzzy3.setGeometry(85, 160, 157, 21)
                g.labelDefuzzy.setVisible(True)
                g.tastoAzz3.setVisible(False)
                g.labelNumClass.setVisible(False)
                g.labelNum.setVisible(False)
                g.comboAccu.setVisible(False)
                g.labelAccu.setVisible(False)
                g.tastoAzz3Class.setVisible(False)
                g.tastoAzz3.setVisible(True)
                g.tastoModTermOClass.setVisible(False)
                g.tastoDelTermOClass.setVisible(False)
                g.tastoModTermO.setVisible(True)
                g.tastoDelTermO.setVisible(True)
                g.labelDom.setVisible(True)
                g.labelInfoDom.setVisible(True)
                g.labelFunz.setVisible(True)
                g.frameTestOut.setVisible(True)
                g.tabInfOut.setVisible(True)
                g.testWidget.setFixedSize(760,400)
                g.frameDict.setVisible(False)
                g.tabInfDict.setVisible(False)
                g.tastoMenuTest.setGeometry(650, 350, 75, 31)
                g.tabellaO.clear()
                g.nomeVar3.clear()
                g.labelNum.setText("0")
                contaT=0
                plt.xlim(0, 100)
                plt.ylim(0, 1.2)
                plt.savefig(perc+str(contaGraf)+".png")
                img = Image.open(perc+str(contaGraf)+".png")
                img = img.resize((500,195), PIL.Image.ANTIALIAS)
                img.save(perc+str(contaGraf)+".png")
                scene = QGraphicsScene()
                scene.addPixmap(QPixmap(perc+str(contaGraf)+".png"))
                g.boxGrafico2.setScene(scene)
                plt.close()
                os.remove(perc+str(contaGraf)+".png")
            else:
                g.chkclass.setChecked(True)
        else:
            flagMod=1

#Variables
termO=[]
contaT=0
temp=0
modifica=0
contaGraf=0
flagMod=0
nomeOut=""
flagRestr=0

#Connect
g.menu.connect(g.tastoOutput, QtCore.SIGNAL('clicked()'), menuWidg3)
g.widget3.connect(g.tastoMenu3, QtCore.SIGNAL('clicked()'), home3)
g.widget3.connect(g.chkTrap3, QtCore.SIGNAL('clicked()'), caricaDef)
g.widget3.connect(g.chkTriangolo3, QtCore.SIGNAL('clicked()'),caricaDef)
# g.widget3.connect(g.chkGauss3, QtCore.SIGNAL('clicked()'),caricaDef)
g.widget3.connect(g.chkSing3, QtCore.SIGNAL('clicked()'), caricaDef)
g.widget3.connect(g.chkTrap3, QtCore.SIGNAL('clicked()'), generaFunzO)
g.widget3.connect(g.chkTriangolo3, QtCore.SIGNAL('clicked()'), generaFunzO)
# g.widget3.connect(g.chkGauss3, QtCore.SIGNAL('clicked()'),generaFunzO)
g.widget3.connect(g.chkSing3, QtCore.SIGNAL('clicked()'), generaFunzO)
g.widget3.connect(g.tastoAgg3, QtCore.SIGNAL('clicked()'),addVarO)
g.widget3.connect(g.tastoAzz3,QtCore.SIGNAL('clicked()'), ControlloW3)
g.widget3.connect(g.tastoModTermO,QtCore.SIGNAL('clicked()'), modVarO)
g.widget3.connect(g.tastoAzz3_2,QtCore.SIGNAL('clicked()'), ControlloW3_3)
g.widget3.connect(g.tastoDelTermO,QtCore.SIGNAL('clicked()'), deleteTermO)
g.widget3.connect(g.chkclass,QtCore.SIGNAL('clicked()'), classificazione)
g.widget3.connect(g.tastoAzz3Class,QtCore.SIGNAL('clicked()'), addTermOClass)
g.widget3.connect(g.tastoDelTermOClass,QtCore.SIGNAL('clicked()'), deleteTermOClass)
g.widget3.connect(g.tastoModTermOClass,QtCore.SIGNAL('clicked()'), modTermOClass)


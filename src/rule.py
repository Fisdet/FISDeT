__author__ = 'Pasquadibisceglie-Zaza'

#Libraries
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore,QtGui
import sys
import FISDeT as g
import inputVariable2 as fi
from importFcl import *
import createFCL as cr

#Functions
def apriRule():
    if g.picG_1.isVisible()==True and g.picG_2.isVisible()==True:
        g.tabR.setColumnCount(len(fi.varI))
        g.tabR.setGeometry(50,60,622,70)
        g.tabR.verticalHeader().hide()
        boxT2 = QtGui.QComboBox(g.widget4)
        boxT2.setGeometry(75, 150, 81, 21)
        boxT2.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
        g.tabR2.setGeometry(692,60,150,70)
        g.tabR2.verticalHeader().hide()
        g.tabR2.setCellWidget(0,0,boxT2)
        nome2=QTableWidgetItem("THEN "+g.nomeVar3.text())
        g.tabR2.setHorizontalHeaderItem(0,nome2)
        i=0
        c=0
        while i<g.tabellaO.rowCount():
            if (g.tabellaO.item(i,0)) == None:
                print "vuoto"
            else:
                c=c+1
            i=i+1
        i=0
        while i<c:
            boxT2.addItem(g.tabellaO.item(i,0).text())
            g.tabR2.setColumnWidth(0,150)
            i=i+1
        i=0
        while i<len(fi.varI):
            j=0
            boxT = QtGui.QComboBox(g.widget4)
            boxT.setGeometry(75, 150, 281, 21)
            boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
            g.tabR.setCellWidget(0,i,boxT)
            g.tabR.setColumnWidth(i,150)
            if i==0:
                nome=QTableWidgetItem("IF "+fi.varI[i].getNome())
                g.tabR.setHorizontalHeaderItem(i,nome)
            else:
                nome=QTableWidgetItem("AND " + fi.varI[i].getNome())
                g.tabR.setHorizontalHeaderItem(i,nome)
            while j<len(fi.termI):
                if fi.varI[i].getNome() == fi.termI[j].getNomev():
                    boxT.addItem(fi.termI[j].getNomet())
                j=j+1
            i=i+1
        g.menu.close()
        g.widget4.show()
    else:
          g.msg.setText("You must create system variables")
          g.msg.show()

def generaRule():
    global controlloRegole
    global numReg

    i=0
    while i<len(fi.varI):
        stringa="IF ("
        j=0
        while j<len(fi.varI):
            if j==0:
                if str(g.tabR.cellWidget(0,j).currentText())!="":
                    stringa= stringa+ fi.varI[j].getNome() +" IS "+str(g.tabR.cellWidget(0,j).currentText())+")"
            elif len(fi.varI)==1:
                if str(g.tabR.cellWidget(0,j).currentText())!="":
                    stringa= stringa+ fi.varI[j].getNome() +" IS "+str(g.tabR.cellWidget(0,j).currentText())+")"
            elif j==len(fi.varI):
                if str(g.tabR.cellWidget(0,j).currentText())!="":
                    stringa= stringa+ fi.varI[j].getNome() +" IS "+str(g.tabR.cellWidget(0,j).currentText())+")"
            else:
                if str(g.tabR.cellWidget(0,j).currentText())!="":
                    stringa=stringa+ " AND ("
                    stringa= stringa+ fi.varI[j].getNome() +" IS "+str(g.tabR.cellWidget(0,j).currentText())+")"
            j=j+1
        stringa = stringa +  " THEN ("+str(g.nomeVar3.text())+" IS "+ str(g.tabR2.cellWidget(0,0).currentText()) +");"
        controlloRegole=1
        i=i+1
    numReg=numReg+1
    cr.salvato=0
    g.listReg.addItem(stringa)

def delRegola():
    flag=0
    for item in g.listReg.selectedItems():
            print "selectedItems", item.text()
            flag=1
    if flag==0:
        g.msg.setText("Invalid selected row/Empty list")
        g.msg.show()
        g.listReg.clearSelection()
    else:
        for item in g.listReg.selectedItems():
            g.listReg.takeItem(g.listReg.row(item))
        g.listReg.clearSelection()
        cr.salvato=0

def menuReg():
    if g.listReg.count()==0:
        g.picG_3.setVisible(False)
        g.picR_3.setVisible(True)
    else:
        g.picG_3.setVisible(True)
        g.picR_3.setVisible(False)
    if cr.salvato==0:
        g.picR_4.setVisible(True)
        g.picG_4.setVisible(False)
    else:
        g.picR_4.setVisible(False)
        g.picG_4.setVisible(True)
    g.widget4.close()
    g.menu.show()

#Variables
numReg=0
controlloRegole=0

#Connect
g.menu.connect(g.tastoRegole, QtCore.SIGNAL('clicked()'), apriRule)
g.widget4.connect(g.tastoAggiungiR, QtCore.SIGNAL('clicked()'), generaRule)
g.widget4.connect(g.tastoDel5, QtCore.SIGNAL('clicked()'), delRegola)
g.widget4.connect(g.tastoMenu4, QtCore.SIGNAL('clicked()'),menuReg)

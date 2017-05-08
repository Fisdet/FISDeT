__author__ = 'Pasquadibisceglie-Zaza'

#Libraries
import FISDeT as g
import os
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import os
import PIL
from PIL import Image
from outputVariable import *
import inference as inf
import rule as ru
import importFcl as im
import createFCL as cr

perc=os.path.dirname("FISDeT2.0\img")

#Functions
def menuWidg2():
    global flagRestr

    if flagRestr==1:
        g.msg.setText("You must add the variable")
        g.msg.show()
    else :
        g.widget2.close()
        g.widget.show()

def applicaMod():
    global temp
    global temps1
    global temps2
    global temps3
    global temps4
    global flagRestr

    nomeVariabile=g.tabellaI.item(g.tabellaI.currentRow(),0).text()
    i=0
    c=0
    while i<g.listaTerminiI.rowCount():
        if (g.listaTerminiI.item(i,0)) == None:
            print "vuoto"
        else:
            c=c+1
        i=i+1
    j=0
    while j<c:
        i=0
        while i<len(termI):
            if termI[i].getNomev() == nomeVariabile:
                del termI[i]
                t=termine()
                t.termine(str(g.nomeVar.text()),str(g.domX.text()),str(g.domY.text()),g.listaTerminiI.item(j,0).text(),g.listaTerminiI.item(j,1).text(),g.listaTerminiI.item(j,2).text(),g.listaTerminiI.item(j,3).text(),g.listaTerminiI.item(j,4).text())
                termI.append(t)
                i=len(termI)
            i=i+1
        j=j+1
    nomeprec=str(g.tabellaI.item(g.tabellaI.currentRow(),0).text())
    controllo=str(g.nomeVar.text())
    i=0
    while i<len(varI):
        if nomeprec == controllo:
            print "vuoto"
        else:
            if nomeprec ==  varI[i].getNome():
                del varI[i]
                v=variabile()
                v.variabile(controllo)
                varI.append(v)
                i=len(varI)
        i=i+1
    cotare=g.listReg.count()
    esatto=g.nomeVar.text()+" IS "+temp
    i=0
    flagRe=0
    while i<len(termI):
        if temp == termI[i].getNomet() and g.nomeVar.text()== termI[i].getNomev():
                flagRe=0
                i=len(termI)
        else:
                flagRe=1
        i=i+1
    i=0
    while i<cotare:
        if flagRe==1:
            if str(esatto) in str(g.listReg.item(i).text()):
                g.listReg.takeItem(i)
                cotare=cotare-1
                i=-1
        else:
            i=cotare
        i=i+1
    i=0
    c=0
    if tempNomeV==g.nomeVar.text():
        print"vuoto"
    else :
        while i<g.listaTerminiI.rowCount():
            if (g.listaTerminiI.item(i,0)) == None:
                print "vuoto"
            else:
                c=c+1
            i=i+1
        if c==0:
            print "vuoto"
        else:
            g.listReg.clear()
    cr.salvato=0
    g.listaTerminiI.clear()
    g.nomeVar.clear()
    g.NomeFuzzy.clear()
    g.R1.clear()
    g.R2.clear()
    g.R3.clear()
    g.R4.clear()
    g.domX.clear()
    g.domY.clear()
    g.widget2.close()

def home():
        if cr.salvato==0:
            g.picR_4.setVisible(True)
            g.picG_4.setVisible(False)
        else:
            g.picR_4.setVisible(False)
            g.picG_4.setVisible(True)
        g.widget.close()
        g.menu.show()

def appMod():
    global contaT
    global tempNomeV

    flag=0
    for item in g.tabellaI.selectedItems():
            print "selectedItems", item.text()
            flag=1
    if flag==0:
        g.msg.setText("Invalid selected row/Empty list")
        g.msg.show()
        g.tabellaI.clearSelection()
    else:
        nomeVariabile=g.tabellaI.item(g.tabellaI.currentRow(),0).text()
        g.tastoAzz2.setVisible(True)
        g.tastoAzz.setVisible(False)
        g.listaTerminiI.clear()
        i=0
        conta=0
        while i<len(termI):
              if termI[i].getNomev()==nomeVariabile:
                   conta=conta+1
              i=i+1
        if conta==0:
            i=0
            while i<len(varI):
                if varI[i].getNome()==nomeVariabile:
                    g.domX.setText(str(im.x[i]))
                    g.domY.setText(str(im.y[i]))
                i=i+1
            g.nomeVar.setText(nomeVariabile)
            g.tastoAgg.setVisible(False)
            g.tastoMod2.setVisible(True)
            g.labelPiu.setText("APPLY")
            g.widgetTabI.close()
            graficiI()
            g.widget2.show()
        else:
            i=0
            c=0
            while i<len(termI):
                print termI[i].getNomev()
                if nomeVariabile == termI[i].getNomev():
                    g.nomeVar.setText(termI[i].getNomev())
                    g.domX.setText(termI[i].getDomX())
                    g.domY.setText(termI[i].getDomY())
                    g.listaTerminiI.setItem(c,0,QTableWidgetItem(termI[i].getNomet()))
                    g.listaTerminiI.setItem(c,1,QTableWidgetItem(termI[i].getS1()))
                    g.listaTerminiI.setItem(c,2,QTableWidgetItem(termI[i].getS2()))
                    g.listaTerminiI.setItem(c,3,QTableWidgetItem(termI[i].getS3()))
                    g.listaTerminiI.setItem(c,4,QTableWidgetItem(termI[i].getS4()))
                    if termI[i].getS1() != "" and termI[i].getS2() != "" and termI[i].getS3() != "" and termI[i].getS4() != "":
                        g.chkTriangolo.setEnabled(False)
                        g.chkGauss.setEnabled(False)
                        g.chkTrap.setEnabled(True)
                        g.chkTrap.setChecked(True)
                        generaFunz()
                    elif termI[i].getS1() != "" and termI[i].getS2() != "" and termI[i].getS3() != "" and termI[i].getS4() == "":
                        g.chkTriangolo.setEnabled(True)
                        g.chkGauss.setEnabled(False)
                        g.chkTrap.setEnabled(False)
                        g.chkTriangolo.setChecked(True)
                        generaFunz()
                    else:
                        g.chkTriangolo.setEnabled(False)
                        g.chkGauss.setEnabled(True)
                        g.chkTrap.setEnabled(False)
                        g.chkGauss.setChecked(True)
                        generaFunz()
                    c=c+1
                    contaT=contaT+1
                i=i+1
            tempNomeV=nomeVariabile
            graficiI()
            g.tastoAgg.setVisible(False)
            g.tastoMod2.setVisible(True)
            g.labelPiu.setText("APPLY")
            g.widgetTabI.close()
            g.widget2.show()

def closeviewInpVar():
    if cr.salvato==0:
        g.picR_4.setVisible(True)
        g.picG_4.setVisible(False)
    else:
        g.picR_4.setVisible(False)
        g.picG_4.setVisible(True)
    g.tabellaI.clear()
    g.widgetTabI.close()
    g.widget.show()

def viewInpVar():
    i=0
    g.tabellaI.clear()
    while i<len(varI):
            g.tabellaI.setItem(i,0,QTableWidgetItem(varI[i].getNome()))
            i=i+1
    g.widgetTabI.show()

def varInput():
    g.menu.close()
    g.widget.show()

def addVar():
    g.widget.close()
    g.chkTriangolo.setEnabled(True)
    g.chkTrap.setEnabled(True)
    g.chkGauss.setEnabled(True)
    plt.xlim(0, 100)
    plt.ylim(0, 1.2)
    plt.savefig(perc+str(contaGraf)+".png")
    img = Image.open(perc+str(contaGraf)+".png")
    img = img.resize((500,195), PIL.Image.ANTIALIAS)
    img.save(perc+str(contaGraf)+".png")
    scene = QGraphicsScene()
    scene.addPixmap(QPixmap(perc+str(contaGraf)+".png"))
    g.boxGrafico.setScene(scene)
    plt.close()
    os.remove(perc+str(contaGraf)+".png")
    g.tastoAgg.setVisible(True)
    g.labelPiu.setVisible(True)
    g.tastoMod2.setVisible(False)
    g.listaTerminiI.clear()
    g.nomeVar.clear()
    g.NomeFuzzy.clear()
    g.tastoAzz.setVisible(True)
    g.tastoAzz2.setVisible(False)
    g.labelPiu.setText("ADD VARIABLE:")
    g.R1.clear()
    g.R2.clear()
    g.R3.clear()
    g.R4.clear()
    g.domY.clear()
    g.domX.clear()
    g.widget2.show()

def controlloGauss():
    if g.chkGauss.isChecked():
        return 1
    else:
        return 0


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

def generaFunz():
    colonna = 0
    if g.chkTriangolo.isChecked():
        g.NomeFuzzy.text()
        g.R1.text()
        g.R2.text()
        g.R3.text()
        g.tastoAzz.show()
        g.NomeFuzzy.show()
        g.R1.show()
        g.R2.show()
        g.R3.show()
        g.R4.setVisible(False)
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        colonna = colonna + 130
    elif g.chkTrap.isChecked():
        g.NomeFuzzy.text()
        g.R1.text()
        g.R2.text()
        g.R3.text()
        g.R4.text()
        g.tastoAzz.show()
        g.NomeFuzzy.show()
        g.R1.show()
        g.R2.show()
        g.R3.show()
        g.R4.show()
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        colonna = colonna + 150
    elif g.chkGauss.isChecked():
        g.NomeFuzzy.text()
        g.R1.text()
        g.R2.text()
        g.tastoAzz.show()
        g.NomeFuzzy.show()
        g.R1.show()
        g.R2.show()
        g.R3.setVisible(False)
        g.R4.setVisible(False)
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        colonna = colonna + 130

class termine():
    nomeV=""
    domX=""
    domY=""
    nomeT=""
    s1=""
    s2=""
    s3=""
    s4=""

    def termine(self,k,a,b,w,x,y,z,j):
        self.nomeV = k
        self.domX = a
        self.domY = b
        self.nomeT = w
        self.s1 = x
        self.s2 = y
        self.s3 = z
        self.s4 = j

    def getNomev(self):
        return self.nomeV

    def getNomet(self):
        return self.nomeT

    def getS1(self):
        return self.s1

    def getS2(self):
        return self.s2

    def getS3(self):
        return self.s3

    def getS4(self):
        return self.s4

    def getDomX(self):
        return self.domX

    def getDomY(self):
        return self.domY

class variabile():
    nome=""
    def variabile(self,w):
        self.nome=w
    def getNome(self):
        return self.nome

def addTerm2():
    i=0
    c=0
    global modifica
    global flagRestr

    while i<g.listaTerminiI.rowCount():
        if (g.listaTerminiI.item(i,0)) == None:
            print "vuota 2"
        else:
            c=c+1
        i=i+1
    if modifica == 0:
        g.listaTerminiI.setItem(c,0,QTableWidgetItem(g.NomeFuzzy.text()))
        g.listaTerminiI.setItem(c,1,QTableWidgetItem(g.R1.text()))
        g.listaTerminiI.setItem(c,2,QTableWidgetItem(g.R2.text()))
        g.listaTerminiI.setItem(c,3,QTableWidgetItem(g.R3.text()))
        g.listaTerminiI.setItem(c,4,QTableWidgetItem(g.R4.text()))
        t=termine()
        t.termine(str(g.nomeVar.text()),str(g.domX.text()),str(g.domY.text()),g.listaTerminiI.item(c,0).text(),g.listaTerminiI.item(c,1).text(),g.listaTerminiI.item(c,2).text(),g.listaTerminiI.item(c,3).text(),g.listaTerminiI.item(c,4).text())
        termI.append(t)
        g.NomeFuzzy.clear()
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        graficiI()
    else:
        flagRestr=1
        g.tastoDelTerm.setEnabled(True)
        g.tastoMod2.setEnabled(True)
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),0,QTableWidgetItem(g.NomeFuzzy.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),1,QTableWidgetItem(g.R1.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),2,QTableWidgetItem(g.R2.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),3,QTableWidgetItem(g.R3.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),4,QTableWidgetItem(g.R4.text()))
        graficiI()
        g.NomeFuzzy.clear()
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        g.listaTerminiI.clearSelection()
        modifica = 0

def addTerm():
    global contaT
    global modifica
    global flagRestr

    g.tastoAzz2.setVisible(False)
    g.tastoAzz.setVisible(True)
    if modifica == 0:
        if g.chkGauss.isChecked():
            g.chkTriangolo.setEnabled(False)
            g.chkTrap.setEnabled(False)
        elif g.chkTrap.isChecked():
            g.chkTriangolo.setEnabled(False)
            g.chkGauss.setEnabled(False)
        else:
            g.chkTrap.setEnabled(False)
            g.chkGauss.setEnabled(False)

        g.listaTerminiI.setItem(contaT,0,QTableWidgetItem(g.NomeFuzzy.text()))
        g.listaTerminiI.setItem(contaT,1,QTableWidgetItem(g.R1.text()))
        g.listaTerminiI.setItem(contaT,2,QTableWidgetItem(g.R2.text()))
        g.listaTerminiI.setItem(contaT,3,QTableWidgetItem(g.R3.text()))
        g.listaTerminiI.setItem(contaT,4,QTableWidgetItem(g.R4.text()))
        contaT += 1
        flagRestr=1
        g.NomeFuzzy.clear()
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        graficiI()
    else:
        flagRestr=1
        g.tastoAgg.setEnabled(True)
        g.tastoDelTerm.setEnabled(True)
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),0,QTableWidgetItem(g.NomeFuzzy.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),1,QTableWidgetItem(g.R1.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),2,QTableWidgetItem(g.R2.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),3,QTableWidgetItem(g.R3.text()))
        g.listaTerminiI.setItem(g.listaTerminiI.currentRow(),4,QTableWidgetItem(g.R4.text()))
        graficiI()
        g.NomeFuzzy.clear()
        g.R1.clear()
        g.R2.clear()
        g.R3.clear()
        g.R4.clear()
        g.listaTerminiI.clearSelection()
        modifica = 0

def modVar():
    global modifica
    global temp
    global temps1
    global temps2
    global temps3
    global temps4
    global flagRestr
    flag=0

    for item in g.listaTerminiI.selectedItems():
            print "selectedItems", item.text()
            flag=1
    if flag==0:
        g.msg.setText("Invalid selected row/Empty list")
        g.listaTerminiI.clearSelection()
        g.msg.show()
    else:
        g.tastoAzz.setIcon(g.iconaApply)
        g.tastoAzz2.setIcon(g.iconaApply)
        g.labelAddTerm.setText("MODIFY TERM:")
        if (str(g.listaTerminiI.item(g.listaTerminiI.currentRow(),3).text()) == "") and (str(g.listaTerminiI.item(g.listaTerminiI.currentRow(),4).text()) == ""):
            g.NomeFuzzy.setVisible(True)
            g.chkGauss.setChecked(True)
            g.R1.setVisible(True)
            g.R2.setVisible(True)
            g.R3.setVisible(False)
            g.R4.setVisible(False)
            g.R1.clear()
            g.R2.clear()
            g.R3.clear()
            g.R4.clear()
            g.NomeFuzzy.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),0).text())
            g.R1.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),1).text())
            g.R2.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),2).text())
            modifica=1
        elif  (str(g.listaTerminiI.item(g.listaTerminiI.currentRow(),4).text()) == ""):
            g.chkTriangolo.setChecked(True)
            g.NomeFuzzy.setVisible(True)
            g.R1.clear()
            g.R2.clear()
            g.R3.clear()
            g.R4.clear()
            g.NomeFuzzy.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),0).text())
            g.R1.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),1).text())
            g.R2.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),2).text())
            g.R3.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),3).text())
            modifica=1
            g.R1.setVisible(True)
            g.R2.setVisible(True)
            g.R3.setVisible(True)
            g.R4.setVisible(False)
        else :
            g.chkTrap.setChecked(True)
            g.NomeFuzzy.setVisible(True)
            g.R1.clear()
            g.R2.clear()
            g.R3.clear()
            g.R4.clear()
            g.NomeFuzzy.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),0).text())
            g.R1.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),1).text())
            g.R2.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),2).text())
            g.R3.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),3).text())
            g.R4.setText(g.listaTerminiI.item(g.listaTerminiI.currentRow(),4).text())
            modifica=1
            g.R1.setVisible(True)
            g.R2.setVisible(True)
            g.R3.setVisible(True)
            g.R4.setVisible(True)
        flagRestr=1
        g.tastoDelTerm.setEnabled(False)
        g.tastoAgg.setEnabled(False)
        g.tastoMod2.setEnabled(False)
        temp= g.NomeFuzzy.text()
        temps1=g.R1.text()
        temps2=g.R2.text()
        temps3=g.R3.text()
        temps4=g.R4.text()

def deleteVariable():
 flag=0
 for item in g.tabellaI.selectedItems():
        print "selectedItems", item.text()
        flag=1
 if flag==0:
    g.msg.setText("Invalid selected row/Empty list")
    g.msg.show()
    g.tabellaI.clearSelection()
 else:
    if ru.controlloRegole==1:
        warning=QtGui.QMessageBox.information(g.widget3, 'Warning', 'Do you really want to delete the variable? If confirmed you will be lost all rules', QtGui.QMessageBox.No | QtGui.QMessageBox.Yes)
        if warning==QtGui.QMessageBox.Yes :
            nomeVariabile=g.tabellaI.item(g.tabellaI.currentRow(),0).text()
            j=0
            cotare2=len(termI)
            while j<cotare2:
                if nomeVariabile==termI[j].getNomev():
                    del termI[j]
                    j=-1
                    cotare2=cotare2-1
                j=j+1
            i=0
            while i<len(varI):
                if nomeVariabile== varI[i].getNome():
                    del varI[i]
                    i=len(varI)
                i=i+1
            g.listReg.clear()
            g.picR_3.setVisible(True)
            g.picG_3.setVisible(False)
            g.tabellaI.removeRow(g.tabellaI.currentRow())
            ru.flagWarning=0
    else:
        nomeVariabile=g.tabellaI.item(g.tabellaI.currentRow(),0).text()
        j=0
        cotare2=len(termI)
        while j<cotare2:
            if nomeVariabile==termI[j].getNomev():
                del termI[j]
                j=-1
                cotare2=cotare2-1
            j=j+1
        i=0
        while i<len(varI):
            if nomeVariabile== varI[i].getNome():
                del varI[i]
                i=len(varI)
            i=i+1
        g.picR_3.setVisible(True)
        g.picG_3.setVisible(False)
        g.listReg.clear()
        g.tabellaI.removeRow(g.tabellaI.currentRow())
    cr.salvato=0
 if len(varI)==0 :
     g.picR_1.setVisible(True)
     g.picG_1.setVisible(False)

 else:
     g.picR_1.setVisible(False)
     g.picG_1.setVisible(True)

def deleteTerm():
 global contaT
 global flagRestr

 flag=0
 for item in g.listaTerminiI.selectedItems():
        print "selectedItems", item.text()
        flag=1
 if flag==0:
    g.msg.setText("Invalid selected row/Empty list")
    g.msg.show()
    g.listaTerminiI.clearSelection()
 elif contaT == 1:
    nomeTerm=g.listaTerminiI.item(g.listaTerminiI.currentRow(),0).text()
    i=0
    while i<len(termI):
        if nomeTerm== termI[i].getNomet():
            del termI[i]
            i=len(termI)
        i=i+1
    i=0
    cotare=g.listReg.count()
    esatto=g.nomeVar.text()+" IS "+nomeTerm
    while i<cotare:
        if str(esatto) in str(g.listReg.item(i).text()):
            g.listReg.takeItem(i)
            cotare=cotare-1
            i=-1
        i=i+1
    flagRestr=1
    g.listaTerminiI.removeRow(g.listaTerminiI.currentRow())
    contaT=contaT-1
    graficiI()
    g.chkTriangolo.setEnabled(True)
    g.chkTrap.setEnabled(True)
    g.chkGauss.setEnabled(True)
 else:
    nomeTerm=g.listaTerminiI.item(g.listaTerminiI.currentRow(),0).text()
    i=0
    while i<len(termI):
        if nomeTerm== termI[i].getNomet():
            del termI[i]
            i=len(termI)
        i=i+1
    flagRestr=1
    g.listaTerminiI.removeRow(g.listaTerminiI.currentRow())
    contaT=contaT-1
    graficiI()
    i=0
    cotare=g.listReg.count()
    esatto=g.nomeVar.text()+" IS "+nomeTerm
    while i<cotare:
            if str(esatto) in str(g.listReg.item(i).text()):
                g.listReg.takeItem(i)
                cotare=cotare-1
                i=-1
            i=i+1

def addVariabile():
  global contaT

  i=0
  if g.nomeVar.text() == "" or g.domY.text() == "" or g.domY.text() == "" or float(g.domX.text())>=float(g.domY.text()) or g.listaTerminiI.item(0,0) == None:
        g.msg.setText("Empty variable name field/domain fields ")
        g.msg.show()
  else:
    g.chkTriangolo.setEnabled(True)
    g.chkTrap.setEnabled(True)
    g.chkGauss.setEnabled(True)
    while i<contaT:
        t=termine()
        t.termine(str(g.nomeVar.text()),str(g.domX.text()),str(g.domY.text()),g.listaTerminiI.item(i,0).text(),g.listaTerminiI.item(i,1).text(),g.listaTerminiI.item(i,2).text(),g.listaTerminiI.item(i,3).text(),g.listaTerminiI.item(i,4).text())
        termI.append(t)
        i=i+1
    v=variabile()
    v.variabile(str(g.nomeVar.text()))
    varI.append(v)
    g.listaTerminiI.clear()
    g.NomeFuzzy.clear()
    g.nomeVar.clear()
    g.domX.clear()
    g.domY.clear()
    g.R1.clear()
    g.R2.clear()
    g.R3.clear()
    g.R4.clear()
    contaT=0
    cr.salvato=0
    g.picR_1.setVisible(False)
    g.picG_1.setVisible(True)
    g.widget2.close()
    g.widget.show()


def graficiI():
        global y1
        global y2
        global listaGaussI
        global listaTrianI
        global rv2
        global contaGraf

        listaPoly=[]
        listaGauss=[]
        y1=[]
        y2=[]
        plt.xlim(float(g.domX.text()), float(g.domY.text()))
        plt.ylim(0, 1.2)
        i=0
        c=0
        while i<g.listaTerminiI.rowCount():
            if (g.listaTerminiI.item(i,0)) == None:
                print "vuoto"
            else:
                c=c+1
            i=i+1
        i=0
        while i<c:
            if str(g.listaTerminiI.item(i,3).text()) == "" and str(g.listaTerminiI.item(i,4).text()) == "":
                medio = (float(str(g.listaTerminiI.item(i,1).text()))) + (float(str(g.listaTerminiI.item(i,2).text()))) / 2
                rv2 = norm(loc=medio, scale=.4)
                k = (np.arange(float(str(g.listaTerminiI.item(i,1).text())), (float(str(g.listaTerminiI.item(i,2).text()))), .00111))
                print k
                listaGauss.append(k)
                y2.append(rv2)
            elif str(g.listaTerminiI.item(i,4).text()) == "":
                listaPoly.append(float(str(g.listaTerminiI.item(i,1).text())))
                y1.append(0)
                listaPoly.append(float(str(g.listaTerminiI.item(i,2).text())))
                y1.append(1)
                listaPoly.append(float(str(g.listaTerminiI.item(i,3).text())))
                y1.append(0)
            else:
                listaPoly.append(float(str(g.listaTerminiI.item(i,1).text())))
                y1.append(0)
                listaPoly.append(float(str(g.listaTerminiI.item(i,2).text())))
                y1.append(1)
                listaPoly.append(float(str(g.listaTerminiI.item(i,3).text())))
                y1.append(1)
                listaPoly.append(float(str(g.listaTerminiI.item(i,4).text())))
                y1.append(0)
            i=i+1
        plt.plot(listaPoly, y1)
        i=0
        while i < len(listaGauss):
            plt.plot(listaGauss[i], y2[i].pdf(listaGauss[i]))
            i = i + 1
        plt.savefig(perc+str(contaGraf)+".png")
        img = Image.open(perc+str(contaGraf)+".png")
        img = img.resize((500,195), PIL.Image.ANTIALIAS)
        img.save(perc+str(contaGraf)+".png")
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(perc+str(contaGraf)+".png"))
        g.boxGrafico.setScene(scene)
        plt.close()
        os.remove(perc+str(contaGraf)+".png")
        contaGraf=contaGraf+1
        del listaPoly[0:len(listaPoly)]
        del y1[0:len(y1)]
        del listaGauss[0:len(listaGauss)]
        del y2[0:len(y2)]

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

def controlloTipo2():
    if g.chkBox2.isChecked():
        return 1
    else:
        return 0

def ControlloW2():
    if (g.nomeVar.text() == "" or g.NomeFuzzy.text() == "" or g.domX.text() == "" or g.domY.text() == ""):
        g.msg.setText("Empty variable name field/domain fields ")
        g.msg.show()
    else:
        if (is_numberF(str(g.domX.text())) == False or is_numberF(str(g.domY.text())) == False or float(
                    g.domX.text()) > float(g.domY.text())):
            g.msg.setText("Wrong variable domain field/empty field")
            g.msg.show()
        if (controlloGauss() == 1):
            if ( g.R1.text() == " " or g.R2.text() == " " or g.R1.text() == "" or g.R2.text() == ""):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                if (is_numberF(str(g.R1.text())) == False or is_numberF(str(g.R2.text())) == False or float(
                            g.R1.text()) < float(g.domX.text()) or float(g.R2.text()) > float(g.domY.text()) or float(
                            g.R1.text()) > float(g.R2.text())):
                    g.msg.setText("Wrong term domain field/empty field ")
                    g.msg.show()
                else:
                    addTerm()
                    g.labelAddTerm.setText("ADD TERM:")
                    g.tastoAzz.setIcon(g.iconaPiu)
                    g.tastoAzz2.setIcon(g.iconaPiu)

        elif (controlloTrian() == 1):
            if (is_numberF(str(g.R1.text())) == False or is_numberF(str(g.R2.text())) == False or is_numberF(
                    str(g.R3.text())) == False or float(g.R1.text()) < float(g.domX.text()) or float(g.R3.text()) > float(g.domY.text()) or g.R1.text() == "" or g.R2.text() == "" or g.R3.text() == "" or float(
                        g.R1.text()) > float(g.R2.text()) or float(g.R2.text()) > float(g.R3.text()) or float(
                        g.R1.text()) > float(g.R3.text())):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                addTerm()
                g.labelAddTerm.setText("ADD TERM:")
                g.tastoAzz.setIcon(g.iconaPiu)
                g.tastoAzz2.setIcon(g.iconaPiu)

        elif (controlloTrap() == 1):
            if (is_numberF(str(g.R1.text())) == False or is_numberF(str(g.R2.text())) == False or is_numberF(
                        str(g.R3.text())) == False or is_numberF(str(g.R4.text())) == False or float(g.R1.text()) < float(
                        g.domX.text()) or float(g.R4.text()) > float(
                        g.domY.text()) or g.R1.text() == "" or g.R2.text() == "" or g.R3.text() == "" or g.R4.text() == "" or float(
                        g.R1.text()) > float(g.R2.text()) or float(g.R2.text()) > float(g.R3.text()) or float(
                        g.R3.text()) > float(g.R4.text()) or float(g.R1.text()) > float(g.R4.text())):
                g.msg.setText("Wrong term domain field/empty field")
                g.msg.show()
            else:
                addTerm()
                g.labelAddTerm.setText("ADD TERM:")
                g.tastoAzz.setIcon(g.iconaPiu)
                g.tastoAzz2.setIcon(g.iconaPiu)

def ControlloW2_2():
    if (g.nomeVar.text() == "" or g.NomeFuzzy.text() == "" or g.domX.text() == "" or g.domY.text() == ""):
        g.msg.setText("Empty variable name field/domain fields ")
        g.msg.show()
    else:
        if (is_numberF(str(g.domX.text())) == False or is_numberF(str(g.domY.text())) == False or float(
                    g.domX.text()) > float(g.domY.text())):
            g.msg.setText("Wrong variable domain field/empty field")
            g.msg.show()
        if (controlloGauss() == 1):
            if ( g.R1.text() == " " or g.R2.text() == " " or g.R1.text() == "" or g.R2.text() == ""):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                if (is_numberF(str(g.R1.text())) == False or is_numberF(str(g.R2.text())) == False or float(g.R1.text()) < float(g.domX.text()) or float(g.R2.text()) > float(g.domY.text()) or float(
                            g.R1.text()) > float(g.R2.text())):
                    g.msg.setText("Wrong term domain field/empty field ")
                    g.msg.show()
                else:
                    addTerm2()
                    g.labelAddTerm.setText("ADD TERM:")
                    g.tastoAzz2.setIcon(g.iconaPiu)
                    g.tastoAzz.setIcon(g.iconaPiu)

        elif (controlloTrian() == 1):
            if (is_numberF(str(g.R1.text())) == False or is_numberF(str(g.R2.text())) == False or is_numberF(
                        str(g.R3.text())) == False or float(g.R1.text()) < float(g.domX.text()) or float(g.R3.text()) > float(
                        g.domY.text()) or g.R1.text() == "" or g.R2.text() == "" or g.R3.text() == "" or float(
                        g.R1.text()) > float(g.R2.text()) or float(g.R2.text()) > float(g.R3.text()) or float(
                        g.R1.text()) > float(g.R3.text())):
                g.msg.setText("Wrong term domain field/empty field ")
                g.msg.show()
            else:
                addTerm2()
                g.labelAddTerm.setText("ADD TERM:")
                g.tastoAzz2.setIcon(g.iconaPiu)
                g.tastoAzz.setIcon(g.iconaPiu)

        elif (controlloTrap() == 1):
            if (is_numberF(str(g.R1.text())) == False or is_numberF(str(g.R2.text())) == False or is_numberF(
                        str(g.R3.text())) == False or is_numberF(str(g.R4.text())) == False or float(g.R1.text()) < float(
                        g.domX.text()) or float(g.R4.text()) > float(
                        g.domY.text()) or g.R1.text() == "" or g.R2.text() == "" or g.R3.text() == "" or g.R4.text() == "" or float(
                        g.R1.text()) > float(g.R2.text()) or float(g.R2.text()) > float(g.R3.text()) or float(
                        g.R3.text()) > float(g.R4.text()) or float(g.R1.text()) > float(g.R4.text())):
                g.msg.setText("Wrong term domain field/empty field")
                g.msg.show()
            else:
                addTerm2()
                g.labelAddTerm.setText("ADD TERM:")
                g.tastoAzz2.setIcon(g.iconaPiu)
                g.tastoAzz.setIcon(g.iconaPiu)
#Variables
varI=[]
termI=[]
contaT=0
temp=""
tempNomeV=""
posizioneT=[]
posizioneV=[]
contaGraf=0
modifica = 0
termini={}
flagRestr=0


#Connect
g.menu.connect(g.tastoInput, QtCore.SIGNAL('clicked()'), varInput)
g.widget.connect(g.tastoMenu, QtCore.SIGNAL('clicked()'), home)
g.widget.connect(g.tastoPiu,QtCore.SIGNAL('clicked()'), addVar)
g.widget2.connect(g.tastoAzz,QtCore.SIGNAL('clicked()'), ControlloW2)
g.widget2.connect(g.tastoAzz2,QtCore.SIGNAL('clicked()'),ControlloW2_2)
g.widget2.connect(g.chkGauss,QtCore.SIGNAL('clicked()'), generaFunz)
g.widget2.connect(g.chkTrap,QtCore.SIGNAL('clicked()'), generaFunz)
g.widget2.connect(g.chkTriangolo,QtCore.SIGNAL('clicked()'), generaFunz)
g.widget2.connect(g.tastoMod,QtCore.SIGNAL('clicked()'), modVar)
g.widget2.connect(g.tastoAgg,QtCore.SIGNAL('clicked()'), addVariabile)
g.widgetTabI.connect(g.tastoDelVarI,QtCore.SIGNAL('clicked()'), deleteVariable)
g.widget2.connect(g.tastoDelTerm,QtCore.SIGNAL('clicked()'), deleteTerm)
g.widget.connect(g.tastoViewTab,QtCore.SIGNAL('clicked()'), viewInpVar)
g.widgetTabI.connect(g.tastoModI,QtCore.SIGNAL('clicked()'),appMod)
g.widget2.connect(g.tastoMod2,QtCore.SIGNAL('clicked()'), applicaMod)
g.widget2.connect(g.tastoMenu2,QtCore.SIGNAL('clicked()'),  menuWidg2)

sys.exit(g.app.exec_())
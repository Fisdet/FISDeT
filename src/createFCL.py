__author__ = 'Pasquadibisceglie-Zaza-Lovascio'

#Libraries
import FISDeT as g
import inputVariable2 as fi
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

from rule import *
import inference as inf

#Functions
def creaFcl():
 global salvato

 if g.picG_1.isVisible()==True and g.picG_2.isVisible()==True and g.picG_3.isVisible()==True:
  filename = QtGui.QFileDialog(g.menu)
  ok = filename.getSaveFileName(g.menu, "Save file", '', ".fcl")
  d2 = QFileInfo(ok).fileName()
  nomeFcl = d2
  f = str(ok)
  inf.percorso= str(f)
  if nomeFcl!="":
    outFile = open(inf.percorso, "w")
    outFile.write("FUNCTION_BLOCK dummy\n\n\tVAR_INPUT\n")
    i=0
    while i<len(fi.varI):
        j=0
        while j< len(fi.termI):
            if fi.varI[i].getNome()==fi.termI[j].getNomev():
                outFile.write("\t\t"+fi.varI[i].getNome()+" :\t REAL; (* RANGE("+fi.termI[j].getDomX()+" .. "+fi.termI[j].getDomY()+") *)\n")
                j=len(fi.termI)
            else:
                j=j+1
        i=i+1
    outFile.write("\tEND_VAR\n\n")
    outFile.write("\tVAR_OUTPUT\n")
    outFile.write("\t\t"+g.nomeVar3.text() + " : REAL; (* RANGE("+str(g.domX3.text())+" .. "+ str(g.domY3.text())+") *)\n")
    outFile.write("\tEND_VAR\n\n")
    i=0
    while i<len(fi.varI):
        outFile.write("\tFUZZIFY "+fi.varI[i].getNome()+"\n")
        j=0
        while j<len(fi.termI):
            if fi.varI[i].getNome()==fi.termI[j].getNomev():
                if fi.termI[j].membership == fi.MEMBERSHIP_SFUN:
                    outFile.write("\t\tTERM "+fi.termI[j].getNomet()+" := (" + fi.termI[j].getS1()+", 0) ("+fi.termI[j].getS2()+", 1) ;\n" )
                elif fi.termI[j].membership == fi.MEMBERSHIP_ZFUN:
                    outFile.write("\t\tTERM "+fi.termI[j].getNomet()+" := (" + fi.termI[j].getS1()+", 1) ("+fi.termI[j].getS2()+", 0) ;\n" )
                elif fi.termI[j].membership == fi.MEMBERSHIP_TRIANG:
                    outFile.write("\t\tTERM "+fi.termI[j].getNomet()+" := (" + fi.termI[j].getS1()+", 0) ("+fi.termI[j].getS2()+", 1) ("+fi.termI[j].getS3()+", 0) ;\n" )
                elif fi.termI[j].membership == fi.MEMBERSHIP_TRAP:
                    outFile.write("\t\tTERM "+fi.termI[j].getNomet()+" := (" + fi.termI[j].getS1()+", 0) ("+fi.termI[j].getS2()+", 1) ("+fi.termI[j].getS3()+", 1) ("+ fi.termI[j].getS4()+", 0) ;\n" )
            j=j+1
        outFile.write("\tEND_FUZZIFY\n\n")
        i=i+1
    outFile.write("\tDEFUZZIFY "+str(g.nomeVar3.text())+"\n")
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
        if (g.chkSing3.isVisible() and g.chkSing3.isChecked()) or g.chkclass.isChecked():
            outFile.write("\t\tTERM "+str(g.tabellaO.item(i,0).text())+" := "
                          + str(g.tabellaO.item(i,1).text())+ ";\n")
        elif g.chkSFun3.isVisible() and g.chkSFun3.isChecked():
            outFile.write("\t\tTERM "+str(g.tabellaO.item(i,0).text())+" := ("
                          + str(g.tabellaO.item(i,1).text())+", 0) ("
                          + str(g.tabellaO.item(i,2).text())+", 1) ;\n" )
        elif g.chkZFun3.isVisible() and g.chkZFun3.isChecked():
            outFile.write("\t\tTERM " + str(g.tabellaO.item(i, 0).text()) + " := ("
                          + str(g.tabellaO.item(i, 1).text()) + ", 1) ("
                          + str(g.tabellaO.item(i, 2).text()) + ", 0) ;\n")
        elif g.chkTriangolo3.isVisible() and g.chkTriangolo3.isChecked():
            outFile.write("\t\tTERM "+str(g.tabellaO.item(i,0).text())+" := ("
                          + str(g.tabellaO.item(i,1).text())+", 0) ("+str(g.tabellaO.item(i,2).text())
                          + ", 1) ("+str(g.tabellaO.item(i,3).text())+", 0) ;\n" )
        else:
            outFile.write("\t\tTERM "+str(g.tabellaO.item(i,0).text())+" := ("
                          + str(g.tabellaO.item(i,1).text())+", 0) ("+str(g.tabellaO.item(i,2).text())
                          + ", 1) ("+str(g.tabellaO.item(i,3).text())+", 1) ("
                          + str(g.tabellaO.item(i,4).text())+", 0) ;\n" )
        i=i+1
    if g.chkclass.isChecked()==True:
            outFile.write("\t\tACCU:"+g.comboAccu.currentText()+";\n")
            outFile.write("\t\tMETHOD:Dict;\n")
    else:
            outFile.write("\t\tACCU:MAX;\n")
            outFile.write("\t\tMETHOD:"+ g.comboDefuzzy.currentText()+";\n")

    if g.defaultValueText.isVisible() and g.defaultValueText.text():
        outFile.write("\t\tDEFAULT := " + str(g.defaultValueText.text()) + ";\n")
    else:
        outFile.write("\t\tDEFAULT := 0;\n")

    outFile.write("\tEND_DEFUZZIFY\n\n")
    outFile.write("\tRULEBLOCK first\n")
    outFile.write("\t\tAND:MIN;\n")
    i=0
    c=0
    while i<g.listReg.count():
        if (g.listReg.item(i)) == None:
            print "vuoto"
        else:
            c=c+1
        i=i+1
    i=0
    while i<g.listReg.count():
        outFile.write("\t\tRULE "+str(i)+":"+str(g.listReg.item(i).text())+"\n")
        i=i+1
    outFile.write("\tEND_RULEBLOCK\n\n")
    outFile.write("END_FUNCTION_BLOCK\n")
    salvato=1
    g.picG_4.setVisible(True)
    g.picR_4.setVisible(False)
  else:
      g.msg.setText("Invalid name")
      g.msg.show()
 else:
     g.msg.setText("You must create a valid system")
     g.msg.show()

#Variable
salvato=0

#Connect
g.menu.connect(g.tastoFcl, QtCore.SIGNAL('clicked()'), creaFcl)

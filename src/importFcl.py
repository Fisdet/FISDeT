__author__ = 'Pasquadibisceglie-Zaza-Lovascio'

# Libraries
import FISDeT as g
import inputVariable2 as fi
import outputVariable as fo
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import sys
import inference as inf
import os, errno
import matplotlib as plt
import os
import PIL
from PIL import Image
from createFCL import *
import outputVariable as ou
import rule as ru
import inputVariable2 as inp
import createFCL as cr

import re as regex


# Functions
def importFcl():
    global flagWarning

    filename = QtGui.QFileDialog(g.menu)
    ok = filename.getOpenFileName(g.menu, 'Open File', '', '(*.fcl)')
    f = str(ok)
    inf.percorso = f
    try:
        g.tabellaO.clear()
        fo.contaT = 0
        listaRegole = []
        outFile = open(inf.percorso, "rU")
        line = outFile.readline()
        azzera()
        while line:
            if "FUNCTION_BLOCK dummy" in line:
                line = outFile.readline()
            elif "VAR_INPUT" in line:
                line = outFile.readline()
            elif "END_VAR" in line:
                break
            else:
                idx1 = line.find("\t")
                idx2 = line.find(" :")
                nomeVariabile = line[idx1 + 2:idx2]
                idx3 = line.find("E(")
                idx4 = line.find(" .")
                dX = line[idx3 + 2:idx4]
                if dX == "":
                    print "vuoto"
                else:
                    x.append(dX)
                idx5 = line.find(". ")
                idx6 = line.find(")")
                dY = line[idx5 + 2:idx6]
                if dY == "":
                    print "vuoto"
                else:
                    y.append(dY)
                line = outFile.readline()
                if nomeVariabile == "":
                    print "vuoto"
                else:
                    v = fi.variabile()
                    v.variabile(nomeVariabile)
                    fi.varI.append(v)
        while line:
            if "VAR_OUTPUT" in line:
                line = outFile.readline()
            elif "END_VAR" in line:
                line = outFile.readline()
            elif "FUZZIFY" in line:
                break
            else:
                idx7 = line.find("\t")
                idx8 = line.find(" :")
                vout = line[idx7 + 2:idx8]
                if vout == "":
                    print "vuoto"
                else:
                    g.nomeVar3.setText(vout)
                idx9 = line.find("E(")
                idx10 = line.find(" .")
                dominioX = line[idx9 + 2:idx10]
                if dominioX == "":
                    print "vuoto"
                else:
                    g.domX3.setText(dominioX)
                idx11 = line.find(". ")
                idx12 = line.find(")")
                dominioY = line[idx11 + 2:idx12]
                if dominioY == "":
                    print "domY vuoto"
                else:
                    g.domY3.setText(dominioY)
                line = outFile.readline()
        indiceD = 0
        while line:
            if "DEFUZZIFY" in line:
                break
            elif "END_FUZZIFY" in line:
                indiceD = indiceD + 1
                line = outFile.readline()
            elif "FUZZIFY" in line:
                idx26 = line.find("FUZZIFY ")
                idx27 = line.find("\n")
                varTermine = line[idx26 + 8:idx27]
                line = outFile.readline()
            else:
                idx13 = line.find(" ")
                idx14 = line.find(" :")
                termine = line[idx13 + 1:idx14]
                occ = line.count(",")
                if occ == 4:
                    idx15 = line.find(" (")
                    idx16 = line.find(",")
                    t1i = line[idx15 + 2:idx16]
                    stringa0 = line[idx15 + 2:idx16]
                    stringa4 = line[(len(stringa0) + len(termine) + 18):]
                    idx23 = stringa4.find(",")
                    t2i = stringa4[0:idx23]
                    idx19 = line.find("1) (")
                    idx20 = line.find(" 1)")
                    stringa = line[idx19 + 4:]
                    idx21 = stringa.find(",")
                    t3i = stringa[0:idx21]
                    stringa2 = stringa[idx21 + 6:]
                    idx22 = stringa2.find(",")
                    t4i = stringa2[0:idx22]
                    termineNuovo = fi.termine()
                    termineNuovo.termine(varTermine, (x[indiceD]), (y[indiceD]), termine, t1i, t2i, t3i, t4i)
                    termineNuovo.membership = fi.MEMBERSHIP_TRAP
                    fi.termI.append(termineNuovo)
                elif occ == 3:
                    idx15 = line.find(" (")
                    idx16 = line.find(",")
                    t1i = line[idx15 + 2:idx16]
                    stringa0 = line[idx15 + 2:idx16]
                    stringa4 = line[(len(stringa0) + len(termine) + 18):]
                    idx23 = stringa4.find(",")
                    t2i = stringa4[0:idx23]
                    idx19 = line.find("1) (")
                    idx20 = line.find(" 1)")
                    stringa = line[idx19 + 4:]
                    idx21 = stringa.find(",")
                    t3i = stringa[0:idx21]
                    t4i = ""
                    termineNuovo = fi.termine()
                    termineNuovo.termine(varTermine, (x[indiceD]), (y[indiceD]), termine, t1i, t2i, t3i, t4i)
                    termineNuovo.membership = fi.MEMBERSHIP_TRIANG
                    fi.termI.append(termineNuovo)
                elif occ == 2:

                    number = line[line.find(",")+1:line.find(")")]
                    idx15 = line.find(" (")
                    idx16 = line.find(",")
                    t1i = line[idx15 + 2:idx16]
                    stringa0 = line[idx15 + 2:idx16]
                    stringa4 = line[(len(stringa0) + len(termine) + 18):]
                    idx23 = stringa4.find(",")
                    t2i = stringa4[0:idx23]
                    t3i = ""
                    t4i = ""
                    termineNuovo = fi.termine()
                    termineNuovo.termine(varTermine, (x[indiceD]), (y[indiceD]), termine, t1i, t2i, t3i, t4i)
                    fi.termI.append(termineNuovo)

                    if int(number) == 0:
                        termineNuovo.membership = fi.MEMBERSHIP_SFUN
                    elif int(number) == 1:
                        termineNuovo.membership = fi.MEMBERSHIP_ZFUN

                line = outFile.readline()
        c = 0
        while line:
            if "END_DEFUZZIFY" in line:
                break
            elif "DEFUZZIFY" in line:
                line = outFile.readline()
            elif "ACCU" in line:
                idx30 = line.find(":")
                idx31 = line.find(";")
                accu = line[idx30 + 1:idx31]
                line = outFile.readline()
            elif "METHOD" in line:
                idx30 = line.find(":")
                idx31 = line.find(";")
                metodo = line[idx30 + 1:idx31]
                if metodo == "COGS":
                    g.comboDefuzzy.addItem("COGS")
                elif metodo == "COG":
                    g.comboDefuzzy.addItem("COG")
                elif metodo == "LM":
                    g.comboDefuzzy.addItem("LM")
                elif metodo == "RM":
                    g.comboDefuzzy.addItem("RM")
                elif metodo == "MaxLeft":
                    g.comboDefuzzy.addItem("MaxLeft")
                elif metodo == "Dict":
                    flagWarning = 1
                    g.chkclass.setChecked(True)
                    ou.classificazione()
                    i = 0
                    c = 0
                    while i < g.tabellaO.rowCount():
                        if (g.tabellaO.item(i, 0)) == None:
                            print "vuota"
                        else:
                            c = c + 1
                        i = i + 1
                    g.labelNum.setText(str(c))
                else:
                    g.comboDefuzzy.addItem("MaxRight")
                line = outFile.readline()
            elif "DEFAULT" in line:
                # line = outFile.readline()
                default_index = line.find("DEFAULT")
                default_value = line[default_index:]
                default_value = default_value[:default_value.index(";")]

                # espressione regolare per recuperare il valore di default dalla stringa
                import re as regex
                default_value = regex.sub("( )*(DEFAULT)( |:=)+", "", default_value)

                g.defaultValueText.setText(default_value)
                line = outFile.readline()
            else:
                idx13 = line.find(" ")
                idx14 = line.find(" :")
                termine = line[idx13 + 1:idx14]
                if termine == "":
                    print "vuoto"
                else:
                    t = QtGui.QTableWidgetItem(str(termine))
                    g.tabellaO.setItem(c, 0, t)
                occ = line.count(",")
                if occ == 4:
                    idx15 = line.find(" (")
                    idx16 = line.find(",")
                    t1 = line[idx15 + 2:idx16]
                    stringa0 = line[idx15 + 2:idx16]
                    stringa4 = line[(len(stringa0) + len(termine) + 18):]
                    idx23 = stringa4.find(",")
                    t2 = stringa4[0:idx23]
                    idx19 = line.find("1) (")
                    idx20 = line.find(" 1)")
                    stringa = line[idx19 + 4:]
                    idx21 = stringa.find(",")
                    t3 = stringa[0:idx21]
                    stringa2 = stringa[idx21 + 6:]
                    idx22 = stringa2.find(",")
                    t4 = stringa2[0:idx22]
                    t_1 = QtGui.QTableWidgetItem(t1)
                    t_2 = QtGui.QTableWidgetItem(t2)
                    t_3 = QtGui.QTableWidgetItem(t3)
                    t_4 = QtGui.QTableWidgetItem(t4)
                    g.tabellaO.setItem(c, 1, t_1)
                    g.tabellaO.setItem(c, 2, t_2)
                    g.tabellaO.setItem(c, 3, t_3)
                    g.tabellaO.setItem(c, 4, t_4)
                    g.chkTrap3.setChecked(True)
                    g.chkTrap3.setEnabled(True)
                    g.chkTriangolo3.setEnabled(False)
                    g.chkSing3.setEnabled(False)
                    fo.generaFunzO()
                elif occ == 3:
                    idx15 = line.find(" (")
                    idx16 = line.find(",")
                    t1 = line[idx15 + 2:idx16]
                    stringa0 = line[idx15 + 2:idx16]
                    stringa4 = line[(len(stringa0) + len(termine) + 18):]
                    idx23 = stringa4.find(",")
                    t2 = stringa4[0:idx23]
                    idx19 = line.find("1) (")
                    idx20 = line.find(" 1)")
                    stringa = line[idx19 + 4:]
                    idx21 = stringa.find(",")
                    t3 = stringa[0:idx21]
                    t4 = ""
                    t_1 = QtGui.QTableWidgetItem(t1)
                    t_2 = QtGui.QTableWidgetItem(t2)
                    t_3 = QtGui.QTableWidgetItem(t3)
                    t_4 = QtGui.QTableWidgetItem(t4)
                    g.tabellaO.setItem(c, 1, t_1)
                    g.tabellaO.setItem(c, 2, t_2)
                    g.tabellaO.setItem(c, 3, t_3)
                    g.tabellaO.setItem(c, 4, t_4)
                    g.chkTriangolo3.setChecked(True)
                    g.chkTriangolo3.setEnabled(True)
                    g.chkTrap3.setEnabled(False)
                    g.chkSing3.setEnabled(False)
                    fo.generaFunzO()
                elif occ == 2:
                    idx15 = line.find(" (")
                    idx16 = line.find(",")
                    t1 = line[idx15 + 2:idx16]
                    stringa0 = line[idx15 + 2:idx16]
                    stringa4 = line[(len(stringa0) + len(termine) + 18):]
                    idx23 = stringa4.find(",")
                    t2 = stringa4[0:idx23]
                    t3 = ""
                    t4 = ""
                    t_1 = QtGui.QTableWidgetItem(t1)
                    t_2 = QtGui.QTableWidgetItem(t2)
                    t_3 = QtGui.QTableWidgetItem(t3)
                    t_4 = QtGui.QTableWidgetItem(t4)
                    g.tabellaO.setItem(c, 1, t_1)
                    g.tabellaO.setItem(c, 2, t_2)
                    g.tabellaO.setItem(c, 3, t_3)
                    g.tabellaO.setItem(c, 4, t_4)
                    g.chkTrap3.setEnabled(False)
                    g.chkTriangolo3.setEnabled(False)
                    g.chkSing3.setEnabled(False)
                    fo.generaFunzO()
                elif occ == 0:
                    idx24 = line.find(";")
                    t1 = line[len(termine) + 11:idx24]
                    t2 = ""
                    t3 = ""
                    t4 = ""
                    t_1 = QtGui.QTableWidgetItem(t1)
                    t_2 = QtGui.QTableWidgetItem(t2)
                    t_3 = QtGui.QTableWidgetItem(t3)
                    t_4 = QtGui.QTableWidgetItem(t4)
                    g.tabellaO.setItem(c, 1, t_1)
                    g.tabellaO.setItem(c, 2, t_2)
                    g.tabellaO.setItem(c, 3, t_3)
                    g.tabellaO.setItem(c, 4, t_4)
                    g.chkSing3.setChecked(True)
                    g.chkSing3.setEnabled(True)
                    g.chkTriangolo3.setEnabled(False)
                    g.chkTrap3.setEnabled(False)
                    fo.generaFunzO()
                fo.contaT = fo.contaT + 1
                c = c + 1
                line = outFile.readline()

        while line:
            line_nospace = regex.sub("[ \n\t]+", "", line)
            if line_nospace == "":
                line = outFile.readline()
            elif "END_DEFUZZIFY" in line_nospace:
                line = outFile.readline()
            elif "RULEBLOCK" in line_nospace:
                line = outFile.readline()
            elif "END_FUNCTION_BLOCK" in line_nospace:
                break
            elif "AND:MIN;" in line_nospace:
                line = outFile.readline()
            elif "(*ACCU:MAX;*)" in line_nospace:
                line = outFile.readline()
            else:
                idx25 = line.find(":")
                idx26 = line.find("\n")
                regola = line[idx25 + 1:idx26]
                listaRegole.append(regola)
                line = outFile.readline()
        if metodo == "Dict":
            g.chkclass.setEnabled(False)
            if accu == "BSUM":
                g.comboAccu.setCurrentIndex(1)
            else:
                g.comboAccu.setCurrentIndex(0)
        else:
            g.chkclass.setEnabled(False)

        i = 0
        while i < len(listaRegole):
            if listaRegole[i] != "":
                g.listReg.addItem(listaRegole[i])
            i = i + 1
        del listaRegole[0:len(listaRegole)]
        ru.controlloRegole = 1
        g.picG_1.setVisible(True)
        g.picG_2.setVisible(True)
        g.picG_3.setVisible(True)
        g.picG_4.setVisible(True)
        g.picR_6.setVisible(True)
        g.picR_1.setVisible(False)
        g.picR_2.setVisible(False)
        g.picR_3.setVisible(False)
        g.picR_4.setVisible(False)
        g.picG_6.setVisible(False)
        cr.salvato = 1
    except IOError, ioex:
        print 'errno:', ioex.errno
        print 'err code:', errno.errorcode[ioex.errno]
        g.msg.setText(os.strerror(ioex.errno))
        g.msg.show()


def classificazione2():
    global contaT
    global flagMod

    g.chkTrap3.setVisible(True)
    g.chkSing3.setVisible(True)
    g.chkTriangolo3.setVisible(True)
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
    g.testWidget.setFixedSize(760, 550)
    g.frameDict.setVisible(False)
    g.tabInfDict.setVisible(False)
    g.tastoMenuTest.setGeometry(650, 390, 75, 31)
    g.tabellaO.clear()
    g.nomeVar3.clear()
    g.labelNum.setText("0")


def azzera():
    del fi.varI[0:]
    del fi.termI[0:]
    del x[0:]
    del y[0:]
    if g.chkclass.isChecked() == True:
        g.chkclass.setChecked(False)
        classificazione2()
    inp.contaT = 0
    ou.nomeOut = ""
    g.listWvarO.clear()
    g.listReg.clear()
    g.listWvarI.clear()
    g.tabellaO.clear()
    g.tabellaI.clear()
    g.listaTerminiI.clear()
    g.tabInfReg.clear()
    g.tabInfOut.clear()
    g.tabInfDict.clear()


# Variables
x = []
y = []
flagWarning = 0

# Connect
g.menu.connect(g.tastoImport, QtCore.SIGNAL('clicked()'), importFcl)

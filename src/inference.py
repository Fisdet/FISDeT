__author__ = 'Pasquadibisceglie-Zaza-Lovascio'

# Libraries
import FISDeT as g
import inputVariable2 as fi
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
from multiprocessing import Pool
from PyQt4 import QtCore, QtGui
import sys
import os
import fuzzy.storage.fcl.Reader
import csv
from reviewSystem import *


# Functions
def apriInference():
    if g.picG_4.isVisible() == True:
        g.menu.close()
        g.frameDict.setTitle("Classes Result of " + str(g.nomeVar3.text()))
        g.tabInf.setColumnCount(len(fi.varI))
        g.tabInf.setGeometry(72, 60, 450, 70)
        g.tabInf.verticalHeader().hide()
        g.tabInfReg.setColumnCount(2)
        g.tabInfReg.setGeometry(72, 220, 450, 190)
        g.tabInfReg.verticalHeader().hide()
        g.tabInfReg.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
        g.tabInfReg.horizontalHeader().setDefaultSectionSize(224)
        nomeR = QTableWidgetItem("RULE")
        g.tabInfReg.setHorizontalHeaderItem(0, nomeR)
        nomeR = QTableWidgetItem("MEMBERSHIP")
        g.tabInfReg.setHorizontalHeaderItem(1, nomeR)
        g.tabInfOut.setGeometry(585, 60, 121, 70)
        g.tabInfOut.verticalHeader().hide()
        nomeO = QTableWidgetItem(g.nomeVar3.text())
        g.tabInfOut.setHorizontalHeaderItem(0, nomeO)
        g.tabInfOut.horizontalHeader().setDefaultSectionSize(119)
        i = 0
        conta = 0
        while i < len(fi.varI):
            j = 0
            while j < len(fi.termI):
                if fi.varI[i].getNome() == fi.termI[j].getNomev():
                    conta = conta + 1
                j = j + 1
            if conta == 0:
                boxT = QtGui.QLineEdit(g.testWidget)
                boxT.setGeometry(90, 150, 121, 21)
                boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(231,231,231);')
                boxT.setText("0.0")
                g.tabInf.setCellWidget(0, i, boxT)
                g.tabInf.cellWidget(0, i)
                nome = QTableWidgetItem(fi.varI[i].getNome())
                g.tabInf.setHorizontalHeaderItem(i, nome)
                g.tabInf.cellWidget(0, i).setEnabled(False)
            else:
                boxT = QtGui.QLineEdit(g.testWidget)
                boxT.setGeometry(90, 150, 121, 21)
                boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
                boxT.setValidator(g.valida2)
                g.tabInf.setCellWidget(0, i, boxT)
                g.tabInf.cellWidget(0, i)
                nome = QTableWidgetItem(fi.varI[i].getNome())
                g.tabInf.setHorizontalHeaderItem(i, nome)
            conta = 0
            i = i + 1
        g.tabInf.resizeColumnsToContents()
        g.tabInf.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
        g.tabInfOut.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
        g.testWidget.show()
    else:
        g.msg.setText("You must save the system")
        g.msg.show()


def main():
    global percorso
    import fuzzy.storage.fcl.Reader

    system = fuzzy.storage.fcl.Reader.Reader().load_from_file(percorso)
    output_values = {str(g.nomeVar3.text()): 0.0}
    input_val = {}
    i = 0
    j = 1
    while i < len(fi.varI):
        input_val[fi.varI[i].getNome()] = float(sys.argv[j])
        j = j + 1
        i = i + 1
    system.fuzzify(input_val)
    system.inference()
    g.tabInfReg.setRowCount(len(system.rules))
    g.tabInfReg.horizontalHeader().setDefaultSectionSize(224)
    g.tabInfReg.horizontalScrollBar().hide()
    i = 0
    while i < len(system.rules):
        boxT = QtGui.QLabel(g.testWidget)
        boxT.setGeometry(90, 150, 80, 21)
        boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
        boxT.setText("RULE " + str(i))
        g.tabInfReg.setCellWidget(i, 0, boxT)
        g.tabInf.cellWidget(i, 0)
        boxT = QtGui.QLabel(g.testWidget)
        boxT.setGeometry(90, 150, 80, 21)
        boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
        boxT.setText(str(round((system.rules["first." + str(i)].operator.__call__()), 3)))
        g.tabInfReg.setCellWidget(i, 1, boxT)
        g.tabInf.cellWidget(i, 1)
        i = i + 1
    if g.chkclass.isChecked() == True:
        ris = system.calculate(input_val, output_values)
        i = 0
        c = 0
        while i < g.tabellaO.rowCount():
            if (g.tabellaO.item(i, 0)) == None:
                print "vuoto"
            else:
                c = c + 1
            i = i + 1
        i = 0
        primo = float(ris[str(g.nomeVar3.text())][str(g.tabellaO.item(0, 0).text())])
        while i < c:
            if primo < float(ris[str(g.nomeVar3.text())][str(g.tabellaO.item(i, 0).text())]):
                primo = float(ris[str(g.nomeVar3.text())][str(g.tabellaO.item(i, 0).text())])
            i = i + 1
        i = 0
        while i < c:
            nomeClass = str(g.tabellaO.item(i, 0).text())
            header = QtGui.QTableWidgetItem()
            header.setText(nomeClass)
            g.tabInfDict.setHorizontalHeaderItem(i, header)
            valore = ris[str(g.nomeVar3.text())][str(g.tabellaO.item(i, 0).text())]
            boxT = QtGui.QLabel(g.testWidget)
            boxT.setGeometry(90, 150, 80, 21)
            if valore == primo:
                boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);font:25px')
            else:
                boxT.setStyleSheet('color: rgb(61,78,121);background-color: rgb(255,255,255);')
            boxT.setText(str(round((valore), 3)))
            g.tabInfDict.setCellWidget(0, i, boxT)
            i = i + 1
    else:
        ris = system.calculate(input_val, output_values)
        idx1 = str(ris).find(":")
        idx2 = str(ris).find("}")
        stringa = str(ris)[idx1 + 1:idx2]
        conversione = round(float((stringa)), 3)
        risultato = QTableWidgetItem(str(conversione))
        g.tabInfOut.setItem(0, 0, (risultato))
    del sys.argv[1:]


def carica():
    flagVuoto = 0
    i = 0
    while i < len(fi.varI):
        print str(g.tabInf.cellWidget(0, i).text())
        if str(g.tabInf.cellWidget(0, i).text()) == "" or str(",") in str(g.tabInf.cellWidget(0, i).text()):
            flagVuoto = 1
        else:
            flagVuoto = 0
        i = i + 1
    if g.chkclass.isChecked() == True:
        i = 0
        c = 0
        while i < g.tabellaO.rowCount():
            if (g.tabellaO.item(i, 0)) == None:
                print "vuoto"
            else:
                c = c + 1
            i = i + 1
        g.tabInfDict.setColumnCount(c)
        if flagVuoto == 1:
            g.msg.setText("Empty/Invalid fields")
            g.msg.show()
        else:
            i = 0
            j = 1
            conta = 0
            while i < len(fi.varI):
                z = 0
                while z < len(fi.termI):
                    if fi.varI[i].getNome() == fi.termI[z].getNomev():
                        conta = conta + 1
                    z = z + 1
                if conta == 0:
                    sys.argv.append(str(0))
                else:
                    sys.argv.append(str(g.tabInf.cellWidget(0, i).text()))
                    print sys.argv[j]
                    j = j + 1
                conta = 0
                i = i + 1
            g.picG_6.setVisible(True)
            g.picR_6.setVisible(False)
            main()
    else:
        if flagVuoto == 1:
            g.msg.setText("Empty/Invalid fields")
            g.msg.show()
        else:
            i = 0
            j = 1
            conta = 0
            while i < len(fi.varI):
                z = 0
                while z < len(fi.termI):
                    if fi.varI[i].getNome() == fi.termI[z].getNomev():
                        conta = conta + 1
                        print conta
                    z = z + 1
                if conta == 0:
                    sys.argv.append(str(0))
                else:
                    sys.argv.append(str(g.tabInf.cellWidget(0, i).text()))
                    print sys.argv[j]
                    j = j + 1
                conta = 0
                i = i + 1
            g.picG_6.setVisible(True)
            g.picR_6.setVisible(False)
            main()


def menuInference():
    g.testWidget.close()
    g.menu.show()


def import_data():
    global percorso

    orario = time
    try:
        fcl_file = open(percorso, "r")
        fcl_string = fcl_file.read()
        fcl_file.close()
        default_index = fcl_string.find("DEFAULT")

        # No Change, se non e' impostato un valore di default
        default_value = "NC"

        # se c'e' un valore di default salvato nel file FCL
        if default_index != -1:
            default_value = fcl_string[default_index:]
            default_value = default_value[:default_value.index(";")]

            # espressione regolare per recuperare il valore di default dalla stringa
            import re as regex
            default_value = regex.sub("( )*(DEFAULT)( |:=)+", "", default_value)

        # setting del FIS attraverso il parsing del FCL
        system = fuzzy.storage.fcl.Reader.Reader().load_from_file(percorso)
        filename = QtGui.QFileDialog(g.testWidget)
        ok = filename.getOpenFileName(g.testWidget, 'Open File', '', '(*.csv)')
        f = str(ok)
        perc2 = os.path.dirname(f)
        out_file = open(perc2 + "/Log-" + orario.strftime("%d-%m-%Y") + "-" + orario.strftime("%H.%M.%S") + ".csv", "a")
        input_val = {}
        cr = open(str(f), "rU")
        reader = csv.reader(cr)
        for row in reader:
            print row
        i = 0
        while i < len(fi.varI):
            z = 0
            cont = 0
            while z < len(fi.termI):
                if fi.varI[i].getNome() == fi.termI[z].getNomev():
                    cont = cont + 1
                z = z + 1
            print "coco"
            print cont
            if cont > 0:
                j = 0
                system.fuzzify(input_val)
                while j < len(fi.termI):
                    if fi.varI[i].getNome() == fi.termI[j].getNomev():
                        out_file.write(fi.varI[i].getNome() + "-" + fi.termI[j].getNomet() + ';')
                    j += 1
            i += 1
        i = 0
        while i < g.listReg.count():
            idx55 = str(system.rules['first.' + str(i)].adjective[0].getName(system)).find(",")
            trovaU = str(system.rules['first.' + str(i)].adjective[0].getName(system))[2:idx55]
            out_file.write("RULE " + str(i) + '-' + trovaU + ';')
            i += 1
        out_file.write("FINAL_RESULT;")
        out_file.write('\n')
        if len(row) == len(fi.varI):
            cr = open(str(f), "rU")
            reader = csv.reader(cr)

            # in questo punto effettua l'inferenza per tutti i dati
            for row in reader:
                i = 0
                while i < len(fi.varI):

                    # recupero il valore di input dal file csv
                    input_val[fi.varI[i].getNome()] = float(row[i])

                    j = 0

                    # effettua la fuzzificazione
                    system.fuzzify(input_val)
                    while j < len(fi.termI):
                        if fi.varI[i].getNome() == fi.termI[j].getNomev():

                            # scrive il risultato sul file per la corrispondente variabile
                            out_file.write(str(round(system.variables[fi.varI[i].getNome()]
                                                     .adjectives[fi.termI[j].getNomet()]
                                                     .getMembership(), 2)) + ';')
                        j += 1
                    i += 1

                # esegue l'inferenza per usando le regole
                system.inference()
                z = 0
                final_result = 0
                while z < g.listReg.count():

                    # scrive i risultati per tutte le regole sul file
                    result = round(system.rules['first.' + str(z)].operator.__call__(), 2)
                    if final_result < result:
                        final_result = result

                        # trova il nome della classe
                        idx55 = str(system.rules['first.' + str(z)].adjective[0].getName(system)).find(",")
                        class_name = str(system.rules['first.' + str(z)].adjective[0].getName(system))[2:idx55]

                    out_file.write(str(result))

                    print str(result) + "; ",
                    out_file.write(';')
                    z += 1

                # controllo sul valore finale di classificazione
                # se nessuna regola e' stata attivata i valori di appartenenza sono tutti pari a zero
                if final_result == 0:
                    try:
                        float(default_value)
                        final_result = 0.0
                    except ValueError:
                        final_result = default_value
                else:
                    final_result = class_name

                out_file.write(str(final_result) + ";")

                print '\n'
                out_file.write('\n')
                g.picG_6.setVisible(True)
                g.picR_6.setVisible(False)
                g.msg.setText("Inference completed")
                g.msg.show()
        else:
            out_file.write("\nERROR: invalid CSV")
            g.msg.setText("Invalid dataset")
            g.msg.show()
    except IOError, ioex:
        g.msg.setText(os.strerror(ioex.errno))
        g.msg.show()


# Variables
percorso = ""

# Connect
g.testWidget.connect(g.tastoTest, QtCore.SIGNAL('clicked()'), apriInference)
g.testWidget.connect(g.tastoRun, QtCore.SIGNAL('clicked()'), carica)
g.testWidget.connect(g.tastoMenuTest, QtCore.SIGNAL('clicked()'), menuInference)
g.testWidget.connect(g.tastoImportTest, QtCore.SIGNAL('clicked()'), import_data)

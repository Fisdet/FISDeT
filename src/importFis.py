__author__ = 'Lovascio'

import FISDeT as g
import inputVariable2 as fi
import outputVariable as ou
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import outputVariable as fo
import re
import importFcl
import os
import rule


def importFis():
    filename = QtGui.QFileDialog(g.menu)
    ok = filename.getOpenFileName(g.menu, 'Open File', '', '(*.fis)')
    complete_path = str(ok)

    if complete_path != "":
        try:
            g.tabellaO.clear()
            fo.contaT = 0
            out_file = open(complete_path, "r")
            fis_string = out_file.read()
            out_file.close()
            importFcl.azzera()

            # lettura della prima parte del FIS [System]
            # impostazione delle variabili utili alla lettura

            # numero variabili di input
            num_input = fis_string[fis_string.find("Ninputs"):]
            num_input = num_input[:num_input.find("\n")]
            num_input = re.sub("( )*(Ninputs)( |=)+", "", num_input)

            # numero variabili di output (FISDeT 2.5 permette una sola variabile di output)
            num_output = fis_string[fis_string.find("Noutputs"):]
            num_output = num_output[:num_output.find("\n")]
            num_output = re.sub("( )*(Noutputs)( |=)+", "", num_output)

            # numero di regole
            num_rule = fis_string[fis_string.find("Nrules"):]
            num_rule = num_rule[:num_rule.find("\n")]
            num_rule = re.sub("( )*(Nrules)( |=)+", "", num_rule)

            # matrice contenente per ogni variabile il corrispondente array di termin
            # E' usata per la generazione delle regole
            var_term_matrix = []

            # message dialog to round the values
            round_box = QtGui.QMessageBox()
            round_box.setText("Round values")
            round_box.setInformativeText("Do you want to round the membership value?")
            round_box.addButton(QtGui.QMessageBox.Yes)
            round_box.addButton(QtGui.QMessageBox.No)
            round_box.setDefaultButton(QtGui.QMessageBox.No)
            user_choise = round_box.exec_() == QtGui.QMessageBox.Yes

            # lettura delle variabili di input
            i = 1
            while i < int(num_input) + 1:
                tag = "[Input" + str(i) + "]"
                input_var = fis_string[fis_string.find(tag):]
                input_var = input_var[:input_var.find("\n\n")]

                # lettura del nome
                name_var = input_var[input_var.find("Name"):]
                name_var = name_var[:name_var.find("\n")]
                name_var = re.sub("( )*(Name)([ =]+)", "", name_var).replace("\'", "")

                input_variable = fi.variabile()
                input_variable.variabile(name_var)
                fi.varI.append(input_variable)

                # lettura del range (dominio)
                range_var = input_var[input_var.find("Range"):]
                range_var = range_var[:range_var.find("\n")]
                range_var = re.sub("( )*(Range)([ =]+)", "", range_var).\
                    replace("[", "").replace("]", "").\
                    split(",", 1)

                # controllo su 'active'
                active = input_var[input_var.find("Active"):]
                active = active[:active.find("\n")]
                active = re.sub("( )*(Active)([ =]+)", "", active).replace("\'", "")

                # lista di termini usata per la generazione delle regole
                term_list = []

                if active == "yes":

                    # lettura del numero di termini
                    term_num = input_var[input_var.find("NMFs"):]
                    term_num = term_num[:term_num.find("\n")]
                    term_num = re.sub("( )*(NMFs)([ =]+)", "", term_num)

                    # lettura dei termini
                    j = 1
                    while j < int(term_num) + 1:
                        tag = "MF" + str(j)
                        input_term = input_var[input_var.find(tag):]
                        input_term = input_term[:input_term.find("\n")]
                        input_term = re.sub("( )*(" + tag + ")([ =]+)", "", input_term)

                        idx = input_term.find(",")
                        term_prop = []
                        k = 0
                        while k < 2:
                            term_prop.append(input_term[:idx - 1].replace("'", ""))
                            input_term = input_term[idx + 1:]
                            idx = input_term.find(",", idx)
                            k += 1
                        term_prop.append(input_term.replace("[", "").replace("]", "").split(","))

                        term = fi.termine()
                        term.nomeV = name_var
                        term.nomeT = term_prop[0]
                        term.domX = range_var[0]
                        term.domY = range_var[1]

                        if term_prop[1] == "trapezoidal":
                            term.membership = fi.MEMBERSHIP_TRAP
                            term.s1 = term_prop[2][0].replace(" ", "")
                            term.s2 = term_prop[2][1].replace(" ", "")
                            term.s3 = term_prop[2][2].replace(" ", "")
                            term.s4 = term_prop[2][3].replace(" ", "")

                        elif term_prop[1] == "door":
                            term.membership = fi.MEMBERSHIP_TRAP
                            term.s1 = term_prop[2][0].replace(" ", "")
                            term.s2 = term_prop[2][0].replace(" ", "")
                            term.s3 = term_prop[2][1].replace(" ", "")
                            term.s4 = term_prop[2][1].replace(" ", "")

                        elif term_prop[1] == "SemiTrapezoidalInf":
                            term.membership = fi.MEMBERSHIP_TRAP
                            term.s1 = term_prop[2][0].replace(" ", "")
                            term.s2 = term_prop[2][0].replace(" ", "")
                            term.s3 = term_prop[2][1].replace(" ", "")
                            term.s4 = term_prop[2][2].replace(" ", "")

                        elif term_prop[1] == "SemiTrapezoidalSup":
                            term.membership = fi.MEMBERSHIP_TRAP
                            term.s1 = term_prop[2][0].replace(" ", "")
                            term.s2 = term_prop[2][1].replace(" ", "")
                            term.s3 = term_prop[2][2].replace(" ", "")
                            term.s4 = term_prop[2][2].replace(" ", "")

                        elif term_prop[1] == "triangular":
                            term.membership = fi.MEMBERSHIP_TRIANG
                            term.s1 = term_prop[2][0].replace(" ", "")
                            term.s2 = term_prop[2][1].replace(" ", "")
                            term.s3 = term_prop[2][2].replace(" ", "")

                        else:
                            raise Exception("Unsupported membership function!")

                        if user_choise:
                            if term.s1:
                                term.s1 = str(round(float(term.s1), 1))
                            if term.s2:
                                term.s2 = str(round(float(term.s2), 1))
                            if term.s3:
                                term.s3 = str(round(float(term.s3), 1))
                            if term.s4:
                                term.s4 = str(round(float(term.s4), 1))

                        fi.termI.append(term)
                        term_list.append(term)
                        j += 1

                    var_term_matrix.append(term_list)

                else:
                    term = fi.termine()
                    term.nomeV = name_var
                    term.domX = range_var[0]
                    term.domY = range_var[1]
                    fi.termI.append(term)
                    term_list.append(term)
                    var_term_matrix.append(term_list)

                i += 1

            # lista contenente per ogni termine di output il corrispondente nome
            # E' usata per la generazione delle regole
            output_term = []

            # lettura della variabile di output
            i = 1
            while i < int(num_output) + 1:
                tag = "[Output" + str(i) + "]"
                output_var = fis_string[fis_string.find(tag):]
                output_var = output_var[:output_var.find("\n\n")]

                # lettura del nome
                name_var = output_var[output_var.find("Name"):]
                name_var = name_var[:name_var.find("\n")]
                name_var = re.sub("( )*(Name)([ =]+)", "", name_var).replace("\'", "")

                # lettura del range (dominio)
                range_var = output_var[output_var.find("Range"):]
                range_var = range_var[:range_var.find("\n")]
                range_var = re.sub("( )*(Range)([ =]+)", "", range_var). \
                    replace("[", "").replace("]", ""). \
                    split(",", 1)

                g.domX3.setText(range_var[0])
                g.domY3.setText(range_var[1])

                # lettura di 'classif'
                classif = output_var[output_var.find("Classif"):]
                classif = classif[:classif.find("\n")]
                classif = re.sub("( )*(Classif)([ =]+)", "", classif).replace("\'", "")

                if classif == "yes":

                    # setting dell'interfaccia per la classificazione
                    importFcl.flagWarning = 1
                    g.chkclass.setChecked(True)
                    ou.classificazione()
                    g.chkclass.setEnabled(False)

                    # lettura del default
                    default = output_var[output_var.find("DefaultValue"):]
                    default = default[:default.find("\n")]
                    default = re.sub("( )*(DefaultValue)([ =]+)", "", default).replace("\'", "")
                    g.defaultValueText.setText(default)

                    # setting delle classi
                    j = int(float(range_var[0]))
                    while j <= int(float(range_var[1])):
                        name_term = "MF" + str(j) + "_OUT"
                        g.tabellaO.setItem(j - 1, 0, QtGui.QTableWidgetItem(str(name_term)))
                        g.tabellaO.setItem(j - 1, 1, QtGui.QTableWidgetItem(str(j)))
                        g.tabellaO.setItem(j - 1, 2, QtGui.QTableWidgetItem(""))
                        g.tabellaO.setItem(j - 1, 3, QtGui.QTableWidgetItem(""))
                        g.tabellaO.setItem(j - 1, 4, QtGui.QTableWidgetItem(""))

                        fo.contaT += 1
                        output_term.append(name_term)
                        j += 1

                    g.labelNum.setText(str(j))
                else:
                    raise Exception("Classification flag is set to 'No'!")

                g.nomeVar3.setText(name_var)

                i += 1

            # lettura delle regole
            tag = "[Rules]"
            rules = fis_string[fis_string.find(tag) + tag.__len__() + 1:]
            rules = rules[:rules.find("\n\n")]

            i = 0
            rules = rules.split(",\n")
            while i < int(num_rule):

                rule_line = rules[i]
                rule_line = rule_line.split(",")

                rule_string = "IF "
                j = 0
                while j < int(num_input):
                    if rule_line[j] != "0":
                        rule_string += \
                            "(" + fi.varI[j].nome + " IS " + var_term_matrix[j][int(rule_line[j]) - 1].nomeT + ")"
                    j += 1

                    if rule_line[j] == "0":
                        continue
                    elif j < int(num_input):
                        rule_string += " AND "
                    elif j == int(num_input):
                        rule_string += " THEN "
                        rule_string += \
                            "(" + str(g.nomeVar3.text()) + " IS " + output_term[int(float(rule_line[j])) - 1] + ");"

                g.listReg.addItem(rule_string)
                i += 1

            # controlli per l'interfaccia
            rule.controllaRegole = 1
            g.picG_1.setVisible(True)
            g.picG_2.setVisible(True)
            g.picG_3.setVisible(True)
            g.picG_4.setVisible(False)
            g.picG_6.setVisible(False)

            g.picR_1.setVisible(False)
            g.picR_2.setVisible(False)
            g.picR_3.setVisible(False)
            g.picR_4.setVisible(True)
            g.picR_6.setVisible(True)

        except IOError as error:
            g.msg.setText(os.strerror(error.errno))
            g.msg.show()
            resetGui()

        except ValueError as error:
            print error.message
            g.msg.setText("An error occured!")
            g.msg.show()
            resetGui()

        except Exception as error:
            g.msg.setText(error.message)
            g.msg.show()
            resetGui()


def resetGui():
    rule.controllaRegole = 0
    g.tabellaO.clear()
    fo.contaT = 0
    importFcl.azzera()
    g.picG_1.setVisible(False)
    g.picG_2.setVisible(False)
    g.picG_3.setVisible(False)
    g.picG_4.setVisible(False)
    g.picG_6.setVisible(False)
    g.picR_1.setVisible(True)
    g.picR_2.setVisible(True)
    g.picR_3.setVisible(True)
    g.picR_4.setVisible(True)
    g.picR_6.setVisible(True)
    g.chkclass.setEnabled(True)

g.menu.connect(g.tastoImportFis, QtCore.SIGNAL('clicked()'), importFis)

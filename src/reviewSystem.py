__author__ = 'Pasquadibisceglie-Zaza-Lovascio'

import FISDeT as g
import inputVariable2 as fi


# Functions
def review():
    g.frameWieO.setTitle("VIEW OUTPUT VARIABLE " + g.nomeVar3.text())
    print "cdcda"
    g.listWvarO.clear()
    g.listWvarI.clear()
    g.listWReg.clear()
    g.menu.close()
    g.widget5.show()
    conta = g.listReg.count()
    i = 0
    while i < conta:
        print str(g.listReg.item(i).text())
        g.listWReg.addItem(str(g.listReg.item(i).text()))
        i = i + 1
    i = 0
    while i < len(fi.termI):

        #trapezoidale
        if fi.termI[i].membership == fi.MEMBERSHIP_TRAP:
            g.listWvarI.addItem(
                fi.termI[i].getNomev() + " - " + fi.termI[i].getNomet() + " (" + fi.termI[i].getS1() + ",0) " + " (" +
                fi.termI[i].getS2() + ",1) " + " (" + fi.termI[i].getS3() + ",1) " + " (" + fi.termI[i].getS4() + ",0) "
            )

        #triangolare
        elif fi.termI[i].membership == fi.MEMBERSHIP_TRIANG:
            g.listWvarI.addItem(
                fi.termI[i].getNomev() + " - " + fi.termI[i].getNomet() + " (" + fi.termI[i].getS1() + ",0) " + " (" +
                fi.termI[i].getS2() + ",1) " + " (" + fi.termI[i].getS3() + ",0) ")

        #sfunction
        elif fi.termI[i].membership == fi.MEMBERSHIP_SFUN:
            g.listWvarI.addItem(
                fi.termI[i].getNomev() + " - " + fi.termI[i].getNomet() + " (" + fi.termI[i].getS1() + ",0) " + " (" +
                fi.termI[i].getS2() + ", 1)")

        #zfunction
        elif fi.termI[i].membership == fi.MEMBERSHIP_ZFUN:
            g.listWvarI.addItem(
                fi.termI[i].getNomev() + " - " + fi.termI[i].getNomet() + " (" + fi.termI[i].getS1() + ",1) " + " (" +
                fi.termI[i].getS2() + ", 0)")

        i += 1
    i = 0
    c = 0
    while i < g.tabellaO.rowCount():
        if (g.tabellaO.item(i, 0)) == None:
            print "vuota 2"
        else:
            c += 1
        i +=  1
    i = 0
    while i < c:

        #trapezoidale
        if g.tabellaO.item(i, 1).text() != "" and g.tabellaO.item(i, 2).text() != "" \
                and g.tabellaO.item(i, 3).text() != "" and g.tabellaO.item(i, 4).text() != "":

            g.listWvarO.addItem(
                str(g.tabellaO.item(i, 0).text()) + " (" + str(g.tabellaO.item(i, 1).text()) + ", 0) " + " (" +
                str(g.tabellaO.item(i, 2).text()) + ", 1) " + " (" + str(g.tabellaO.item(i, 3).text()) + ", 1) "
                + " (" + str(g.tabellaO.item(i, 4).text()) + ", 0) ")

        #triangolare
        elif g.tabellaO.item(i, 1).text() != "" and g.tabellaO.item(i, 2).text() != "" \
                and g.tabellaO.item(i, 3).text() != "" and g.tabellaO.item(i, 4).text() == "":

           g.listWvarO.addItem(
                str(g.tabellaO.item(i, 0).text()) + " (" + str(g.tabellaO.item(i, 1).text()) + ", 0) " + " (" + str(
                    g.tabellaO.item(i, 2).text()) + ", 1) " + " (" + str(g.tabellaO.item(i, 3).text()) + ", 0) ")

        #gaussiana
        elif g.tabellaO.item(i, 1).text() != "" and g.tabellaO.item(i, 2).text() != "" \
                and g.tabellaO.item(i,3).text() == "" and g.tabellaO.item(i, 4).text() == "":

            g.listWvarO.addItem(
                str(g.tabellaO.item(i, 0).text()) + " (mean: " + str(g.tabellaO.item(i, 1).text()) + ", sd: " + str(
                    g.tabellaO.item(i, 2).text()) + ") ")

        #singleton
        else:
            g.listWvarO.addItem(str(g.tabellaO.item(i, 0).text()) + " " + str(g.tabellaO.item(i, 1).text()))
        i += 1


def menu5():
    g.widget5.close()
    g.menu.show()


# Connect
g.menu.connect(g.tastoRew, g.QtCore.SIGNAL('clicked()'), review)
g.widget5.connect(g.tastoMenu5, g.QtCore.SIGNAL('clicked()'), menu5)

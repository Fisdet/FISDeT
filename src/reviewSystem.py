__author__ = 'Pasquadibisceglie-Zaza'

import FISDeT as g
import inputVariable2 as fi

#Functions
def review():
    g.frameWieO.setTitle("VIEW OUTPUT VARIABLE "+g.nomeVar3.text())
    print "cdcda"
    g.listWvarO.clear()
    g.listWvarI.clear()
    g.listWReg.clear()
    g.menu.close()
    g.widget5.show()
    conta = g.listReg.count()
    i=0
    while i<conta:
        print str(g.listReg.item(i).text())
        g.listWReg.addItem(str(g.listReg.item(i).text()))
        i=i+1
    i=0
    while i<len(fi.termI):
        if fi.termI[i].getS1()!="" and fi.termI[i].getS2()!="" and fi.termI[i].getS3()!="" and fi.termI[i].getS4()!="":
            g.listWvarI.addItem(fi.termI[i].getNomev()+" - "+fi.termI[i].getNomet()+" (0,"+fi.termI[i].getS1()+") "+" (1,"+fi.termI[i].getS2()+") "+" (1,"+fi.termI[i].getS3()+") "+" (0,"+fi.termI[i].getS4()+") ")
        elif fi.termI[i].getS1()!="" and fi.termI[i].getS2()!="" and fi.termI[i].getS3()!="" and fi.termI[i].getS4()=="":
            g.listWvarI.addItem(fi.termI[i].getNomev()+" - "+fi.termI[i].getNomet()+" (0,"+fi.termI[i].getS1()+") "+" (1,"+fi.termI[i].getS2()+") "+" (0,"+fi.termI[i].getS3()+") ")
        else:
            g.listWvarI.addItem(fi.termI[i].getNomev()+" - "+fi.termI[i].getNomet()+" (0,"+fi.termI[i].getS1()+") "+" (1,"+fi.termI[i].getS2()+")")
        i=i+1
    i=0
    c=0
    while i<g.tabellaO.rowCount():
            if (g.tabellaO.item(i,0)) == None:
                print "vuota 2"
            else:
                c=c+1
            i=i+1
    i=0
    while i<c:
        if g.tabellaO.item(i,1).text()!="" and g.tabellaO.item(i,2).text()!="" and g.tabellaO.item(i,3).text()!="" and g.tabellaO.item(i,4).text()!="":
            g.listWvarO.addItem(str(g.tabellaO.item(i,0).text())+" (0,"+str(g.tabellaO.item(i,1).text())+") "+" (1,"+str(g.tabellaO.item(i,2).text())+") "+" (1,"+str(g.tabellaO.item(i,3).text())+") "+" (0,"+str(g.tabellaO.item(i,4).text())+") ")
        elif g.tabellaO.item(i,1).text()!="" and g.tabellaO.item(i,2).text()!="" and g.tabellaO.item(i,3).text()!="" and g.tabellaO.item(i,4).text()=="":
            g.listWvarO.addItem(str(g.tabellaO.item(i,0).text())+" (0,"+str(g.tabellaO.item(i,1).text())+") "+" (1,"+str(g.tabellaO.item(i,2).text())+") "+" (1,"+str(g.tabellaO.item(i,3).text())+") ")
        elif g.tabellaO.item(i,1).text()!="" and g.tabellaO.item(i,2).text()!="" and g.tabellaO.item(i,3).text()=="" and g.tabellaO.item(i,4).text()=="":
            g.listWvarO.addItem(str(g.tabellaO.item(i,0).text())+" (0,"+str(g.tabellaO.item(i,1).text())+") "+" (1,"+str(g.tabellaO.item(i,2).text())+") ")
        else:
            g.listWvarO.addItem(str(g.tabellaO.item(i,0).text())+" "+str(g.tabellaO.item(i,1).text()))
        i=i+1

def menu5():
    g.widget5.close()
    g.menu.show()

#Connect
g.menu.connect(g.tastoRew, g.QtCore.SIGNAL('clicked()'), review )
g.widget5.connect(g.tastoMenu5, g.QtCore.SIGNAL('clicked()'), menu5)
import sys
import re
import math
import os
from PySide.QtGui import *

from EntryForm import *

class EntryApplication(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(EntryApplication, self).__init__(parent)
        self.setupUi(self)
        self.fnErr = 0
        self.lnErr = 0
        self.adErr = 0
        self.ctErr = 0
        self.stErr = 0
        self.zpErr = 0
        self.emErr = 0
        self.fn = ''
        self.ln = ''
        self.ad = ''
        self.ct = ''
        self.st = ''
        self.zp = ''
        self.em = ''

        self.btnClear.clicked.connect(self.clickedClear)
        self.enterText()
        self.btnSave.clicked.connect(self.clickedSave)
        self.btnLoad.clicked.connect(self.clickedLoad)
        
    def clickedClear(self):
        self.txtAddress.setText('')
        self.txtCity.setText('')
        self.txtEmail.setText('')
        self.txtFirstName.setText('')
        self.txtLastName.setText('')
        self.txtState.setText('')
        self.txtZip.setText('')
        self.fnErr = 0
        self.lnErr = 0
        self.addErr = 0
        self.ctyErr = 0
        self.stErr = 0
        self.zpErr = 0
        self.emErr = 0
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)

    def enterText(self):        
        self.fn = self.txtFirstName.text()
        self.ln = self.txtLastName.text()
        self.em = self.txtEmail.text()
        self.st = self.txtState.text()
        self.zp = self.txtZip.text()
        self.ad = self.txtAddress.text()
        self.ct = self.txtCity.text()
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)
        self.btnSave.clicked.connect(self.clickedSave)

    def clickedSave(self):
        if (self.checkForError(self.fn, self.ln, self.ad, self.ct, self.st, self.zp, self.em)):
            if (self.fnErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('First Name Error.')
            elif (self.lnErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('Last Name Error.')
            elif (self.adErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('Address Error.')
            elif (self.ctErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('City Error.')
            elif (self.stErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('State Error.')
            elif (self.zpErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('Zip code Error.')
            elif (self.emErr == 1):
                self.lblError.setEnabled(True)
                self.lblError.setText('Email Error.')
            else: #no error
                self.lblError.setEnabled(False)
                #now write it to an xml file
                fo = open('target.xml', 'w')
                fo.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
                fo.write("\n<user>\n")
                fo.write("    <FirstName>" + self.txtFirstName.text() + "</FirstName>\n")
                fo.write("    <LastName>" + self.txtLastName.text() + "</LastName>\n")
                fo.write("    <Address>" + self.txtAddress.text() + "</Address>\n")
                fo.write("    <City>" + self.txtCity.text() + "</City>\n")
                fo.write("    <State>" + self.txtState.text() + "</State>\n")
                fo.write("    <ZIP>" + self.txtZip.text() + "</ZIP>\n")
                fo.write("    <Email>" + self.txtEmail.text() + "</Email>\n")
                fo.write("</user>")

    def checkForError(self, fn, ln, ad, ct, st, zp, em):
        if (fn == ''):
            self.fnErr = 1
        else:
            self.fnErr = 0
        if (ln == ''):
            self.lnErr = 1
        else:
            self.lnErr = 0
        if (ad == ''):
            self.adErr = 1
        else:
            self.adErr = 0
        if (ct == ''):
            self.ctErr = 1
        else:
            self.ctErr = 0
        if (st == ''):
            self.stErr = 1
        if (st != ''):
            status = 0
            for i in range(0, len(states)):
                if st == states[i]:
                    status = 1
                    break
            if (status == 0):
                self.stErr = 1
            else:
                self.stErr = 0

        if (zp == ''):
            self.zpErr = 1
        if (zp != ''):
            if len(zp != 5):
                self.zpErr = 1
            else:
                m = re.search(r"([\d]{5})$", zp)
                if not m:
                    self.zpErr = 1
                else:
                    self.zpErr = 0

        if (em == ''):
            self.emErr = 1
        if (em != ''):
            m = re.search(r"\w+@\w+\.\w+", em)
            if not m:
                self.emErr = 1
            else:
                self.emErr = 0

        if (self.fnErr == 1) or (self.lnErr == 1) or (self.adErr == 1) or (self.ctErr == 1) or (self.stErr == 1) or (self.zpErr == 1) or (self.emErr == 1):
            return 1
        else:
            return 0
        
    def loadFromXmlFile(self, filePath):
        """
        Handling the loading of the data from the given file name. This method should only be  invoked by the
        'loadData' method.
        """
        #pass
        fi = open(filePath, 'r')
        fn = ''
        ln = ''
        ad = ''
        ct = ''
        st = ''
        zp = ''
        em = ''
        for lines in fi:
            if re.search(r"<FirstName>(?P<fn>[\w]+)</FirstName>", lines):
                fn = re.search(r"<FirstName>(?P<fn>[\w]+)</FirstName>", lines).group("fn")
                
            if re.search(r"<LastName>(?P<ln>[\w]+)</LastName>", lines):
                ln = re.search(r"<LastName>(?P<ln>[\w]+)</LastName>", lines).group("ln")
            
            if re.search(r"<Address>(?P<ad>[\w]+)</Address>", lines):
                ad = re.search(r"<Address>(?P<ad>[\w]+)</Address>", lines).group("ad")
            if re.search(r"<City>(?P<ct>[\w]+)</City>", lines):
                ct = re.search(r"<City>(?P<ct>[\w]+)</City>", lines).group("ct")
                
            if re.search(r"<State>(?P<st>[\w]+)</State>", lines):
                st = re.search(r"<State>(?P<st>[\w]+)</State>", lines).group("st")
            if re.search(r"<ZIP>(?P<fn>[\w]+)</ZIP>", lines):
                zp = re.search(r"<ZIP>(?P<zp>[\w]+)</ZIP>", lines).group("zp")
                
            if re.search(r"<Email>(?P<em>[\w]+)</Email>", lines):
                em = re.search(r"<Email>(?P<em>[\w]+)</Email>", lines).group("em")
        self.txtAddress.setText(ad)
        self.txtCity.setText(ct)
        self.txtEmail.setText(em)
        self.txtFirstName.setText(fn)
        self.txtLastName.setText(ln)
        self.txtState.setText(st)
        self.txtZip.setText(zp)
        

    def clickedLoad(self):
        self.loadData()


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD, OR THE TEST WILL NOT PASS! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadFromXmlFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = EntryApplication()

    currentForm.show()
    currentApp.exec_()

import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import pandas
import copy

# Create a QUiLoader instance to load .ui files
loader = QUiLoader()

# Initialize the QApplication
app = QtWidgets.QApplication(sys.argv)


class WhoToEdit(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentlyVisibleWidget = loader.load("database/windows/QEditWhichPreferences.ui", None)

        # Set the layout and add the loaded widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.currentlyVisibleWidget)
        self.setLayout(layout)

        # Find button and connect it to the setEditTeachers method
        goToEditTeachersButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "editTeachers")
        goToEditTeachersButton.clicked.connect(self.setEditTeachers)

        goToEditClassroomsButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "editClassrooms")
        goToEditClassroomsButton.clicked.connect(self.setEditClassrooms)

        comeBackButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "ComeBackButton")
        comeBackButton.clicked.connect(self.comeBackToMainWindow)

    def comeBackToMainWindow(self):
        # Switching back to main window properly
        self.parent().setCurrentWidget(self.parent().currentlyVisibleWidget)  # Use parent() for reference

    def setEditTeachers(self):
        # Switch to the 'openTeachers' widget
        self.parent().setCurrentWidget(self.parent().openTeachersWidget)  # Reference the instance

    def setEditClassrooms(self):
        # Switch to the 'openTeachers' widget
        self.parent().setCurrentWidget(self.parent().openClassroomsWidget)  # Reference the instance


class openTeachers(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the UI file
        self.currentlyVisibleWidget = loader.load("database/windows/QEditTeachers.ui", None)

        comeBackButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "ComeBackButton")
        comeBackButton.clicked.connect(self.comeBackToWhoToEdit)



        self.ComboBoxTeachers = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxTeachers")
        self.ComboBoxDeleteTeachers = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxDeleteTeachers")
        self.ComboBoxTeachers.addItem("ADD TEACHER")
        self.ComboBoxDeleteTeachers.addItem("WHICH TEACHER")
        dfTeachers = pandas.read_excel("database\data\dataTeachers.xlsx", "Sheet1")
        self.teachers = []
        for i in range(len(dfTeachers)):
          nameT = dfTeachers.iloc[i,0]
          screenT = dfTeachers.iloc[i,1]
          subject1T = dfTeachers.iloc[i,2]
          subject2T = dfTeachers.iloc[i,3]
          subject3T = dfTeachers.iloc[i,4]
          subject4T = dfTeachers.iloc[i,5]
          subject5T = dfTeachers.iloc[i,6]
          subject6T = dfTeachers.iloc[i,7]
          size1T = dfTeachers.iloc[i,8]
          size2T = dfTeachers.iloc[i,9]
          size3T = dfTeachers.iloc[i,10]
          size4T = dfTeachers.iloc[i,11]
          size5T = dfTeachers.iloc[i,12]
          size6T = dfTeachers.iloc[i,13]
          classroomPreferenceT = dfTeachers.iloc[i,14]

          
          self.teachers.append([
            str(nameT), 
            bool(screenT), 
            str(subject1T),
            str(subject2T),
            str(subject3T),
            str(subject4T),
            str(subject5T),
            str(subject6T),
            int(size1T),
            int(size2T),
            int(size3T),
            int(size4T),
            int(size5T),
            int(size6T),
            str(classroomPreferenceT)
          ])
        
        for i in range(len(self.teachers)):
          for j in range(len(self.teachers)-1-i):
            if (self.teachers[j][0] > self.teachers[j+1][0]):
              self.teachers[j], self.teachers[j+1] = self.teachers[j+1], self.teachers[j]

        for i in range(len(self.teachers)):
          self.ComboBoxTeachers.addItem(self.teachers[i][0])
          self.ComboBoxDeleteTeachers.addItem(self.teachers[i][0])
  


        self.textHolderNameT = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueName")

        self.textHolderNumberOfStudents = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "labelSumOfStudents")

        loadTeachersButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "loadTeachers")
        loadTeachersButton.clicked.connect(self.loadTeachersData)

 


        self.TeacherNameSaveLineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditName")
        self.TeacherSubject1ComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxSubject1")
        self.TeacherSubject2ComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxSubject2")
        self.TeacherSubject3ComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxSubject3")
        self.TeacherSubject4ComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxSubject4")
        self.TeacherSubject5ComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxSubject5")
        self.TeacherSubject6ComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxSubject6")

        TeacherSubject1SaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject1")
        TeacherSubject2SaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject2")
        TeacherSubject3SaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject3")
        TeacherSubject4SaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject4")
        TeacherSubject5SaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject5")
        TeacherSubject6SaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject6")

        TeacherSubject1SaveButton.clicked.connect(self.TeacherSubject1Clicked)
        TeacherSubject2SaveButton.clicked.connect(self.TeacherSubject2Clicked)
        TeacherSubject3SaveButton.clicked.connect(self.TeacherSubject3Clicked)
        TeacherSubject4SaveButton.clicked.connect(self.TeacherSubject4Clicked)
        TeacherSubject5SaveButton.clicked.connect(self.TeacherSubject5Clicked)
        TeacherSubject6SaveButton.clicked.connect(self.TeacherSubject6Clicked)

        self.textHolderScreenT = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valuseTScreen")
        self.textHolderScreenT = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valuseTScreen")
        self.textHolderSubject1T = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject1")
        self.textHolderSubject2T = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject2")
        self.textHolderSubject3T = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject3")
        self.textHolderSubject4T = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject4")
        self.textHolderSubject5T = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject5")
        self.textHolderSubject6T = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject6")



        self.TeacherSubject1SIZELineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSubject1Size")
        self.TeacherSubject2SIZELineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSubject2Size")
        self.TeacherSubject3SIZELineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSubject3Size")
        self.TeacherSubject4SIZELineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSubject4Size")
        self.TeacherSubject5SIZELineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSubject5Size")
        self.TeacherSubject6SIZELineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSubject6Size")

        TeacherSubject1SIZESaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject1Size")
        TeacherSubject2SIZESaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject2Size")
        TeacherSubject3SIZESaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject3Size")
        TeacherSubject4SIZESaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject4Size")
        TeacherSubject5SIZESaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject5Size")
        TeacherSubject6SIZESaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSubject6Size")

        TeacherSubject1SIZESaveButton.clicked.connect(self.TeacherSubject1SizeClicked)
        TeacherSubject2SIZESaveButton.clicked.connect(self.TeacherSubject2SizeClicked)
        TeacherSubject3SIZESaveButton.clicked.connect(self.TeacherSubject3SizeClicked)
        TeacherSubject4SIZESaveButton.clicked.connect(self.TeacherSubject4SizeClicked)
        TeacherSubject5SIZESaveButton.clicked.connect(self.TeacherSubject5SizeClicked)
        TeacherSubject6SIZESaveButton.clicked.connect(self.TeacherSubject6SizeClicked)

        self.textHolderSubject1SIZET = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject1Size")
        self.textHolderSubject2SIZET = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject2Size")
        self.textHolderSubject3SIZET = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject3Size")
        self.textHolderSubject4SIZET = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject4Size")
        self.textHolderSubject5SIZET = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject5Size")
        self.textHolderSubject6SIZET = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSubject6Size")
        




        TeacherScreenButtonFalse = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "TScreenFalse")
        TeacherScreenButtonFalse.clicked.connect(lambda: self.changeTeacherScreen(False))

        TeacherScreenButtonTrue = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "TScreenTrue")
        TeacherScreenButtonTrue.clicked.connect(lambda: self.changeTeacherScreen(True))

        TeacherNameSaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveName")
        TeacherNameSaveButton.clicked.connect(self.TeacherNameSave)

        deleteTeacherButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "deleteTeacher")
        deleteTeacherButton.clicked.connect(self.deleteTeacher)

        self.classroomPreferenceComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "classroomPreferenceComboBox")
        self.classroomPreferenceComboBox.addItem("Favourite classroom")



        #====================GATHER===SUBJECTS===================
        dfPrevious = pandas.read_excel("database\data\dataProg.xlsx", "Sheet1")
        dataGathered = [["path", "notifications"]]

        for i in range(len(dfPrevious)):
          dataGathered.append(dfPrevious.iloc[i].tolist())  

        file_path = dataGathered[1][0]
        try:
          RawDP1Schedule = pandas.read_excel(file_path, sheet_name="dp1")
          RawDP2Schedule = pandas.read_excel(file_path, sheet_name="dp2")
          ALLlessons_DP1_array_Gathered = []

          for day in range (len(RawDP1Schedule.columns)-2):
            for hour in range (10):
                cell = RawDP1Schedule.iloc[hour,day+2]
                ALLlessons_DP1_array_Gathered.append(cell)

          i = len(ALLlessons_DP1_array_Gathered) - 1
          while i >= 0:
            subjectCeck = str(ALLlessons_DP1_array_Gathered[i])
            if ("tok" in subjectCeck.lower()):
              del ALLlessons_DP1_array_Gathered[i] 
            i -= 1 

          JustLessons_DP1_array_sorted = []
          JustLessons_DP1_array_sorted.append("chose subject")
          for i in range(len(ALLlessons_DP1_array_Gathered)):
            presentOnList = False
            for j in range(len(JustLessons_DP1_array_sorted)):
              if (ALLlessons_DP1_array_Gathered[i] == JustLessons_DP1_array_sorted[j]):
                presentOnList = True
            if not(presentOnList) and pandas.notna(ALLlessons_DP1_array_Gathered[i]):
              JustLessons_DP1_array_sorted.append(ALLlessons_DP1_array_Gathered[i])

          for i in range(1, len(JustLessons_DP1_array_sorted)):
            for j in range(1, len(JustLessons_DP1_array_sorted)-i):
              if (JustLessons_DP1_array_sorted[j] > JustLessons_DP1_array_sorted[j+1]):
                JustLessons_DP1_array_sorted[j], JustLessons_DP1_array_sorted[j+1] = JustLessons_DP1_array_sorted[j+1], JustLessons_DP1_array_sorted[j]
          
          for i in range(1, len(JustLessons_DP1_array_sorted)):
            JustLessons_DP1_array_sorted[i] = JustLessons_DP1_array_sorted[i] + " DP 1"
          
          ALLlessons_DP2_array_Gathered = []

          for day in range (len(RawDP2Schedule.columns)-2):
            for hour in range (10):
                cell = RawDP2Schedule.iloc[hour,day+2]
                ALLlessons_DP2_array_Gathered.append(cell)


          i = len(ALLlessons_DP2_array_Gathered) - 1
          while i >= 0:
            subjectCeck = str(ALLlessons_DP2_array_Gathered[i])
            if ("tok" in subjectCeck.lower()):
              del ALLlessons_DP2_array_Gathered[i] 
            i -= 1 
          
          JustLessons_DP2_array_sorted = []
          JustLessons_DP2_array_sorted.append("chose subject")
          for i in range(len(ALLlessons_DP2_array_Gathered)):
            presentOnList = False
            for j in range(len(JustLessons_DP2_array_sorted)):
              if (ALLlessons_DP2_array_Gathered[i] == JustLessons_DP2_array_sorted[j]):
                presentOnList = True
            if not(presentOnList) and pandas.notna(ALLlessons_DP2_array_Gathered[i]):
              JustLessons_DP2_array_sorted.append(ALLlessons_DP2_array_Gathered[i])

          for i in range(1, len(JustLessons_DP2_array_sorted)):
            for j in range(1, len(JustLessons_DP2_array_sorted)-i):
              if (JustLessons_DP2_array_sorted[j] > JustLessons_DP2_array_sorted[j+1]):
                JustLessons_DP2_array_sorted[j], JustLessons_DP2_array_sorted[j+1] = JustLessons_DP2_array_sorted[j+1], JustLessons_DP2_array_sorted[j]
          
          for i in range(1, len(JustLessons_DP2_array_sorted)):
            JustLessons_DP2_array_sorted[i] = JustLessons_DP2_array_sorted[i] + " DP 2"  
          #====================GATHER===SUBJECTS===================
          for j in range(len(JustLessons_DP1_array_sorted)):
            self.TeacherSubject1ComboBox.addItem(JustLessons_DP1_array_sorted[j])
            self.TeacherSubject2ComboBox.addItem(JustLessons_DP1_array_sorted[j])
            self.TeacherSubject3ComboBox.addItem(JustLessons_DP1_array_sorted[j])
            self.TeacherSubject4ComboBox.addItem(JustLessons_DP1_array_sorted[j])
            self.TeacherSubject5ComboBox.addItem(JustLessons_DP1_array_sorted[j])
            self.TeacherSubject6ComboBox.addItem(JustLessons_DP1_array_sorted[j])

          for j in range(1, len(JustLessons_DP2_array_sorted)):
            self.TeacherSubject1ComboBox.addItem(JustLessons_DP2_array_sorted[j])
            self.TeacherSubject2ComboBox.addItem(JustLessons_DP2_array_sorted[j])
            self.TeacherSubject3ComboBox.addItem(JustLessons_DP2_array_sorted[j])
            self.TeacherSubject4ComboBox.addItem(JustLessons_DP2_array_sorted[j])
            self.TeacherSubject5ComboBox.addItem(JustLessons_DP2_array_sorted[j])
            self.TeacherSubject6ComboBox.addItem(JustLessons_DP2_array_sorted[j])

          
          
          dfClasrooms = pandas.read_excel("database\data\dataClassrooms.xlsx", "Sheet1")
          self.classrooms = [
            ["206", 22, True, "1A"],
            ["207", 21, False, "non"],
            ["208/209", 24, True, "non"],
            ["210", 14, False, "non"],
            ["211", 27, True, "2A"],
            ["212", 14, False, "2C"],
            ["213", 12, False, "non"],
            ["214", 12, True, "non"],
            ["215", 12, True, "non"],
            ["216", 6, False, "non"],
            ["218", 6, False, "non"]
          ]
          for i in range(len(dfClasrooms)):
            nameC = dfClasrooms.iloc[i,0]
            size = dfClasrooms.iloc[i,1]
            screenC = dfClasrooms.iloc[i,2]
            homeroom = dfClasrooms.iloc[i,3]
            self.classrooms[i] = [str(nameC), int(size), bool(screenC), str(homeroom)]

          for i in range(len(self.classrooms)):
            self.classroomPreferenceComboBox.addItem(self.classrooms[i][0])

          classroomPreferenceSaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveClassroomPreference")

          self.textHolderPreferedClassroom = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "classroomPreferenceLabel")
          
          classroomPreferenceSaveButton.clicked.connect(self.classroomPreference)

          addTeacherButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "addTeacher")
          addTeacherButton.clicked.connect(self.addTeachersData)

          comeBackButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "ComeBackButton")
          comeBackButton.clicked.connect(self.saveChangedProgress)

        except FileNotFoundError:
          self.errorComunicate("file not found")
          self.comeBackToWhoToEdit()








        # Set the layout and add the loaded widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.currentlyVisibleWidget)
        self.setLayout(layout)









    #=====================TEACHER====EDIT==============================
  
    def TeacherNameSave(self):
      text = self.TeacherNameSaveLineEdit.text()
      self.textHolderNameT.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][0] = text
      
      self.ComboBoxTeachers.clear()
      self.ComboBoxDeleteTeachers.clear()

      self.ComboBoxTeachers.addItem("ADD TEACHER")
      self.ComboBoxDeleteTeachers.addItem("WHICH TEACHER")
      
      self.ComboBoxTeachers.setCurrentIndex(0)
      self.ComboBoxDeleteTeachers.setCurrentIndex(0)

      for i in range(len(self.teachers)):
        self.ComboBoxTeachers.addItem(self.teachers[i][0])
        self.ComboBoxDeleteTeachers.addItem(self.teachers[i][0])


    def TeacherSubject1Clicked(self):
      text = self.TeacherSubject1ComboBox.currentText()
      if (text == "chose subject"):
        text = "subject name"
      self.textHolderSubject1T.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][2] = text
    
    
    def TeacherSubject2Clicked(self):
      text = self.TeacherSubject2ComboBox.currentText()
      if (text == "chose subject"):
        text = "subject name"
      self.textHolderSubject2T.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][3] = text
    
    def TeacherSubject3Clicked(self):
      text = self.TeacherSubject3ComboBox.currentText()
      if (text == "chose subject"):
        text = "subject name"
      self.textHolderSubject3T.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][4] = text

    def TeacherSubject4Clicked(self):
      text = self.TeacherSubject4ComboBox.currentText()
      if (text == "chose subject"):
        text = "subject name"
      self.textHolderSubject4T.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][5] = text

    def TeacherSubject5Clicked(self):
      text = self.TeacherSubject5ComboBox.currentText()
      if (text == "chose subject"):
        text = "subject name"
      self.textHolderSubject5T.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][6] = text

    def TeacherSubject6Clicked(self):
      text = self.TeacherSubject6ComboBox.currentText()
      if (text == "chose subject"):
        text = "subject name"
      self.textHolderSubject6T.setText(text)
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        self.teachers[TeachersIndex][7] = text

    def loadSumOfStudents(self, whichTeacher):
      sum = 0
      for j in range(8, 14):
        sum = sum + self.teachers[whichTeacher][j]
      self.textHolderNumberOfStudents.setText("number of students: " + str(sum))

    def TeacherSubject1SizeClicked(self):
      try:
        value = int(self.TeacherSubject1SIZELineEdit.text())
        self.textHolderSubject1SIZET.setText(str(value))
        if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
          self.teachers[TeachersIndex][8] = int(value)
          self.loadSumOfStudents(TeachersIndex) # I put it after update of subject size
      except ValueError:
        self.errorComunicate("inapropriate type")


    def TeacherSubject2SizeClicked(self):
      try:
        value = int(self.TeacherSubject2SIZELineEdit.text())
        self.textHolderSubject2SIZET.setText(str(value))
        if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
          self.teachers[TeachersIndex][9] = int(value)
          self.loadSumOfStudents(TeachersIndex)
      except ValueError:
        self.errorComunicate("inapropriate type")


    def TeacherSubject3SizeClicked(self):
      try:
        value = int(self.TeacherSubject3SIZELineEdit.text())
        self.textHolderSubject3SIZET.setText(str(value))
        if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
          self.teachers[TeachersIndex][10] = int(value)
          self.loadSumOfStudents(TeachersIndex)
      except ValueError:
        self.errorComunicate("inapropriate type")


    def TeacherSubject4SizeClicked(self):
      try:
        value = int(self.TeacherSubject4SIZELineEdit.text())
        self.textHolderSubject4SIZET.setText(str(value))
        if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
          self.teachers[TeachersIndex][11] = int(value)
          self.loadSumOfStudents(TeachersIndex)
      except ValueError:
        self.errorComunicate("inapropriate type")


    def TeacherSubject5SizeClicked(self):
      try:
        value = int(self.TeacherSubject5SIZELineEdit.text())
        self.textHolderSubject5SIZET.setText(str(value))
        if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
          self.teachers[TeachersIndex][12] = int(value)
          self.loadSumOfStudents(TeachersIndex)
      except ValueError:
        self.errorComunicate("inapropriate type")


    def TeacherSubject6SizeClicked(self):
      try:
        value = int(self.TeacherSubject6SIZELineEdit.text())
        self.textHolderSubject6SIZET.setText(str(value))
        if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
          self.teachers[TeachersIndex][13] = int(value)
          self.loadSumOfStudents(TeachersIndex)
      except ValueError:
        self.errorComunicate("inapropriate type")


    def classroomPreference(self):
      text = self.classroomPreferenceComboBox.currentText()
      if (text == "Favourite classroom"):
        text = "no preference"
      self.textHolderPreferedClassroom.setText(text)
      if (self.ComboBoxTeachers.currentText() != "Favourite classroom"):
        global TeachersIndex
        self.teachers[TeachersIndex][14] = text
    #=====================TEACHER====EDIT==============================


    def errorComunicate(self, whatError):
      messageText = ""
      requestText = ""
      if (whatError == "inapropriate type"):
        messageText = "inapropriate type of size"
        requestText = "please enter an integer"
         

      message = QtWidgets.QMessageBox()
      message.setWindowTitle("Error")
      message.setText(messageText)
      message.setInformativeText(requestText)
      message.setIcon(QtWidgets.QMessageBox.Critical)  
      message.setStandardButtons(QtWidgets.QMessageBox.Ok)
      message.exec()  


    #=====================SAVE====SCREEN==============================
    def changeTeacherScreen(self, boolean):
      self.textHolderScreenT.setText(str(boolean))
      if (self.ComboBoxTeachers.currentText() != "ADD TEACHER"):
        global TeachersIndex
        self.teachers[TeachersIndex][1] = boolean
  
  
    #=====================SAVE====SCREEN==============================




    #=====================ADD====TEACHER==============================
    def addTeachersData(self):

      nameCURRENT = self.textHolderNameT.text()
      screenCURRENT = self.textHolderScreenT.text()
      if (screenCURRENT == "True/False"):
        screenCURRENT = ""
      subjectsCURRENT = ["","","","","",""]
      subjectsCURRENT[0] = self.textHolderSubject1T.text()
      subjectsCURRENT[1] = self.textHolderSubject2T.text()
      subjectsCURRENT[2] = self.textHolderSubject3T.text()
      subjectsCURRENT[3] = self.textHolderSubject4T.text()
      subjectsCURRENT[4] = self.textHolderSubject5T.text()
      subjectsCURRENT[5] = self.textHolderSubject6T.text()
      
      size1T = int(self.textHolderSubject1SIZET.text())
      size2T = int(self.textHolderSubject2SIZET.text())
      size3T = int(self.textHolderSubject3SIZET.text())
      size4T = int(self.textHolderSubject4SIZET.text())
      size5T = int(self.textHolderSubject5SIZET.text())
      size6T = int(self.textHolderSubject6SIZET.text())

      favouriteClassroom = self.textHolderPreferedClassroom.text()

      self.teachers.append([str(nameCURRENT), 
        bool(screenCURRENT), 
        str(subjectsCURRENT[0]),
        str(subjectsCURRENT[1]),
        str(subjectsCURRENT[2]),
        str(subjectsCURRENT[3]),
        str(subjectsCURRENT[4]),
        str(subjectsCURRENT[5]),
        int(size1T),
        int(size2T),
        int(size3T),
        int(size4T),
        int(size5T),
        int(size6T),
        str(favouriteClassroom)
      ])
      addedTeacherIndex = len(self.teachers)-1
      print(self.teachers[addedTeacherIndex])
      self.ComboBoxTeachers.addItem(self.teachers[addedTeacherIndex][0])
      self.ComboBoxDeleteTeachers.addItem(self.teachers[addedTeacherIndex][0])

      self.TeacherNameSaveLineEdit.clear()
      self.textHolderScreenT.setText("True/False")
      self.TeacherSubject1ComboBox.setCurrentIndex(0)
      self.TeacherSubject2ComboBox.setCurrentIndex(0)
      self.TeacherSubject3ComboBox.setCurrentIndex(0)
      self.TeacherSubject4ComboBox.setCurrentIndex(0)
      self.TeacherSubject5ComboBox.setCurrentIndex(0)
      self.TeacherSubject6ComboBox.setCurrentIndex(0)
      
      self.ComboBoxTeachers.setCurrentIndex(0)
      self.ComboBoxDeleteTeachers.setCurrentIndex(0)
      
      self.textHolderNameT.setText("Teacher Name")
      self.textHolderScreenT.setText("True/False")
      self.textHolderSubject1T.setText("subject name")
      self.textHolderSubject2T.setText("subject name")
      self.textHolderSubject3T.setText("subject name")
      self.textHolderSubject4T.setText("subject name")
      self.textHolderSubject5T.setText("subject name")
      self.textHolderSubject6T.setText("subject name")
      self.textHolderSubject1SIZET.setText("0")
      self.textHolderSubject2SIZET.setText("0")
      self.textHolderSubject3SIZET.setText("0")
      self.textHolderSubject4SIZET.setText("0")
      self.textHolderSubject5SIZET.setText("0")
      self.textHolderSubject6SIZET.setText("0")
      self.TeacherSubject1SIZELineEdit.clear()
      self.TeacherSubject2SIZELineEdit.clear()
      self.TeacherSubject3SIZELineEdit.clear()
      self.TeacherSubject4SIZELineEdit.clear()
      self.TeacherSubject5SIZELineEdit.clear()
      self.TeacherSubject6SIZELineEdit.clear()
      for i in range(len(self.teachers)):
        for j in range(len(self.teachers)-1-i):
          if (self.teachers[j][0] > self.teachers[j+1][0]):
            self.teachers[j], self.teachers[j+1] = self.teachers[j+1], self.teachers[j]

    #=====================ADD====TEACHER==============================



    #=====================DELETE====TEACHER==============================
    def deleteTeacher(self):
      for i in range(len(self.teachers)):
        if (self.ComboBoxDeleteTeachers.currentText() == self.teachers[i][0]):
          del self.teachers[i]
          break
      self.ComboBoxTeachers.clear()
      self.ComboBoxDeleteTeachers.clear()

      self.ComboBoxTeachers.addItem("ADD TEACHER")
      self.ComboBoxDeleteTeachers.addItem("WHICH TEACHER")
      
      self.ComboBoxTeachers.setCurrentIndex(0)
      self.ComboBoxDeleteTeachers.setCurrentIndex(0)

      for i in range(len(self.teachers)):
        self.ComboBoxTeachers.addItem(self.teachers[i][0])
        self.ComboBoxDeleteTeachers.addItem(self.teachers[i][0])
      
      self.textHolderNameT.setText("Teacher Name")
      self.textHolderScreenT.setText("True/False")
      self.textHolderSubject1T.setText("subject name")
      self.textHolderSubject2T.setText("subject name")
      self.textHolderSubject3T.setText("subject name")
      self.textHolderSubject4T.setText("subject name")
      self.textHolderSubject5T.setText("subject name")
      self.textHolderSubject6T.setText("subject name")
      self.textHolderSubject1SIZET.setText("0")
      self.textHolderSubject2SIZET.setText("0")
      self.textHolderSubject3SIZET.setText("0")
      self.textHolderSubject4SIZET.setText("0")
      self.textHolderSubject5SIZET.setText("0")
      self.textHolderSubject6SIZET.setText("0")
    
    #=====================DELETE====TEACHER==============================

    #=====================LOAD====DATA==============================
    def loadTeachersData(self):
      global TeachersIndex
      TeachersIndex = -1
      print(self.ComboBoxTeachers.currentText())
      for i in range(len(self.teachers)):
        if (self.ComboBoxTeachers.currentText() == "ADD TEACHER"):
          self.textHolderNameT.setText("Teacher Name")
          self.textHolderScreenT.setText("True/False")
          self.textHolderSubject1T.setText("subject name")
          self.textHolderSubject2T.setText("subject name")
          self.textHolderSubject3T.setText("subject name")
          self.textHolderSubject4T.setText("subject name")
          self.textHolderSubject5T.setText("subject name")
          self.textHolderSubject6T.setText("subject name")
          self.textHolderSubject1SIZET.setText("0")
          self.textHolderSubject2SIZET.setText("0")
          self.textHolderSubject3SIZET.setText("0")
          self.textHolderSubject4SIZET.setText("0")
          self.textHolderSubject5SIZET.setText("0")
          self.textHolderSubject6SIZET.setText("0")
          self.TeacherSubject1ComboBox.setCurrentIndex(0)
          self.TeacherSubject2ComboBox.setCurrentIndex(0)
          self.TeacherSubject3ComboBox.setCurrentIndex(0)
          self.TeacherSubject4ComboBox.setCurrentIndex(0)
          self.TeacherSubject5ComboBox.setCurrentIndex(0)
          self.TeacherSubject6ComboBox.setCurrentIndex(0)
          self.TeacherSubject1SIZELineEdit.clear()
          self.TeacherSubject2SIZELineEdit.clear()
          self.TeacherSubject3SIZELineEdit.clear()
          self.TeacherSubject4SIZELineEdit.clear()
          self.TeacherSubject5SIZELineEdit.clear()
          self.TeacherSubject6SIZELineEdit.clear()
          self.textHolderNumberOfStudents.setText("number of students: 00")
          self.classroomPreferenceComboBox.setCurrentIndex(0)
          self.textHolderPreferedClassroom.setText("no preference")
        elif (self.ComboBoxTeachers.currentText() == self.teachers[i][0]):
          print(self.teachers[i])
          TeachersIndex = i
          self.textHolderNameT.setText(self.teachers[i][0])
          self.textHolderScreenT.setText(str(self.teachers[i][1]))
          self.textHolderSubject1T.setText(self.teachers[i][2])
          self.textHolderSubject2T.setText(self.teachers[i][3])
          self.textHolderSubject3T.setText(self.teachers[i][4])
          self.textHolderSubject4T.setText(self.teachers[i][5])
          self.textHolderSubject5T.setText(self.teachers[i][6])
          self.textHolderSubject6T.setText(self.teachers[i][7])
          self.textHolderSubject1SIZET.setText(str(self.teachers[i][8]))
          self.textHolderSubject2SIZET.setText(str(self.teachers[i][9]))
          self.textHolderSubject3SIZET.setText(str(self.teachers[i][10]))
          self.textHolderSubject4SIZET.setText(str(self.teachers[i][11]))
          self.textHolderSubject5SIZET.setText(str(self.teachers[i][12]))
          self.textHolderSubject6SIZET.setText(str(self.teachers[i][13]))
          self.TeacherSubject1ComboBox.setCurrentIndex(0)
          self.TeacherSubject2ComboBox.setCurrentIndex(0)
          self.TeacherSubject3ComboBox.setCurrentIndex(0)
          self.TeacherSubject4ComboBox.setCurrentIndex(0)
          self.TeacherSubject5ComboBox.setCurrentIndex(0)
          self.TeacherSubject6ComboBox.setCurrentIndex(0)
          self.TeacherSubject1SIZELineEdit.clear()
          self.TeacherSubject2SIZELineEdit.clear()
          self.TeacherSubject3SIZELineEdit.clear()
          self.TeacherSubject4SIZELineEdit.clear()
          self.TeacherSubject5SIZELineEdit.clear()
          self.TeacherSubject6SIZELineEdit.clear()
          self.classroomPreferenceComboBox.setCurrentIndex(0)
          self.textHolderPreferedClassroom.setText(str(self.teachers[i][14]))
          sum = 0
          for j in range(8, 14):
            sum = sum + self.teachers[i][j]
          self.textHolderNumberOfStudents.setText("number of students: " + str(sum))
          break
    
    
      
    #=====================LOAD====DATA==============================

    #====================SAVE=DATA=GATHERED===========================
    def saveChangedProgress(self):
      changedTeachers = []
      changedTeachers.append(["name", "screen", "subject1", "subject2", "subject3", "subject4", "subject5", "subject6", "size1", "size2", "size3", "size4", "size5", "size6", "class preference"])
      for i in range(len(self.teachers)):
        changedTeachers.append(self.teachers[i])
      dfTeach = pandas.DataFrame(changedTeachers[1:], columns=changedTeachers[0])
      dfTeach.to_excel("database\data\dataTeachers.xlsx", index=False)
      self.comeBackToWhoToEdit()
      
    #====================SAVE=DATA=GATHERED===========================






    def comeBackToWhoToEdit(self):
        # Switching back to AddPreferences widget properly
        self.parent().setCurrentWidget(self.parent().addPreferencesWidget)


class openClassrooms(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the UI file
        self.currentlyVisibleWidget = loader.load("database/windows/QEditClassrooms.ui", None)

        comeBackButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "ComeBackButton")
        comeBackButton.clicked.connect(self.saveChangedProgress)

        self.ComboBoxClassrooms = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "comboBoxClassrooms")
        dfClasrooms = pandas.read_excel("database\data\dataClassrooms.xlsx", "Sheet1")
        self.Clasroomindex = -1

        self.classrooms = [
          ["206", 22, True, "1A"],
          ["207", 21, False, "non"],
          ["208/209", 24, True, "non"],
          ["210", 14, False, "non"],
          ["211", 27, True, "2A"],
          ["212", 14, False, "2C"],
          ["213", 12, False, "non"],
          ["214", 12, True, "non"],
          ["215", 12, True, "non"],
          ["216", 6, False, "non"],
          ["218", 6, False, "non"]
        ]
        for i in range(len(dfClasrooms)):
          nameC = dfClasrooms.iloc[i,0]
          size = dfClasrooms.iloc[i,1]
          screenC = dfClasrooms.iloc[i,2]
          homeroom = dfClasrooms.iloc[i,3]
          self.classrooms[i] = [str(nameC), int(size), bool(screenC), str(homeroom)]

        self.ComboBoxClassrooms.addItem("CHOSE CLASSROOM")
        
        for i in range(len(self.classrooms)):
          self.ComboBoxClassrooms.addItem(self.classrooms[i][0])
        
        self.textHolderSizeC = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueSize")
        self.textHolderScreenC = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valuseCScreen")
        self.textHolderWhoseC = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueWhose")


        loadClassroomButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "loadClassrooms")
        loadClassroomButton.clicked.connect(self.loadClassroomData)

        saveClassroomSizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize")
        saveClassroomSizeButton.clicked.connect(self.saveClassroomSize)


        saveClassroomWhoseButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveWhose")
        saveClassroomWhoseButton.clicked.connect(self.saveClassroomWhose)


        lassroomScreenButtonFalse = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "CScreenFalse")
        lassroomScreenButtonFalse.clicked.connect(lambda: self.saveClassroomScreen(False))
        lassroomScreenButtonTrue = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "CScreenTrue")
        lassroomScreenButtonTrue.clicked.connect(lambda: self.saveClassroomScreen(True))




        dfPrevious = pandas.read_excel("database\data\dataProg.xlsx", "Sheet1")
        dataGathered = [["path", "notifications"]]

        for i in range(len(dfPrevious)):
          dataGathered.append(dfPrevious.iloc[i].tolist())  

        file_path = dataGathered[1][0]

        try:
          RawDP1Schedule = pandas.read_excel(file_path, sheet_name="dp1")
          RawDP2Schedule = pandas.read_excel(file_path, sheet_name="dp2")
          
          ALLlessons_DP1_array_Gathered = []

          for day in range (len(RawDP1Schedule.columns)-2):
            for hour in range (10):
                cell = RawDP1Schedule.iloc[hour,day+2]
                ALLlessons_DP1_array_Gathered.append(cell)

          i = len(ALLlessons_DP1_array_Gathered) - 1
          while i >= 0:
            subjectCeck = str(ALLlessons_DP1_array_Gathered[i])
            if not("tok" in subjectCeck.lower()):
              del ALLlessons_DP1_array_Gathered[i] 
            i -= 1 

          JustTOK_DP1_array_sorted = []
          for i in range(len(ALLlessons_DP1_array_Gathered)):
            presentOnList = False
            for j in range(len(JustTOK_DP1_array_sorted)):
              if (ALLlessons_DP1_array_Gathered[i] == JustTOK_DP1_array_sorted[j]):
                presentOnList = True
            if not(presentOnList):
              JustTOK_DP1_array_sorted.append(ALLlessons_DP1_array_Gathered[i])

          for i in range(len(JustTOK_DP1_array_sorted)):
            for j in range(len(JustTOK_DP1_array_sorted)-i-1):
              if (JustTOK_DP1_array_sorted[j] > JustTOK_DP1_array_sorted[j+1]):
                JustTOK_DP1_array_sorted[j], JustTOK_DP1_array_sorted[j+1] = JustTOK_DP1_array_sorted[j+1], JustTOK_DP1_array_sorted[j]
          
          for i in range(len(JustTOK_DP1_array_sorted)):
            JustTOK_DP1_array_sorted[i] = JustTOK_DP1_array_sorted[i] + " DP 1"
          

          ALLlessons_DP2_array_Gathered = []

          for day in range (len(RawDP2Schedule.columns)-2):
            for hour in range (10):
                cell = RawDP2Schedule.iloc[hour,day+2]
                ALLlessons_DP2_array_Gathered.append(cell)

          i = len(ALLlessons_DP2_array_Gathered) - 1
          while i >= 0:
            subjectCeck = str(ALLlessons_DP2_array_Gathered[i])
            if not("tok" in subjectCeck.lower()):
              del ALLlessons_DP2_array_Gathered[i] 
            i -= 1 

          JustTOK_DP2_array_sorted = []
          for i in range(len(ALLlessons_DP2_array_Gathered)):
            presentOnList = False
            for j in range(len(JustTOK_DP2_array_sorted)):
              if (ALLlessons_DP2_array_Gathered[i] == JustTOK_DP2_array_sorted[j]):
                presentOnList = True
            if not(presentOnList):
              JustTOK_DP2_array_sorted.append(ALLlessons_DP2_array_Gathered[i])

          for i in range(len(JustTOK_DP2_array_sorted)):
            for j in range(len(JustTOK_DP2_array_sorted)-i-1):
              if (JustTOK_DP2_array_sorted[j] > JustTOK_DP2_array_sorted[j+1]):
                JustTOK_DP2_array_sorted[j], JustTOK_DP2_array_sorted[j+1] = JustTOK_DP2_array_sorted[j+1], JustTOK_DP2_array_sorted[j]
          
          for i in range(len(JustTOK_DP2_array_sorted)):
            JustTOK_DP2_array_sorted[i] = JustTOK_DP2_array_sorted[i] + " DP 2"
          
          ALLTOKs = [""] * 18
          lastDP1TOK = 0
          for i in range(len(JustTOK_DP1_array_sorted)):
            ALLTOKs[i] = JustTOK_DP1_array_sorted[i]
            lastDP1TOK = i
          
          for i in range(len(JustTOK_DP2_array_sorted)):
            ALLTOKs[lastDP1TOK+i+1] = JustTOK_DP2_array_sorted[i]
          
          #====================GATHER===SUBJECTS===================

          dfTOKteacher = pandas.read_excel("database\data\dataTOKTeacher.xlsx", "Sheet1")
          
          self.TOKTeacherData = []
          loadTOKteacherClassroomPreference = True
          self.TOKTeacherClassroomPreference = ""
          if (loadTOKteacherClassroomPreference):
            self.TOKTeacherClassroomPreference
            valueOfTOKpreference = dfTOKteacher.iloc[0,2]
            if isinstance(valueOfTOKpreference, str):
              self.TOKTeacherClassroomPreference = valueOfTOKpreference
            else: 
              self.TOKTeacherClassroomPreference = str(int(valueOfTOKpreference))
            loadTOKteacherClassroomPreference = False
          
          self.TOKTeacherClassroomPreferenceLabel = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "classroomPreferenceLabel")
          self.TOKTeacherClassroomPreferenceLabel.setText(self.TOKTeacherClassroomPreference)
          for i in range(18):
            subjectName = dfTOKteacher.iloc[i,0]
            size = dfTOKteacher.iloc[i,1]
            self.TOKTeacherData.append([str(subjectName), int(size)])

          for i in range(18):
            if (ALLTOKs[i] == ""):
              self.TOKTeacherData[i][0] = "no"
            else:
              self.TOKTeacherData[i][0] = ALLTOKs[i]

          whichTOKLabel1 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK1")
          whichTOKLabel1.setText(ALLTOKs[0])    
          whichTOKLabel2 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK2")
          whichTOKLabel2.setText(ALLTOKs[1])    
          whichTOKLabel3 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK3")
          whichTOKLabel3.setText(ALLTOKs[2])    
          whichTOKLabel4 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK4")
          whichTOKLabel4.setText(ALLTOKs[3])    
          whichTOKLabel5 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK5")
          whichTOKLabel5.setText(ALLTOKs[4])    
          whichTOKLabel6 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK6")
          whichTOKLabel6.setText(ALLTOKs[5])    
          whichTOKLabel7 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK7")
          whichTOKLabel7.setText(ALLTOKs[6])    
          whichTOKLabel8 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK8")
          whichTOKLabel8.setText(ALLTOKs[7])    
          whichTOKLabel9 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK9")
          whichTOKLabel9.setText(ALLTOKs[8])    
          whichTOKLabel10 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK10")
          whichTOKLabel10.setText(ALLTOKs[9])    
          whichTOKLabel11 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK11")
          whichTOKLabel11.setText(ALLTOKs[10])    
          whichTOKLabel12 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK12")
          whichTOKLabel12.setText(ALLTOKs[11])    
          whichTOKLabel13 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK13")
          whichTOKLabel13.setText(ALLTOKs[12])    
          whichTOKLabel14 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK14")
          whichTOKLabel14.setText(ALLTOKs[13])    
          whichTOKLabel15 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK15")
          whichTOKLabel15.setText(ALLTOKs[14])    
          whichTOKLabel16 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK16")
          whichTOKLabel16.setText(ALLTOKs[15])    
          whichTOKLabel17 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK17")
          whichTOKLabel17.setText(ALLTOKs[16])    
          whichTOKLabel18 = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "whichTOK18")
          whichTOKLabel18.setText(ALLTOKs[17])
          
          
          

          saveTOK1sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize1")
          self.sizeTOK1LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents1")
          self.textHolderTOK1Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize1")


          saveTOK2sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize2")
          saveTOK3sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize3")
          saveTOK4sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize4")
          saveTOK5sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize5")
          saveTOK6sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize6")
          saveTOK7sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize7")
          saveTOK8sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize8")
          saveTOK9sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize9")
          saveTOK10sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize10")
          saveTOK11sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize11")
          saveTOK12sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize12")
          saveTOK13sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize13")
          saveTOK14sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize14")
          saveTOK15sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize15")
          saveTOK16sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize16")
          saveTOK17sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize17")
          saveTOK18sizeButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveSize18")
          

          
          self.sizeTOK2LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents2")
          self.sizeTOK3LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents3")
          self.sizeTOK4LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents4")
          self.sizeTOK5LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents5")
          self.sizeTOK6LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents6")
          self.sizeTOK7LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents7")
          self.sizeTOK8LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents8")
          self.sizeTOK9LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents9")
          self.sizeTOK10LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents10")
          self.sizeTOK11LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents11")
          self.sizeTOK12LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents12")
          self.sizeTOK13LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents13")
          self.sizeTOK14LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents14")
          self.sizeTOK15LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents15")
          self.sizeTOK16LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents16")
          self.sizeTOK17LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents17")
          self.sizeTOK18LineEdit = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "numberOfStudents18")
          

          
          self.textHolderTOK2Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize2")
          self.textHolderTOK3Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize3")
          self.textHolderTOK4Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize4")
          self.textHolderTOK5Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize5")
          self.textHolderTOK6Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize6")
          self.textHolderTOK7Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize7")
          self.textHolderTOK8Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize8")
          self.textHolderTOK9Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize9")
          self.textHolderTOK10Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize10")
          self.textHolderTOK11Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize11")
          self.textHolderTOK12Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize12")
          self.textHolderTOK13Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize13")
          self.textHolderTOK14Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize14")
          self.textHolderTOK15Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize15")
          self.textHolderTOK16Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize16")
          self.textHolderTOK17Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize17")
          self.textHolderTOK18Size = self.currentlyVisibleWidget.findChild(QtWidgets.QLabel, "valueOfsize18")

          self.textHolderTOK1Size.setText(str(self.TOKTeacherData[0][1]))
          self.textHolderTOK2Size.setText(str(self.TOKTeacherData[1][1]))
          self.textHolderTOK3Size.setText(str(self.TOKTeacherData[2][1]))
          self.textHolderTOK4Size.setText(str(self.TOKTeacherData[3][1]))
          self.textHolderTOK5Size.setText(str(self.TOKTeacherData[4][1]))
          self.textHolderTOK6Size.setText(str(self.TOKTeacherData[5][1]))
          self.textHolderTOK7Size.setText(str(self.TOKTeacherData[6][1]))
          self.textHolderTOK8Size.setText(str(self.TOKTeacherData[7][1]))
          self.textHolderTOK9Size.setText(str(self.TOKTeacherData[8][1]))
          self.textHolderTOK10Size.setText(str(self.TOKTeacherData[9][1]))
          self.textHolderTOK11Size.setText(str(self.TOKTeacherData[10][1]))
          self.textHolderTOK12Size.setText(str(self.TOKTeacherData[11][1]))
          self.textHolderTOK13Size.setText(str(self.TOKTeacherData[12][1]))
          self.textHolderTOK14Size.setText(str(self.TOKTeacherData[13][1]))
          self.textHolderTOK15Size.setText(str(self.TOKTeacherData[14][1]))
          self.textHolderTOK16Size.setText(str(self.TOKTeacherData[15][1]))
          self.textHolderTOK17Size.setText(str(self.TOKTeacherData[16][1]))
          self.textHolderTOK18Size.setText(str(self.TOKTeacherData[17][1]))

          saveTOK1sizeButton.clicked.connect(self.changeTOK1Size)
          saveTOK2sizeButton.clicked.connect(self.changeTOK2Size)
          saveTOK3sizeButton.clicked.connect(self.changeTOK3Size)
          saveTOK4sizeButton.clicked.connect(self.changeTOK4Size)
          saveTOK5sizeButton.clicked.connect(self.changeTOK5Size)
          saveTOK6sizeButton.clicked.connect(self.changeTOK6Size)
          saveTOK7sizeButton.clicked.connect(self.changeTOK7Size)
          saveTOK8sizeButton.clicked.connect(self.changeTOK8Size)
          saveTOK9sizeButton.clicked.connect(self.changeTOK9Size)
          saveTOK10sizeButton.clicked.connect(self.changeTOK10Size)
          saveTOK11sizeButton.clicked.connect(self.changeTOK11Size)
          saveTOK12sizeButton.clicked.connect(self.changeTOK12Size)
          saveTOK13sizeButton.clicked.connect(self.changeTOK13Size)
          saveTOK14sizeButton.clicked.connect(self.changeTOK14Size)
          saveTOK15sizeButton.clicked.connect(self.changeTOK15Size)
          saveTOK16sizeButton.clicked.connect(self.changeTOK16Size)
          saveTOK17sizeButton.clicked.connect(self.changeTOK17Size)
          saveTOK18sizeButton.clicked.connect(self.changeTOK18Size)

          self.classroomPreferenceTOKComboBox = self.currentlyVisibleWidget.findChild(QtWidgets.QComboBox, "classroomPreferenceComboBox")
          classroomTOKPreferenceSaveButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "saveClassroomPreference")
          classroomTOKPreferenceSaveButton.clicked.connect(self.classroomPreference)

          self.classroomPreferenceTOKComboBox.addItem("Prefered classroom")

          for i in range(len(self.classrooms)):
            self.classroomPreferenceTOKComboBox.addItem(self.classrooms[i][0])
          
          


        except FileNotFoundError:
          self.errorComunicate("file not found")
          self.comeBackToWhoToEdit()


        # Set the layout and add the loaded widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.currentlyVisibleWidget)
        self.setLayout(layout)


    #=====================LOAD====DATA==============================
    def loadClassroomData(self):
      self.Clasroomindex = -1
      for i in range(len(self.classrooms)):
        if (self.ComboBoxClassrooms.currentText() == self.classrooms[i][0]):
          self.Clasroomindex = i
          self.textHolderSizeC.setText(str(self.classrooms[i][1]))
          self.textHolderScreenC.setText(str(self.classrooms[i][2]))
          self.textHolderWhoseC.setText(self.classrooms[i][3])
          break
    #=====================LOAD====DATA==============================


    #=====================SAVE====SIZE==============================
    def saveClassroomSize(self):
      try:
        self.loadClassroomData()
        self.Clasroomindex
        firstSize = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditSize")
        intSize = int(firstSize.text())
        self.classrooms[self.Clasroomindex][1] = intSize
        self.textHolderSizeC.setText(str(self.classrooms[self.Clasroomindex][1]))
      except ValueError:
        self.errorComunicate("inapropriate type")
    #=====================SAVE====SIZE==============================


    #=====================SAVE====WHOSE==============================
    def saveClassroomWhose(self):
      self.loadClassroomData()
      self.Clasroomindex
      firstWhose = self.currentlyVisibleWidget.findChild(QtWidgets.QLineEdit, "lineEditWhose")
      strWhose = firstWhose.text()
      self.classrooms[self.Clasroomindex][3] = strWhose
      self.textHolderWhoseC.setText(self.classrooms[self.Clasroomindex][3])

    #=====================SAVE====WHOSE==============================


    #=====================SAVE====SCREEN==============================
    def saveClassroomScreen(self, boolean):
      self.loadClassroomData()
      self.Clasroomindex
      self.classrooms[self.Clasroomindex][2] = boolean
      self.textHolderScreenC.setText(str(self.classrooms[self.Clasroomindex][2]))

    
    #=====================SAVE====SCREEN==============================




    #=======================TOK==TEACHER==============================
    def changeTOK1Size(self):
      try:
        value = int(self.sizeTOK1LineEdit.text())
        self.textHolderTOK1Size.setText(str(value))
        self.TOKTeacherData[0][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")
    

    def changeTOK2Size(self):
      try:
        value = int(self.sizeTOK2LineEdit.text())
        self.textHolderTOK2Size.setText(str(value))
        self.TOKTeacherData[1][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK3Size(self):
      try:
        value = int(self.sizeTOK3LineEdit.text())
        self.textHolderTOK3Size.setText(str(value))
        self.TOKTeacherData[2][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK4Size(self):
      try:
        value = int(self.sizeTOK4LineEdit.text())
        self.textHolderTOK4Size.setText(str(value))
        self.TOKTeacherData[3][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK5Size(self):
      try:
        value = int(self.sizeTOK5LineEdit.text())
        self.textHolderTOK5Size.setText(str(value))
        self.TOKTeacherData[4][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK6Size(self):
      try:
        value = int(self.sizeTOK6LineEdit.text())
        self.textHolderTOK6Size.setText(str(value))
        self.TOKTeacherData[5][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK7Size(self):
      try:
        value = int(self.sizeTOK7LineEdit.text())
        self.textHolderTOK7Size.setText(str(value))
        self.TOKTeacherData[6][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK8Size(self):
      try:
        value = int(self.sizeTOK8LineEdit.text())
        self.textHolderTOK8Size.setText(str(value))
        self.TOKTeacherData[7][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK9Size(self):
      try:
        value = int(self.sizeTOK9LineEdit.text())
        self.textHolderTOK9Size.setText(str(value))
        self.TOKTeacherData[8][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK10Size(self):
      try:
        value = int(self.sizeTOK10LineEdit.text())
        self.textHolderTOK10Size.setText(str(value))
        self.TOKTeacherData[9][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK11Size(self):
      try:
        value = int(self.sizeTOK11LineEdit.text())
        self.textHolderTOK11Size.setText(str(value))
        self.TOKTeacherData[10][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK12Size(self):
      try:
        value = int(self.sizeTOK12LineEdit.text())
        self.textHolderTOK12Size.setText(str(value))
        self.TOKTeacherData[11][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK13Size(self):
      try:
        value = int(self.sizeTOK13LineEdit.text())
        self.textHolderTOK13Size.setText(str(value))
        self.TOKTeacherData[12][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK14Size(self):
      try:
        value = int(self.sizeTOK14LineEdit.text())
        self.textHolderTOK14Size.setText(str(value))
        self.TOKTeacherData[13][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK15Size(self):
      try:
        value = int(self.sizeTOK15LineEdit.text())
        self.textHolderTOK15Size.setText(str(value))
        self.TOKTeacherData[14][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK16Size(self):
      try:
        value = int(self.sizeTOK16LineEdit.text())
        self.textHolderTOK16Size.setText(str(value))
        self.TOKTeacherData[15][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK17Size(self):
      try:
        value = int(self.sizeTOK17LineEdit.text())
        self.textHolderTOK17Size.setText(str(value))
        self.TOKTeacherData[16][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def changeTOK18Size(self):
      try:
        value = int(self.sizeTOK18LineEdit.text())
        self.textHolderTOK18Size.setText(str(value))
        self.TOKTeacherData[17][1] = int(value)
      except ValueError:
        self.errorComunicate("inapropriate type")

    def classroomPreference(self):
        self.TOKTeacherClassroomPreference # przywolac ze to nie jest lokalna tylko tak glowna
        text = self.classroomPreferenceTOKComboBox.currentText()
        self.TOKTeacherClassroomPreferenceLabel.setText(text)
        self.TOKTeacherClassroomPreference = text
    #=======================TOK==TEACHER==============================



    #====================SAVE=DATA=GATHERED===========================
    def saveChangedProgress(self):
      changedClassrooms = []
      changedClassrooms.append(["classroom", "size", "screen", "HR"])
      for i in range(len(self.classrooms)):
        changedClassrooms.append(self.classrooms[i])

      dfClass = pandas.DataFrame(changedClassrooms[1:], columns=changedClassrooms[0])
      dfClass.to_excel("database\data\dataClassrooms.xlsx", index=False)


      changedTOKteacher = []
      changedTOKteacher.append(["tok name", "size", "preference"])

      for i in range(18):
        tokName = ""
        size = ""
        preference = ""
        if (i == 0):
          tokName = self.TOKTeacherData[i][0]
          size = str(self.TOKTeacherData[i][1])
          self.TOKTeacherClassroomPreference
          preference = self.TOKTeacherClassroomPreference
        else:
          tokName = self.TOKTeacherData[i][0]
          size = str(self.TOKTeacherData[i][1])
          preference = "null"
        changedTOKteacher.append([tokName, size, preference])
      dfTOKt = pandas.DataFrame(changedTOKteacher[1:], columns=changedTOKteacher[0])
      dfTOKt.to_excel("database\data\dataTOKTeacher.xlsx", index=False)

      self.comeBackToWhoToEdit()
      
  #====================SAVE=DATA=GATHERED===========================


    def errorComunicate(self, whatError):
      messageText = ""
      requestText = ""
      if (whatError == "inapropriate type"):
        messageText = "inapropriate type of size"
        requestText = "please enter an integer"
      elif (whatError == "file not found"):
        messageText = "file not found"
        requestText = "please make sure the file exists"
        

      message = QtWidgets.QMessageBox()
      message.setWindowTitle("Error")
      message.setText(messageText)
      message.setInformativeText(requestText)
      message.setIcon(QtWidgets.QMessageBox.Critical)  
      message.setStandardButtons(QtWidgets.QMessageBox.Ok)
      message.exec()  


    def comeBackToWhoToEdit(self):
        # Switching back to AddPreferences widget properly
        self.parent().setCurrentWidget(self.parent().addPreferencesWidget)


class PreparedSchedule(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentlyVisibleWidget = loader.load("database/windows/QPreparedSchedule.ui", None)

        #=================LOAD===ADD=PREFERENCES===DATA=============================
        #=================LOAD===ADD=PREFERENCES===DATA=============================
        dfClasrooms = pandas.read_excel("database\data\dataClassrooms.xlsx", "Sheet1")
        
        self.classrooms = [
          ["206", 22, True, "1A"],
          ["207", 21, False, "non"],
          ["208/209", 24, True, "non"],
          ["210", 14, False, "non"],
          ["211", 27, True, "2A"],
          ["212", 14, False, "2C"],
          ["213", 12, False, "non"],
          ["214", 12, True, "non"],
          ["215", 12, True, "non"],
          ["216", 6, False, "non"],
          ["218", 6, False, "non"]
        ]
        for i in range(len(dfClasrooms)):
          nameC = dfClasrooms.iloc[i,0]
          size = dfClasrooms.iloc[i,1]
          screenC = dfClasrooms.iloc[i,2]
          homeroom = dfClasrooms.iloc[i,3]
          self.classrooms[i] = [str(nameC), int(size), bool(screenC), str(homeroom)]
        #==================BUBBLE=======SORT=================
        #self.classrooms = ["206", 22, True, "1A"]
        
        for i in range(len(self.classrooms)):
          for j in range(len(self.classrooms)-i-1):
            if (self.classrooms[j][1] < self.classrooms[j+1][1]):
              self.classrooms[j], self.classrooms[j+1] = self.classrooms[j+1], self.classrooms[j]
        #==================BUBBLE=======SORT=================

        dfTeachers = pandas.read_excel("database\data\dataTeachers.xlsx", "Sheet1")
        teachers = []
        for i in range(len(dfTeachers)):
          nameT = dfTeachers.iloc[i,0]
          screenT = dfTeachers.iloc[i,1]
          subject1T = dfTeachers.iloc[i,2]
          subject2T = dfTeachers.iloc[i,3]
          subject3T = dfTeachers.iloc[i,4]
          subject4T = dfTeachers.iloc[i,5]
          subject5T = dfTeachers.iloc[i,6]
          subject6T = dfTeachers.iloc[i,7]
          size1T = dfTeachers.iloc[i,8]
          size2T = dfTeachers.iloc[i,9]
          size3T = dfTeachers.iloc[i,10]
          size4T = dfTeachers.iloc[i,11]
          size5T = dfTeachers.iloc[i,12]
          size6T = dfTeachers.iloc[i,13]
          classroomPreferenceT = dfTeachers.iloc[i,14]

          teachers.append([
            str(nameT), 
            bool(screenT), 
            str(subject1T),
            str(subject2T),
            str(subject3T),
            str(subject4T),
            str(subject5T),
            str(subject6T),
            int(size1T),
            int(size2T),
            int(size3T),
            int(size4T),
            int(size5T),
            int(size6T),
            str(classroomPreferenceT)
          ])

        dfTOKteacher = pandas.read_excel("database\data\dataTOKTeacher.xlsx", "Sheet1")
          
        TOKTeacherData = []
        TOKTeacherClassroomPreferencearedSchedule = ""
        if (dfTOKteacher.iloc[0,2] != "Prefered classroom"):
          TOKTeacherClassroomPreferencearedSchedule = int(dfTOKteacher.iloc[0,2])
        for i in range(18):
          subjectName = dfTOKteacher.iloc[i,0]
          size = dfTOKteacher.iloc[i,1]
          TOKTeacherData.append([str(subjectName), int(size)])
        #=================LOAD===ADD=PREFERENCES===DATA=============================
        #=================LOAD===ADD=PREFERENCES===DATA=============================



        dfPrevious = pandas.read_excel("database\data\dataProg.xlsx", "Sheet1")
        dataGathered = [["path", "notifications"]]

        for i in range(len(dfPrevious)):
          dataGathered.append(dfPrevious.iloc[i].tolist())  

        file_path = dataGathered[1][0]
        

        
        

        try:
          RawDP1Schedule = pandas.read_excel(file_path, sheet_name="dp1")
          RawDP2Schedule = pandas.read_excel(file_path, sheet_name="dp2")
          headers_DP1_df = pandas.read_excel(file_path, sheet_name="dp1", nrows=0)
          headers_DP2_df = pandas.read_excel(file_path, sheet_name="dp2", nrows=0)
          #==================HEADERS=========DP1=================
          headers_DP1_array_Gathered = []
          for i in range(len(headers_DP1_df.columns)):
            headers_DP1_array_Gathered.append(headers_DP1_df.columns[i]) 
          del headers_DP1_array_Gathered[0]
          del headers_DP1_array_Gathered[0]
          
          for i in range(1, len(headers_DP1_array_Gathered)):
            for j in range(len(headers_DP1_array_Gathered)+5):
              if (headers_DP1_array_Gathered[i] == f"Unnamed: {j}"):
                headers_DP1_array_Gathered[i] = headers_DP1_array_Gathered[i-1]
                break

          for i in range(7):
            headers_DP1_array_Gathered.append(headers_DP1_array_Gathered[len(headers_DP1_array_Gathered)-1])

          #==================HEADERS=========DP2=================
          headers_DP2_array_Gathered = []
          for i in range(len(headers_DP2_df.columns)):
            headers_DP2_array_Gathered.append(headers_DP2_df.columns[i]) 
          del headers_DP2_array_Gathered[0]
          del headers_DP2_array_Gathered[0]
          
          for i in range(1, len(headers_DP2_array_Gathered)):
            for j in range(len(headers_DP2_array_Gathered)+5):
              if (headers_DP2_array_Gathered[i] == f"Unnamed: {j}"):
                headers_DP2_array_Gathered[i] = headers_DP2_array_Gathered[i-1]
                break
        
          for i in range(7):
            headers_DP2_array_Gathered.append(headers_DP2_array_Gathered[len(headers_DP2_array_Gathered)-1])


          #=======================================================
          # GETS THE ARRAY OF DP1 CLASSES
          lessons_DP1_array_Gathered = [[""] * len(headers_DP1_array_Gathered) for _ in range(11)]

          for day in range (len(headers_DP1_array_Gathered)-3):
            for hour in range (10):
                cell = RawDP1Schedule.iloc[hour,day+2]
                lessons_DP1_array_Gathered[hour+1][day+1] = cell

          for i in range(10):
            lessons_DP1_array_Gathered[i+1][0] = i+1

          for i in range(len(lessons_DP1_array_Gathered[0])-1):
            lessons_DP1_array_Gathered[0][i+1] = headers_DP1_array_Gathered[i]
          # GETS THE ARRAY OF DP1 CLASSES
          #=======================================================

          #=======================================================
          # GETS THE ARRAY OF DP2 CLASSES
          lessons_DP2_array_Gathered = [[""] * len(headers_DP2_array_Gathered) for _ in range(11)]

          for day in range (len(headers_DP2_array_Gathered)-4):
            for hour in range (10):
              cell = RawDP2Schedule.iloc[hour,day+2]
              lessons_DP2_array_Gathered[hour+1][day+1] = cell

          for i in range(10):
            lessons_DP2_array_Gathered[i+1][0] = i+1

          for i in range(len(lessons_DP2_array_Gathered[0])-1):
            lessons_DP2_array_Gathered[0][i+1] = headers_DP2_array_Gathered[i]
          # GETS THE ARRAY OF DP2 CLASSES
          #=======================================================


          whole_week_array_combined = [[""] * (len(lessons_DP1_array_Gathered[0]) + len(lessons_DP2_array_Gathered[0])) for _ in range(11)]

          for i in range(11):
            whole_week_array_combined[i][0] = i


          
          days_of_the_week_array = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']

          length_of_day = [0,0,0,0,0,0]
          day = headers_DP1_array_Gathered[0]

          from_day = 1
          to_day = 0

          for j in range (4):
            day_count = 0
              

            for k in range(len(headers_DP1_array_Gathered)-2):
              if (days_of_the_week_array[j] == headers_DP1_array_Gathered[k]):
                day_count += 1
            for k in range(len(headers_DP2_array_Gathered)-2):
              if (days_of_the_week_array[j] == headers_DP2_array_Gathered[k]):
                day_count += 1
            length_of_day[j+1] = day_count
            if j == 0:
              to_day = to_day + day_count + 1
            else:
              to_day = to_day + day_count

            for i in range(from_day, to_day):
              whole_week_array_combined[0][i] = days_of_the_week_array[j]
            from_day = to_day


            for i in range(len(whole_week_array_combined[0])):
              if (whole_week_array_combined[0][i]==""):
                whole_week_array_combined[0][i] = days_of_the_week_array[4]
            length_of_day[5] = len(whole_week_array_combined[0]) - length_of_day[0] - length_of_day[1] - length_of_day[2] - length_of_day[3]- length_of_day[4]



          def one_hour (index, array):
            one_hour_array = [""] * 10
            for j in range(len(array)-1):  
                one_hour_array[j] = str(array[j+1][index]) 
            return one_hour_array
          
          
          additional = 0
          for day in range (len(days_of_the_week_array)):
            additional = additional + length_of_day[day]
            deviation = 0
            for i in range(len(headers_DP1_array_Gathered)-1):
              if(days_of_the_week_array[day]==headers_DP1_array_Gathered[i]):
                temp_array = one_hour(i+1, lessons_DP1_array_Gathered)
                for k in range(len(temp_array)):
                  whole_week_array_combined[k + 1][i +1+ additional-deviation] = str(temp_array[k]) + " DP 1"
              else:
                deviation += 1

          for i in range(len(lessons_DP2_array_Gathered[0])-1):
            temp_array = one_hour(i+1, lessons_DP2_array_Gathered)
            for k in range(len(whole_week_array_combined[0])-1):
              if ((whole_week_array_combined[1][k+1] == "")):
                for j in range(len(temp_array)):
                  whole_week_array_combined[j + 1][k + 1] = str(temp_array[j]) + " DP 2"
                break
          
          

        
          # CREATE A SEARCH ALGORITHM FOR EACH HOUR
          def hour_array(hour_id, day):
            this_hour_array = []
            for i in range(len(whole_week_array_combined[0])):
              if ((whole_week_array_combined[0][i] == days_of_the_week_array[day]) and not(whole_week_array_combined[hour_id+1][i] in [" DP 1", " DP 2", "nan DP 1", "nan DP 2"])):
                this_hour_array.append(whole_week_array_combined[hour_id+1][i])
            return this_hour_array
          # CREATE A SEARCH ALGORITHM FOR EACH HOUR

          


          self.full_this_hour_arr = [[None for _ in range(5)] for _ in range(11)]
          self.empty_classroonms = [[None for _ in range(5)] for _ in range(11)]

          print(hour_array(0,0))

          
          def findTeacherData(subjectSearch):
            array = ["not found", 0, False, ""]
            for i in range(len(teachers)):
              for j in range(2, 8):
                if (subjectSearch == teachers[i][j]):
                  array[0] = teachers[i][0]   # TEACHER NAME
                  array[1] = teachers[i][j+6] # SUBJECT SIZE
                  array[2] = teachers[i][1]   # SCREEN PREFERENCE
                  array[3] = teachers[i][14]  # PREFERENCE
                  
            return array
          
          #print(self.classrooms)
          for day in range(5):
            for hour in range(10):
              hour_day_classroom_assigned = []
              hour_day_array_gather = hour_array(hour,day)
              if (day ==0 and hour == 0):
                print(hour_day_array_gather)
              self.empty_classroonms_array = []
              self.classrooms_avaiable_array = copy.deepcopy(self.classrooms)
              
              #print(self.classrooms_avaiable_array)

              for i in range(len(hour_day_array_gather)):
                subject = hour_day_array_gather[i]
                arrayOfData = findTeacherData(subject)
                teacherName = arrayOfData[0]
                if (teacherName != "not found"):
                  size = arrayOfData[1]
                  screen_av = arrayOfData[2]
                  classroomPreference = arrayOfData[3]
                  #                                                                                           classroom
                  hour_day_classroom_assigned.append([subject, teacherName, screen_av, classroomPreference, size, ""])

                elif (teacherName == "not found"):
                  for i in range(len(TOKTeacherData)):
                    if (subject == TOKTeacherData[i][0]):
                      teacherName = "TOK teacher"
                      size = TOKTeacherData[i][1]
                      if isinstance (TOKTeacherClassroomPreferencearedSchedule, str):
                        classroomPreference = TOKTeacherClassroomPreferencearedSchedule
                      else:
                        classroomPreference = str(TOKTeacherClassroomPreferencearedSchedule)
                  hour_day_classroom_assigned.append([subject, teacherName, True, classroomPreference, size, ""])
              #print(hour_day_classroom_assigned)


              # SORTS THE ARRAY
              for i in range(len(hour_day_classroom_assigned)):
                for j in range(len(hour_day_classroom_assigned)-i-1):
                  if (hour_day_classroom_assigned[j][4] < hour_day_classroom_assigned[j+1][4]):
                    hour_day_classroom_assigned[j], hour_day_classroom_assigned[j+1] = hour_day_classroom_assigned[j+1], hour_day_classroom_assigned[j]

              # assign homehours
              for b in range(len(hour_day_classroom_assigned)):
                for a in range(len(self.classrooms)):
                  if (hour_day_classroom_assigned[b][0] == ("HR " + self.classrooms[a][3]) and (hour_day_classroom_assigned[b][4] < self.classrooms[a][1])):
                    hour_day_classroom_assigned[b][5] = self.classrooms[a][0]
                    self.classrooms_avaiable_array[a][0] = ""
                    break
              

              # assign other classes by size
              for c in range (len(hour_day_classroom_assigned)):
                if (hour_day_classroom_assigned[c][5] == ""):
                  for m in range(len(self.classrooms_avaiable_array)):
                    if not(self.classrooms_avaiable_array[m][0] == ""):
                      hour_day_classroom_assigned[c][5] = self.classrooms_avaiable_array[m][0]
                      self.classrooms_avaiable_array[m][0] = ""
                      break
              
                
              # assign prefered ones
              for i in range(len(hour_day_classroom_assigned)):
                if (hour_day_classroom_assigned[i][3] != "no preference"):
                  preferedClassroom = hour_day_classroom_assigned[i][3]
                  for j in range(len(self.classrooms_avaiable_array)):
                    if (self.classrooms_avaiable_array[j][0] == preferedClassroom) and (hour_day_classroom_assigned[i][4] < self.classrooms_avaiable_array[j][1]):
                      previousClassroom = hour_day_classroom_assigned[i][5]
                      hour_day_classroom_assigned[i][5] = self.classrooms_avaiable_array[j][0]
                      self.classrooms_avaiable_array[j][0] = ""
                      for n in range(len(self.classrooms_avaiable_array)):
                        if (self.classrooms_avaiable_array[n][0] == ""):
                          self.classrooms_avaiable_array[n][0] = previousClassroom
                          break
                      break
                  for j in range(len(hour_day_classroom_assigned)):
                    if (hour_day_classroom_assigned[j][5] == preferedClassroom):
                      preferedClassroomSize = 0
                      replacingClassroomSize = 0
                      for m in range(len(self.classrooms)):
                        if (self.classrooms[m][0] == preferedClassroom):
                          preferedClassroomSize = self.classrooms[m][1]
                        elif(self.classrooms[m][0] == hour_day_classroom_assigned[j][5]):
                          replacingClassroomSize = self.classrooms[m][1]
                      if (replacingClassroomSize > hour_day_classroom_assigned[i][4]) and (preferedClassroomSize > hour_day_classroom_assigned[j][4]) :
                        if not("HR" in hour_day_classroom_assigned[j][0]):
                          hour_day_classroom_assigned[i][5],  hour_day_classroom_assigned[j][5] = hour_day_classroom_assigned[j][5],  hour_day_classroom_assigned[i][5]
                          break
              
                    
              #["207", 21, False, "non"],

              for i in range(len(hour_day_classroom_assigned)):
                screenPreference = hour_day_classroom_assigned[i][2]
                if (screenPreference):
                  for j in range(len(self.classrooms_avaiable_array)):
                    if (self.classrooms_avaiable_array[j][2] == screenPreference and self.classrooms_avaiable_array[j][0] != "") and (hour_day_classroom_assigned[i][4] < self.classrooms_avaiable_array[j][1]):
                      previousClassroom = hour_day_classroom_assigned[i][5]
                      hour_day_classroom_assigned[i][5] = self.classrooms_avaiable_array[j][0]
                      self.classrooms_avaiable_array[j][0] = ""
                      for n in range(len(self.classrooms_avaiable_array)):
                        if (self.classrooms_avaiable_array[n][0] == ""):
                          self.classrooms_avaiable_array[n][0] = previousClassroom
                          break
                      break
                  for j in range(len(hour_day_classroom_assigned)):
                    if (hour_day_classroom_assigned[j][2] == screenPreference):
                      preferedClassroomSize = 0
                      replacingClassroomSize = 0
                      replacingTeacherScreenAvailability = hour_day_classroom_assigned[j][2]
                      replacingClassroomsScreenAvailability = False
                      for m in range(len(self.classrooms)):
                        if (self.classrooms[m][0] == preferedClassroom):
                          preferedClassroomSize = self.classrooms[m][1]
                        elif(self.classrooms[m][0] == hour_day_classroom_assigned[j][5]):
                          replacingClassroomSize = self.classrooms[m][1]
                          replacingClassroomsScreenAvailability = self.classrooms[m][2]
                      if (replacingClassroomSize > hour_day_classroom_assigned[i][4]) and (preferedClassroomSize > hour_day_classroom_assigned[j][4]) and not(hour_day_classroom_assigned[j][0]  in "HR"):
                        if (replacingTeacherScreenAvailability != replacingClassroomsScreenAvailability) and not("HR" in hour_day_classroom_assigned[j][0]):
                          hour_day_classroom_assigned[i][5],  hour_day_classroom_assigned[j][5] = hour_day_classroom_assigned[j][5],  hour_day_classroom_assigned[i][5]
                          break
              
                  
              # put non used classess to the next array
              for f in range(len(self.classrooms_avaiable_array)):
                if (self.classrooms_avaiable_array[f][0] != ""):
                  self.empty_classroonms_array.append(self.classrooms_avaiable_array[f][0])




              self.full_this_hour_arr[hour][day] = hour_day_classroom_assigned
              self.empty_classroonms[hour][day] = self.empty_classroonms_array
          print(self.empty_classroonms[1][3])
          print("============================")
          print(self.full_this_hour_arr[0][0])

          '''
          print(self.full_this_hour_arr[2][1])
          print(self.full_this_hour_arr[1][3])
          print("============================")
          print("============================")
          '''

          #=======================NOTIFICATIONS=========================================
          
          self.full_notification_array = [[None for _ in range(5)] for _ in range(10)]
          for day in range(5):
            for hour in range(10):
              notifications = []
              check_hour_problems = self.full_this_hour_arr[hour][day] 
              if (check_hour_problems):
                for i in range(len(check_hour_problems)):
                  teacher_screen_preference = check_hour_problems[i][2]
                  teacher_assigned_classroom = check_hour_problems[i][5]
                  for j in range(len(self.classrooms)):
                    if (self.classrooms[j][0] == teacher_assigned_classroom) and not(teacher_screen_preference ^ self.classrooms[j][2]):
                      text_of_notification = ("teacher: " + check_hour_problems[i][1] + " could not have a screen available")
                      notifications.append(text_of_notification)
                      break

                for i in range(len(check_hour_problems)):
                  teacher_clasroom_preference = check_hour_problems[i][3]
                  teacher_assigned_classroom = check_hour_problems[i][5]
                  if (teacher_clasroom_preference != teacher_assigned_classroom):
                    text_of_notification = ("teacher: " + check_hour_problems[i][1] + " could not have classes at preferred classroom")
                    notifications.append(text_of_notification)
              self.full_notification_array[hour][day] = notifications
                    


  
          GoToDay1hour1Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_1")
          GoToDay1hour1Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,0))

          GoToDay1hour2Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_2")
          GoToDay1hour2Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,1))

          GoToDay1hour3Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_3")
          GoToDay1hour3Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,2))

          GoToDay1hour4Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_4")
          GoToDay1hour4Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,3))

          GoToDay1hour5Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_5")
          GoToDay1hour5Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,4))

          GoToDay1hour6Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_6")
          GoToDay1hour6Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,5))

          GoToDay1hour7Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_7")
          GoToDay1hour7Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,6))

          GoToDay1hour8Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_8")
          GoToDay1hour8Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,7))

          GoToDay1hour9Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_9")
          GoToDay1hour9Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,8))

          GoToDay1hour10Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourM_10")
          GoToDay1hour10Button.clicked.connect(lambda: self.goToSituationInTheBuilding(0,9))

          GoToDay2hour1Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_1")
          GoToDay2hour1Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,0))

          GoToDay2hour2Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_2")
          GoToDay2hour2Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,1))

          GoToDay2hour3Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_3")
          GoToDay2hour3Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,2))

          GoToDay2hour4Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_4")
          GoToDay2hour4Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,3))

          GoToDay2hour5Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_5")
          GoToDay2hour5Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,4))

          GoToDay2hour6Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_6")
          GoToDay2hour6Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,5))

          GoToDay2hour7Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_7")
          GoToDay2hour7Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,6))

          GoToDay2hour8Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_8")
          GoToDay2hour8Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,7))

          GoToDay2hour9Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_9")
          GoToDay2hour9Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,8))

          GoToDay2hour10Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourT_10")
          GoToDay2hour10Button.clicked.connect(lambda: self.goToSituationInTheBuilding(1,9))

          GoToDay3hour1Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_1")
          GoToDay3hour1Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,0))

          GoToDay3hour2Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_2")
          GoToDay3hour2Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,1))

          GoToDay3hour3Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_3")
          GoToDay3hour3Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,2))

          GoToDay3hour4Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_4")
          GoToDay3hour4Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,3))

          GoToDay3hour5Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_5")
          GoToDay3hour5Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,4))

          GoToDay3hour6Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_6")
          GoToDay3hour6Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,5))

          GoToDay3hour7Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_7")
          GoToDay3hour7Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,6))

          GoToDay3hour8Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_8")
          GoToDay3hour8Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,7))

          GoToDay3hour9Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_9")
          GoToDay3hour9Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,8))

          GoToDay3hour10Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourW_10")
          GoToDay3hour10Button.clicked.connect(lambda: self.goToSituationInTheBuilding(2,9))

          GoToDay4hour1Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_1")
          GoToDay4hour1Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,0))

          GoToDay4hour2Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_2")
          GoToDay4hour2Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,1))

          GoToDay4hour3Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_3")
          GoToDay4hour3Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,2))

          GoToDay4hour4Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_4")
          GoToDay4hour4Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,3))

          GoToDay4hour5Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_5")
          GoToDay4hour5Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,4))

          GoToDay4hour6Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_6")
          GoToDay4hour6Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,5))

          GoToDay4hour7Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_7")
          GoToDay4hour7Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,6))

          GoToDay4hour8Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_8")
          GoToDay4hour8Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,7))

          GoToDay4hour9Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_9")
          GoToDay4hour9Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,8))

          GoToDay4hour10Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourTH_10")
          GoToDay4hour10Button.clicked.connect(lambda: self.goToSituationInTheBuilding(3,9))

          GoToDay5hour1Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_1")
          GoToDay5hour1Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,0))

          GoToDay5hour2Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_2")
          GoToDay5hour2Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,1))

          GoToDay5hour3Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_3")
          GoToDay5hour3Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,2))

          GoToDay5hour4Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_4")
          GoToDay5hour4Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,3))

          GoToDay5hour5Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_5")
          GoToDay5hour5Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,4))

          GoToDay5hour6Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_6")
          GoToDay5hour6Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,5))

          GoToDay5hour7Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_7")
          GoToDay5hour7Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,6))

          GoToDay5hour8Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_8")
          GoToDay5hour8Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,7))

          GoToDay5hour9Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_9")
          GoToDay5hour9Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,8))

          GoToDay5hour10Button = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "hourF_10")
          GoToDay5hour10Button.clicked.connect(lambda: self.goToSituationInTheBuilding(4,9))

          downloadPreparedScheduleButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "DownloadSchedule")
          downloadPreparedScheduleButton.clicked.connect(lambda: downloadPreparedSchedule())



          #self.full_this_hour_arr[hour][day] = hour_day_classroom_assigned
          #self.empty_classroonms[hour][day] = self.empty_classroonms_array
          '''
          headers_DP1_array_Gathered
          headers_DP2_array_Gathered
          lessons_DP1_array_Gathered
          lessons_DP2_array_Gathered     






          RawDP1Schedule = pandas.read_excel(file_path, sheet_name="dp1")
          RawDP2Schedule = pandas.read_excel(file_path, sheet_name="dp2")
          headers_DP1_df = pandas.read_excel(file_path, sheet_name="dp1", nrows=0)
          headers_DP2_df = pandas.read_excel(file_path, sheet_name="dp2", nrows=0)
          
          file_path
          '''


          def downloadPreparedSchedule():
            print("yeahh....")
            
            
            
            preparedDP1Schedule = copy.deepcopy(lessons_DP1_array_Gathered)
            preparedDP2Schedule = copy.deepcopy(lessons_DP2_array_Gathered)


            print(preparedDP1Schedule)
            print(len(preparedDP1Schedule))
            print(preparedDP1Schedule[0][5])
            print(preparedDP1Schedule[5][0])
            print("========================================================")

            days_of_the_week_array = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
            for day in range(5):
              for hour in range(10):
                # [subject, teacherName, screen_av, classroomPreference, size, ""]
                assigned_classrooms_to_classes = self.full_this_hour_arr[hour][day]
                day_of_the_week = days_of_the_week_array[day]

                for i in range(len(preparedDP1Schedule[0])):
                  if (day_of_the_week == preparedDP1Schedule[0][i]):
                    class_which_seeks_classroom = str(preparedDP1Schedule[hour+1][i])
                    for j in range(len(assigned_classrooms_to_classes)):
                      if (class_which_seeks_classroom + " DP 1" == assigned_classrooms_to_classes[j][0]):
                        subjects_classroom = assigned_classrooms_to_classes[j][5]
                        preparedDP1Schedule[hour+1][i] = class_which_seeks_classroom + " " + subjects_classroom
                        break

                for i in range(len(preparedDP2Schedule[0])):
                  if (day_of_the_week == preparedDP2Schedule[0][i]):
                    class_which_seeks_classroom = str(preparedDP2Schedule[hour+1][i])
                    for j in range(len(assigned_classrooms_to_classes)):
                      if (class_which_seeks_classroom + " DP 2" == assigned_classrooms_to_classes[j][0]):
                        subjects_classroom = assigned_classrooms_to_classes[j][5]
                        preparedDP2Schedule[hour+1][i] = class_which_seeks_classroom + " " + subjects_classroom
                        break

            preparedDP1Schedule = pandas.DataFrame(preparedDP1Schedule)
            preparedDP2Schedule = pandas.DataFrame(preparedDP2Schedule)

            headersDP1Prep = preparedDP1Schedule.iloc[0].tolist()
            # Remove the first row from the DataFrame since it's now being used as headers
            preparedDP1Schedule = preparedDP1Schedule[1:].reset_index(drop=True)

            headersDP2Prep = preparedDP2Schedule.iloc[0].tolist()
            # Remove the first row from the DataFrame since it's now being used as headers
            preparedDP2Schedule = preparedDP2Schedule[1:].reset_index(drop=True)


            preparedDP1Schedule.columns = headersDP1Prep
            preparedDP2Schedule.columns = headersDP2Prep
            fileName = "preparedSchedule.xlsx"
            
            try :
              with pandas.ExcelWriter(fileName, engine="xlsxwriter") as writer:
                preparedDP1Schedule.to_excel(writer, sheet_name="dp1", index=False)
                preparedDP2Schedule.to_excel(writer, sheet_name="dp2", index=False)
            except FileExistsError or Exception:
              self.errorComunicate("file already exist")
          
          # Create deep copies of the data
          








          comeBackButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "ComeBackButton")
          comeBackButton.clicked.connect(self.comeBackToMainWindow)


        except FileNotFoundError:
          self.errorComunicate("file not found")
          self.comeBackToMainWindow

        
        
















        # Set the layout and add the loaded widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.currentlyVisibleWidget)
        self.setLayout(layout)

        

    def errorComunicate(self, whatError):
      messageText = ""
      requestText = ""
      if (whatError == "file not found"):
        messageText = "file not found"
        requestText = "please make sure the file exists"
  

      message = QtWidgets.QMessageBox()
      message.setWindowTitle("Error")
      message.setText(messageText)
      message.setInformativeText(requestText)
      message.setIcon(QtWidgets.QMessageBox.Critical)  
      message.setStandardButtons(QtWidgets.QMessageBox.Ok)
      message.exec()  

    def goToSituationInTheBuilding(self, day, hour):
        # Load the UI for the building situation
        building_ui = QtWidgets.QWidget()
        self.buildingSituationWidget = loader.load("database/windows/QBuildingSituation.ui", None)

        # Set layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.buildingSituationWidget)
        building_ui.setLayout(layout)

        # Add this widget to the stacked widget (parent)
        self.parent().addWidget(building_ui)
        
        # Switch to the new widget
        self.parent().setCurrentWidget(building_ui)


        array_of_classess = self.full_this_hour_arr[hour][day]
        if (array_of_classess):
          for i in range(len(array_of_classess)):
            teacherName = array_of_classess[i][1]
            subjectName = array_of_classess[i][0]
            classroomName = array_of_classess[i][5]
            classroomSize = 0
            for j in range(len(self.classrooms)):
              if (self.classrooms[j][0] == classroomName):
                classroomSize = self.classrooms[j][1]
                break
            emptyPlaces = classroomSize - int(array_of_classess[i][4])
            if (i == 0):
              subject1NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className1")
              subject1NameLabel.setText(subjectName)
              teacher1NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName1")
              teacher1NameLabel.setText(teacherName)
              classroom1NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName1")
              classroom1NameLabel.setText(classroomName)
              emptyPlaces1NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces1")
              emptyPlaces1NameLabel.setText(str(emptyPlaces))
            elif (i == 1):
              subject2NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className2")
              subject2NameLabel.setText(subjectName)
              teacher2NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName2")
              teacher2NameLabel.setText(teacherName)
              classroom2NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName2")
              classroom2NameLabel.setText(classroomName)
              emptyPlaces2NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces2")
              emptyPlaces2NameLabel.setText(str(emptyPlaces))
            elif (i == 2):
              subject3NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className3")
              subject3NameLabel.setText(subjectName)
              teacher3NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName3")
              teacher3NameLabel.setText(teacherName)
              classroom3NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName3")
              classroom3NameLabel.setText(classroomName)
              emptyPlaces3NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces3")
              emptyPlaces3NameLabel.setText(str(emptyPlaces))
            elif (i == 3):
              subject4NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className4")
              subject4NameLabel.setText(subjectName)
              teacher4NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName4")
              teacher4NameLabel.setText(teacherName)
              classroom4NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName4")
              classroom4NameLabel.setText(classroomName)
              emptyPlaces4NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces4")
              emptyPlaces4NameLabel.setText(str(emptyPlaces))
            elif (i == 4):
              subject5NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className5")
              subject5NameLabel.setText(subjectName)
              teacher5NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName5")
              teacher5NameLabel.setText(teacherName)
              classroom5NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName5")
              classroom5NameLabel.setText(classroomName)
              emptyPlaces5NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces5")
              emptyPlaces5NameLabel.setText(str(emptyPlaces))
            elif (i == 5):
              subject6NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className6")
              subject6NameLabel.setText(subjectName)
              teacher6NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName6")
              teacher6NameLabel.setText(teacherName)
              classroom6NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName6")
              classroom6NameLabel.setText(classroomName)
              emptyPlaces6NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces6")
              emptyPlaces6NameLabel.setText(str(emptyPlaces))
            elif (i == 6):
              subject7NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className7")
              subject7NameLabel.setText(subjectName)
              teacher7NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName7")
              teacher7NameLabel.setText(teacherName)
              classroom7NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName7")
              classroom7NameLabel.setText(classroomName)
              emptyPlaces7NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces7")
              emptyPlaces7NameLabel.setText(str(emptyPlaces))
            elif (i == 7):
              subject8NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className8")
              subject8NameLabel.setText(subjectName)
              teacher8NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName8")
              teacher8NameLabel.setText(teacherName)
              classroom8NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName8")
              classroom8NameLabel.setText(classroomName)
              emptyPlaces8NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces8")
              emptyPlaces8NameLabel.setText(str(emptyPlaces))
            elif (i == 8):
              subject9NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className9")
              subject9NameLabel.setText(subjectName)
              teacher9NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName9")
              teacher9NameLabel.setText(teacherName)
              classroom9NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName9")
              classroom9NameLabel.setText(classroomName)
              emptyPlaces9NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces9")
              emptyPlaces9NameLabel.setText(str(emptyPlaces))
            elif (i == 9):
              subject10NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className10")
              subject10NameLabel.setText(subjectName)
              teacher10NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName10")
              teacher10NameLabel.setText(teacherName)
              classroom10NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName10")
              classroom10NameLabel.setText(classroomName)
              emptyPlaces10NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces10")
              emptyPlaces10NameLabel.setText(str(emptyPlaces))
            elif (i == 10):
              subject11NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "className11")
              subject11NameLabel.setText(subjectName)
              teacher11NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "teacherName11")
              teacher11NameLabel.setText(teacherName)
              classroom11NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomName11")
              classroom11NameLabel.setText(classroomName)
              emptyPlaces11NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "classroomPlaces11")
              emptyPlaces11NameLabel.setText(str(emptyPlaces))



          array_of_empty_classess = self.empty_classroonms[hour][day]
          if (array_of_empty_classess):
            for i in range(len(array_of_empty_classess)):
              emptyClassroomName = array_of_empty_classess[i]
              if (i == 0):
                emptyClassroom1NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom1")
                emptyClassroom1NameLabel.setText(emptyClassroomName)
              elif (i == 1):
                emptyClassroom2NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom2")
                emptyClassroom2NameLabel.setText(emptyClassroomName)
              elif (i == 2):
                emptyClassroom3NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom3")
                emptyClassroom3NameLabel.setText(emptyClassroomName)
              elif (i == 3):
                emptyClassroom4NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom4")
                emptyClassroom4NameLabel.setText(emptyClassroomName)
              elif (i == 4):
                emptyClassroom5NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom5")
                emptyClassroom5NameLabel.setText(emptyClassroomName)
              elif (i == 5):
                emptyClassroom6NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom6")
                emptyClassroom6NameLabel.setText(emptyClassroomName)
              elif (i == 6):
                emptyClassroom7NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom7")
                emptyClassroom7NameLabel.setText(emptyClassroomName)
              elif (i == 7):
                emptyClassroom8NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom8")
                emptyClassroom8NameLabel.setText(emptyClassroomName)
              elif (i == 8):
                emptyClassroom9NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom9")
                emptyClassroom9NameLabel.setText(emptyClassroomName)
              elif (i == 9):
                emptyClassroom10NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom10")
                emptyClassroom10NameLabel.setText(emptyClassroomName)
              elif (i == 10):
                emptyClassroom11NameLabel = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "emptyClassroom11")
                emptyClassroom11NameLabel.setText(emptyClassroomName)


          array_of_notifications = self.full_notification_array[hour][day]
          if (array_of_notifications):
            for i in range(len(array_of_notifications)):
              notificationText = array_of_notifications[i]
              if (i == 0):
                notification1Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification1")
                notification1Label.setText(notificationText)
              elif (i == 1):
                notification2Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification2")
                notification2Label.setText(notificationText)
              elif (i == 2):
                notification3Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification3")
                notification3Label.setText(notificationText)
              elif (i == 3):
                notification4Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification4")
                notification4Label.setText(notificationText)
              elif (i == 4):
                notification5Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification5")
                notification5Label.setText(notificationText)
              elif (i == 5):
                notification6Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification6")
                notification6Label.setText(notificationText)
              elif (i == 6):
                notification7Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification7")
                notification7Label.setText(notificationText)
              elif (i == 7):
                notification8Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification8")
                notification8Label.setText(notificationText)
              elif (i == 8):
                notification9Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification9")
                notification9Label.setText(notificationText)
              elif (i == 9):
                notification10Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification10")
                notification10Label.setText(notificationText)
              elif (i == 10):
                notification11Label = self.buildingSituationWidget.findChild(QtWidgets.QLabel, "notification11")
                notification11Label.setText(notificationText)


            
          print("notifications")
          print(array_of_notifications)
          print("==================")
          print("empty classess")
          print(array_of_empty_classess)
          print("==================")
          print("occupied classess")
          print(array_of_classess)
          print("==================")


















        # Find the ComeBackButton and connect it properly
        comeBackButton = self.buildingSituationWidget.findChild(QtWidgets.QPushButton, "ComeBackButton")
        comeBackButton.clicked.connect(self.comeBackToPreparedSchedule)



    def comeBackToPreparedSchedule(self):
        self.parent().setCurrentWidget(self.parent().openPreparedScheduleWidget)

    def comeBackToMainWindow(self):
        # Switching back to main window properly
        self.parent().setCurrentWidget(self.parent().currentlyVisibleWidget)  # Use parent() for reference


class mainW(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the UI file
        self.currentlyVisibleWidget = loader.load("database/windows/QMainWindow.ui", None)
        self.currentlyVisibleWidget.setWindowTitle("THE BEST PROG")
        self.addWidget(self.currentlyVisibleWidget)  # Add the main window widget

        self.addPreferencesWidget = WhoToEdit(self)
        self.addWidget(self.addPreferencesWidget)  # Add the preferences widget

        self.openTeachersWidget = openTeachers(self)
        self.addWidget(self.openTeachersWidget)  # Add the teachers widget

        self.openClassroomsWidget = openClassrooms(self)
        self.addWidget(self.openClassroomsWidget)  # Add the teachers widget

        self.openPreparedScheduleWidget = PreparedSchedule(self)
        self.addWidget(self.openPreparedScheduleWidget)  # Add the teachers widget

        # Set the initial visible widget
        self.setCurrentWidget(self.currentlyVisibleWidget)
        self.resize(950, 650)

        # Find the button in the main window and connect it to open AddPreferences
        self.OpenWhoToEditButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "AddPreferencesButton")
        self.OpenWhoToEditButton.clicked.connect(self.showAddPreferences)

        self.OpenPreparedScheduleButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "PreparedScheduleButton")
        self.OpenPreparedScheduleButton.clicked.connect(self.showPreparedSchedule)

        self.uploadFileButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "UploadFileButton")
        self.uploadFileButton.clicked.connect(self.uploadFile)

        self.ExitButton = self.currentlyVisibleWidget.findChild(QtWidgets.QPushButton, "ExitButton")
        self.ExitButton.clicked.connect(app.exit)

    def uploadFile(self):
      # Open a file dialog to select an Excel file
      file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
        self.currentlyVisibleWidget,
        "Select an Excel File",
        "",
        "Excel Files (*.xlsx *.xls);;All Files (*)"
      )
      
      # if the new path was gathered
      if (file_path):
        # prevention of chosing inproper file
        if not("plan" in file_path.lower()):
          # informs user that chosen file isn't named plan
          self.errorComunicate("not plan file")
        # program opens stored data using pandas
        dfPrevious = pandas.read_excel("database\data\dataProg.xlsx", "Sheet1")
        # creates header for updated file
        dataGathered = [["path", "notifications"]]
        # converts Pandas' array into python one
        for i in range(len(dfPrevious)):
          dataGathered.append(dfPrevious.iloc[i].tolist())  
        # updates the new path
        dataGathered[1][0] = file_path  
        # stores the updated path into program's memory
        dfChanged = pandas.DataFrame(dataGathered[1:], columns=dataGathered[0])
        # edits program memory and saves new file path
        dfChanged.to_excel("database\data\dataProg.xlsx", index=False)

    def errorComunicate(self, whatError):
      messageText = ""
      requestText = ""
      if (whatError == "not plan file"):
        messageText = "chosen file is not named 'plan'"
        requestText = "if you are aware of that, please proceed"
         
      message = QtWidgets.QMessageBox()
      message.setWindowTitle("Error")
      message.setText(messageText)
      message.setInformativeText(requestText)
      message.setIcon(QtWidgets.QMessageBox.Critical)  
      message.setStandardButtons(QtWidgets.QMessageBox.Ok)
      message.exec()  

    def showPreparedSchedule(self):
        self.setCurrentWidget(self.openPreparedScheduleWidget)

    def showAddPreferences(self):
        # Switch to the AddPreferences widget
        self.setCurrentWidget(self.addPreferencesWidget)




# Initialize and show the main window
window = mainW()
window.setWindowTitle("THE BEST PROG")
window.show()

# Execute the application
sys.exit(app.exec())
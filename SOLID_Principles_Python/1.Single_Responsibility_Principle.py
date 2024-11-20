class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"Title: {self.title}\nContent: {self.content}"

    def save_to_file(self, filename):  # Violates SRP
        with open(filename, 'w') as file:
            file.write(self.generate())
#--- Issue: The Report class has two responsibilities: generating report content and saving it to a file. 
# If you need to change how the report is saved (e.g., to a database), you have to modify the Report class, violating the SRP.

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"Title: {self.title}\nContent: {self.content}"

class ReportSaver:
    def save_to_file(self, report, filename): #-- Here the report object is passed through
        with open(filename, 'w') as file:
            file.write(report.generate())

#--- Improvement: The Report class only focuses on generating report content, while ReportSaver handles saving the report. 
# This separation makes it easier to manage changes and adheres to SRP.
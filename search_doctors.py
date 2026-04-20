from bs4 import BeautifulSoup
import requests

class Doctors:
    
    def __init__(self):

        # Instance Variable
        
        self.html_text = requests.get('https://www.uchbd.com/all-doctors').text

        self.soup = BeautifulSoup(self.html_text, 'lxml')
        self.doctors = self.soup.find_all('h3')
        for i in range(len(self.doctors)-4):
            print(str(i+1)+". "+self.doctors[i].text)
            
        

class SpecificDoctors(Doctors):
    def __init__(self):
        super().__init__()
        index = int(input("Enter index: "))
        self.doctors_text = requests.get('https://www.uchbd.com/speciality/'+self.doctors[index-1].text.replace(' ','%20')[3:-3]).text
        self.doctor_soup = BeautifulSoup(self.doctors_text, 'lxml')
        self.specific_doctors = self.doctor_soup.find_all('h3')
        for i in range(len(self.specific_doctors)-4):
           print(str(i+1)+". "+self.specific_doctors[i].text)

doctor_list = SpecificDoctors()

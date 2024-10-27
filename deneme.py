
import datetime,time,sqlite3
from tqdm import tqdm
from faker import Faker

clocks = ["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00"]

tıp_branşları = [
    "Anatomi",
    "Biyofizik",
    "Tıbbi Biyoloji",
    "Tıp Eğitimi",
    "Tıp Etiği ve Tıp Tarihi",
    "İmmünoloji",
    "Fizyoloji",
    "Histoloji ve Embriyoloji",
    "Tıbbi Mikrobiyoloji",
    "Tıp Bilişimi",
    "Tıbbi Biyokimya",
    "Dahili Tıp Bilimleri",
    "Acil Tıp",
    "Adli Tıp",
    "Çocuk Ruh Sağlığı",
    "Çocuk Sağlığı ve Hastalıkları",
    "Dermatoloji",
    "Enfeksiyon Hastalıkları",
    "Fiziksel Tıp ve Rehabilitasyon",
    "Göğüs Hastalıkları",
    "Halk Sağlığı",
    "İç Hastalıkları",
    "Kardiyoloji",
    "Nöroloji",
    "Nükleer Tıp",
    "Radyasyon Onkolojisi",
    "Radyoloji",
    "Psikiyatri",
    "Tıbbi Farmakoloji",
    "Tıbbi Genetik",
    "Cerrahi Tıp Bilimleri",
    "Anestezi ve Reanimasyon",
    "Beyin ve Sinir Cerrahisi",
    "Çocuk Cerrahisi",
    "Genel Cerrahi",
    "Kalp ve Damar Cerrahisi",
    "Göğüs Cerrahisi",
    "Göz Hastalıkları",
    "Kadın Hastalıkları ve Doğum",
    "Kulak Burun Boğaz",
    "Ortopedi ve Travmatoloji",
    "Tıbbi Patoloji",
    "Üroloji",
    "Plastik Rekonstrüktif ve Estetik Cerrahi"
]

fake = Faker()

def create_doctor():
   
    
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
        
    for brans in tıp_branşları:
        for i in range(2):
            name = fake.first_name()
            surname = fake.last_name()
            email = fake.email()
            username = fake.user_name()
            password = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
            birthdate = "1972-02-02"
            phone = fake.phone_number()
            gender = "Erkek"
            address = fake.address()
            department = brans
            hospital = "LaDoctor"
            
            created_date = datetime.datetime.now()
            
            cursor.execute("INSERT INTO user_doctor (name, surname, email, username, password, birthdate, phone, gender, address, department, hospital, created_date) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(name,surname,email,username,password,birthdate,phone,gender,address,department,hospital,created_date))
            
            
    con.commit()
    
    
    con.close()
    
    
def create_appointments():
    start_date = datetime.datetime(2024, 5, 1)
    end_date = datetime.datetime(2024, 12, 31)
    
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    
    # cursor.execute("INSERT INTO user_patient (name, surname, username, email, password, birthdate, phone, gender, address, created_date) VALUES (?,?,?,?,?,?,?,?,?,?)",("test","test","test","test@test.com","9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08","1972-02-02","test","test","test",datetime.datetime.now()))
    # con.commit()
    
            
    cursor.execute("SELECT * FROM user_doctor")
    
    doctors = cursor.fetchall()
    
    current_date = start_date
    while current_date <= end_date:
        for clock in clocks:
            for doctor in doctors:
                appointment_date = current_date.strftime('%Y-%m-%d')
                appointment_date = datetime.datetime.strptime(appointment_date, '%Y-%m-%d').date()
                
                cursor.execute("INSERT INTO appointment_appointment(appointment_date,appointment_time,appointment_details,granted,created_date,doctor_id,patient_id,is_taken) VALUES (?,?,?,?,?,?,?,?)",(appointment_date,clock,"",0,datetime.datetime.now(),doctor[0],1,0))
                
                
        current_date += datetime.timedelta(days=1)
        print(current_date,end="\r")
    
    con.commit()
    
    
def another():
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    
    cursor.execute("SELECT appointmentID,appointment_time FROM appointment_appointment")
    data = cursor.fetchall()
    
    for i in data:
        cursor.execute("UPDATE appointment_appointment SET appointment_time = ? WHERE appointmentID = ?",(i[1]+":00",i[0]))
        
    con.commit()
    
if __name__=="__main__":
    
    another()

import datetime

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, patient_name, doctor, date_time):
        self.patient_name = patient_name
        self.doctor = doctor
        self.date_time = date_time

class HealthcareApp:
    def __init__(self):
        self.doctors = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient_name, doctor_name, date_time):
        for doc in self.doctors:
            if doc.name == doctor_name:
                appointment = Appointment(patient_name, doc, date_time)
                self.appointments.append(appointment)
                print("Appointment scheduled successfully.")
                return
        print("Doctor not found.")

    def display_appointments(self):
        for appointment in self.appointments:
            print("Patient:", appointment.patient_name)
            print("Doctor:", appointment.doctor.name, "(Specialty:", appointment.doctor.specialty, ")")
            print("Date and Time:", appointment.date_time)
            print("-------------------")

if __name__ == "__main__":
    app = HealthcareApp()

    doctor1 = Doctor("Dr. Smith", "Cardiologist")
    doctor2 = Doctor("Dr. Johnson", "Dermatologist")

    app.add_doctor(doctor1)
    app.add_doctor(doctor2)

    date_time = datetime.datetime(2023, 8, 20, 14, 30)
    app.schedule_appointment("John Doe", "Dr. Smith", date_time)

    date_time = datetime.datetime(2023, 8, 20, 15, 45)
    app.schedule_appointment("Jane Doe", "Dr. Johnson", date_time)

    app.display_appointments()


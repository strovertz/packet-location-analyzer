class Person:

    def __init__(self, Address, ip, i):
        self.name = rand_name()
        self.email = rand_email()
        self.gender = gender()
        self.birthday = birthday()
        self.cpf = cpf_gen()
        self.cellphone = cellphone()
        self.user = rand_user()
        self.address = Address
        self.ipAddress = ip
        self.person_id = i
        self.covid = covid_status()
        self.vaccination = vaccination_status()

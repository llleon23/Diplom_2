from faker import Faker
fake = Faker()

def mail_generator():
    generated_mail = fake.email(domain="maeil.com")
    return generated_mail

def fake_password():
    password_fake = str(fake.random_number(8))
    return password_fake

def fake_firstname():
    firstname_fake = fake.first_name()
    return firstname_fake


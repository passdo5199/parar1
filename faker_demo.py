from faker import Faker

fake = Faker()

print("=" * 40)
print("Случай Данные:")
print("=" * 40)

print(f"Имя: {fake.name()}")

print(f"Имя: {fake.name()}")
print(f"Адрес: {fake.address()}")
print(f"Email: {fake.email()}")

print(f"Телефон: {fake.phone_number()}")

print(f"Дата рождение : {fake.date_of_birth()}")

print(f"Професия : {fake.job()}")

print("=" * 40)
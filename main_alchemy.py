from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your PostgreSQL database URL (replace 'your_username', 'your_password', 'your_host', 'your_port', and 'your_database')
DB_URL = 'postgresql://postgres:postgres@localhost:5432/week8'

engine = create_engine(DB_URL, echo=True)

Base = declarative_base()

# Define the Employee class
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    salary = Column(Integer)
    contact_info = Column(String)

Base.metadata.create_all(engine)

# Create a new employee and add them to the database
def create_employee(name, age, salary, contact_info):
    new_employee = Employee(name=name, age=age, salary=salary, contact_info=contact_info)
    session = Session()
    session.add(new_employee)
    session.commit()
    session.close()

# Read all employees from the database
def read_employees():
    session = Session()
    employees = session.query(Employee).all()
    session.close()
    return employees

# Update an employee's information in the database
def update_employee(employee_id, new_info):
    session = Session()
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        for key, value in new_info.items():
            setattr(employee, key, value)
        session.commit()
    session.close()

# Delete an employee from the database
def delete_employee(employee_id):
    session = Session()
    employee = session.query(Employee).filter_by(id=employee_id).first()
    if employee:
        session.delete(employee)
        session.commit()
    session.close()

# Create a session
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    # Example usage

    # Create a new employee
    create_employee("John Doe", 30, 60000, "john@example.com")

    # Read and display all employees
    employees = read_employees()
    print("Employees:")
    for employee in employees:
        print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}, Contact: {employee.contact_info}")

    # Update an employee's information
    update_employee(1, {"salary": 65000, "contact_info": "john.doe@example.com"})

    # Delete an employee
    delete_employee(1)

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

engine= create_engine('postgresql://jerinjose:jerinjose@localhost:5432/alchemy',echo=False)
session= sessionmaker(bind=engine)
session =session()

Base = declarative_base()

class Student(Base):
    __tablename__='student'

    id=Column(Integer, primary_key=True)
    name=Column(String (50))
    age=Column(Integer)
    grade=Column(Integer)

# Base.metadata.create_engine(engine)

student1= Student(name='kelly', age=24, grade='Fifth')
student23= Student(name='Wanyungu', age='29', grade='First')

session.add(student1)
#session.add_all(student1,student2)
session.commit()

#Get all data
students = session.querry(Student)
for student in students:
    print(student.name,student.age,student.age)

#get data by order
students =session.query(Student).order_by(student.name)

for student in students:
    print(student.name)
    
#get data by filtering
student =session.query(student).filter(student.name=="jerrin",).first()

for student in students:
    print(student.name)
    
student = session.query(Student).filter(student.name=="jane", student.name=="kellly")

for student in students:
    print(student.name, student.age)

#count of results
student_count = session.query(Student).filter(or(student.name=="jane", student.name="kellly")).count()
print(student_count)
 
 
# update data
student = session.query(Student).filter(Student.name=='kelvin').first()
student.name="kevin"
session.commit()
print(student.name)


#delete data
student =session.qury(Student).filter(Student.name=="kelvin").first()
session.delete(student)
session.commit()
print(student.name)


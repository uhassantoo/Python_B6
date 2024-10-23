import sqlite3

#Connect to the database
conn = sqlite3.connect('student.db')
cur = conn.cursor()
# Create the students table
cur.execute('''CREATE TABLE student(id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER , course TEXT , grade TEXT)
            ''')

# Commit the changes
conn.commit()

#.....................................................................

# Create a function to add a student

def add_std(id , name ,age , course, grade):
    conn.execute("INSERT INTO student VALUES (?, ? , ? ,?, ?);", (id ,name, age,course,grade))
    conn.commit()
    print(f'Student {name} added Successfully')
    
def view_std():
    cur.execute('SELECT * FROM student')
    return cur.fetchall()
    

#User Interface
def main():
    while True:
        print('\n Student Management System')
        print('1. Add Student')
        print('2. View Students')
        print('6. Exit')
        
        choice = input('Enter your choice:')
        
        if choice == '1':
            id = input('Enter ID..')
            name = input('Enter Name..')
            age = input('Enter age..')
            course = input('Enter Course..')
            grade = input('Enter grade...')
            add_std(id,name,age,course,grade)
        elif choice == '2':
            student = view_std()
            if student:
                print('ALL Students')
                for std in student:
                    print(std)
            else:
                print('No Student data found')
    

# Run the user interface
if __name__ == "__main__":
    main()

conn.close
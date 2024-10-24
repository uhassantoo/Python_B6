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
#Update Function
def update_std(std_id,name,age,course,grade):
    cur.execute('UPDATE student SET name = ?, age = ?, course = ?, grade = ?  WHERE id = ?',(name,age,course,grade,std_id))
    conn.commit()
    print(f"Student ID {std_id} Updated Successfully")

#Delete Function
def delete_std(id):
    cur.execute('DELETE FROM student WHERE id = ? ' ,(id,))
    conn.commit()
    print(f"Student ID {id} Deleted Successfully")
    
#Search Function
def search_std(name):
    cur.execute('SELECT * FROM student WHERE name LIKE ?', ('%' + name + '%'))
    return cur.fetchall()
    

#User Interface
def main():
    while True:
        print('\n Student Management System')
        print('1. Add Student')
        print('2. View Students')
        print('3. Update Students')
        print('4. Delete Students')
        print('5. Search Students')
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
        elif choice == '3':
            std_id = int(input('Enter the Student ID to Update:..'))
            name = input('Enter Name..')
            age = input('Enter age..')
            course = input('Enter Course..')
            grade = input('Enter grade...')
            update_std(std_id,name,age,course,grade)
        elif choice == '4':
            id = int(input('Enter the student ID to delete:'))
            delete_std(id)
        elif choice == '5':
            name = input('Enter the name....')
            print('Search Details...')
            for std in search_std(name):
                print(std)
        elif choice == '6':
            print('Exit the System')
            break
        else:
            print('Invalid Choice Please try again and again....')

# Run the user interface
if __name__ == "__main__":
    main()

conn.close
# You are managing an online course portal that keeps track of student enrollments in two subjects: "Frontend" and "Backend".
# Create two sets:
# One with the names of students enrolled in the Frontend course
# One with the names of students enrolled in the Backend course
# Perform the following tasks:
# Add a new student to the Backend course
# Remove a student from the Frontend course
# Display the list of students who are enrolled in both courses
# Display the list of students who are enrolled only in Backend, but not in Frontend
# Display the total number of unique students
# Create a dictionary where:
# Keys are course names ("Frontend", "Backend")
# Values are the number of students enrolled in each
# Print each course name with the number of students using a loop
# Using dictionary comprehension, create a new dictionary that adds a "Fullstack" course by combining student counts from both existing courses.




frontend_students = {"Alice", "Bob", "Charlie", "Diana"}
backend_students = {"Charlie", "Evan", "Fiona", "Bob"}


backend_students.add("George")


frontend_students.remove("Diana")


both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)


only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)


unique_students = frontend_students | backend_students
print("Total unique students:", len(unique_students))


course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}


for course, count in course_counts.items():
    print(f"{course} has {count} students")


course_counts_with_fullstack = {
    **course_counts,
    "Fullstack": len(unique_students)
}

print("Courses with Fullstack added:", course_counts_with_fullstack)


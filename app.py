from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Helper function to check keywords
def contains_keywords(user_input, keywords):
    return any(word in user_input for word in keywords)

# Rule-based chatbot
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you']
    courses_keywords = ['course', 'classes', 'subjects']
    schedule_keywords = ['schedule', 'timing', 'when', 'time']
    faculty_keywords = ['professor', 'faculty', 'teacher', 'instructor']
    facilities_keywords = ['library', 'lab', 'cafeteria', 'gym', 'facility']
    admission_keywords = ['admission', 'apply', 'requirement', 'deadline']
    location_keywords = ['where', 'location', 'address', 'contact', 'phone']

    # Quit
    if user_input == 'quit':
        return "Thank you for chatting. Have a great day!"

    # Greetings
    if contains_keywords(user_input, greetings):
        return "Hello! How can I help you today?"

    # Farewells
    if contains_keywords(user_input, farewells):
        return "Goodbye! Have a great day!"

    # Thank you
    if 'thank' in user_input:
        return "You're welcome! Do you need help with anything else?"

    # Courses
    if contains_keywords(user_input, courses_keywords):
        if 'computer science' in user_input:
            return "Computer Science courses include Programming, Data Structures, Algorithms, and AI."
        elif 'business' in user_input:
            return "Business courses include Management, Marketing, Finance, and Entrepreneurship."
        elif 'engineering' in user_input:
            return "Engineering courses include Mechanical, Electrical, and Civil Engineering."
        else:
            return "We offer Computer Science, Business, and Engineering programs."

    # Schedule
    if contains_keywords(user_input, schedule_keywords):
        if 'exam' in user_input:
            return "Final exams are scheduled for Dec 15-22."
        if 'class' in user_input or 'lecture' in user_input:
            return "Classes run from 9 AM to 4 PM, Monday–Friday."
        return "Are you asking about classes, exams, or something else?"

    # Faculty
    if contains_keywords(user_input, faculty_keywords):
        if 'computer science' in user_input:
            return "CS department faculty include Dr. Smith (AI) and Dr. Johnson (Data Science)."
        if 'contact' in user_input or 'email' in user_input:
            return "You can find faculty contact info from the university directory."
        return "Experienced faculty are available in all departments."

    # Facilities
    if contains_keywords(user_input, facilities_keywords):
        if 'library' in user_input:
            return "Library open: 8 AM–10 PM weekdays, 10 AM–6 PM weekends."
        if 'lab' in user_input:
            return "Computer labs open until 8 PM weekdays."
        if 'cafeteria' in user_input or 'food' in user_input:
            return "Cafeteria serves breakfast, lunch, and dinner."
        if 'gym' in user_input:
            return "Gym open 6 AM–10 PM, includes cardio, weights, and pool."
        return "Our campus has library, labs, cafeteria, and gym."

    # Admissions
    if contains_keywords(user_input, admission_keywords):
        if 'deadline' in user_input:
            return "Application deadline for Fall semester is Jan 31."
        if 'requirement' in user_input:
            return "Requirements: application, transcripts, and test scores."
        return "For admission details, visit the admissions office."

    # Location
    if contains_keywords(user_input, location_keywords):
        return "University address: 123 Education Street, Knowledge City. Phone: (555) 123-4567."

    # Default fallback
    return "I'm not sure I understand. I can help with courses, schedules, faculty, facilities, and admissions."

# API route
@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

# Home page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

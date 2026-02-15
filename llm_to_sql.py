def nl_to_sql(query):
    query = query.lower()

    if "all students" in query:
        return "SELECT * FROM students"

    elif "cse" in query:
        return "SELECT * FROM students WHERE department='CSE'"

    elif "age" in query:
        return "SELECT name, age FROM students"

    elif "count" in query:
        return "SELECT COUNT(*) FROM students"

    else:
        return None
students = {
    "Mohamed": {
        "grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100
        },
        "age": 20
    },
    "Ahmed": {
        "grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100
        },
        "age": 21
    },
    "Ali": {
        "grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100
        },
        "age": 19
    }
}

mohamed_grades_value = students["Mohamed"]["grades"].values()
sum_mohamed = sum(mohamed_grades_value)
print(f"mohamed's total score is: ")
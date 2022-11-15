import pandas as pd

from collections import defaultdict

names = ["Lessly", "Carlos", "Mathilda", "Pooka"]
ages = [23, 27, 23, 19]
courses = ["Law", "CS", "Business", "Influencer"]


def main() -> None:
    students: dict = defaultdict(dict)
    for i in range(len(names)):
        students[i + 100]["name"] = names[i]
        students[i + 100]["age"] = ages[i]
        students[i + 100]["course"] = courses[i]
    print(f"Current student data:")
    print(students)
    df_students = pd.DataFrame.from_dict(students, orient="index")
    print(f"\nStudents data as DataFrames:")
    print(df_students)


if __name__ == "__main__":
    main()

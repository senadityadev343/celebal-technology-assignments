"""
Q16: The Report - Generate report with Name, Grade, and Mark
"""
query = """
SELECT s.Name, g.Grade, g.Marks
FROM Students s
LEFT JOIN Grades g ON s.ID = g.ID;
"""

if __name__ == '__main__':
    print(query)

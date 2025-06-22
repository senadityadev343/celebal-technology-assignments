"""
Q9: Average Population - Rounded down average population for all cities
"""
query = """
SELECT FLOOR(AVG(Population))
FROM CITY;
"""

if __name__ == '__main__':
    print(query)

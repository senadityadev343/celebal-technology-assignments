"""
Q7: Weather Observation Station 4 - Difference between total and distinct CITY entries
"""
query = """
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;
"""

if __name__ == '__main__':
    print(query)

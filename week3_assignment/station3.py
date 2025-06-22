"""
Q6: Weather Observation Station 3 - Cities with even ID
"""
query = """
SELECT CITY
FROM STATION
WHERE MOD(ID, 2) = 0
ORDER BY ID;
"""

if __name__ == '__main__':
    print(query)

"""
Q8: Weather Observation Station 5 - Shortest and longest city names with lengths
"""
query = """
(SELECT CITY, LENGTH(CITY) AS name_length
 FROM STATION
 ORDER BY name_length
 LIMIT 1)
UNION ALL
(SELECT CITY, LENGTH(CITY) AS name_length
 FROM STATION
 ORDER BY name_length DESC
 LIMIT 1);
"""

if __name__ == '__main__':
    print(query)

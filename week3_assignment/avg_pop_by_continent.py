"""
Q10: Average Population of Each Continent - Rounded down per continent
"""
query = """
SELECT Continent, FLOOR(AVG(Population)) AS avg_population
FROM COUNTRY
GROUP BY Continent
ORDER BY Continent;
"""

if __name__ == '__main__':
    print(query)

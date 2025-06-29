"""
Q15: African Cities - Names of cities where continent is Africa
"""
query = """
SELECT c.Name
FROM City c
JOIN Country ctr ON c.CountryCode = ctr.Code
WHERE ctr.Continent = 'Africa'
ORDER BY c.Name;
"""

if __name__ == '__main__':
    print(query)

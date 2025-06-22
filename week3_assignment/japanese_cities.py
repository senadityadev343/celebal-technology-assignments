"""
Q4: Japanese Cities - Filter Japanese cities in CITY
"""
query = """
SELECT *
FROM CITY
WHERE CountryCode = 'JPN';
"""

if __name__ == '__main__':
    print(query)

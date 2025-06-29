"""
Q12: Population Density Difference - Difference between max and min populations
"""
query = """
SELECT MAX(Population) - MIN(Population)
FROM CITY;
"""

if __name__ == '__main__':
    print(query)

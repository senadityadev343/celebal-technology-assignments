"""
Q2: Select By ID - Fetch details by ID from CITY
"""
query = """
SELECT *
FROM CITY
WHERE ID = <id>;
"""

if __name__ == '__main__':
    print(query)

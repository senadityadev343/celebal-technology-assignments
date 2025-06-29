"""
Q13: Weather Observation Station 19 - Euclidean distance between extremes
"""
query = """
SELECT ROUND(
  SQRT(
    POWER(MAX(LAT_N) - MIN(LAT_N), 2)
    + POWER(MAX(LONG_W) - MIN(LONG_W), 2)
  ), 4
)
FROM STATION;
"""

if __name__ == '__main__':
    print(query)

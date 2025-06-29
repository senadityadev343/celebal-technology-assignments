"""
Q19: Contest Leaderboard - Total score per hacker
"""
query = """
SELECT a.hacker_id, a.name, SUM(b.sscore) AS total_score
FROM Hackers AS a
INNER JOIN (
  SELECT hacker_id, MAX(score) AS sscore
  FROM Submissions
  GROUP BY hacker_id, challenge_id
) AS b ON a.hacker_id = b.hacker_id
GROUP BY a.hacker_id, a.name
HAVING SUM(b.sscore) > 0
ORDER BY SUM(b.sscore) DESC, a.hacker_id ASC;
"""

if __name__ == '__main__':
    print(query)

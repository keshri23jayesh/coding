# https://www.youtube.com/watch?v=IiAsqfjhZnY&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=29

n = 5
k = 4

dp_arr = [[0] * (n + 1) for _ in range (k+1)]

for i in range(0, k+1):
    for j in range(0, n+1):
        if i == 0 or j == 0:
            # first row and first column.
            dp_arr[i][j] = 0
        elif i==j:
            # when team size equal to members, only one way to fill.
            dp_arr[i][j] = 1
        elif i == 1 and j > 0:
            # when only one team needs to be created.
            dp_arr[i][j] = 1

for num_teams in range(1, k+1):
    for team_size in range(2, n+1):
        if num_teams > team_size:
            # not possible
            dp_arr[team_size][num_teams] = 0
        else:
            dp_arr[num_teams][team_size] = dp_arr[num_teams][team_size - 1] * num_teams + dp_arr[num_teams - 1][team_size - 1]


for i in range(k + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            dp_arr[i][j] = 0  # No teams or no members
        elif i == j or i == 1:
            dp_arr[i][j] = 1  # One way to distribute when i == j or all members in one team
        elif i > j:
            dp_arr[i][j] = 0  # More teams than members (not possible)
        else:
            dp_arr[i][j] = dp_arr[i][j - 1] * i + dp_arr[i - 1][j - 1]

print(dp_arr[-1][-1])
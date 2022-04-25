'''
문제
재현이는 주변을 살펴보던 중 체스판과 말을 이용해서 새로운 게임을 만들기로 했다. 
새로운 게임은 크기가 N×N인 체스판에서 진행되고, 사용하는 말의 개수는 K개이다. 
말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다. 
체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.

게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번부터 K번까지 번호가 매겨져 있고, 
이동 방향도 미리 정해져 있다. 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.

턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다. 
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동하며, 가장 아래에 있는 말만 이동할 수 있다. 
말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다. 
턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.

A번 말이 이동하려는 칸이
흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 
A번 말이 이동한 후에는 D, E, A, B, C가 된다.
빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.
파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 
방향을 반대로 한 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 방향만 반대로 바꾼다.
체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
다음은 크기가 4×4인 체스판 위에 말이 4개 있는 경우이다.



첫 번째 턴은 다음과 같이 진행된다.

			
두 번째 턴은 다음과 같이 진행된다.

			
체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때, 게임이 종료되는 턴의 번호를 구해보자.

입력
첫째 줄에 체스판의 크기 N, 말의 개수 K가 주어진다. 둘째 줄부터 N개의 줄에 체스판의 정보가 주어진다. 
체스판의 정보는 정수로 이루어져 있고, 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.

다음 K개의 줄에 말의 정보가 1번 말부터 순서대로 주어진다. 말의 정보는 세 개의 정수로 이루어져 있고, 
순서대로 행, 열의 번호, 이동 방향이다. 행과 열의 번호는 1부터 시작하고, 
이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.

같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다.

출력
게임이 종료되는 턴의 번호를 출력한다. 그 값이 1,000보다 크거나 절대로 게임이 
종료되지 않는 경우에는 -1을 출력한다.

제한
4 ≤ N ≤ 12
4 ≤ K ≤ 10
예제 입력 1 
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2
예제 출력 1 
-1
'''

# 구현+스택 문제라서 코딩 짜는데에는 어렵지 않았음
# 하지만 문제에서 맨 아래에 있는 말만 이동가능하다는 조건을 간과해서 정답과 다른 값이 출려되었음
# 이걸 잡아주니까 해결됨
from sys import stdin
input = stdin.readline 
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
back = [0,2,1,4,3]

def Blue(num,x,y,dir):
  dir = back[dir]
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx<0 or ny<0 or nx>=n or ny>=n or gr[nx][ny]==2:
    inform[num] = [x,y,dir]
    return 0 
  elif gr[nx][ny]==0:
    return White(num,x,y,nx,ny,dir)
  else:
    return Red(num,x,y,nx,ny,dir)

def White(num,x,y,nx,ny,dir):
  t = []
  inform[num] = [nx,ny,dir]
  while(horse[x][y][-1]!=num):
    tt=horse[x][y].pop()
    t.append(tt)
    inform[tt][0] = nx
    inform[tt][1] = ny
  t.append(horse[x][y].pop())
  
  while(t):
    horse[nx][ny].append(t.pop())
  return 4 if len(horse[nx][ny])>=4 else 0
  
def Red(num,x,y,nx,ny,dir):
  inform[num] = [nx,ny,dir]
  while(horse[x][y][-1]!=num):
    t = horse[x][y].pop()
    inform[t][0]=nx
    inform[t][1]=ny
    horse[nx][ny].append(t)
    
  horse[nx][ny].append(horse[x][y].pop())
  return 4 if len(horse[nx][ny])>=4 else 0
n, k = map(int,input().rsplit())
gr = [[0]*n for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input().rsplit()))

horse = [[[] for j in range(n)]for i in range(n)]
inform = [[0,0,0] for i in range(k)]
for i in range(k):
  a,b,c = map(int,input().rsplit())
  a-=1
  b-=1
  inform[i]=[a,b,c]
  horse[a][b].append(i)

check=0
while(check<=1000):
  check+=1
  trigger = False
  for start in range(k):
    x,y,dir = inform[start]
    if horse[x][y][0] != start:
      continue
    nx = x + dx[dir]
    ny = y + dy[dir]
    answer = 0
    if nx<0 or ny<0 or nx>=n or ny>=n or gr[nx][ny]==2:
      answer = Blue(start,x,y,dir)
    elif gr[nx][ny]==0:
      answer = White(start,x,y,nx,ny,dir)
    else:
      answer = Red(start,x,y,nx,ny,dir)
    if answer==4:
      trigger = True
      break
  
  if trigger==True:
    break
print(check if check<1001 else -1)

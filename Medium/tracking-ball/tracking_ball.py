# -*- charset=utf-8 -*-
N = int(input())

"""
Input

5
1 50 1 1 1000
1 50 1 1 6
1 60 -2 1 6
2 10 1 95 -1 2 30
2 10 1 95 -1 2 60

Output

100
56
48
65
70
"""
scenarios = [] # Senaryoları saklayacağımız array

class Scenario:
  def __init__(self, balls, d, t):
    self.balls = balls
    self.d = d
    self.t = t

class Ball:
  def __init__(self, x, v):
    self.x = x
    self.v = v

# Inputu parsela (istenilen işlem için gereksiz, sadece rahatlık ve anlaşılabilirlik için)
for s in range(N):
  inp = list(map(int, input().split()))

  t = inp[len(inp) - 1] # Zamanı al
  d = inp[len(inp) - 2] # İstenilen topun index'ini al

  balls = [] # Topları tutacağımız array

  for i in range(1, 1 + inp[0] * 2, 2):
    # Topları nesneleştir, (Input'un ilk index'i X, ikinci index'i V)
    balls.append(Ball(inp[i], inp[i+1]))

  scenario = Scenario(balls, d, t) # Senaryo için de nesne oluştur

  scenarios.append(scenario) # Senaryoları sakla


"""
Topları bilardo masasında hareket ettir

:param balls: Topların içinde bulunduğu array
:param d: Konumu istenilen topun index'i
:param t: Toplar kaç saniye boyunca hareket edecek
:returns: İstenilen topun en d saniye sonundaki konumu
"""
def simulate(balls, d, t):

  # Zaman döngüsü
  for i in range(t):
	
    for b in range(len(balls)):

      if (b + 1) < len(balls) and balls[b].x >= balls[b + 1].x: # Çarpışma yaşamış mıyız kontrol et

        # Yaşadıysak ivmeleri ters çevir
        balls[b].v = 0 - balls[b].v
        balls[b + 1].v = 0 - balls[b + 1].v
        balls[b + 1].x -= balls[b].v # Vuran topun etkisiyle hareket ettir

      balls[b].x += balls[b].v # Topu hareket ettir

      # Cebe girdiyse masanın dışına çıkartıyoruz topu
      if balls[b].x <= 0 or balls[b].x >= 100:
        if b == d - 1: # Masanın dışına çıkarmadan önce istenilen top bu mu kontrol ediyoruz
          return min([0, 100], key=lambda x:abs(x-balls[b].x)) # 0 - 100 arasında hangisine yakınsa onu döndür
        balls[b].v = 0
        balls[b].x = -1


  return balls[d - 1].x

# Verilen değerleri simulasyona sok
for s in scenarios:
  print(simulate(s.balls, s.d, s.t))

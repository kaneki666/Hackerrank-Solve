def howManyGames(p, d, m, s):
	games = 0
	while s >= p:
		s -= p
		p = max(p - d, m)
		games += 1
	return games

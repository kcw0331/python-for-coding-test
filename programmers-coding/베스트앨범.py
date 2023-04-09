# 프로그래머스 - 해시(베스트앨범)
def solution(genres, plays):
    answer = []
    _dict = {}
    # Use the length of the genres to us a loop in Python.
    for i in range(len(genres)):
        if genres[i] in _dict:
            _dict[genres[i]].append([plays[i], i])
        else:
            _dict[genres[i]] = [[plays[i], i]]
    # Python converts a dictionary into the list.
    _dict_rank = {}
    for i in _dict.keys():
        plays_sum = 0
        for song in _dict[i]:
            plays_sum += song[0]
        _dict_rank[i] = plays_sum
    _dict_rank = sorted(_dict_rank.items(), key = lambda x : x[1], reverse=True)
    # Result of _dict_rank is [4, 1, 3, 0].
    # This is where I create a ranking for the song.
    # And I did the sorting in ascending order.
    for j in _dict_rank:
        song_rank = sorted(_dict[j[0]], key = lambda x : (-x[0], x[1]))
        # -x[0] is the sorting in descending order. Then x[1] is the sorting in ascending order.
        best_two = 0
        # Result of song_rank is [[800, 3], [500, 0], [150, 2]].
        for song in song_rank:
            answer.append(song[1])
            best_two += 1
            if best_two == 2:
                break
    return answer
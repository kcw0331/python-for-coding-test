# 프로그래머스 - 해시(베스트앨범)
def solution(genres, plays):
    answer = []
    _dict = {}
    for i in range(len(genres)):
        if genres[i] in _dict:
            _dict[genres[i]].append([plays[i], i])
        else:
            _dict[genres[i]] = [[plays[i], i]]
    _dict_rank = []
    for i in _dict.keys():
        plays_sum = 0
        for song in _dict[i]:
            plays_sum += song[0]
        _dict_rank[i] = plays_sum
    _dict_rank = sorted(_dict_rnak.items(), key = lambda x : x[1], reverse=True)
    print(_dict_rank)
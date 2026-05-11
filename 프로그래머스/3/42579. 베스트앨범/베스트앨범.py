def solution(genres, plays):
    from collections import defaultdict

    # 장르별 재생 횟수 및 곡 정보 저장
    genres_dict = defaultdict(list)
    for i, genre in enumerate(genres):
        genres_dict[genre].append((plays[i], i))  # (재생 횟수, 인덱스) 형태로 저장

    # 장르별 총 재생 횟수를 기준으로 정렬
    genre_play_counts = {genre: sum(play for play, _ in songs) for genre, songs in genres_dict.items()}
    sorted_genres = sorted(genre_play_counts.keys(), key=lambda g: genre_play_counts[g], reverse=True)

    # 각 장르별 상위 두 곡 선택
    answer = []
    for genre in sorted_genres:
        # 장르 내에서 재생 횟수, 인덱스 기준으로 상위 두 곡 선택
        top_songs = sorted(genres_dict[genre], key=lambda x: (-x[0], x[1]))[:2]
        answer.extend([index for _, index in top_songs])

    return answer

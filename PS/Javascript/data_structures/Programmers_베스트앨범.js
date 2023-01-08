function solution(genres, plays) {
  var answer = [];

  const playPerGenre = new Map();
  const musicPerGenre = new Map();

  genres.forEach((genre, index) => {
    const play = plays[index];

    if (playPerGenre.has(genre)) {
      playPerGenre.set(genre, playPerGenre.get(genre) + play);
      musicPerGenre.get(genre).push([index, play]);
      return;
    }

    playPerGenre.set(genre, play);
    musicPerGenre.set(genre, [[index, play]]);
  });

  const playPerGenreEntries = Array.from(playPerGenre.entries());

  playPerGenreEntries.sort((a, b) => b[1] - a[1]);

  playPerGenreEntries.forEach(([genre, play]) => {
    const musics = musicPerGenre.get(genre);

    musics.sort((a, b) => {
      if (a[1] < b[1]) {
        return 1;
      } else if (a[1] == b[1]) {
        if (a[0] < b[0]) {
          return -1;
        } else if (a[0] === b[0]) {
          return 0;
        }

        return 1;
      }

      return -1;
    });

    answer.push(musics[0][0]);

    if (musics.length >= 2) {
      answer.push(musics[1][0]);
    }
  });

  return answer;
}

class GolfScore:
    def __init__(self, par: list[int], strokes: list[int]):
        if any(map(lambda x: not (3 <= x <=5), par)):
            raise ValueError('規定打数には3以上5以下の数値を入力してください。')
        if any(map(lambda x: not (1 <= x), strokes)):
            raise ValueError('打数には1以上の数値を入力してください。') 
        self._par = par
        self._strokes = strokes
        self._score_dict = {
            -4: 'コンドル',
            -3: 'アルバトロス',
            -2: 'イーグル',
            -1: 'バーディ',
            0: 'パー',
        }
    
    def _check_holeinone(self, par: int, stroke: int) -> bool:
        return stroke == 1 and par in [3, 4]
    
    def _check_bogey(self, par: int, stroke: int) -> bool:
        return stroke - par > 0
    
    def _determine_score(self, par: int, stroke: int) -> str:
        if self._check_holeinone(par, stroke):
            return 'ホールインワン'
        elif self._check_bogey(par, stroke):
            bogey_count = stroke - par
            return 'ボギー' if bogey_count == 1 else f'{bogey_count}ボギー'
        else:
            return self._score_dict.get(stroke - par, '不明なスコア')
    
    def create(self) -> str:
        result = []
        for par, stroke in zip(self._par, self._strokes):
            score = self._determine_score(par, stroke)
            result.append(score)
        return ','.join(result)
    
def view_scores(par: list[int], strokes: list[int]):
    scores = GolfScore(par, strokes).create()
    print(scores)
    

if __name__ == '__main__':
    par = list(map(int, input().split(',')))
    stroke = list(map(int, input().split(',')))
    view_scores(par, stroke)
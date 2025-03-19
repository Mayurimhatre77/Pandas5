import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by=['score'], inplace=True, ascending=False, ignore_index=True)
    scores['rank']=scores['score'].rank(method='dense', ascending=False)

    result= scores[['score', 'rank']]

    return result
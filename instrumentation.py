from collections import defaultdict
from surprise import accuracy

class RecommenderInstrumentation:
    
    def mae(predictions):
        return accuracy.mae(predictions, verbose=False)
    
    def rmse(predictions):
        return accuracy.rmse(predictions, verbose=False)
    
    def getTopN(predictions, n=10):
        topN = defaultdict(list)
        
        for uid, iid, rr, er, _ in predictions:
            topN[int(uid)].append(((int(iid)), er))
            
        for uid, ratings in topN.items():
            ratings.sort(key=lambda x: x[1], reverse=True)
            topN[(int(uid))] = ratings[:n]
            
        return topN
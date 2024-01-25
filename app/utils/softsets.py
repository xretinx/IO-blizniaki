from utils.features import features_softSet

def classification(sample):
        data = features_softSet
        result = {}
        for breed, traits in data.items():
            fit_level = 0
            for trait in traits.keys():
                if traits[trait] == 1:
                    fit_level += sample[trait]
                else:
                    fit_level += 1 - sample[trait]
            result[breed] = (fit_level / len(traits)) 
        # result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        return result

#Example of usage
# sample = {
#     'Sensitive': 0.6,
#     'Introvert': 0,
#     'Family-oriented': 1,
#     'Protective': 0.4,
#     'Friendly': 1,
#     'Extravert': 0.8,
#     'Quick learner': 0,
#     'Intelligent': 0.5,
#     'Communicative': 0.6,
#     'Curious': 0.2,
#     'Energetic': 1,
#     'Emotional': 0.5,
#     'Sport freak': 0.1,
#     'Playfull': 0.9
# }

# print(classification(sample))
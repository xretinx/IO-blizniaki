import pytest

from softsets import classification

def test_correct_result_sample1():
        sample1 = {
    'Sensitive': 0.6,
    'Introvert': 0,
    'Family-oriented': 1,
    'Protective': 0.4,
    'Friendly': 1,
    'Extravert': 0.8,
    'Quick learner': 0,
    'Intelligent': 0.5,
    'Communicative': 0.6,
    'Curious': 0.2,
    'Energetic': 1,
    'Emotional': 0.5,
    'Sport freak': 0.1,
    'Playfull': 0.9
        }


        result = classification(sample1)
        
        assert result=={'Affenpinscher': 72.85714285714286, 'Afghan Hound': 62.85714285714287, 'Airedale Terrier': 55.714285714285715, 'Basenji': 52.85714285714286, 'Basset Hound': 61.42857142857142, 'Beagle': 68.57142857142857, 'Bedlington Terrier': 65.71428571428571, 'Bernese Mountain Dog': 64.28571428571429, 'Black and Tan Coonhound': 67.14285714285714, 'Bloodhound': 62.85714285714285, 'Border Collie': 57.14285714285714, 'Borzoi': 61.42857142857142, 'Bouvier des Flandres': 54.285714285714285, 'Boxer': 57.14285714285714, 'Bullmastiff': 67.14285714285715, 'Chihuahua': 51.42857142857144, 'Cocker Spaniel': 62.85714285714287, 'Dobermann': 52.85714285714287, 'Entlebucher Mountain Dog': 61.42857142857142, 'German Shepherd': 58.57142857142856, 'Golden Retriever': 64.28571428571429, 
'Great Dane': 65.71428571428571, 'Ibizan Hound': 67.14285714285715, 'Irish Terrier': 59.999999999999986, 'Irish Water Spaniel': 65.71428571428571, 'Keeshond': 71.42857142857143, 'Labrador Retriever': 65.71428571428571, 'Lakeland Terrier': 59.999999999999986, 'Maltese': 61.42857142857142, 'Miniature Pinscher': 58.57142857142856, 'Miniature Schnauzer': 47.142857142857146, 'Otterhound': 58.57142857142856, 'Papillon': 64.28571428571429, 'Pekingese': 54.285714285714285, 'Pomeranian': 48.57142857142857, 'Pug': 68.57142857142857, 'Redbone Coonhound': 64.28571428571429, 'Rottweiler': 58.57142857142856, 'Saint Bernard': 70.0, 'Samoyed': 67.14285714285715, 'Schipperke': 57.14285714285714, 'Shetland Sheepdog': 65.71428571428571, 'Shih Tzu': 68.57142857142857, 'Siberian Husky': 68.57142857142857, 'Tibetan Mastiff': 72.85714285714286, 'Toy Fox Terrier': 57.14285714285714, 'Vizsla': 61.42857142857142, 'Weimaraner': 48.57142857142858, 'West Highland White Terrier': 61.42857142857142, 'Yorkshire Terrier': 61.42857142857142}
        

def test_correct_result_sample2():

        sample2 = {
    'Sensitive': 0.1,
    'Introvert': 0,
    'Family-oriented': 0.3,
    'Protective': 0.4,
    'Friendly': 0.7,
    'Extravert': 1,
    'Quick learner': 0.2,
    'Intelligent': 0.8,
    'Communicative': 0.5,
    'Curious': 0.2,
    'Energetic': 1,
    'Emotional': 0.2,
    'Sport freak': 0.6,
    'Playfull': 0.4
}

        result2 = classification(sample2)
        
        assert result2=={'Papillon': 68.57142857142857,
 'Bedlington Terrier': 67.14285714285715,
 'Affenpinscher': 64.28571428571429,
 'Black and Tan Coonhound': 62.85714285714287,
 'Shih Tzu': 62.85714285714285,
 'Basenji': 61.42857142857142,
 'Golden Retriever': 61.42857142857142,
 'Ibizan Hound': 61.42857142857142,
 'Irish Water Spaniel': 61.42857142857142,
 'Shetland Sheepdog': 61.42857142857142,
 'Keeshond': 60.0,
 'Bloodhound': 58.57142857142856,
 'Border Collie': 58.57142857142856,
 'Beagle': 57.14285714285714,
 'Bernese Mountain Dog': 57.14285714285714,
 'Irish Terrier': 57.14285714285714,
 'Labrador Retriever': 57.14285714285714,
 'Lakeland Terrier': 57.14285714285714,
 'Saint Bernard': 57.14285714285714,
 'Samoyed': 57.14285714285714,
 'Siberian Husky': 57.14285714285714,
 'Tibetan Mastiff': 57.14285714285714,
 'Airedale Terrier': 55.714285714285715,
 'Borzoi': 55.714285714285715,
 'Otterhound': 55.714285714285715,
 'Pekingese': 55.71428571428571,
 'Boxer': 54.28571428571429,
 'German Shepherd': 54.28571428571429,
 'Pug': 54.28571428571429,
 'Rottweiler': 54.28571428571429,
 'Afghan Hound': 54.285714285714285,
 'Basset Hound': 54.285714285714285,
 'Great Dane': 52.85714285714286,
 'Vizsla': 52.85714285714286,
 'Entlebucher Mountain Dog': 51.42857142857144,
 'Schipperke': 51.42857142857144,
 'Cocker Spaniel': 50.000000000000014,
 'Redbone Coonhound': 50.0,
 'West Highland White Terrier': 50.0,
 'Miniature Pinscher': 48.57142857142857,
 'Yorkshire Terrier': 48.57142857142857,
 'Bouvier des Flandres': 47.142857142857146,
 'Maltese': 47.142857142857146,
 'Toy Fox Terrier': 47.142857142857146,
 'Miniature Schnauzer': 45.714285714285715,
 'Pomeranian': 45.714285714285715,
 'Dobermann': 44.28571428571429,
 'Chihuahua': 42.85714285714287,
 'Weimaraner': 42.85714285714287,
 'Bullmastiff': 41.42857142857143}
        


from math import *
import csv

#Calculate euclidean distance
#Create dictionary to track euclidean distance
track_euc = {}

def euclidean_distance(x,y):
    result = []
    for a, b in zip(x, y):
        result.append(pow(a-b,2))
    return (sqrt(sum(result)))

fi = open("data.csv", encoding='utf-8')
row_count = sum(1 for row in fi)
print(row_count)
with open('eudist.csv', 'w') as fo:
    v =[]
    for count in range(row_count):
        #print(count)
        fi = open("data.csv", encoding='utf-8')
        dist = []
        #print (fi)
        #print ("count =" +str(count) )
        for x, line in enumerate(fi):
            article_base = [count]
            article_matching = [x]
            if (count < row_count):
                v.append([int(z) for z in (line.split(',')) if z])
                dist.append(euclidean_distance(v[count],v[x]))
        print (dist, file=fo)


#calculate jacard distance
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

fi = open("data.csv", encoding='utf-8')
row_count = sum(1 for row in fi)
print(row_count)
with open('jacdist.csv', 'w') as fo:
    v =[]
    for count in range(row_count):
        fi = open("data.csv", encoding='utf-8')
        dist = []
        for x, line in enumerate(fi):
            article_base = [count]
            article_matching = [x]
            if (count < row_count):
                v.append([int(z) for z in (line.split(',')) if z])
                dist.append(jaccard_similarity(v[count],v[x]))
        print (dist, file=fo)

#Calculate cosine distance
def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
fi = open("data.csv", encoding='utf-8')
row_count = sum(1 for row in fi)
print(row_count)
with open('cosdist.csv', 'w') as fo:
    v =[]
    for count in range(row_count):
        fi = open("data.csv", encoding='utf-8')
        dist = []
        for x, line in enumerate(fi):
            article_base = [count]
            article_matching = [x]
            if (count < row_count):
                v.append([int(z) for z in (line.split(',')) if z])
                dist.append(cosine_similarity(v[count],v[x]))
        print (dist, file=fo)

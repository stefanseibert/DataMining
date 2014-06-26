import feedparser
import re
import numpy as np
from nltk.corpus import stopwords

FEEDLIST = ['http://feeds.reuters.com/reuters/topNews',
            'http://feeds.reuters.com/reuters/businessNews',
            'http://feeds.reuters.com/reuters/worldNews',
            'http://feeds2.feedburner.com/time/world',
            'http://feeds2.feedburner.com/time/business',
            'http://feeds2.feedburner.com/time/politics',
            'http://rss.cnn.com/rss/edition.rss',
            'http://rss.cnn.com/rss/edition_world.rss',
            'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml',
            'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/europe/rss.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml']

# deletes html / xml tags
def stripHTML(h):
  p=''
  s=0
  for c in h:
    if c=='<': s=1
    elif c=='>':
      s=0
      p+=' '
    elif s==0:
      p+=c
  return p

# word separator helper function
sw=stopwords.words('english')
def separatewords(text):
    splitter=re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 4 and s not in sw]

# function parses RSS feed entries, prints them and adds them to one big list
def parseFeeds(feeds):
    parsedFeeds = []
    for feed in feeds:
        parsedFeed = feedparser.parse(feed)
        print "--- News from " + feed + " ---"
        for e in parsedFeed.entries:
            print "-" * 50
            fulltext=stripHTML(e.title+' '+e.description)
            print fulltext
            parsedFeeds.append({'title': stripHTML(e.title), 'description': stripHTML(e.description)})
        print "-" * 50 + "\n"
    return  parsedFeeds



# function returns all words in all feeds, all words in one feed each and all article themes
def getarticlewords():
    feeds = parseFeeds(FEEDLIST)
    allwords = {}
    articlewords = []
    articletitles = []

    splittedStringList = ""
    for feed in feeds:
        articlewordlist = {}
        wholeFeed = feed["title"] + " " + feed["description"]
        splittedStringList = separatewords(wholeFeed.lower())
        for word in splittedStringList:

            if not word in allwords:
                allwords[word] = 1
            else:
                allwords[word] += 1

            if not word in articlewordlist:
                articlewordlist[word] = 1
            else:
                articlewordlist[word] += 1

        articlewords.append(articlewordlist)
        articletitles.append(feed["title"])

    return allwords, articlewords, articletitles

# functions makes a matrix!
def makematrix(allwords, articlewords):
    pass

# execution
allwords, articlewords, articletitles = getarticlewords()
print articlewords


# parseFeeds(FEEDLIST)


def cost(A, B):
    k = 0
    for i in xrange(0,len(A)):
        for j in xrange(0,len(A[i])):
            k += (A[i][j] - B[i][j])**2
    return k


A = np.arange(12).reshape((4,3))

def nnmf(A, m, it):
    c = A.shape[1]      # number of words
    r = A.shape[0]      # number of articles
    H = np.random.random(m * c).reshape((m, c))
    W = np.random.random(r * m).reshape((r, m))

    for i in range(it):
        B = W.dot(H)
        k = cost(A,B)
        print k
        if(k <= 5):
            print H, W
            print W.dot(H)
            return (H, W)
        else:
            for i in range(len(H)):
                for j in range(len(H[i])):
                    nom = (np.transpose(W).dot(A))[i][j]
                    den = (np.transpose(W).dot(W).dot(H))[i][j]
                    H[i][j] = H[i][j] * (nom/den)

            for i in range(len(W)):
                for j in range(len(W[i])):
                    nom = A.dot(np.transpose(H))[i][j]
                    den =(W.dot(H).dot(np.transpose(H)))[i][j]
                    W[i][j] = W[i][j] * (nom/den)


    return (H, W)

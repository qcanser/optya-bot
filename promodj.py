import feedparser

d = feedparser.parse("https://promodj.com/strogonov-radioshow-technopolis/podcast.xml")

print(d.entries[0]['link'])
print(d['entries'][0]['url'])
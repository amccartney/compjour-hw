import requests
dirname = "data-hold/stuff"
print ("Downloading the news.stanford.edu homepage")

response = requests.get("http://news.stanford.edu")

rawhtml = response.text

print ("news.stanford.edu has", len(rawhtml), "characters")

print ("Saving the current news.stanford.edu to my %s folder" % dirname)

f = open(dirname + "/news.stanford.edu.html", "w")
f.write(rawhtml)
f.close
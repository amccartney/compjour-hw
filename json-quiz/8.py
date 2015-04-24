import requests, json, os
from collections import Counter
from operator import itemgetter

data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'

data = json.loads(requests.get(data_url).text)
books = data['results']['books']

# Answer A
scrib = 0
for b in books:
	if b['publisher'] == 'Scribner':
		scrib += 1

print("A. " + str(scrib))


# Answer B
detective_books = 0
for b in books:
	if 'detective' in b['description'].lower():
		detective_books += 1

print("B. " + str(detective_books))		


# Answer C
book_list = []
for b in books:
	book_list.append(b)

t = sorted(book_list, key = itemgetter('weeks_on_list'), reverse = True)
s = t[0]

print("C. " + s['title'] + "|" + str(s['weeks_on_list']))


# Answer D
x = sorted(book_list, key = itemgetter('rank_last_week'), reverse = True)
y = x[0]

print("D. " + y['title'] + '|' + str(y['rank']) + '|' + str(y['rank_last_week']))


# Answer E
new_books = 0
for b in books:
	if b['rank_last_week'] == 0:
		new_books += 1

print("E. " + str(new_books))		


# Answer F
new_books_list = []
for b in books:
	if b['rank_last_week'] == 0:
		new_books_list.append(b)

g = sorted(new_books_list, key = itemgetter('rank'))
h = g[0]

print("F. " + h['title'] + '|' + str(h['rank']))


# Answer G
def calc_rank_change(book_obj):
    return book_obj["rank_last_week"] - book_obj["rank"]

books_ranked_last_week = [b for b in books if b['rank_last_week'] > 0]
x = max(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("G.", s)


# Answer H
x = min(books_ranked_last_week, key = calc_rank_change)
s = "|".join([x['title'], str(x['rank']), str(calc_rank_change(x))])
print("H.", s)


# Answer I
changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v > 0]
s = sum(x)
print("I. " + str(s))


# Answer J
changes = [calc_rank_change(b) for b in books_ranked_last_week]
x = [v for v in changes if v < 0]
s = sum(x)
print("J. " + str(len(x)) + '|' + str(s))


# Answer K
print('K.', max([len(b['title']) for b in books]))	


# Answer L
totes_titles = 0
for b in books:
	totes_titles += len(b['title'])

avg_title_len = int(totes_titles / len(books))	

print("L. " + str(avg_title_len))

"""
Prompt
------------------
Given a list of page impression logging events on a website, write a function that takes as input: 1) log events, 2) a page url, 3) an integer “n”, and reports the top n referrers to the given page url. You can assume that log events can be stored in memory in list of objects of the following type: Entry(visitor_id: String, page: String, prev_page: String, ts: String)

Definitions
------------------
Page: A unique page on a website identified by a unique URL. For this question, we will assume these are simple strings rather than fully formed urls.
Referrer: When visiting a web page, the referrer or referring page is the URL of the previous web page from which a link was followed.

Example

------------------
For the following input:
log_events: …
page: pdp
n: 3

Example input for log_event

entries=[
   (111, 'pdp', 'checkout', '2023-01-01 01:01:01'),
   (111, 'pdp', 'checkout', '2023-01-01 01:01:01'),
   (111, 'pdp', 'search', '2023-01-01 01:01:01'),
   (111, 'pdp', 'search', '2023-01-01 01:01:01'),
   (111, 'pdp', 'search', '2023-01-01 01:01:01'),
   (111, 'pdp', 'pdp', '2023-01-01 01:01:01'),
   (111, 'pdp', 'pdp', '2023-01-01 01:01:01'),
   (111, 'pdp', 'wishlist', '2023-01-01 01:01:01')
]

The function should return the top 3 referrers to the pdp page (the exact format can be flexible as long as the results are valid):
result = {
    checkout: 2,
    search: 3,
    pdp: 2
}

"""

def top_n_referrers(entries, page, n):
    dict = {}

    if len(entries) == 0:
        return None

    for item in entries:
        if item[1] != page:
            continue
        if item[2] in dict.keys():
            dict[item[2]] = dict[item[2]] + 1
        else:
            dict[item[2]] = 1

    return sorted(dict.items(), key=lambda x: x[1], reverse=True)[:3]

def main():

    entries = [
        (111, 'pdp', 'checkout', '2023-01-01 01:01:01'),
        (111, 'pdp', 'checkout', '2023-01-01 01:01:01'),
        (111, 'pdp', 'search', '2023-01-01 01:01:01'),
        (111, 'pdp', 'search', '2023-01-01 01:01:01'),
        (111, 'pdp', 'search', '2023-01-01 01:01:01'),
        (111, 'pdp', 'pdp', '2023-01-01 01:01:01'),
        (111, 'pdp', 'pdp', '2023-01-01 01:01:01'),
        (111, 'pdp', 'wishlist', '2023-01-01 01:01:01'),
        (111, 'home', 'pdp', 'something')
    ]

    page = 'pdp'
    n = 3
    print(top_n_referrers(entries, page, n))

if __name__=='__main__':
    main()
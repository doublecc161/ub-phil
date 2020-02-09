# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import re
from datetime import datetime

#
# # Read in a page
html = scraperwiki.scrape("https://auslastung.ub.uni-muenchen.de/index.php?r=site/grafik&user=phil")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("div[align='left']")


now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y_%H:%M:%S")



regex = r"(?<=google\.visualization\.arrayToDataTable\()(.*?)(?=\)\;)"
matches = re.findall(regex, html, flags=0)

print("matches: ",matches, "date: ", date_time)

#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"match": matches, "date": date_time})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

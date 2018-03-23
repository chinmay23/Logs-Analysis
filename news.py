#!/usr/bin/env python

import psycopg2

question_1 = 'What are the most popular three articles of all time?'
query_1 = """
select title, count(*) as views from articles inner join
log on concat('/article/', articles.slug) = log.path
where log.status like '%200%'
group by log.path, articles.title order by views desc limit 3;
"""

question_2 = 'Who are the most popular article authors of all time?'
query_2 = """
select authors.name, count(*) as views from articles inner join
authors on articles.author = authors.id inner join
log on concat('/article/', articles.slug) = log.path where
log.status like '%200%' group by authors.name order by views desc
"""

question_3 = 'On which days did more than 1% of requests lead to errors?'
query_3 = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where errp > 1.0;
"""


class News:

    def __init__(self):
        # fetch data from database
        self.db = psycopg2.connect('dbname=news')
        self.cursor = self.db.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # execution and fetching results
    def analysis(self, question, query, suffix='views'):
        query = query.replace('\n', ' ')
        result = self.execute(query)
        print question
        for i in range(len(result)):
            print '\t', result[i][0], ':', result[i][1], suffix
        # blank line
        print ''
    # close connection

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    news = News()
    # function call
    news.analysis(question_1, query_1)
    news.analysis(question_2, query_2)
    news.analysis(question_3, query_3, '% error')
    news.exit()

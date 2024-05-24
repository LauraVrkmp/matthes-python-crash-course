from operator import itemgetter
import plotly.express as px

import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f"Key Error for {response_dict['title']}")

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

post_links, comment_counts, hover_texts = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict['title'][:30]
    discussion_link = submission_dict['hn_link']
    post_link = f"<a href='{discussion_link}'>{title}</a>"
    comment_count = submission_dict['comments']

    post_links.append(post_link)
    comment_counts.append(comment_count)
    hover_texts.append(submission_dict['title'])

title = "Most-Commented posts on Hacker News"
labels = {'x': 'Post', 'y': 'Comments'}
fig = px.bar(x=post_links, y=comment_counts, title=title, 
             labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.write_html('first_figure.html', auto_open=True)

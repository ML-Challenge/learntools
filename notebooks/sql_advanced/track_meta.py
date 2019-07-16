# See also examples/example_track/example_meta.py for a longer, commented example
track = dict(
    author_username='dansbecker',
    course_name='SQL',
    course_url='https://www.kaggle.com/learn/advanced-sql'
)

lessons = [ {'topic': topic_name} for topic_name in
                    ['Window Functions',]
            ]

notebooks = [
    dict(
        filename='tut1.ipynb',
        lesson_idx=0,
        type='tutorial',
        dataset_sources = ["chicago/chicago-taxi-trips-bq", "datasf/san-francisco", "hacker-news/hacker-news"],
        ),
    dict(
        filename='ex1.ipynb',
        lesson_idx=0,
        type='exercise',
        dataset_sources = ["hacker-news/hacker-news", "chicago/chicago-crime"],
        scriptid=-1
        ),
]

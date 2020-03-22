import json

from questions.redis_client import redis_client


def get_questions() -> dict:
    if redis_client.hget('questions', 'basic'):
        questions = json.loads(redis_client.hget('questions', 'basic'))

    else:
        with open('questions/data/questions.json') as data_file:
            questions = json.load(data_file)
            redis_client.hset('questions', 'basic', json.dumps(questions))

    return questions


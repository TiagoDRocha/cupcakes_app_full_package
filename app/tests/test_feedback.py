def test_feedback_submission(client):
    rv = client.get('/feedback')
    assert rv.status_code == 200

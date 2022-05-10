def test_about(test_app):
    res = test_app.get('/about')
    assert res.status_code == 200
    assert b'Meet the Team' in res.data


def test_forum_page(test_app):
    res = test_app.get('/forum')
    assert res.status_code == 200
    assert b'Forum' in res.data


def test_user_page(test_app):
    res = test_app.post(
        '/signup',
        data={
            'fullname': 'Ross',
            'username': 'strongman18',
            'email': 'email@gmail.com',
            'password': 'password123',
        },
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert b'Ross' in res.data
    assert b'strongman18' in res.data

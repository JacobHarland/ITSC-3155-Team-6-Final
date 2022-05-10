from petpals.models import Post, User, Pet

testuser = User(
    fullname='Ross',
    username='strongman18',
    email='email@gmail.com',
    password='password123',
)
testpost = Post(title='Test title', content='Test content', user_id=1)
testpet = Pet(
    name='Garcia',
    species='Cat',
    subspecies='Friend',
    color='Orange',
    tagline='Tagline',
    biography='Bio',
    user_id=1,
)


def test_user_model():
    assert testuser.fullname == 'Ross'
    assert testuser.username == 'strongman18'
    assert testuser.email == 'email@gmail.com'
    assert testuser.password == 'password123'


def test_post_model():
    assert testpost.title == 'Test title'
    assert testpost.content == 'Test content'
    assert testpost.user_id == 1


def test_pet_model():
    assert testpet.name == 'Garcia'
    assert testpet.species == 'Cat'
    assert testpet.subspecies == 'Friend'
    assert testpet.color == 'Orange'
    assert testpet.tagline == 'Tagline'
    assert testpet.biography == 'Bio'
    assert testpet.user_id == 1

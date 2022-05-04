from petpals.models import Post, User, Pet, Reply

testuser = User(1, 'Ross', 'strongman18', 'email@gmail.com', 'images/image.png', 'password123')
testpost = Post(1, 'Test title', 'Test content', 5, testuser)
testreply = Reply(1, 'Reply content', testuser, testpost)
testpet = Pet(1, 'Garcia', 'Cat', 'Orange', testuser)

def test_user_model():
    assert testuser.fullname == 'Ross'
    assert testuser.username == 'strongman18'
    assert testuser.email == 'email@gmail.com'
    assert testuser._image_file == 'images/image.png'
    assert testuser.password == 'password123'

def test_post_model():
    assert testpost.post_id == 1
    assert testpost.title == 'Test title'
    assert testpost.content == 'Test content'
    assert testpost.views == 5

    assert testpost.author == testuser
    assert testpost.author.id == 1

def test_reply_model():
    assert testreply.reply_id == 1
    assert testreply.content == 'Reply content'
    assert testreply.author == testuser
    assert testreply.op == testpost

def test_pet_model():
    assert testpet.pet_id == 1
    assert testpet.name == 'Garcia'
    assert testpet.species == 'Cat'
    assert testpet.subspecies == 'Orange'
    assert testpet.owner == testuser
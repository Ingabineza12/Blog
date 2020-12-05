import unittest
from app.models import User,Post
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        '''
        method to set all test
        '''
        self.user=User(username='deborah',pass_secure='deborah',email='ingabineza@gmail.com')
        self.newpost=Post(title='read',category='read',user_id=self.id)
    def tearDown(self):
        '''
        detete test
        '''
        User.query.delete()
        Post.query.delete()

    def test_check_instance_variables(self):
        '''
        test
        '''
        self.assertEquals(self.newpost.title,'read')
        self.assertEquals(self.newpost.category,'read')
        self.assertEquals(self.newpost.user_id,self.user_admin)

    def test_save(self):
        '''
        test for saving
        '''
        self.newpost.save_u()
        got_post=Post.query.get(1)
        self.assertTrue(len(got_post)==1)

    # def test_save_article(self):
    #     '''
    #     test saving in the db
    #     '''
    #     self.new_article.save_article()
    #     self.assertTrue(len(Review.query.all())>0)

    # def test_get_article_by_id(self):
    #     '''
    #     tests getting article by id
    #     '''
    #     self.new_article.save_article()
    #     got_article = Article.query.get(1)
    #     self.assertTrue(len(got_article)==1)

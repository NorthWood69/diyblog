from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blogger, Blog, Comment
import datetime

class BloggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        Blogger.objects.create(name=test_user1, bio='This is a bio')

    def test_get_absolute_url(self):
        name=Blogger.objects.get(id=2)
        self.assertEquals(name.get_absolute_url(),'/blog/blogger/2')

    def test_name_label(self):
        name=Blogger.objects.get(id=2)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Name')

    def test_bio_label(self):
        bio=Blogger.objects.get(id=2)
        field_label = bio._meta.get_field('bio').verbose_name
        self.assertEquals(field_label,'Bio')

    def test_bio_max_length(self):
        bio=Blogger.objects.get(id=2)
        max_length = bio._meta.get_field('bio').max_length
        self.assertEquals(max_length,1000)

    def test_object_name(self):
        name=Blogger.objects.get(id=2)
        expected_object_name = name.name.username
        self.assertEquals(expected_object_name,str(name))

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        blog_author = Blogger.objects.create(name=test_user1, bio='This is a bio')
        blog = Blog.objects.create(title='Test Blog 1',author=blog_author,description='Test Blog 1 Description')

    def test_get_absolute_url(self):
        blog=Blog.objects.get(id=1)
        self.assertEquals(blog.get_absolute_url(),'/blog/1')

    def test_name_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_name_max_length(self):
        blog=Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length,100)

    def test_description_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'Description')

    def test_description_max_length(self):
        blog=Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEquals(max_length,1000)

    def test_author_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEquals(field_label,'Author')

    def test_date_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label,'Post date')

    def test_date(self):
        blog=Blog.objects.get(id=1)
        the_date = blog.post_date
        self.assertEquals(the_date,datetime.date.today())

    def test_object_name(self):
        blog=Blog.objects.get(id=1)
        expected_object_title = blog.title
        self.assertEquals(expected_object_title,str(blog))

class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345') 
        test_user2.save()
        blog_author = Blogger.objects.create(name=test_user1, bio='This is a bio')
        blog_test = Blog.objects.create(title='Test Blog 1',author=blog_author,description='Test Blog 1 Description')
        blog_comment=Comment.objects.create(comment='Test Blog 1 Comment 1 Description', author=test_user2,blog=blog_test)

    def test_description_label(self):
        blogcomment=Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('comment').verbose_name
        self.assertEquals(field_label,'Comment')

    def test_description_max_length(self):
        blogcomment=Comment.objects.get(id=1)
        max_length = blogcomment._meta.get_field('comment').max_length
        self.assertEquals(max_length,1000)

    def test_author_label(self):
        blogcomment=Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('author').verbose_name
        self.assertEquals(field_label,'author')

    def test_date_label(self):
        blogcomment=Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('comment_date').verbose_name
        self.assertEquals(field_label,'Created')

    def test_blog_label(self):
        blogcomment=Comment.objects.get(id=1)
        field_label = blogcomment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label,'blog')

    def test_object_name(self):
        blogcomment=Comment.objects.get(id=1)
        expected_object_name = ''
        if len(blogcomment.comment)>75:
            expected_object_name=blogcomment.comment[:72] + '...'
        else:
            expected_object_name=blogcomment.comment
        self.assertEquals(expected_object_name,str(blogcomment))

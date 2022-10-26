from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog(title="Blog", author="Test")
        self.assertEqual(blog.title, "Blog")
        self.assertEqual(blog.author, "Test")
        self.assertEqual(len(blog.posts), 0)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog = Blog(title="Blog", author="Test")
        blog2 = Blog(title="Test", author="Test Author")

        self.assertEqual(blog.__repr__(), "Blog by Test (0 posts)")
        self.assertEqual(blog2.__repr__(), "Test by Test Author (0 posts)")

    def test_repr_multiple_posts(self):
        blog = Blog(title="Blog", author="Test")
        blog2 = Blog(title="Blog", author="Test")
        blog.posts = ["testing"]
        blog2.posts = ["orange", "tomato"]
        self.assertEqual(blog.__repr__(), "Blog by Test (1 post)")
        self.assertEqual(blog2.__repr__(), "Blog by Test (2 posts)")





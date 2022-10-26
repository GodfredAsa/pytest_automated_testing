from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        blog = Blog(title="Blog", author="Test Author")
        blog.create_post("Test Post", "Test Content")
        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, "Test Post")
        self.assertEqual(blog.posts[0].content, "Test Content")

    def test_json_no_post(self):
        blog = Blog(title="Test", author="Test Author")
        expected = {"title": "Test", "author": "Test Author",
                    "posts": []
                    }
        actual = blog.json()
        self.assertDictEqual(expected, actual)

    def test_json(self):
        blog = Blog(title="Test", author="Test Author")
        blog.create_post("Test Post", "Test Content")
        expected = {
            "title": "Test", "author": "Test Author",
            "posts": [
                {"title": "Test Post",
                 "content": "Test Content"
                 }
            ]
        }
        self.assertDictEqual(expected, blog.json())

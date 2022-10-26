from unittest import TestCase

from blog.post import Post


class PostTest(TestCase):
    def test_create_post(self):
        post = Post(title="Test", content="Test Content")
        self.assertEqual("Test", post.title)
        self.assertEqual("Test Content", post.content)

    def test_json(self):
        post = Post(title="Test", content="Test Content")
        expected = {"title": "Test", "content": "Test Content"}
        actual = post.json()
        self.assertDictEqual(expected, actual)

    def test_repr(self):
        post = Post(title="Test", content="Test Content")
        expected = "title: Test and content: Test Content"
        self.assertTrue(post, expected)





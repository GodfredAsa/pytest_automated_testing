from unittest import TestCase
from unittest.mock import patch
from blog import app
from blog.blog import Blog
from blog.post import Post


class AppTest(TestCase):
    def setUp(self) -> None:
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}


    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            with patch("app.create_blog") as mocked_create_blog:
                mocked_input.side_effect("c", "Test Create Blog", "q")
                app.menu()
                mocked_create_blog.assert_called()

    def test_print_blogs(self):

        with patch('builtins.print') as mock_print:
            app.print_blogs()
            mock_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mock_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mock_print_blogs.assert_called()

    def test_menu_print_prompt(self):
        with patch('builtins.input', return_value="q") as mock_print:
            app.menu()
            mock_print.assert_called_with(app.MENU_PROMPT)

    # return_value = "Test" could have been used in the patch however it returns just a single value hence
    # using the side effect to return multiple values
    # it returns one of the values at each instance of the run of the test
    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ("Test", "Test Author")
            app.create_blog()
            self.assertIsNotNone(app.blogs.get("Test"))

    def test_read_blogs(self):
        blog = app.blogs["Test"]
        with patch('builtins.input', return_value="Test"):
            with patch('blog.app.print_posts') as mocked_print_posts:
                app.read_blogs()
                mocked_print_posts.ssert_called_with(blog)

    def test_print_posts(self):
        blog = app.blogs["Test"]
        blog.create_post("Test Post", "Test Content")
        with patch('blog.app.print_posts') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog)

    def test_print_post(self):
        post = Post("Post title", "Post content")
        expected = "Title: Post title content: Post content"
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected)

    def test_create_post(self):
        blog = app.blogs["Test"]
        blog.create_post("Test Title", "Test Content")
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Title", "Test Content")
            app.create_post()
            self.assertEqual(blog.posts[0].title, "Test Title")
            self.assertEqual(blog.posts[0].content, "Test Content")
            self.assertEqual(blog.title, "Test")

    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs["Test Create Blog"])

    def test_menu_calls_print_blog(self):
        blog = app.blogs["Test"]
        blog.create_post("Test Title", "Test Content")
        with patch("builtins.input", return_value="") as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            app.menu()
            self.assertIsNone(app.print_post(blog.posts[0]))















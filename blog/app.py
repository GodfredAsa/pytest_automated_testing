from blog.blog import Blog

blogs = dict() # blog_name to blog_object
MENU_PROMPT = "Enter 'c' create blog, 'l' list blogs 'p' create post and 'q' quit"
POST_TEMPLATE = "Title: {} content: {}"

def menu():
    # show available blogs
    # let user make a choice
    # do something with the choice
    # exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blogs()
        elif selection == 'p':
            create_post()
        selection = input(MENU_PROMPT)


def read_blogs():
    title = input("Enter blog Title: ")
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def create_blog():
    title = input("Enter blog Title: ")
    blog_author = input("Enter blog Author: ")
    blogs[title] = Blog(title, blog_author)

def create_post():
    blog_name = input("Enter blog name or title: ")
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    blogs[blog_name].create_post(title, content)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


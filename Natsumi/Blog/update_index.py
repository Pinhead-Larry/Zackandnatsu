import os

# Directory containing the posts
posts_directory = 'Posts'
index_file = 'index.md'
recent_posts_count = 5  # Number of recent posts to display

# Get a list of Markdown files in the posts directory
posts = [f for f in os.listdir(posts_directory) if f.endswith('.md')]
posts_with_dates = []

# Collect post filenames and their modification times
for post in posts:
    post_path = os.path.join(posts_directory, post)
    modification_time = os.path.getmtime(post_path)
    posts_with_dates.append((post, modification_time))

# Sort posts by modification time (most recent first)
sorted_posts = sorted(posts_with_dates, key=lambda x: x[1], reverse=True)

# Prepare the content for index.md with Markdown formatting
index_content = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            margin-bottom: 20px;
        }
        .post {
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background: white;
        }
        a {
            text-decoration: none;
            color: #007bff;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Recent Blog Posts</h1>
"""

for post, _ in sorted_posts[:recent_posts_count]:
    post_path = os.path.join(posts_directory, post)

    # Read the content of the post and extract a portion (e.g., first 100 characters)
    with open(post_path, 'r', encoding='utf-8') as f:
        post_content = f.read()

    # Generate a snippet
    snippet = post_content[:100] + "..." if len(post_content) > 100 else post_content

    # Format the entry for the index
    index_content += f"""\
    <div class="post">
        <h2><a href="{posts_directory}/{post}">{post[:-3]}</a></h2>
        <p>{snippet}</p>
    </div>
"""

# Close HTML tags
index_content += """\
</body>
</html>
"""

# Write the index content to index.md
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Updated {index_file} with the latest posts.")

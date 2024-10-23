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
index_content = "# Recent Blog Posts\n\n"

for post, _ in sorted_posts[:recent_posts_count]:
    post_path = os.path.join(posts_directory, post)

    # Read the content of the post and extract a portion (e.g., first 100 characters)
    with open(post_path, 'r', encoding='utf-8') as f:
        post_content = f.read()

    # Generate a snippet
    snippet = post_content[:100] + "..." if len(post_content) > 100 else post_content

    # Format the entry for the index
    index_content += f"## [{post[:-3]}]({posts_directory}/{post})  \n{snippet}\n\n"

# Write the index content to index.md
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Updated {index_file} with the latest posts.")

import json

# Full path to the files
posts_path = r"details.json"
comments_path = r"comments.json"
output_path = r"merged_posts.json"

with open(posts_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

with open(comments_path, "r", encoding="utf-8") as f:
    comments = json.load(f)

# Group and merge
comments_by_shortcode = {}
for comment in comments:
    shortcode = comment.get("shortCode")
    if shortcode:
        comment_copy = comment.copy()
        comment_copy.pop("shortCode", None)
        comments_by_shortcode.setdefault(shortcode, []).append(comment_copy)

for post in posts:
    shortcode = post.get("shortcode")
    post["comments_data"] = comments_by_shortcode.get(shortcode, [])

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("✅ Merging complete. Output saved to merged_posts.json")

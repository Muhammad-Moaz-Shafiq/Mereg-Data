# 🧩 Instagram Post Comments Merger

This Python script merges Instagram **post details** with their corresponding **comments**, providing a complete, structured dataset for each post. It’s perfect for data analysis, archiving, and reporting.

## ✅ Features

- 📂 Accepts multiple `post detail` and `post comments` JSON files
- 🔗 Automatically matches posts using `shortcode` or `id`
- 🔁 Batch processing — handles multiple posts at once
- 💬 Merges all comments and replies into their respective posts
- 💾 Outputs a clean, structured JSON file
- 🔧 Ideal for content research, engagement tracking, and machine learning datasets

---

## 📥 Input Requirements

You need two types of input files:

1. **Post Details File**  
   Example format:
   ```json
   {
     "input_url": "https://www.instagram.com/p/DJEoJ7soZ6G/",
     "id": 3622196604748013190,
     "shortcode": "DJEoJ7soZ6G",
     "type": "image",
     "caption": "...",
     "likes": 953,
     "timestamp": "2025-04-30 13:25:05",
     "comments": 27,
     ...
   }

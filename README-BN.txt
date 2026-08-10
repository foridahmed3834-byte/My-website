FORID AHMED — UNLIMITED BLOG WEBSITE

GitHub Pages-এর জন্য তৈরি।

ফাইল:
- index.html              = Blog list
- blog-post-1.html ...    = static Blog pages
- posts.json              = এখানেই নতুন Blog যোগ করবে
- generate_blogs.py       = সব Blog page নতুন করে তৈরি করবে
- style.css               = design
- images/                 = blog images রাখবে

নতুন Blog যোগ:
posts.json-এ এমন একটি object যোগ করো:
{
  "id": 9,
  "title": "Blog Post 9: আমার নতুন পোস্ট — Forid Ahmed",
  "description": "ছোট description",
  "image": "images/blog9.jpg",
  "date": "2026-08-10",
  "content": "<p>এখানে সম্পূর্ণ Blog লেখা...</p>"
}

তারপর PC-তে:
python generate_blogs.py

এতে blog-post-9.html তৈরি হবে।

গুরুত্বপূর্ণ:
প্রতিটি static Blog page-এ আলাদা og:title, og:description, og:image,
og:url এবং Twitter Card আছে। তাই Facebook share preview-এর জন্য
প্রতিটি URL আলাদা।

তোমার আসল blog ছবি images/ ফোল্ডারে blog1.jpg, blog2.jpg ... নামে রাখবে।
GitHub repository-তে এই files upload/replace করে commit করলে GitHub Pages-এ website চলবে।

যদি তোমার existing index.html-এ অন্য design থাকে, সেটি backup রেখে এই demo index.html সরাসরি replace না করে
শুধু blog অংশ integrate করাই ভালো।

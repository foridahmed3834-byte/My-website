UNLIMITED BLOG SYSTEM

নতুন Blog যোগ করতে posts.json-এ এই structure ব্যবহার করো:

{
  "id": 9,
  "date": "10-08-2026",
  "title": "Blog Post 9: নতুন পোস্ট — Forid Ahmed",
  "description": "ছোট description",
  "image": "images/blog9.jpg",
  "content": "<p>এখানে সম্পূর্ণ Blog লেখা...</p>"
}

তারপর generate_blogs.bat double-click করো।
তাহলে blog-post-9.html তৈরি হবে।

ID 10, 11, 12... দিয়ে যত Blog দরকার তৈরি করতে পারবে।
blog.html সব Blog automatically list করবে।

Facebook share preview-এর জন্য প্রতিটি Blog-এর আলাদা static HTML এবং
আলাদা og:title, og:description, og:image, og:url আছে।

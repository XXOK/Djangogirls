# from django import template
# from blog.models import Post
# import re
#
# register = template.Library()
# posts = Post.objects.all().order_by('-created_at')
#
# @register.filter
# def add_link(value):
#     content = value.content # 전달된 value 객체의 content 멤버변수를 가져온다.
#     posts = Post.objects.all().order_by('-created_at') # 전달된 value 객체의 tag_set 전체를 가져오는 queryset을 리턴한다.
#
#     # tags의 각각의 인스턴를(tag)를 순회하며, content 내에서 해당 문자열을 => 링크를 포함한 문자열로 replace 한다.
#     for post in posts:
#         regex = re.compile(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$')
#         result = re.match(regex, post.text)
#         content = re.sub(r''+result+r'', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content)
#     return content # 원하는 문자열로 치환이 완료된 content를 리턴한다.
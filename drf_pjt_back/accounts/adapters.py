from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        # super()를 사용하여 부모의 데이터(기본 데이터)를 저장
        user = super().save_user(request, user, form, False)
        # 저장하고자 하는 추가 필드를 아래와 같이 여러 개 정의한 다음 user의 속성 값에 할당
        # user의 속성 값은 우리가 지정한 데이터 필드 이름
        profile_img = data.get("profile_img")
        school = data.get("school")
        career = data.get("career")
        introduce = data.get("introduce")
        github_url = data.get("github_url")
        blog_url = data.get("blog_url")
        notion_url = data.get("notion_url")
        
        if profile_img:
            user.profile_img = profile_img
        if school:
            user.school = school
        if career:
            user.career = career
        if introduce:
            user.introduce = introduce
        if github_url:
            user.github_url = github_url
        if blog_url:
            user.blog_url = blog_url
        if notion_url:
            user.notion_url = notion_url

        user.save() # 저장
        return user
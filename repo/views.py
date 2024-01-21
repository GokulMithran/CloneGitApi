from django.shortcuts import render

from django.core.paginator import Paginator

# Create your views here.
# def home(request):
#     return render(request,'index.html')

from django.shortcuts import render
import requests
from .models import UserProfile, Repository ,Topic

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        repos_per_page=request.POST.get('repos_per_page')
        api_url = f'https://api.github.com/users/{username}'
        headers={
            "Authorization":"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"
        }

        try:
            user_data = requests.get(api_url).json()
            repositories = requests.get(f'{api_url}/repos?per_page={int(repos_per_page)}',headers=headers).json()
            # pp=request.get(f'{api_url}/repos?per_page=10')
            # Create or update user profile
            user_profile, created = UserProfile.objects.get_or_create(username=username, defaults={'avatar_url': user_data.get('avatar_url', '')})
            user_profile.avatar_url = user_data.get('avatar_url', '')
            user_profile.userlocation=user_data.get('location')
            user_profile.userbio=user_data.get('bio')
            user_profile.usertwitter=user_data.get('twitter_username')
            # print(user_data['location'])
            user_profile.repositories.clear()

            for repo_data in repositories:
                repo, _ = Repository.objects.get_or_create(
                    name=repo_data['name'],
                    defaults={'description': repo_data.get('description', ''), 'html_url': repo_data['html_url']}
                )
                user_profile.repositories.add(repo)
                topics_data = requests.get(f'https://api.github.com/repos/{username}/{repo_data["name"]}/topics',headers=headers).json() 
                
                repo.topics.clear()
                for topic_name in topics_data.get('names', []):
                    topic, _ = Topic.objects.get_or_create(name=topic_name)
                    repo.topics.add(topic)
            user_profile.save()
            # p = Paginator(user_profile.repositories.all(), 10)
            # page = request.GET.get('page')
            # venues = p.get_page(page)
            # nums = "a" * venues.paginator.num_pages
            

            return render(request, 'index.html', {'user_profile': user_profile})
        except requests.exceptions.RequestException as e:
            return render(request, 'error.html', {'error_message': str(e)})

    # if request.method == 'GET':
    #         p = Paginator(user_profile.repositories.all(), 10)
    #         page = request.GET.get('page')
    #         venues = p.get_page(page)
    #         return render(request, 'index.html',{'venues': venues})    
        
    return render(request, 'index.html')
    


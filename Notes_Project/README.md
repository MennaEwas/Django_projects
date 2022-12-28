# Smart-Notes Project from LinkedIn Course:

## Goal: 
to build a django website contains smart notes for my courses list 

### personal Goal:
to learn the basics of Django 

### Language: Python 
### Duration: 3 weeks 

## content: 

1. smartnotes: (Root)
  Contains settings: to put any new apps, any static directors, and any static urls, templetes
           urls: the urlpatterns which include all the major paths for examples "smart/" in "smart/notes/1"
3. Home: 
  Contains urls: path from home as view and authorized as view 
          views: classes like HomeViews(a templete-view instead of render in the home path) and AuthorizedView
            same as HomeViews but used with LoginRequiredMixin, TemplateView
5. notes:
  contains the whole application
  
7. static: Contains all the style of the website 
8. db.sqlite3

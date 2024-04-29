from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)

def home(request):
    html = "<html><body><p>Dating Site Rules</p> <ul> <li>Be honest in your profile information.</li> <li>Respect other users’ boundaries and privacy.</li> <li>Do not harass or send unsolicited messages.</li> <li>Use appropriate language and be respectful in your communication.</li> <li>Do not share personal contact information too soon.</li> <li>Report any suspicious or inappropriate behavior to the site administrators.</li> <li>Be patient and open-minded when getting to know someone.</li> <li>Remember that not everyone will be a perfect match, and that’s okay.</li> <li>Have fun and enjoy the process of meeting new people!</li></body></html>"
    return HttpResponse(html)

def venues(request):
    html = "<html><body><p>List of establishments</p><ul><li>Empty at the moment</ul></body></html>" 
    return HttpResponse(html)
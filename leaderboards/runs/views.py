from django.http import HttpResponse
from django.template import loader
from django.views import View


class RunLeaderboardView(View):
    def get(self, request):
        template = loader.get_template("run/index.html")
        leaders = [
            {
                "user": "Alice",
                "distance": 120,
                "time": "1:30:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
            {
                "user": "Bob",
                "distance": 110,
                "time": "1:45:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
            {
                "user": "Charlie",
                "distance": 100,
                "time": "2:00:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
        ]
        others = [
            {
                "user": "Dave",
                "distance": 90,
                "time": "2:15:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
            {
                "user": "Eve",
                "distance": 80,
                "time": "2:30:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
            {
                "user": "Frank",
                "distance": 70,
                "time": "2:45:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
            {
                "user": "Grace",
                "distance": 60,
                "time": "3:00:00",
                "image": "https://media.istockphoto.com/id/862317986/photo/dynamic-running-uphill-on-trail-male-athlete-runner-side-view.jpg?s=612x612&w=0&k=20&c=rlDBbq42wkdZ8md-B5lWw_0B1ak8vREr2IWHzY9l1F4=",
            },
        ]
        context = {"leaders": leaders, "others": others}
        return HttpResponse(template.render(context, request))

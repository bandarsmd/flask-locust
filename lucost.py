from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index_page(self):
        self.client.get(url="/")

    # @task
    # def index(self):
    #     self.client.get("/")
    #     self.client.get("/static/assets.js")
    #
    # @task
    # def about(self):
    #     self.client.get("/about/")

from locust import HttpUser , task , between



class MywebUser(HttpUser):

    wait_time=between(1,3)
    host = "https://demo.opencart.com/"

    @task
    def Lunch_URL(self):
        resp1=self.client.get("https://www.opencart.com/", name="View")


    @task
    def Login_URL(self):
        resp2=self.client.post("/admin/index.php?route=common/login", name="login",data= {"username": "demo",
        "password": "demo"})





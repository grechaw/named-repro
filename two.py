import ray

ray.init(address="auto")
x = ray.get_actor("x")

answer = x.msg.remote("message")

print(ray.get(answer))





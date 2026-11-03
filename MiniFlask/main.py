class MiniFlask:
    def __init__(self):
        # dicitionzly structure [ path: { method: function }]
        self.routes = {}

    def route(self, path:str, methods=None):
        if methods is None:
            methods['GET']

        def decorator(func): 
            if path not in self.routes:
                self.routes[path] = {}

            for method in methods:
                self.routes[path][method] = func

            return func
        return decorator


    def simulate_request(self, path:str, method: str = 'GET'):
        print(f"\nBrowser request: {method} {path}")

        if path in self.routes:
            if method in self.routes[path]:
                response = self.routes[path][method]()
                print(f"\nBrowser request: {method} {path}")
            else:
                print(f"\server response: {method} {path}")
        else:
            print(f"\server response: {method} {path}")
## Testiing the extended version

app = MiniFlask()

@app.route("/", methods=["GET"])
def home():
    return "homepage (get)"

if __name__ == "__main__":
    app.simulate_request("/",method="GET")
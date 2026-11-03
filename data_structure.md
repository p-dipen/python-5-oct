What is data structures :- digital specialized format for organizing processing, storing and accessing data in a computer system. Data structures are essential for efficient data management and manipulation, allowing for optimized performance in various applications. They provide a way to store data in a structured manner, enabling quick retrieval, insertion, deletion, and modification of data elements. Common examples of data structures include arrays, linked lists, stacks, queues, trees, and graphs. Each data structure has its own advantages and use cases, depending on the specific requirements of the application or algorithm being implemented.

Two data structures :- 
- Primitive data structures:- integers(numbers), strings, characters and booleans
- Non-primitive data structures:- Complex structures constucted by combining primitive types 
- Lists, Tree, Graphs, Heaps, Array, Stack, Queue, Linked List

- lists, Array = [30,40,50,60]
- Stack, Queue = []
QueueLists = [30,40,50,60] FIFO order(First In, FIrst out)
StackLists = [30,40,50,60] LIFO order (Last In, First Out) 

What is An API ? -> Application Programming Interface 
Requests and Response 

working apis using Http(protocal) depends on the request and response cycle. 
Request: Http Method, Headers, Body and Parameters

HTTP method(or action or verb) is how you tell the server which type of operation you'd like to perform 

- Get : Ask the server to get a resource 
- Post : ASk the server to create a resources, with the data that you have provide
- PUT : Edit or update a resource 
- Delete : Delete a resources

Headers: metadata, auth(token)

Response : JSON, XML, and others 

JSON most common format 

HTTP Status Code 
- 1xx: Informational
  - Not Commonly used 
- 2xx: Success
  - 200 OK - Standard response 
  - 201 Created a new resources was created 
- 3xx: Redirected 
  - 301 Moved permanently
- 4xx: Client Error 
  - 404 Not found - 
- 5xx: A server Error 
  - 500 Internal Server error 
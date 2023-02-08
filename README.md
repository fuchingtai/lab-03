# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Ching-Tai (Vincent) Fu
- none

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
Answer for Question 1: RESTful APIs are scalable because the server end of REST is stateless. This means that the server doesn't have to store informations across requests, which doesn't require it to communicate between servers. Previous request does not call for any storage, so the server only has to work with the current request that is being called, thus making it scalable.

Question 2: According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients?
Answer for Question 2: In the AWS article, when a request is called by the client, resources are the information that is being provided by the server. In a mailing system, mails are the resource system.

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
Answer for Question 3: The common REST Method that we did not use is PUT. PUT enables users to update current existing resources. For our mailing system, PUT could be employed to change/modify the email entires.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
Answer for Question 4: API keys are used for authentication. In particular, for the case when clients are making requests to the server. It is just like any other key. The server must check if the client has the API key to access the specific information that is being requested. Every client has a unique key, so it also adds another layer of secuirty by tracking who is sending the request.

Resources: 
https://aws.amazon.com/tw/what-is/restful-api/
https://zh.wikipedia.org/zh-tw/API%E5%AF%86%E9%91%B0
https://developers.google.com/maps/documentation/javascript/get-api-key?hl=zh-tw
https://swagger.io/docs/specification/authentication/api-keys/

# Resume-Swype-Back-End

## What is AWS S3?
- S3 is a service used for file storage for web apps.
- For my app, it is used to store the PDF files that a user submits with their information.
----
## Biggest struggles:
1) 
- Setting up AWS S3 for file storage on back-end. I tried to follow a document from `devcenter.heroku` to get it to upload to AWS S3 directly using Python but it did not work. The code was for a Flask app.
- So I consulted with Alexis and he recommended I create a test project following a document on how to upload files to AWS S3 using the Django REST framework.
- After creating a test-project and being able to upload with the Django REST framework, I compared my own code to the test-project code and added the necessary code and was able to upload a PDF to S3.

2.
- Uploading a file through the front-end was giving issues, so I had to search up ways that people did to upload their files.

- I kept getting the error message: `no file was submitted` when trying to do an axios POST between react and django rest framework. After a lot of trial and error, I fixed it by following the code on this page: `https://stackoverflow.com/questions/71241619/no-file-was-submitted-error-when-trying-to-do-an-axios-post-between-react-and-dj`

- After following the code, I got more errors saying some things were not defined.

- Error message from Django: `Response is not defined`. Source to resolve error: `https://stackoverflow.com/questions/65194508/django-rest-framework-response-is-not-defined-error`

- Error message from Django: `status is not defined`. Source to resolve error: `https://stackoverflow.com/questions/61282713/django-rest-framework-error-name-is-not-defined`

- Error message from Django: `cannot import name MultiPartParser`. Source to resolve erro: `https://stackoverflow.com/questions/36457217/import-error-cannot-import-name-multipartparser`

----
## Difficulties I ran into:
- Ran into backport.zoneinfo problem during Heroku deployment. I looked it up on stackoverflow and found a solution that fixed it. I editted my `requirements.txt` file from: `backports.zoneinfo==0.2.1` to `backports.zoneinfo==0.2.1;python_version<"3.9"`

----
## Sources:
- To fix backport.zoneinfo problem: `https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta`

- Code from the Flask app: `https://devcenter.heroku.com/articles/s3-upload-python`

- Setting up AWS S3 using Django REST Framework: `https://www.section.io/engineering-education/how-to-upload-files-to-aws-s3-using-django-rest-framework/`

- Setting up environment variables to hide sensitive information such as secret key and AWS secret key/access key: `https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f`

- What MultiPartParser does:`https://www.django-rest-framework.org/api-guide/parsers/#multipartparser`

# Resume-Swype-Back-End

## Biggest struggles:
1) 
- Setting up AWS S3 for file storage on back-end. I tried to follow a document from `devcenter.heroku` to get it to upload to AWS S3 directly using Python but it did not work. The code was for a Flask app.
- So I consulted with Alexis and he recommended I create a test project following a document on how to upload files to AWS S3 using the Django REST framework.
- After creating a test-project and being able to upload with the Django REST framework, I compared my own code to the test-project code and added the necessary code and was able to upload a PDF to S3.
- Uploading a file 

2) 
----
## Difficulties I ran into:
- Ran into backport.zoneinfo problem during Heroku deployment. I looked it up on stackoverflow and found a solution that fixed it. I editted my `requirements.txt` file from: `backports.zoneinfo==0.2.1` to `backports.zoneinfo==0.2.1;python_version<"3.9"`

----
## Sources:
- To fix backport.zoneinfo problem: `https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta`

- Code from the Flask app: `https://devcenter.heroku.com/articles/s3-upload-python`

- Setting up AWS S3 using Django REST Framework: `https://www.section.io/engineering-education/how-to-upload-files-to-aws-s3-using-django-rest-framework/`

- https://stackoverflow.com/questions/65194508/django-rest-framework-response-is-not-defined-error

- https://stackoverflow.com/questions/61282713/django-rest-framework-error-name-is-not-defined

- https://stackoverflow.com/questions/36457217/import-error-cannot-import-name-multipartparser

- https://www.django-rest-framework.org/api-guide/parsers/#multipartparser

- https://stackoverflow.com/questions/71241619/no-file-was-submitted-error-when-trying-to-do-an-axios-post-between-react-and-dj

- https://www.google.com/search?q=react+django+no+file+was+submitted&oq=react+django+no+file+was+submitted&aqs=chrome..69i57j69i60.5068j0j7&sourceid=chrome&ie=UTF-8

- https://www.google.com/search?q=django+no+file+was+submitted&oq=django+no+file+was&aqs=chrome.0.0i512j69i57j0i390l5j69i60.1957j0j7&sourceid=chrome&ie=UTF-8
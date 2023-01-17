# Resume-Swype-Back-End

## My biggest struggle:
- My biggest struggle was setting up AWS S3 for file storage.
----
## Difficulties I ran into:
- Ran into backport.zoneinfo problem during Heroku deployment. I looked it up on stackoverflow and found a solution that fixed it. I editted my `requirements.txt` file from: `backports.zoneinfo==0.2.1` to `backports.zoneinfo==0.2.1;python_version<"3.9"`

----
## Sources:
- To fix backport.zoneinfo problem: `https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta`

- Code from the Flask app: `https://devcenter.heroku.com/articles/s3-upload-python`

- Setting up AWS S3 using Django REST Framework: `https://www.section.io/engineering-education/how-to-upload-files-to-aws-s3-using-django-rest-framework/`
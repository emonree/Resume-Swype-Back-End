# Back-end Commit Log

## January 13th, 2023
- 10:30 AM: initial commit.
- 3 PM: getting Django to work locally.
----
## January 14th, 2023
- 5 PM: changed double quotes to single quotes for consistency.
-----
## January 15th, 2023
- 2 PM: heroku deployment and attempt to fix backports.zoneinfo issue.
- 2:30 PM: fixed Procfile error.
- 3:30 PM: attempt at fixing Heroku problems since Heroku kept crashing.
- 7:56 PM: fixed allowed host issue with local host.
----
## January 17th, 2023:
- Started at 10 AM and commited at 4:05 PM:
- changed resume_url in models.py from TextField to FileField for uploading a file.
- Consulted Alexis on how to get AWS S3 to work.
- Created a test-project following this document: `https://www.section.io/engineering-education/how-to-upload-files-to-aws-s3-using-django-rest-framework/`
- Created a .env file for environment variables to store my AWS secret key and access keys.
- Added the necessary code into models.py, urls.py, views.py, and settings.py

- Commited at 4:40 PM:
- adding missing packages to to requirements.txt
----
## January 18th, 2023:
- Worked on it until 10:30 PM on Jan 17th and committed today at 11 AM:
- looked up a lot of documentation because the file was not processing. Added code in resume_api/views.py and resume_api/urls.py to process the file upload.
- added to README.

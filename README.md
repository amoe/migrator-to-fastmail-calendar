# migrator-to-fastmail-calendar

Use `FASTMAIL_USERNAME` and `FASTMAIL_PASSWORD` in the environment to login to
Fastmail.

The credentials should be your email address and your app-specific password
which is configured in the "Third-party apps" section of the Fastmail settings
panel.

For the Google part, you need to register an app in the Cloud Console.  For me
this link is here:
https://console.cloud.google.com/apis/credentials?project=api-project-846782172465&pli=1

Google provides a `credentials.json` you can download.

Running `export_gcal.py` will create a file `out.json` which is a
reasonably-faithful copy of the main Google calendar for the account.

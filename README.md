# migrator-to-fastmail-calendar

This migrates Google calendars to Fastmail calendars using a slightly different
method from their official sync tool.

Notably this preserves the **colour** of the individual calendar events which is
useful if you've colour-coded them in the past.  Fastmail's default migration
does not do this.

## Details

You need `caldav` 0.10.0 (older versions won't work!)
You need `google-api-python-client` 2.65.0, `google-auth-httplib2` 0.1.0,
`google-auth-oauthlib` 0.7.1.

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

Having done this, you run `write_to_fastmail.py` to

Note that as of late 2022 the Google CalDAV interface that uses the Python
`caldav` library does NOT work.

You can use `clear_calendar.py` to delete all items from the calendar if
something goes wrong with the migration.

Likewise, `list_calendar.py` can be used as a debugging tool to ensure that iCal
events are getting created properly within Fastmail.

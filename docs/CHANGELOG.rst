:orphan:

Changelog
=========


2.0.0a1 (2023-11-03)
--------------------

- Remove the includeDependecies directive from the package configure.zcml


1.1.4 (2021-11-30)
------------------

- Fix for Unauthorized on transaction commit.
  [reinhardt]


1.1.3 (2021-10-07)
------------------

- Support for older Plone/Zope versions.
  [reinhardt]
- Prevent the log level getting set to DEBUG
  [goibhniu]


1.1.2 (2021-02-15)
------------------

- Support for WSGI.
  [reinhardt]

1.1.1 (2021-02-15)
------------------

- ZCML namespace cleanup.
  [thet]


1.1.0 (2019-01-28)
------------------

- Added InstanceScript class for use with `instance run`.
  [reinhardt]


1.0.4 (2017-08-29)
------------------

- Improve log handling:

  * only log errors during startup
  * log INFO to stdout
  * log ERROR to stderr
  * log to instance's event.log too

  This makes it possible to only escalate errors in cronjobs, send
  normal logging to /dev/null and protocol what has been done in
  the instance.log

  [frisi]


1.0.3 (2016-05-19)
------------------

- traverse to context as run_as user [reinhardt]
- Allow selecting a portal by id [reinhardt]


1.0.2 (2016-03-18)
------------------

- better manifest [reinhardt]


1.0.1 (2016-03-18)
------------------

- Allow passing a context_path [reinhardt]
- Updated README [reinhardt]


1.0 (2015-12-11)
----------------

- Initial release.
  [reinhardt]


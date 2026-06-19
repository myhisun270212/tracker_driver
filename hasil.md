You reached the start of the range
Jun 20, 2026, 2:17 AM
Starting Container
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 332, in dashboard
    return render_template('dashboard.html')
[2026-06-19 19:18:52 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2026-06-19 19:18:52 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
[2026-06-19 19:18:52 +0000] [1] [INFO] Using worker: sync
[2026-06-19 19:18:52 +0000] [4] [INFO] Booting worker with pid: 4
[2026-06-19 19:18:53,018] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
[2026-06-19 19:18:54,053] ERROR in app: Exception on / [GET]
         ^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 332, in dashboard
    return render_template('dashboard.html')
NameError: name 'render_template' is not defined
[2026-06-19 19:18:56,088] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    rv = self.dispatch_request()
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
         ^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 332, in dashboard
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return render_template('dashboard.html')
           ^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 332, in dashboard
    return render_template('dashboard.html')
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
[2026-06-19 19:19:00,120] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[2026-06-19 19:19:08,154] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 332, in dashboard
    return render_template('dashboard.html')
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
[2026-06-19 19:19:24,192] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/venv/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 332, in dashboard
    return render_template('dashboard.html')
           ^^^^^^^^^^^^^^^
NameError: name 'render_template' is not defined
const { exec } = require('child_process')

exec("cd content && rm -rf uxui && git clone git@github.com:nevanscott/uxui.git && rm -rf uxui/.git")

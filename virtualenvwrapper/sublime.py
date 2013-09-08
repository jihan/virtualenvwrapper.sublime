#!/usr/bin/env python
# encoding: utf-8

"""Create a sublime project file
"""

import logging
import os
import subprocess

log = logging.getLogger('virtualenvwrapper.sublime')


def template(args):
    """Deduces project directory to create a new sublime project.
    """
    project_filename = "%s/%s" % (os.environ.get('VIRTUAL_ENV'),
                                  os.environ.get('VIRTUALENVWRAPPER_PROJECT_FILENAME'))
    with open(project_filename) as f:
        project_dir = f.read()

    log.info('%s', args)

    project = args[0]
    project_dir = project_dir.strip()
    os.chdir(project_dir)
    """Beware this will overwrite pre-existing project 
       file in the current directory
    """
    log.info('Creating a SublimeText project file for %s"', project)
    file = open('%s.sublime-project' % project, 'w')
    file.write('''{
    "folders":
    [
        {
            "follow_symlinks": true,
            "path": "%s"
        }
    ]
}''' % project_dir)
    return

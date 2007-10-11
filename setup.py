#   Copyright (c) 2006-2007 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from setuptools import setup, find_packages
import os

PACKAGE_NAME = "windmill"
PACKAGE_VERSION = "0.2rc2"

SUMMARY = 'Web testing framework intended for complete automation of user interface testing, with strong test debugging and recording capabilities.'

DESCRIPTION = """Windmill is an Open Source AJAX Web UI Testing framework that was originally built to automate testing for the Chandler Server Project at OSAF. After spending time with Selenium we realized we had a variety of needs that weren't being fulfilled and built Windmill from the ground up. 

Windmill implements cross browser testing, in-browser recording and playback, and functionality for fast accurate debugging and test environment integration.

We are a relatively young project, but as far as we know we already implement a larger set of a browser testability than Selenium. We welcome any and all interest and contribution, as we work diligently at adding new features and keeping up with your bugs.

Thanks for your interest and participation!
"""

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      description=SUMMARY,
      long_description=DESCRIPTION,
      author='Open Source Applications Foundation',
      author_email='windmill-dev@osafoundation.org',
      url='http://windmill.osafoundation.org/',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      include_package_data = True,
      packages=find_packages(),
      package_data = {'': ['*.js', '*.css', '*.html', '*.txt'],},
      scripts=[os.path.join(os.path.dirname(__file__),'windmill','bin','windmill')],
      platforms =['Any'],
      install_requires = ['cherrypy >= 3.0.2',
                          'simplejson >= 1.7.1',
                          # All these wsgi_ libraries used to be part of windmill but are now seperate libraries.
                          'wsgi_jsonrpc >= 0.2.2',
                          'wsgi_xmlrpc >= 0.2.3',
                          'wsgi_fileserver >= 0.2.3',
                          'functest >= 0.5.4',
                          ],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                  ],
     )


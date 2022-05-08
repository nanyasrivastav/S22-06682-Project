
# Table of Contents

1.  [Project layout](#org9983b2e)
2.  [Project checklist <code>[8/8]</code>](#orge9bc0f9)
3.  [Summary and Grade](#orga7ec2d7)



<a id="org9983b2e"></a>

# Project layout

    tree -F

    ./
    ├── data/
    │   ├── AucolCurow.json
    │   ├── AucolCurowoutput.xlsx
    │   ├── AucolSnrow.json
    │   ├── AucolSnrowoutput.xlsx
    │   ├── PdcolPbrow.json
    │   ├── PdcolPbrowoutput.xlsx
    │   └── readme.md
    ├── feedback.org
    ├── makefile
    ├── project-proposal.md
    ├── readme.md
    └── src/
        ├── LICENSE
        ├── MANIFEST.in
        ├── README.md
        ├── __pycache__/
        │   └── utilities.cpython-37.pyc
        ├── h2activity/
        │   ├── __init__.py
        │   ├── __pycache__/
        │   │   ├── __init__.cpython-37.pyc
        │   │   └── utilities.cpython-37.pyc
        │   ├── data_examples/
        │   │   ├── AucolCurow.json
        │   │   ├── AucolSnrow.json
        │   │   └── PdcolPbrow.json
        │   ├── display.py
        │   ├── high_activity.py
        │   ├── start.py
        │   └── stats.py
        ├── h2activity.egg-info/
        │   ├── PKG-INFO
        │   ├── SOURCES.txt
        │   ├── dependency_links.txt
        │   └── top_level.txt
        ├── setup.py
        ├── tests/
        │   ├── __init__.py
        │   ├── __pycache__/
        │   │   ├── __init__.cpython-37.pyc
        │   │   ├── test_fail.cpython-37-pytest-7.1.1.pyc
        │   │   └── test_path.cpython-37-pytest-7.1.1.pyc
        │   ├── test_fail.py
        │   └── test_path.py
        └── utilities.py
    
    9 directories, 37 files


<a id="orge9bc0f9"></a>

# Project checklist <code>[8/8]</code>

-   [X] Put your project proposal in a document called <./project-proposal.md>. You
    should refine this to clarify your plan and what you want your project to
    accomplish.

Your project should:

-   [X] Put a link to your Deepnote repository where you did the work in the
    <./readme.md>, and make sure to give Prof. Kitchin edit access to it.
-   [X] solve a practical problem that is not too trivial, and that a reusable
    package would be helpful for.
-   [X] be pip installable
-   [X] have a License
-   [X] have a readme.md file that explains what it is, and how to use it. If you
    have a command line utility, there should be examples of how to use it, and
    the output. If your package is for a notebook you should provide an example
    notebook, including data if it is needed.
-   [X] Should pass black, flake8 and pylint (ideally you would setup pre-commit
    hooks to help ensure this)
-   [X] Should have some tests that are run in a GitHUB action, and your project
    should pass them.


<a id="orga7ec2d7"></a>

# Summary and Grade

Nice work! I like the interactive start.py function. You could put that kind of information in a help string too.

Grade: A/B

The installation is not quite right, but if you follow your directions they work. For example, there should not be src in the paths that you import in the commands.

Something is not right in your pre-commit setup, but it looks like all the tests work on GitHUB.

    exec 2>&1
    pre-commit run --all
    :

    An error has occurred: InvalidConfigError: 
    ==> File .pre-commit-config.yaml
    =====> mapping values are not allowed in this context
      in "<unicode string>", line 15, column 8
    Check the log at /Users/jkitchin/.cache/pre-commit/pre-commit.log

The tests pass on GitHUB, but it isn't clear they were run. For example locally flake8 does not pass, and there is no output in Actions for this. That seems odd.

    exec 2>&1
    make all
    :

    black src
    All done! ✨ 🍰 ✨
    10 files left unchanged.
    flake8 --max-line-length 85 src
    src/setup.py:1:1: D210 No whitespaces allowed surrounding docstring text
    src/utilities.py:1:1: D205 1 blank line required between summary line and description
    src/utilities.py:1:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/utilities.py:1:1: D400 First line should end with a period
    src/utilities.py:11:1: D401 First line should be in imperative mood
    src/utilities.py:22:1: D205 1 blank line required between summary line and description
    src/utilities.py:22:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/utilities.py:22:1: D400 First line should end with a period
    src/utilities.py:22:1: D401 First line should be in imperative mood
    src/utilities.py:56:1: D401 First line should be in imperative mood
    src/tests/__init__.py:1:1: D104 Missing docstring in public package
    src/tests/test_fail.py:1:1: D205 1 blank line required between summary line and description
    src/tests/test_fail.py:1:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/tests/test_fail.py:1:1: D400 First line should end with a period
    src/tests/test_fail.py:8:1: D403 First word of the first line should be properly capitalized
    src/tests/test_fail.py:14:1: D403 First word of the first line should be properly capitalized
    src/tests/test_fail.py:20:1: D403 First word of the first line should be properly capitalized
    src/tests/test_path.py:1:1: D205 1 blank line required between summary line and description
    src/tests/test_path.py:1:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/tests/test_path.py:1:1: D400 First line should end with a period
    src/h2activity/high_activity.py:2:1: D205 1 blank line required between summary line and description
    src/h2activity/high_activity.py:2:1: D400 First line should end with a period
    src/h2activity/high_activity.py:19:1: D205 1 blank line required between summary line and description
    src/h2activity/high_activity.py:19:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/h2activity/high_activity.py:19:1: D400 First line should end with a period
    src/h2activity/high_activity.py:19:1: D401 First line should be in imperative mood
    src/h2activity/__init__.py:1:1: D104 Missing docstring in public package
    src/h2activity/start.py:2:1: D205 1 blank line required between summary line and description
    src/h2activity/start.py:2:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/h2activity/start.py:2:1: D400 First line should end with a period
    src/h2activity/display.py:2:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/h2activity/display.py:12:1: D401 First line should be in imperative mood
    src/h2activity/stats.py:2:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/h2activity/stats.py:11:1: D205 1 blank line required between summary line and description
    src/h2activity/stats.py:11:1: D209 Multi-line docstring closing quotes should be on a separate line
    src/h2activity/stats.py:11:1: D400 First line should end with a period
    src/h2activity/stats.py:11:1: D401 First line should be in imperative mood
    make: *** [flake8] Error 1

Some files are committed that should not be, .e.g. .pyc, <span class="underline"><span class="underline">pycache</span></span> files, egg-info.


Title: Writing better code Javascrit even when you're not a rockstar
Date: 2013-04-19 01:00
Tags: code-better, javascript
Slug: writing-better-code-even-when-youre-not-a-rockstar
Summary: Even if you're not a rockstar developer, there are ways to easily produce better code while learning new tricks, using freely available tools that, aditionally, can automate source code inspections. Let go over a few of them.

Even if you're not a rockstar developer, there are ways to easily produce better code while learning new tricks, using freely available tools that, aditionally, can automate source code inspections.


### Improving Javascript source code with Google Closure Tools

There are several Javascript source code linters available. The one i have bee working with is [Closure Linter](https://developers.google.com/closure/utilities/) wich is part of [Google Closure Tools](https://developers.google.com/closure/).

#### About the Closure Linter

From <https://developers.google.com/closure/utilities/>

> The Closure Linter ensures that all of your project's JavaScript code follows the guidelines in the [Google JavaScript Style Guide](http://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml). It can also automatically fix many common errors, which saves you time and lets you focus on coding.

Closure Linter is a Python library that also adds a couple of command-line utilities to out toolbelt, `gjslint` for Javascript source code lintint and `fixjsstyle` to automatically apply corrections to them.  

#### Installing

The Closure Linter can be obtained on the Google Code project page, in the downloads section <https://code.google.com/p/closure-linter/downloads/>. It's Python package, so let's use `pip` to install it on a fresh Python virtual environment:
    
let's create a fresh virtual enviroment

    :::console
    zemanel@victory ➜ WorkDir  mkvirtualenv blogging
    New python executable in blogging/bin/python
    Installing setuptools............done.
    Installing pip...............done.


and `pip` install the package 

    :::console
    (blogging)zemanel@victory ➜  WorkDir  pip install https://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz
     Downloading/unpacking https://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz
      Downloading closure_linter-latest.tar.gz (88kB): 88kB downloaded
      Running setup.py egg_info for package from https://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz    
     Downloading/unpacking python-gflags (from closure-linter==2.3.9)
      Running setup.py egg_info for package python-gflags    
     Installing collected packages: python-gflags, closure-linter
      Running setup.py install for python-gflags
      Running setup.py install for closure-linter
        Installing fixjsstyle script to /Users/zemanel/.virtualenvs/blogging/bin
        Installing gjslint script to /Users/zemanel/.virtualenvs/blogging/bin
     Successfully installed python-gflags closure-linter
     Cleaning up...

Our test script will be *CloudAppSelectAllItems.js*, a <https://gist.github.com/zemanel/4974451> i created to to mass deletion of uploads on <http://GetCloudApp.com>.
    
    :::javascript
    /*
     * Checks all list items on http://getcloudapp.com upload list,
     *  which is useful for multiple item deletion (AKA nuke the crap of all the uploads)
     * 
     * License:
     * José Moreira, in 2013 and beyond, doesn't care what you do with this piece of code.
     * 
     */
    
    (function(){
        var items = $$('ol#listing input[type="checkbox"]');
        if (items.length && items.length >= 0) {
            //  check all items
            var i;
            for (i=0; i < items.length; i++) {
                items[i].click();
            }
        }
    })();
    
    // #1 click "Delete Selected"
    // #2 ...
    // #3 Profit !
    // #4 Refresh page or whatever
    // #5 GOTO 1 

Let's apply `gjslint` to the script and behold, crappy formatted code:
    
    :::shell
    (blogging)zemanel@victory ➜  WorkDir  gjslint CloudAppSelectAllItems.js
    ----- FILE  :  /Users/zemanel/WorkDir/CloudAppSelectAllItems.js -----
    Line 3, E:0110: Line too long (85 characters).
    Line 4, E:0001: Extra space at end of line
    Line 6, E:0110: Line too long (87 characters).
    Line 7, E:0001: Extra space at end of line
    Line 10, E:0002: Missing space before "{"
    Line 15, E:0002: Missing space before "="
    Line 15, E:0002: Missing space after "="
    Line 25, E:0001: Extra space at end of line
    Found 8 errors, including 0 new errors, in 1 files (0 files OK).

    Some of the errors reported by GJsLint may be auto-fixable using the script
    fixjsstyle. Please double check any changes it makes and report any bugs. The
    script can be run by executing:

    fixjsstyle CloudAppSelectAllItems.js 

The script analyzed out script and warned about 8 errors. At this we can either apply the corrections ourselves and iterate until it's all good or, as stated on the last message we can apply the `fixjsstyle` script to it. Let's try that:
    
    :::shell
    (blogging)zemanel@victory ➜  WorkDir  fixjsstyle CloudAppSelectAllItems.js
    Fixed 6 errors in /Users/zemanel/WorkDir/CloudAppSelectAllItems.js


6 of the 8 errors were corrected automatically by the script. Re-running the linter we get:
    
    :::shell
    (blogging)zemanel@victory ➜  WorkDir  fixjsstyle CloudAppSelectAllItems.js
    Fixed 6 errors in /Users/zemanel/WorkDir/CloudAppSelectAllItems.js
    (blogging)zemanel@victory ➜  WorkDir  gjslint CloudAppSelectAllItems.js
    ----- FILE  :  /Users/zemanel/WorkDir/CloudAppSelectAllItems.js -----
    Line 3, E:0110: Line too long (85 characters).
    Line 6, E:0110: Line too long (87 characters).
    Found 2 errors, including 0 new errors, in 1 files (0 files OK).
    
    Some of the errors reported by GJsLint may be auto-fixable using the script
    fixjsstyle. Please double check any changes it makes and report any bugs. The
    script can be run by executing:
    
    fixjsstyle CloudAppSelectAllItems.js

The remaning warnings are related to 80 column line length. After manual editing the javascript source, we have this result:

    :::javascript
    /*
     * Checks all list items on http://getcloudapp.com upload list,
     *  which is useful for multiple item deletion (AKA nuke the crap of
     *  all the uploads)
     *
     * License:
     * José Moreira, in 2013 and beyond, doesn't care what you do with
     * this piece of code.
     *
     */

    (function() {
        var items = $$('ol#listing input[type="checkbox"]');
        if (items.length && items.length >= 0) {
            //  check all items
            var i;
            for (i = 0; i < items.length; i++) {
                items[i].click();
            }
        }
    })();

    // #1 click "Delete Selected"
    // #2 ...
    // #3 Profit !
    // #4 Refresh page or whatever
    // #5 GOTO 1
    
Running the linting tool again, we're in the clear:
    
    :::shell
    (blogging)zemanel@victory ➜  WorkDir  gjslint CloudAppSelectAllItems.js
    1 files checked, no errors found.

Obviously this was a very simple, with hardly noticeable differentes between versions, but here's a `diff -u`:

    :::udiff
    --- CloudAppSelectAllItems.js   2013-04-19 02:50:56.000000000 +0100
    +++ CloudAppSelectAllItems-linted.js    2013-04-19 02:53:05.000000000 +0100
    @@ -1,18 +1,20 @@
     /*
      * Checks all list items on http://getcloudapp.com upload list,
    - *  which is useful for multiple item deletion (AKA nuke the crap of all the uploads)
    - *
    + *  which is useful for multiple item deletion (AKA nuke the crap of
    + *  all the uploads)
    + *
      * License:
    - * José Moreira, in 2013 and beyond, doesn't care what you do with this piece of code.
    - *
    + * José Moreira, in 2013 and beyond, doesn't care what you do with
    + * this piece of code.
    + *
      */

    -(function(){
    +(function() {
         var items = $$('ol#listing input[type="checkbox"]');
         if (items.length && items.length >= 0) {
             //  check all items
             var i;
    -        for (i=0; i < items.length; i++) {
    +        for (i = 0; i < items.length; i++) {
                 items[i].click();
             }
         }
    @@ -22,4 +24,4 @@
     // #2 ...
     // #3 Profit !
     // #4 Refresh page or whatever
    -// #5 GOTO 1
    +// #5 GOTO 1
    > // #5 GOTO 1

The script can also be customized with command-line parameters, for which the list can be obtained with `gjslint --help` and can check even JSDoc validity.

The case in point is that an apparently simple script, triggered 8 violations of the formatting coding standard. Automating the linting process as part of a development workflow either manually, source control hooks or CI automated builds, will greatly increase the quality of any project, at a very small cost.













